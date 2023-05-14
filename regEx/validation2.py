import re
email = input("What is your email addres? ").strip()  #.lower()
# re.search(pattern, string, flags=0)

            # r - raw string - pass exacly as is
            #[^] compliment you cannot match any of the items

if re.search(r"^\w+@\w+\.(com|edu|uk|org)$", email, re.IGNORECASE): #finite state machine #lower()
    print("Valid")
else:
    print("Invalid email address")

