import re
email = input("What is your email addres? ").strip()
# re.search(pattern, string, flags=0)

            # r - raw string - pass exacly as is
            #[^] compliment you cannot match any of the items

if re.search(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_]+\.edu$", email): #finite state machine
    print("Valid")
else:
    print("Invalid email address")

