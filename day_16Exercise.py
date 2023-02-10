#quation_1
from datetime import datetime
from datetime import datetime
now = datetime.now()
 # dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("The current date and time are:", dt_string)
#quation_3
date_str = '05-12-2019'

date_object = datetime.strptime(date_str, '%m-%d-%Y').date()
print(type(date_object))
print(date_object)  
#quation_4
import datetime
next_year_time=datetime.datetime(2024,1,1)
current_time=datetime.datetime.now()
diff=next_year_time-current_time
print("The time difference in second is",int(diff.total_seconds()/(60)))
#quation_5
import datetime
today = datetime.datetime.now()
given_date = datetime.datetime(1970,12,5)
diff = today-given_date
print("The time difference between the current time with the given time is:",diff)


