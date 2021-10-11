time=input('enter the time(hh:mm:ss) :')
t=time.split(":")
h=int(t[0])*3600
m=int(t[1])*60
s=int(t[2])*1
sum=s+m+h
print(sum)