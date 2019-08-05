# -*- coding: utf-8 -*-
import os
import codecs
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote

# 中文不能直接读取，需要先用urllib.parse.quote转码
domains = ["中立牌组","北方领域牌组","尼弗迦德帝国牌组","松鼠党牌组","怪物牌组","史凯利杰牌组"]
classes = ['卡牌','说明']
path = 'D:/PythonProject/Crawler/GwentUp/'
url = "https://witcher.huijiwiki.com/wiki/"


for domain in domains:
    html = url+quote(domain)
    content = urlopen(html).read().decode('UTF-8')
    soup = BeautifulSoup(content,'html.parser')
    # 读取所有tag为tr的网页信息，抽取td项
    for tag in soup.find_all('tr'):
        card = tag.find_all('td')
        try:
            # 由于windows系统不可用'/ ? * : | \ < >'字符命名的文件，将':'替换为'：'
            name = card[1].get_text().strip()
            name = name.replace(':','：')
            role = card[2].get_text().strip()
            power = card[3].get_text().strip()
            # 获取<a><title='',...></a>中title的类名
            try:
                position = card[4].find('a')['title']
            except (KeyError,TypeError):
                position = 'N/A'
            ability = card[5].get_text().strip()
            fetch = card[6].get_text().strip()
            source = card[7].get_text().strip()
        except IndexError:
            continue
        print('\n')
        print('---name:',name,'\n',
              '---role:',role,'\n',
              '---power:',power,'\n',
              '---position',position,'\n',
              '---ability:',ability,'\n',
              '---fetch:',source,'\n',
              'source:',fetch)
        name_ = name+'.txt'
        path_ = os.path.join(path,domain,classes[1],name_)
        print(path_)
        if len(name)>0:
            with codecs.open(path_,'w+') as f:
                f.write(name)
                f.write(' ')
                f.write(role)
                f.write(' ')
                f.write(power)
                f.write(' ')
                f.write(position)
                f.write(' ')
                f.write(ability)
                f.write(' ')
                f.write(source)
                f.write(' ')
                f.write(fetch)
        else:
            print('Wrong format!')





