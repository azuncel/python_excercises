import csv

with open ('prueba.txt') as text_file:
  text_data = text_file.read()
print(text_data)

with open('prueba.txt') as lines_doc:
  for lines in lines_doc.readlines():
    print(lines)

with open('azu.txt', 'w') as azu_doc:
  azu_doc.write("Github @azuncel")
  azu_doc.write(" Github @azuncel2")

with open('insurance.csv') as insurance_csv_file:
  insurance = insurance_csv_file.read()


list = []
with open('insurance.csv') as insu:
  file = csv.DictReader(insu)
  for row in file:
    print(row['age'])
    list.append(row['sex'])


example_log = [{'time': '09:39:37', 'limit': 855505, 'address': '1.227.124.183'}, {'time': '12:13:35', 'limit': 543761, 'address': '198.51.139.198'}, {'time': '19:50:45', 'limit': 3041, 'address': '172.1.254.218'}, {'time': '17:37:16', 'limit': 67031867, 'address': '172.58.247.229'}, {'time': '14:56:22', 'limit': 108, 'address': '192.31.185.8'}, {'time': '18:56:55', 'limit': 6209, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv

with open('logger.csv', 'w') as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fields)
  log_writer.writeheader()
  for item in example_log:
    log_writer.writerow(item)

import json

with open('message.json') as message_json:
  message = json.load(message_json)
  print(message['text'])

  data_payload = [
  {'message': 'What is JSON?',
   'follow': 'Follow me!'}
]

import json
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)






