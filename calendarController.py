import read
from datetime import datetime

#if in that day already have data 1 if not 2

def update(dataIn):
    data = read.readfile('configDate.json')
    current_time = datetime.now().strftime('%Y-%m-%d')
    if (current_time in data):
        print('1')
        x = data[current_time]
        x.append(dataIn)
        read.writeW('configDate.json',{current_time : x})
    else:
        print('2')
        read.writeW('configDate.json',{ current_time : [dataIn]})

#@ date => yyyy-mm-dd
#@ x => 0 === breakfast , 1 === lunch , 2 === dinner 
def get(date):
    data = read.readfile('configDate.json')
    print(date)
    if date in data:  
        x = data[date]
    else:
        x = None
    #whole day .cal , .name , .ingredent
    return x
#update({"name" : "omet" , "ingredent" : "egg" ,"cal" : 200})
#print(get("2024-06-08"))
    