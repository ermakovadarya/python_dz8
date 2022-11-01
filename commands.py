
import do_file
import json
import commands

def com(students):
    while True:
            command=input('Введите команду ')
            if command=='/stop':
                print('Бот оcтановил работу. Приходите еще, будем рады')
                do_file.save(students)
                break
            elif command=='/all':
                print('Вот текущий список учеников')
                for i in students:
                    print(i)
            elif command=='/help':
                print('Вот список команд: ')
                print('/stop-Остановить работу')
                print('/all-показать всю БД')
                print('/add-Добавить нового ученика')
                print('/del-Удалить ученика')
                print('/save-Сохранить БД')
                print('/name-Выводит все имена')
                print('/performance-выводит все имена+успеваемость')
                print('/class-выводит все имена+класс')
                print('/search_class-найти учеников в нужном классе')
                print('/search_perf-найти учеников с определенной успеваемостью')
            elif command=='/add':
                print('Введите Ученика для добавления в список в формате фамилия(пробел)класс(пробел)успеваемость')
                stud=input().split()
                temp={"Name":stud[0],"Class":stud[1],"Performance":stud[2]}
                students.append(temp)
                print('Ученик успешно добавлен')
            elif command=='/name':
                for i in students:
                    print(i['Name'])
            elif command=='/performance':
                for i in students:
                    print(i['Name'], ' ', i['Performance'])
            elif command=='/class':
                for i in students:
                    print(i['Name'], ' ', i['Class'])
            elif command=='/search_class':
                print('Введите цифру класса для поиска учеников')
                clas=input()
                for i in students:
                    if i['Class']==clas:
                        print(i)
            elif command=='/search_perf':
                print('Введите успеваемость для поиска учеников')
                perf=input()
                for i in students:
                    if i['Performance']==perf:
                        print(i)
            elif command=='/del':
                f=input('Введите Фамилию ученика для удаления ')
                try:
                    for i in students:
                        if i['Name'].lower()==f.lower():
                            students.remove(i)
                            print('Ученик успешно удален')
                except:
                    print('Ученик не найден')
            elif command=='/save':
                do_file.save(students)
            else:
                print('неопознанная команда. Просьба изучить мануал через /help')