from matplotlib import pyplot as plt

a=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
oa = [1.0,0.866,0.85,0.808,0.766,0.7583,0.7583,0.75,0.75]

plt.plot(a,oa)
plt.xlabel("α")
plt.ylabel("Accuracy")
plt.title("Accuracy v.s. α")
plt.show()