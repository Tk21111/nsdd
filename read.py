import json
def readfile(fileName):
    with open(fileName) as f:
        data = json.load(f)

    return data

def writeW(fileName,data):
    with open(fileName, "w") as outfile:
        json.dump(data, outfile)