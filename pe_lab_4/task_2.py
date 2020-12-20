from operator import itemgetter
import csv
import texttable as tt

path = 'C:\\Users\\MC_VIC\\Dropbox\\1 семестр\\ПИ\\лр3\\students.csv'
path2 = 'C:\\Users\\MC_VIC\\Dropbox\\1 семестр\\ПИ\\лр3\\students_changed.csv'


class Students:

    def __init__(self):
        self.data = []
        self.title_data = []

    def read_file(self, path):
        file = open(path, 'r', encoding='utf-8')
        self.data = file.read()
        if path2:
            self.data = self.data[:-1]
        file.close()

        self.convert_str_to_list(self.data)

    def convert_str_to_list(self, d):
        list_of_students = d.split('\n')
        for i in range(len(list_of_students)):
            list_of_students[i] = list_of_students[i].split(';')
        self.title_data = list_of_students.pop(0)
        self.data = list_of_students
        self.output()

    def output(self, d=None, t=None):
        tab = tt.Texttable()

        if d == None:
            d = self.data                                   ##original, no sorted data
            ##d = sorted(self.data, key=itemgetter(1))      ##sorted by surname data
        if t == None:
            t = self.title_data

        tab.header(t)

        for row in d:                                       ##table with all info
            tab.add_row(row)

        ##n = int(input("Введите возрастной ограничитель: ")) ##enter "n"
        ##for row in d:
            ##if int(row[2]) >= n:                            ##table with older "n" age
                ##tab.add_row(row)

        table = tab.draw()
        print(table)

    def add_new_info(self):                                   ##add new student and write new file

        new_number = self.data[-1][0]
        new_fio = input("Введите ФИО нового студента: ")
        new_age = input("Введите возраст нового студента: ")
        new_group = input("Введите группу нового студента: ")

        with open(path, encoding='utf-8') as r_file:
            old_data = []
            reader = csv.reader(r_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            for i in reader:
                old_data.append(i)

        new_data = old_data + [[str(int(new_number)+1),
                               str(new_fio),
                               str(new_age),
                               str(new_group)]]

        new_csv = str(path[:-4] + '_changed.csv')

        with open(new_csv, 'w', encoding='utf-8', newline='') as n_file:
            writer = csv.writer(n_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(new_data)

        print("Новые данные сохранены в новый файл " + new_csv + "!")


s = Students()
s.read_file(path)
s.add_new_info()
s.read_file(path2)