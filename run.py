import random
from datetime import datetime
import time
import rand
# User input
age = 12
ibm = 1
mealTime = [23, 10, 52]  # Meal times in hours
cal_out = 89
#logic something lol
gg = age+ibm
gotten_meal = True #by the meaning this should be false
while gotten_meal: 
    # Get the current time
    current_time = datetime.now().strftime('%H:%M')
    hr, min = map(int, current_time.split(':'))

    for meal in mealTime:
        if hr == meal and min >= 0  and min <= 59:
            cal_in = gg
            a = rand.Food(cal_in ,cal_out)
            a.foodrandom()
            b = a.__dict__
            print(b['randFoodList'])
            gotten_meal = False #this too should be true by the meaning
        

    # Add a delay to avoid a tight loop
    time.sleep(60)  # Check every minute
