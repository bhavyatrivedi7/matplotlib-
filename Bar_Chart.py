import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
school=["Bhavya","Harshil","Rishil","Raj","Rushil"]
stu1=[13,24,24,27,11]
stu2=[15,23,28,14,22]
stu3=[17,19,29,24,10]
school_index=np.arange(len(school))
width=0.2
plt.bar(school_index,stu1,color="r",width=0.2)
plt.bar(school_index+width,stu2,color="g",width=0.2)
plt.bar(school_index+width+width,stu3,color="b",width=0.2)
plt.xticks(school_index+width,school)
plt.title("King School")
plt.xlabel("School Name")
plt.ylabel("Students")
style.use("ggplot")
plt.legend(["stu1","stu2","stu3"])
plt.show()
