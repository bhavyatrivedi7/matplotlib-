import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random
x=np.random.randint(10,20,(10))
y=np.random.randint(12,20,(10))
print("values of x is: ",x)
print("values of y is: ",y)
bins=[10,12,14,16,18,20]
style.use("ggplot")
plt.hist([x,y],bins,rwidth=0.8,color=["g","m"],orientation="vertical")
plt.title("age X&Y")
plt.xlabel("age")
plt.ylabel("number of people")
plt.legend(["bhavya","rushil"])
plt.show()
