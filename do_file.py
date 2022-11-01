import json
def save(students):
    with open('students.json','w',encoding='utf-8') as fh:
        fh.write(json.dumps(students,ensure_ascii=False))
    print('Наша БД успешно сохранена в файле students.json')

def load():
    f='/Users/Dasha/Desktop/Разработчик/python/students.json'
    with open(f,'r',encoding='utf-8') as fh:
        students=json.load(fh)
    print('Наша БД успешно загружена')
    return students