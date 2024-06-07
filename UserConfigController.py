import read    
#@use key , value instead of obj
def update(key , value):
    x = read.readfile('userConFig.json')
    x[key] = value
    
    read.writeW('userConFig.json', x)
    
#write({"username" : "meow"})
#update("op" , "cd")