import csv
import random

datei = csv.reader(open('DoneDone.csv', newline=''))


class RandomQuest:
    def __init__(self):
        self.quest = None
        self.question = None
        self.answer = None
        self.wanswer = None
        self.datei = csv.reader(open('DoneDone.csv', 'r'))

    def getquest(self):
        for d in self.datei:
            self.quest = random.sample(list(self.datei), 2)
            # print(self.quest, type(self.quest))

        self.question = self.quest.copy().pop(0)
        self.answer = self.question.pop(0)
        self.wanswer = self.quest.pop(1).pop(0)

        #print(self.question, self.answer, self.wanswer)
        return self.question, self.answer, self.wanswer


r = RandomQuest()
r.getquest()
