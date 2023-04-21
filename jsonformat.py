import json # javascript object notation

def json_open(file):
    with open(file,'r') as f:
        jsonfile=json.load(f)
    return jsonfile

def save_json(file,change):
    with open(file,'w') as f:
        json.dump(change,f,indent=2)

def print_to_screen(file):
    with open(file,'r') as f:
        jsonfile=json.load(f)
        print(json.dumps(jsonfile,indent=2))

class car(object):
    def __init__(self,make,model,trans,color,doors=4,features={}):
        self.make=make
        self.model=model
        self.trans=trans
        self.color=color
        self.doors=doors
        self.features=features

def save_object_as_json(file,info):
    with open(file,'w') as f:
        json.dump(vars(info),f,indent=2)
    
def main():
    car=json_open("car.json")
    """
    print(car)
    print(type(car)) # dictionary
    print(car.keys()) # {keys:values}
    print(car['mycar'])
    print(car['mycar']['model'])
    print(car['mycar']['features'])
    car['mycar']['color']='black' # change made
    save_json("car.json",car)
    print_to_screen("car.json")
    mycar=car("Chevy","Cruze","manual","silver",5,{"tv":true,})
    print(vars(mycar)) # prints variables of the class, only self.""
    """
    save_object_as_json("newcar.json",mycar) # file that will be written to
    
main()
