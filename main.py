import re
import datetime
import collections
import csv 

dt_now = datetime.datetime.now()
path = dt_now.strftime('%Y%m%d')+'.txt'

#発言者 時間 最初の行 に成形
with open(path,encoding='utf-8') as f:
    lines_strip = [line for line in f.readlines()]
    first_line = [c for c in lines_strip if bool(re.match(r'\d+:\d+\t.*\t.*|\d+/\d+/\d+\(.\)',c))]
    for i in range(len(first_line)):
        first_line[i].split()

# 昨日から今日までの会話を抽出
talk_list = []#会話を格納
count = 0#探索用
#正規表現用に使う 今日→t_ 昨日y_
t_day = (datetime.datetime.now()).day
t_year = (datetime.datetime.now()).year
t_month = (datetime.datetime.now()).month
y_day = (datetime.datetime.now() + datetime.timedelta(days = -1)).day
y_year = (datetime.datetime.now() + datetime.timedelta(days = -1)).year
y_month = (datetime.datetime.now() + datetime.timedelta(days = -1)).month
t_date = str(t_year) + '/' + str(t_month) + '/' + str(t_day)
y_date = str(y_year) + '/' + str(y_month) + '/' + str(y_day)

#会話の抽出
while(not bool(re.match(y_date + r'+\(.\)',first_line[count]))):
    count += 1
count += 1
while(not bool(re.match(t_date + r'+\(.\)',first_line[count]))):
# while(count != len(first_line)):
    talk_splited = first_line[count].split("\t")
    if(not bool(re.match(r'.*\[スタンプ\].*',talk_splited[2]))):    
        talk_list.append(talk_splited[1])
    count += 1
    

#発言回数のカウント
counted = sorted(collections.Counter(talk_list).items(), key=lambda x:x[1], reverse=True)
    
#CSV出力
y_date_ = (dt_now + datetime.timedelta(days=-1)).strftime("%Y%m%d")

with open(y_date_ +'.csv', 'w',  newline='', encoding='UTF-8') as csvf:
    writer = csv.writer(csvf)
    for c in counted:
        writer.writerow(c)
print()

