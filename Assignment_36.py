# Birthday list
import json
from collections import Counter
from bokeh.plotting import figure, show, output_file

with open(r"C:\Users\tsida\PycharmProjects\First_Project\info.json", "r") as f:
    birthdayLibrary = json.load(f)

months = {"01":"January", "02":"February", "03":"March", "04":"April", "05":"May", "06":"June", "07":"July",
          "08":"August", "09":"September", "10":"October", "11":"November", "12":"December"}

month=[]
for key in birthdayLibrary.keys():
    month.append(months[birthdayLibrary[key][0:2]])

c = Counter(month)

output_file("plot.html")
x_months = list(c.keys())
y_counts = list(c.values())

p = figure(x_range=list(months.values()))
p.vbar(x=x_months, top=y_counts, width=0.5)
show(p)