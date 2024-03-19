with open('output.txt', 'w', encoding='utf-8') as out_file:
    with open('visitor_record.txt', 'r', encoding='utf-8') as in_file:
        for line in in_file:
            if '東京' in line:
                out_file.write(line)
