from flask import Flask
app = Flask('app')

@app.route('/')
def hello():
  return 'Hello and welcome to password creator! Give me one second to create your password... ' + 'die'  + password + 'haha i pranked you now remember dont trust things you think are a scam'
import random
length = input ("How long do you want your password?")
length = 90000
password = ''
lowercase = '1234567890'
for i in range(int(length)):
  randchar = random.choice(lowercase) 
  password = password + randchar
print ("die" + password + ' you are now being hacked')
print("haha i prank you")
print("and remember dont trust things that you think are scams")
@app.route('/')
def lol():
  return ("lol") + password + ("haha")
app.run(host='0.0.0.0', port=8080)