import pandas as pd
import math
from selenium.common.exceptions import NoSuchElementException
import translators as ts
from datetime import datetime
import dateparser
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

df = pd.read_excel("myversion.xlsx")

to_b_drpd = []
for n in range(len(df)):
    if ';' in df['G04Q52V'][n]:
        nicks=df['G04Q52V'][n].split(';')
        to_b_drpd.append(n)
        for z in nicks:
            new_obs=df.iloc[[n]]
            new_obs['G04Q52V']=z
            df= pd.concat([df, new_obs], ignore_index=True)
df=df.drop(to_b_drpd)



authors=df['G04Q52V'].to_list()
df=pd.read_csv("enquetediscussionlinks.csv")

final_list = []

try:
    dati = pd.read_csv(
        "enquetediscussiondata.csv")
    starting_point = max(dati['step_of_process'])
except:
    pd.DataFrame(final_list,
                 columns=[
                     'comment',
                     'tag',
                     'sender',
                     'receiver',
                     'datetime',
                     'historical_discussion_link',
                     'pagelink',
                     'step_of_process',
                 ]).to_csv(
        "enquetediscussiondata.csv", index=False)

contribution_links = pd.read_csv("enquetesubjectcontributionlinks.csv")['0'].to_list()

options = Options()
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(options=options)
starting_point = 0


for author_id in range(starting_point+1, len(authors)):
    final_list = []
    all_author_comments = []
    data=df.loc[df['author'] == authors[author_id]]
    for z in range(len(data)):
        author=data['author'][z]
        link=data['historical_discussion_link'][z]
        driver.get(link)
        commenti = []
        pagelink=link.split('&oldid')[0]
        commenti_tag = []
        elementi=driver.find_elements(By.TAG_NAME, 'span')
        for l in driver.find_elements(By.TAG_NAME, 'span'):
            try:
                if 'data-mw-comment-start' and 'c-' + author in l.get_attribute('outerHTML'):
                    txt=1
                    if l.find_element(By.XPATH, '..').tag_name=='dd':
                        txt=l.find_element(By.XPATH, '..').text
                    elif l.find_element(By.XPATH, '..').find_element(By.XPATH,'..').tag_name!='dd':
                        txt=l.find_element(By.XPATH, '..').find_element(By.XPATH, '..').find_element(By.XPATH,'..').text
                    elif l.find_element(By.XPATH, '..').find_element(By.XPATH, '..').find_element(By.XPATH,'..').tag_name=='dd':
                        txt=l.find_element(By.XPATH, '..').find_element(By.XPATH, '..').find_element(By.XPATH,'..').text
                    if type(txt)==str:
                        if txt not in commenti:
                            if l.get_attribute('id') != '':
                                commenti.append(txt)
                                commenti_tag.append([txt, l.get_attribute('id')])

            except:
                pass
        for n in commenti_tag:
            banana = []
            half1 = n[1].split('c-', 1)[1]
            if half1.count('-') == 3:
                if author in half1.split('-', 3)[0]:
                    try:
                        date = half1.split('-', 3)[1]
                        n.append(half1.split('-', 3)[0])
                        n.append(half1.split('-', 3)[2])
                        n.append('{}/{}/{} {}:{}:{}'.format(date[0:4], date[4:6],
                                                        date[6:8],
                                                        date[8:10], date[8:10],
                                                        date[10:12]))
                        n.append(link)
                        n.append(pagelink)
                    except:
                        print(
                            'An error occurred in the data collection process due to '
                            'data format. ')
            elif half1.count('-') == 7:
                if author in half1.split('-', 6)[0]:
                    try:
                        date = half1.split('.000Z', 1)[0]
                        date = date.split('-', 1)[1]
                        n.append(half1.split('-', 6)[0])
                        n.append(half1.split('-', 6)[4])
                        n.append('{}/{}/{} {}'.format(date[0:4], date[5:7], date[8:10],
                                                  date.split('T', 1)[1]))
                        n.append(link)
                        n.append(pagelink)
                    except:
                        print(
                            'An error occurred in the data collection process due to '
                            'data format. ')
            if len(n)== 7:
                all_author_comments.append(n)

    for element in all_author_comments:
        if any(element[1] in sublist for sublist in final_list):
            pass
        else:
            element.append(author_id)
            final_list.append(element)
            print(element)

    for y in final_list:
        pd.DataFrame([y]).to_csv("enquetediscussiondata.csv", mode='a', index=False, header=False)

