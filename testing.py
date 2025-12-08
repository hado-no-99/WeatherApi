import re

date_pattern = r"^\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1])$"
temp = "1999-01-31"
match = re.search(date_pattern, temp)
pattern2=r"^\d+|(?:\d{4}-(?:0?[1-9]|1[0-2])-(?:0?[1-9]|[1-2][0-9]|3[0-1]))$"
temp2 = "222222"
match2 = re.fullmatch(pattern2, temp2)
print(match2)