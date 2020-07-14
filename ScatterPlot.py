import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
plt.figure(figsize=(16,9))
style.use("ggplot")
df=pd.read_csv("d:\\bhavya.csv")
x=df["Period"]
y=df["Data_value"]
plt.scatter(x,y,color="r",marker="o",s=80,linewidth=3)
plt.title("Electronics & sales")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.legend(["Sales"])
plt.show()
