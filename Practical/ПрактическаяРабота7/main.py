import re
import urllib.request
import csv

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
reply = urllib.request.urlopen(url)
content = reply.read().decode()

name_pattern = r"class=\"org-widget-header__title-link\"[^>]*>\s*(?P<names>[^<]+)"
street_pattern = r"<span[^>]*class=\"[^\"]*(?:street|address|location|meta-location|geo)[^\"]*\"[^>]*>\s*(?P<street>[^<\n\r]+)"
num_pattern  = r"<dd class=[^>]+>(?P<numbers>(?:\+|7|8)[^<]+)"
table_pattern = r"<dd class=\"spec__value\">(?P<raspi>[^<]*?\d{1,2}:\d{2}[^<]*)"


names = re.findall(name_pattern, content, re.IGNORECASE)
streets = re.findall(street_pattern, content, re.IGNORECASE)
phone = re.findall(num_pattern, content, re.IGNORECASE)
table = re.findall(table_pattern, content, re.IGNORECASE)

with open('data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Наименование организации', 'Адрес организации', 'Телефон организации', 'Время работы организации'])
 
    max_len = max(len(names), len(streets), len(phone), len(table))
    

    for i in range(max_len):
        row = [
            names[i] if i < len(names) else '',
            streets[i] if i < len(streets) else '',
            phone[i] if i < len(phone) else '',
            table[i] if i < len(table) else ''
        ]
        writer.writerow(row)


