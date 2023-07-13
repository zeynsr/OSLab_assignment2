sum = int(input())
hour = int(sum/3600)
if int(hour/10) == 0:
    hour = '0' + str(hour)
sum = int(sum - (int(hour)*3600))
minute = int(sum/60)
if int(minute/10) == 0:
    minute = '0' + str(minute)
second = int(sum - (int(minute)*60))
if int(second/10) == 0:
    second = '0' + str(second)

print(str(hour) + ':' + str(minute) + ':' + str(second))
