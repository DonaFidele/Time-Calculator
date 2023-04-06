#coding:utf-8

def add_time(hour,duration,days=None):
    dict={1:13,2:14,3:15,4:16,5:17,6:18,7:19,8:20,9:21,10:22,11:23,12:0}
    liste=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    
    h1=int(hour.split(':')[0])    
    h2=int((hour.split(':')[1])[:-2])

    d1=int(duration.split(':')[0])
    d2=int(duration.split(':')[1])

    heure=0
    minute=h2+d2
    if minute > 60 :
        heure+=1
        minute -=60

    heure+=h1+d1

    while heure > 12:
        heure=heure-12

    # détermination des AM et PM   
    if hour[-2:] == 'PM':
        jour=0
        h=dict[h1]
        h+=d1
        h2+=d2

        if h2 > 60:
            h+=1
            h2-=60
        while h>=24:
            h-=24
            jour+=1
        if h>=12:
            t="PM"
        else:
            t="AM"
    else:
        jour=0
        h1+=d1
        h2+=d2
        if h2 > 60:
            h1+=1
            h2-=60
        while h1>=24:
            h1-=24
            jour+=1
        if h1>=12:
            t="PM"
        else:
            t="AM"

    if days!=None:
        if jour==0:
            return f"{heure}:{minute:02d} {t}, {days}"
        elif jour==1:
            return f"{heure}:{minute:02d} {t}, {liste[(liste.index(days.capitalize())+jour)]} (next day)"
        else:
            return f"{heure}:{minute:02d} {t}, {liste[(liste.index(days.capitalize())+jour)%7]} ({jour} days later)"

    else:
        if jour==0:
            return f"{heure}:{minute:02d} {t}"
        elif jour==1:
            return f"{heure}:{minute:02d} {t} (next day)"
        else:
            return f"{heure}:{minute:02d} {t} ({jour} days later)"


print(add_time("3:00 PM", "3:10"))
# Returns: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Returns: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Returns: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Returns: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tueSday"))
# Returns: 12:03 AM, Thursday (2 days later)

print(add_time("6:30 PM", "205:12"))
# Returns: 7:42 AM (9 days later)
