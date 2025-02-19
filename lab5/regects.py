import re
#1
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

#4
enter = input("enter ")
text = r"[A-Z][a-z]+"
match = re.findall(text, enter)
print(match)

#5
enter = input("enter ")
text = r"a.*b$"
match = re.findall(text, enter)
print(match)

#6
enter = input("enter ")
text = r",|/.|\s"
replaceto = ":"
match = re.sub(text, replaceto, enter)
print(match)