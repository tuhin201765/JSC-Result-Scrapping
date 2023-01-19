import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import csv

data = {
'sr': '3',
'et': '2',
'exam': 'jsc',
'year': '2017',
'board': 'jessore',
'roll': '400173',
'reg': '1713114324',
'value_s': '15',
'button2': 'Submit',
}

link = 'http://www.educationboardresults.gov.bd/'
result_link = 'http://www.educationboardresults.gov.bd/result.php'


def create_value(s,link):
    res = s.get(link)
    soup = bs(res.text, 'html.parser')
    table = soup.find('table', {'class': 'black12bold'})
    trs = table.findAll('tr')
    tds = trs[6].findAll('td')
    captcha = tds[1].text
    x, y = captcha.split('+')
    value_s = str(int(x) + int(y))
    return value_s


s = requests.Session()
s.headers['headers'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
data['value_s']=create_value(s,link)
res = s.post(result_link,data=data)
data_2 = bs(res.text,'html.parser')
table = data_2.findAll('table')
trs=table[7].findAll('tr')
# tds = trs[1].findAll('td')
data_list = []
# for td in tds:
#     data_list.append(td.text)

for tr in trs:
    throw = tr.findAll('td')
    for trw in throw:
        thro = trw.text.replace('\n','-')
        data_list.append(thro)

list_of_result = data_list[1:25]
all_dic = dict(zip( list_of_result[0::2],list_of_result[1::2]))
print(all_dic)
# print(data_list)
with open('links.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=all_dic.keys())
    writer.writerow(all_dic)

