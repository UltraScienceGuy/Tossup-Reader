import json
import csv

json_name = input("json file name: ")
csv_name = input("csv destiation name: ")


f = open(f'{json_name}.json', encoding="utf8")

data = json.load(f)

tu_list = []
ans_list = []


for i in range (len(data["data"]["tossups"]) - 1):
    tu = data["data"]["tossups"][i]["text"]
    ans = data["data"]["tossups"][i]["answer"]
    tu_list.insert(i, [tu])
    ans_list.insert(i, [ans])

file = open(f'{csv_name}', 'w+', newline ='', encoding="utf-8")
with file:
    write = csv.writer(file)
    write.writerows(tu_list)
    write.writerows(ans_list)

print(tu_list)
print(ans_list)

#Data from QuizDB, json file must be in same dir as reader.py
