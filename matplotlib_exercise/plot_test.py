import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [11,22,33,44,55]

# --- Figure 1: Line Plot ---
plt.figure()
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("line_plot.png", dpi=300, bbox_inches="tight")

# --- Figure 2: Bar Plot ---
plt.figure()
plt.bar(x, y)
plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("bar_plot.png", dpi=300, bbox_inches="tight")

# --- Figure 3: Scatter Plot ---
plt.figure()
plt.scatter(x, y)
plt.title("Scatter Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("scatter_plot.png", dpi=300, bbox_inches="tight")

# --- Figure 4: Histogram ---
plt.figure()
data = np.random.randn(1000)
plt.hist(data, bins=30, color="purple", edgecolor="black")
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.savefig("histogram.png", dpi=300, bbox_inches="tight")

# Show all figures (each will open in its own window)
plt.show()
