# importing userinput.py to main.py to access the defined variables
import userinput

# printing recipients name and age as per Assignment request.
print(f"Hi {userinput.recipient_name}, let celebrate your {userinput.age} years of awesomeness! \n Wishing you a day "
      f"filled with joy and laughter as you turn {userinput.age}!")

# print personalized message
print(userinput.special_message)

# print sender's name
print(userinput.sender_name)
