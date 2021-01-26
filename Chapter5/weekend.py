print()
import datetime
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
currentDate = datetime.date.today()
presentDay = currentDate.weekday()
today = days[presentDay]
timeToWeekend = 6 - presentDay
print(f'{timeToWeekend - 1} days until the weekend.')
ansPrint = 0
for e in days[presentDay:timeToWeekend]:
    if (today == 'Monday' or today == 'Wednesday') and ansPrint == 0:
        print(f'{today}: get ready for class at 10:15 AM.')
        ansPrint = 1
    elif (today == 'Tuesday' or today == 'Sunday') and ansPrint == 0:
        print(f'{today}: work on homework for class tomorrow.')
        ansPrint = 1
    elif (today == 'Thursday' or today == 'Friday' or today == 'Saturday') and ansPrint == 0:
        print(f'{today}: feel free to do chores or relax!')
        ansPrint = 1
    else:
        print(e)
print()
