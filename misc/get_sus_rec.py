import json

with open('problems_json.txt', 'r') as f:
    problems = json.load(f)


keys = []
for i, v in problems.items():
    # print(i)
    keys.append(i)

recommendations = []
suspicious = []

for i in keys:
    # print(problems[i]['recommendation'])
    # print(problems[i]['suspicious'])
    for n in problems[i]['recommendation']:
        recommendations.append(n)

    for n in problems[i]['suspicious']:
        suspicious.append(n)


# print(recommendations)
# print(suspicious)

for i in recommendations:
    print(i)

for i in suspicious:
    print(i)
