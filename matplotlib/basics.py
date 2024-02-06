import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [1, 4, 9, 16, 25, 36]

fix, ax = plt.subplots()

ax.plot(x, y)

ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_title("Line Plot")

plt.show()
