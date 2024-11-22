# i_got_that.py
while True:
    user_input = input("Enter something (type 'STOP' to quit): ")
    if user_input.upper() == "STOP":
        print("Goodbye!")
        break
    else:
        print(f"I got that: {user_input}")
