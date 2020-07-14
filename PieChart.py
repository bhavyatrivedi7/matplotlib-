import matplotlib.pyplot as plt
school=["bhavya","rishil","harshil","tatva","rushil"]
x=[24,19,34,32,22]
colors=["r","g","b","m","y"]
plt.pie(x,labels=school,autopct="%0.2f%%",radius=1.4,shadow=True,explode=[0.1,0,0,0,0],colors=colors,)
plt.show()
