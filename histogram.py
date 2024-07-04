
import matplotlib.pyplot as plt
a=[12,8,78,94,34,3,56,90,33.76,65,45,53,42,28,23,20,68,20,18,31,12,16,10]
plt.hist(a,bins=10,edgecolour="black")
plt.xlabel("a")
plt.ylabel("frequency")
plt.title("student marks histogram")
plt.show()
