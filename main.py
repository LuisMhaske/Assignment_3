# importing userinput.py to main.py to access the defined variables
import userinput

print(100 * "-")
# printing recipients name and age as per Assignment request.
print(f"Hi {userinput.recipient_name}, let's celebrate your {userinput.age} years of awesomeness! \nWishing you a day "
      f"filled with joy and laughter as you turn {userinput.age}!")

# print personalized message
print(f"\n{userinput.special_message}")

# print sender's name
print(f"\nWith love and best wishes,\n{userinput.sender_name}")
