import re

with open("input.txt") as f:
    dane = f.read()


data_pattern = re.compile('\d{2}- \w{2}-\d{2,4}| \d{2}-\d{2}-\d{2,4} | \d{2}-\d{2}-\d{2,4}')
kody_pattern = re.compile('\d{2}-\d{3}| \d{5}} | \d{2}--\d{3}')
emaile_pattern = re.compile('[\w._\-}+@{\w._\-]+')


print(kody_pattern.findall(dane))
print(data_pattern.findall(dane))
print(emaile_pattern.findall(dane))