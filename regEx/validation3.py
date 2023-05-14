# format 
import re
name = input("Whatis is your name ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):  # := if and only if 
    name = matches.group(1) + " " + matches.group(2)

print(f"hello, {name}")