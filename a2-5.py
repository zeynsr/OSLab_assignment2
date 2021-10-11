sum=int(input())
h=int(sum/3600)
if int(h/10)==0:
    h='0'+str(h)
sum=int(sum-(int(h)*3600))
m=int(sum/60)
if int(m/10)==0:
    m='0'+str(m)
s=int(sum-(int(m)*60))
if int(s/10)==0:
    s='0'+str(s)

print(str(h)+':'+str(m)+':'+str(s))