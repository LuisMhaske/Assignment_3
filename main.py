import userinput
import datetime

today = datetime.date.today()
curr_year = today.year
age = curr_year - userinput.birth_year
print(userinput.recipient_name, age)
