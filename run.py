from datetime import datetime
import time
import rand
import calendarController
# User input
mealTime = [1, 15, 18]  # Meal times in hours
cal_out = 89
#logic something lol
gotten_meal = True #by the meaning this should be false
while gotten_meal: 
    # Get the current time
    current_time = datetime.now().strftime('%H:%M')
    hr, min = map(int, current_time.split(':'))
    current_date = datetime.now().strftime('%Y-%m-%d')
    x = calendarController.get(current_date)
    if x:
        x = len(x)
    else:
        x = 0
    # check if have meal yet
    if x  < 3:
        for meal in mealTime:
            if hr == meal and min >= 0  and min <= 59 :
                a = rand.Food(cal_out)
                a.refresh()
                a.foodrandom()
                b = a.__dict__
                print(b['randFoodList'])
                gotten_meal = False #this too should be true by the meaning

    print('loop')
    # Add a delay to avoid a tight loop
    time.sleep(10)
