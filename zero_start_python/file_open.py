with open('visitor_record.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if '千葉' in line:
            print(line.replace('\n', ''))
