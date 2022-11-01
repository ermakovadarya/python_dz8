
import do_file
import json
import commands

students= []
# print (students)  

while True:
    command=input('Введите команду /start для начала работы или /exit для выхода ')
    if command=='/start':
        print('ИС начинает свою работу')
        students=do_file.load()
        commands.com(students)
    elif command=='/exit':
        break
    


