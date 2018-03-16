from datetime import datetime

today = datetime.now()
brazil_birthday = datetime(1500, 4, 22)
delta = today - brazil_birthday

print("Today is %s" % today.strftime("%Y-%m-%d"))
print("%s days have been passed since Brazil was discovered" % delta.days)

brazil_republic_birthday = datetime.strptime("1889-11-15", "%Y-%m-%d")

print("Brazil is a republic since %s" % brazil_republic_birthday)