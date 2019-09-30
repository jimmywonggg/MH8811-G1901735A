print('welcome!')
print('input the number you would like to choose. or input "exit" to quit this program')
print('01-say hello to the world!\n02- say hello to someone!\n03-know the temp')
while True:
    a=input('which one would you like to choose?(01 or 02 or 03 or exit)')
    if a =="01":
        print('hello,world')
        continue
    if a =="02":
        nam = input('who are you?')
        print('hello,',nam)
        continue
    if a =='03':
        c=input('temp in Celsius')
        f=float(c)*1.8+32
        print('Fahrenheit=',f)
        continue
    if a =='exit':
        print('thanks for your try! See you!')
        break