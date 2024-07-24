import re
import json
from datetime import datetime


def structure_soap(text):
    soap_structure = {
        'Subjective': '',
        'Objective': {
            'raw': '',
            'measurements': {}
        },
        'Assessment': '',
        'Plan': []
    }

    patterns = {
        'Subjective': r'S[：:]\s*([\s\S]*?)(?=O[：:]|\Z)',
        'Objective': r'O[：:]\s*([\s\S]*?)(?=A[：:]|\Z)',
        'Assessment': r'A[：:]\s*([\s\S]*?)(?=P[：:]|\Z)',
        'Plan': r'P[：:]\s*([\s\S]*)'
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            if key == 'Objective':
                soap_structure[key]['raw'] = match.group(1).strip()
            elif key == 'Plan':
                soap_structure[key] = [item.strip() for item in match.group(1).split('\n') if item.strip()]
            else:
                soap_structure[key] = match.group(1).strip()

    objective_text = soap_structure['Objective']['raw']
    measurements = re.findall(r'([\w\s]+):\s*([\d.]+)\s*([^\n]*)', objective_text)
    for measure, value, unit in measurements:
        soap_structure['Objective']['measurements'][measure.strip()] = {
            'value': float(value),
            'unit': unit.strip()
        }

    return soap_structure


def save_soap_to_json(soap_data, filename=None):
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"soap_record_{timestamp}.json"

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(soap_data, f, ensure_ascii=False, indent=2)

    return filename


# 使用例
sample_soap = """
S: 患者は45歳の男性。3日前から続く頭痛を訴える。痛みは前頭部に集中し、光と音に過敏。睡眠不足と仕事のストレスがあると報告。

O: 体温: 37.2 ℃
   血圧: 130/85 mmHg
   脈拍: 72 bpm
   SpO2: 98 %
   呼吸数: 16 回/分
   BMI: 24.5 kg/m2
   神経学的検査: 異常なし

A: 緊張性頭痛の可能性が高い。片頭痛の可能性も考慮。脱水症状や睡眠障害も関連している可能性がある。

P: 1. アセトアミノフェン 500mg 6時間ごと 必要時
   2. 水分摂取の増加を指導（1日最低2L）
   3. ストレス管理技法の指導（深呼吸法、漸進的筋弛緩法）
   4. 睡眠衛生の改善（就寝時間の規則化、ブルーライトの制限）
   5. 1週間後に再診。症状が悪化した場合は早めの受診を指示。
"""

structured_soap = structure_soap(sample_soap)

# 構造化されたデータをコンソールに出力
print(json.dumps(structured_soap, ensure_ascii=False, indent=2))

# 構造化されたデータをJSONファイルとして保存
saved_filename = save_soap_to_json(structured_soap)
print(f"\nSOAPデータが {saved_filename} に保存されました。")
