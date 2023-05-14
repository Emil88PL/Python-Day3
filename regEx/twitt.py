import re
url = input("URL: ").strip()

# non-capturing version

if matches := re.search(r"^(https?://)?(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
 print(f"Username: ", matches.group(2))
    



# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)

# print(f"Username: {username}")



