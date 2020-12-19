from operator import itemgetter

import texttable as tt

path = 'C:\\Users\\MC_VIC\\Dropbox\\1 семестр\\ПИ\\лр3\\students.csv'


class Students:

    def __init__(self):
        self.data = []
        self.title_data = []

    def read_file(self, path):
        file = open(path, 'r', encoding='utf-8')
        self.data = file.read()
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
            ##d = self.data                             ##original, no sorted data
            d = sorted(self.data, key=itemgetter(1))    ##sorted by surname data
        if t == None:
            t = self.title_data

        tab.header(t)

        for row in d:
            tab.add_row(row)

        table = tab.draw()
        print(table)


s = Students()
s.read_file(path)