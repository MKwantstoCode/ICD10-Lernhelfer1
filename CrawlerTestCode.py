import requests
from bs4 import BeautifulSoup
import csv

r = requests.get(
    'https://de.wikipedia.org/wiki/Liste_der_psychischen_und_Verhaltensst%C3%B6rungen_nach_ICD-10#F00%E2%80'
    '%93F09_Organische,_einschlie%C3%9Flich_symptomatischer_psychischer_St%C3%B6rungen',
    auth=('user', 'pass'))

unfinished = BeautifulSoup(r.text, "html.parser")
writer = csv.writer(open('FCode.csv', 'w'))

for row in unfinished.select(".wikitable tr"):
    rowlist = [text for text in row.stripped_strings]
    rowlist = rowlist[0:2]
    writer.writerow(rowlist)

