
def greet(name):
    message = 'Hello, ' + name + '-san!'
#もしname=San を入力したら、 message に Hello San -san!になる。
from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    
    print(message)


greet('Inoue')
