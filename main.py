import os
import csv

class Flow:
    def __init__(self):
        self.name = None
        self.restaurant = None

    def greet(self):
        print('こんにちは!私はRobokoです。あなたの名前は何ですか?')
        self.name = input()

    def question(self):
        print('{}さん。どこのレストランが好きですか?'.format(self.name))
        self.restaurant = input()

    def bye(self):
        print('{}さん。ありがとうございました。\n良い1日を！さようなら。'.format(self.name))

    def count(self):
        fileName = 'count.csv'
        with open(fileName, 'w+') as csv_file:
            fieldnames = ['Name', 'Count']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            dict = {}
            with open(fileName, 'r') as read_csv:
                reader = csv.DictReader(read_csv)
                for row in reader:
                    dict[row['Name']] = row['Count']

            if self.restaurant in dict:
                dict[self.restaurant] = dict[self.restaurant] + 1
            else:
                dict[self.restaurant] = 1

            for key in dict.keys():
                writer.writerow({'Name': key, 'Count': dict[key]})

if __name__ == '__main__':
    f = Flow()
    f.greet()
    f.question()
    f.count()
    f.bye()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
