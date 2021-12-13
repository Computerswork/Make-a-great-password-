import random
length = input ("How long do you want your password?")
length = 90000
password = ''
lowercase = '1234567890'
for i in range(int(length)):
  randchar = random.choice(lowercase)
  password = password + randchar
print("die" + password + ' you are now being hacked')
print("haha i prank you")
print("and remember dont trust things that you think are scams")