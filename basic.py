import os
import codecs

path = 'D:/PythonProject/Crawler/GwentUp/'
domains = ['中立牌组','怪物牌组','尼弗迦德帝国牌组','北方领域牌组',"松鼠党牌组",'史凯利杰牌组']
classes = ['卡牌','说明']


# 获取指定路径下所有文件名
def get_log_path_dict(log_path):
    file_name = []
    for root,dir,files in os.walk(log_path):
        # print(files)
        for file in files:
            file_name.append(file)
    return file_name
# print(get_log_path_dict(os.path.join(path,domain[0],class_[0])))


# 遍历文件夹创建空文档用于存放卡片内容描述
for domain in domains:
    card_path = os.path.join(path,domain,classes[0])
    # print(card_path)
    file_name = get_log_path_dict(card_path)
    # print(file_name)
    for name in file_name:
        name_ = name[:-4]+'.txt'
        note_path = os.path.join(path,domain,classes[1],name_)
        print(note_path)
        if not os.path.exists(note_path):
            with codecs.open(note_path,'a+') as f:
                print(note_path+' file created! ')
        else:
            print(note_path+' file found!')


