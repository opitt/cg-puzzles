# this is correct
import datetime
n=int(input())
if n%1000>500:n+=1000
print("24plus"if n>86400000 else datetime.datetime.fromtimestamp(n/1000).strftime("%H:%M:%S"))

# this is not correct ... but what is wrong?
d=divmod
m,s=d(round(int(input())/1000),60)
h,m=d(m,60)
print([f"{h:02}:{m:02}:{s:02}","24plus"][h>24])
