def jimmy():
    print('welcome!')
    print('input the number you would like to choose. or input "exit" to quit this program')
    print('01-say hello to the world!')
    print('02-say hello to someone!')
    print('n03-know the temp')
    while True:
        a=input('which one would you like to choose?(01 or 02 or 03 or exit)')
        if a =="01":
           print('hello,world')
        elif a =="02":
           nam = input('who are you?')
           print('hello,',nam)
        elif a =='03':
           c=input('temp in Celsius')
           f=float(c)*1.8+32
           print('Fahrenheit=',f)
        elif a =='exit':
           print('thanks for your try! See you!')
        else:
           print('sorry,please try again, type 01/02/03 or exit')
jimmy()