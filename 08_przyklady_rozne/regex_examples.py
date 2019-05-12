import re

tekst ="""16-03-2012 16-03-12 aaaa 11-02-1980 123-22-2010202"""

pattern =re.compile('^\d{2}-\d{2}-\d{2,4}| \d{2}-\d{2}-\d{2,4} | \d{2}-\d{2}-\d{2,4}$, re.MULTILINE)

results =pattern.findall(tekst)
print(results)