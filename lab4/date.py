#exercise1
import datetime
x = datetime.date.today()
print("Now:", x)
print("After substracting:", x - datetime.timedelta(5))

#exercise2
import datetime
x = datetime.date.today()
print("Yesterday:", x - datetime.timedelta(1))
print("Now:", x)
print("Tomorrow:", x + datetime.timedelta(1))

#exercise3
import datetime
x = datetime.datetime.now().replace(microsecond=0)
print(x)

#exercise4
import datetime
def difference(dt1, dt2):
    delta=dt2-dt1
    return delta.days*24* 3600 + delta.seconds
dt1 = input("Enter the first date: ")
dt2 = input("Enter the second date: ")
dt1=datetime.datetime.strptime(dt1, "%Y-%m-%d")
dt2=datetime.datetime.strptime(dt2, "%Y-%m-%d")
print(difference(dt1, dt2))


    



