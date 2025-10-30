import matplotlib.pyplot as plt
import random

# Part 1: Simple Plot Line
def plot_line():
    x = list(range(1, 11))
    y = [i**2 for i in x]

    plt.title("Squares of Numbers")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.plot(x, y, color="red", linestyle="--", marker="o")
    plt.grid()
    plt.show()

# Part 2: Scatter Plot
def scatter_plot():
    x_scatter = [random.randint(0, 100) for _ in range(50)]
    y_scatter =  [random.randint(0, 100) for _ in range(50)]

    plt.scatter(x_scatter, y_scatter, s = 10, c = "#332364", label = "Random Points", marker = "x")
    plt.title("Random Scatter Plot")
    plt.xlabel("XValues")
    plt.ylabel("YValues")
    plt.legend()
    plt.show()

# Part 3: Bar Chart
def bar_chart():
    categories = ["A", "B", "C", "D", "E"]
    values = [20, 35, 30, 25, 40]

    plt.bar(categories, values, color="#332364")
    plt.title("Category Values")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.show()


# Part 4: Customization
while True:

    print("\n============================================")
    print("===== Visualizing Data with Matplotlib =====")
    print("============================================\nOptions:")
    print("[1] - Plot Line")
    print("[2] - Scatter Plot")
    print("[3] - Bar Chart")
    print("[4] - Exit")

    enterChoice = input("\nEnter what you want to see: ")
    if enterChoice == "1":
        plot_line()

    elif enterChoice == "2":
        scatter_plot()

    elif enterChoice == "3":
        bar_chart()

    elif enterChoice == "4":
        break

    else:
        print("The choice only contains 1, 2, 3, & 4")