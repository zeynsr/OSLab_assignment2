time = input('enter the time(hh:mm:ss) :')
t = time.split(":")
hour = int(t[0])*3600
minute = int(t[1])*60
second = int(t[2])*1
sum = second + minute + hour
print(sum)
