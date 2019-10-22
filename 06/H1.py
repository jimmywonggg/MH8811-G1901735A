import passwd

n = int(input('Please input password length: '))
# generate password
passwd = passwd.genPassword(n)
print(passwd)