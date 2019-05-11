# Birthday list
import json
from collections import Counter

with open(r"C:\Users\tsida\PycharmProjects\First_Project\info.json", "r") as f:
    birthdayLibrary = json.load(f)

months = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July",
          "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"}

month=[]
for key in birthdayLibrary.keys():
    month.append(months[birthdayLibrary[key][0:2]])
print(month)

c = Counter(month)

print(c)