#1
import re
enter = input("enter: ")
text = r"ab*"
match = re.findall(text, enter)
print("'a' followed by zero or more 'b''s")
print(match)

#2
enter = input("enter ")
text = r"ab{2,3}"
match = re.findall(text, enter)
print(match)

#3
enter = input("enter ")
text = r"[a-z]+(?:_[a-z]+)+"
match = re.findall(text, enter)
print(match)