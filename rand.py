import random
import copy
import json

class Food:
    
    def __init__(self,cal_in,cal_out) -> None:
        with open('list.json') as f:
            data = json.load(f)
        #food
        self.cal_in = cal_in
        #exercise
        self.cal_out = cal_out
        self.food_list_500 = data['list_500']
        self.food_list_1000 = []
        self.food_list_1500 = []
        self.food_list_2000 = []
        self.randFoodList = ''
    
    def foodrandom(self):
        # convert to order string 
        if  self.cal_in < 500 :
            food_list =  copy.deepcopy(self.food_list_500)
        elif self.cal_in <1000:
            food_list =  copy.deepcopy(self.food_list_1000)
        elif self.cal_in < 1500:
            food_list =  copy.deepcopy(self.food_list_1500)
        elif self.cal_in < 2000:
            food_list =  copy.deepcopy(self.food_list_2000)

        randFood = random.randint(0,len(food_list)-1)
        self.randFoodList = food_list[randFood]
        #print(self.randFoodList)
        
    def __str__(self):
        return self.randFoodList
    
    ###def __str__(self):
        return(str(self.cal_in) + ' ' + str(self.cal_out) )
    ###

#@ cal = int , dataIn = obj    
def addFood(cal,dataIn):
    dataIn = {"name" : "adsfg", "ingredent" : "asdfdg"}
    with open('list.json') as f:
            data = json.load(f)
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
    with open("list.json", "w") as outfile:
        json.dump(data, outfile)

