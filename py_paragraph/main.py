import re
file = open("american_tabloid.txt", "r")
sample = file.read()

print (re.split("(?<=[.!?]) +", sample))
# print sample