
import statistics
import pandas as pd
import os
os.system("cls")
df = pd.read_csv("Internet Users.csv")
users = df["InternetUsers"].tolist()
sum = 0
for i in users:
    sum+=float(i)
mean = sum/len(users)

n = len(users)
if n%2==0:
    n1 = users[n//2]
    n2 = users[(n//2)-1]
    median = (n1+n2)/2
else:
    median = users[n//2]

mode = statistics.mode(users)
print("Mode: " + str(mode))
print("Median: " + str(median))
print("Mean: " + str(mean))
