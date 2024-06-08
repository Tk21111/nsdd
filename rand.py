import random
import copy
import read
import calendarController
from datetime import datetime
class Food:
    
    def __init__(self,cal_out) -> None:
        self.data = read.readfile('list.json')
        self.user = read.readfile('userConFig.json')
        current_time = datetime.now().strftime('%Y-%m-%d')
        time = calendarController.get(current_time)
        #food
        if time != None:
            for i in time:
                self.user["cal_in"] -= int(i['cal'])
            self.cal_in = self.user["cal_in"]
        else:
            self.cal_in = self.user["cal_in"]
        #exercise
        self.cal_out = cal_out
        self.food_list_500 = self.data['list_500']
        self.food_list_1000 = self.data['list_1000']
        self.food_list_1500 = self.data['list_1500']
        self.food_list_2000 = self.data['list_2000']
        self.randFoodList = ''
    
    def foodrandom(self):
        # convert to order string 
        if  self.cal_in <= 500 and self.cal_in > 0:
            food_list =  copy.deepcopy(self.food_list_500)
        elif self.cal_in <= 1000:
            food_list =  copy.deepcopy(self.food_list_1000)
        elif self.cal_in <=  1500:
            food_list =  copy.deepcopy(self.food_list_1500)
        elif self.cal_in <=  2000:
            food_list =  copy.deepcopy(self.food_list_2000)
        else:
            food_list = None

        randFood = random.randint(0,len(food_list)-1)
        self.randFoodList = food_list[randFood]
        calendarController.update(self.randFoodList)
        #print(self.randFoodList)
        
    def refresh(self):
        self.cal_in = self.user["cal_in"]
        
    def __str__(self):
        return self.randFoodList
    
    

#@ cal = int , dataIn = obj    
def addFood(cal,dataIn):
    dataIn = {"name" : "aiykhjbmnfhn", "ingredent" : "asdfdg" ,"cal" : 200}
    data = read.readfile("list.json")
    
    if cal <= 500:
        y = data['list_500']
        y.append(dataIn)
        data['list_500'] = y
    elif cal <= 1000:
        y = data['list_1000']
        y.append(dataIn)
        data['list_1000'] = y
    elif cal <=1500:
        y = data['list_1500']
        y.append(dataIn)
        data['list_1500'] = y
    elif cal <=2000:
        y = data['list_2000']
        y.append(dataIn)
        data['list_2000'] = y
    
    read.writeW('list.json',data)

#addFood(200,{})