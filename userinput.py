import datetime

"""importing datetime so that we can retract the current year """
"""incase the program is used next year it will have the correct year to do the maths."""

today = datetime.date.today()
curr_year = today.year  # getting current year from today's date.
recipient_name = input("Please enter recipient_name: ")
birth_year = input("Please enter the year of birth: ")
birth_year = int(birth_year)  # type casting str to int
age = curr_year - birth_year
special_message = input("Please enter a personalized message: ")
sender_name = input("Please enter your name: ")
