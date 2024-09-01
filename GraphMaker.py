#run all at the same time

import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datasets import load_dataset

# #report 1 
# df1a = df1.groupby(['month'])['totalUsers'].sum()
df1 = pd.read_csv("Example-Report-2023-1-01report1.csv") 
sns.relplot(data=df1, x="month", y="totalUsers", kind="line")
plt.title("Total Users by Month")
plt.savefig('report1.png')
#plt.show()
#print('saving image 1')

#report 2
df2 = pd.read_csv("Example-Report-2023-1-01report2.csv") 
df2a = df2.groupby(['month'])['averageSessionDuration'].sum()
df2a.plot(x="month", y="averageSessionDuration", kind="bar")
plt.title("Average Session Duration by Month")
plt.xlabel("Month")
plt.ylabel("Average Session Duration")
plt.savefig('report2.png')
print('saving image 2')

#check to ensure counting and grouping all data#
 
#report 3
df3 = pd.read_csv("Example-Report-2023-1-01report3.csv") 
#df3a = df3.groupby(['region'])['eventsPerSession'].sum()
df3atop10 = df3.sort_values(by="eventsPerSession", ascending=False).head(10)
df3atop10.plot(x="region", y="eventsPerSession", kind="bar")
plt.subplots_adjust(bottom=0.3)
plt.title("Events Per Session by Region")
plt.xlabel("Region")
plt.ylabel("Events Per Session")
plt.savefig('report3.png')
print('saving image 3')

#report 4
df4 = pd.read_csv("Example-Report-2023-1-01report4.csv") 
#df4a = df4atop10.groupby(['pagePath'])['sessions'].sum()
df4atop10 = df4.sort_values(by="sessions", ascending=False).head(10)
df4atop10.plot(x="pagePath", y="sessions", kind="bar")
plt.subplots_adjust(bottom=0.3)
plt.title("Sessions by Page Path")
plt.xlabel("Page Path")
plt.ylabel("Sessions")
plt.savefig('report4.png')
print('saving image 4')

#report 5
df5 = pd.read_csv("Example-Report-2023-1-01report5.csv") 
#df5a = df5atop10.groupby(['sessionSource'])['sessions'].sum()
df5atop10 = df5.sort_values(by="sessions", ascending=False).head(10)
df5atop10.plot(x="sessionSource", y="sessions", kind="bar")
plt.subplots_adjust(bottom=0.3)
plt.title("Sessions by Session Source")
plt.xlabel("Session Source")
plt.ylabel("Sessions")
plt.savefig('report5.png')
print('saving image 5')