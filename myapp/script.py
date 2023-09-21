import matplotlib.pyplot as plt
from lib import read_dataset, top_salesperson, most_sold_make, most_sold_model


if __name__ == "__main__":
    # Fetch dataset
    working_df = read_dataset()
    print(working_df.head())

    # Fetch top sales from lib and print
    top_sales_p = top_salesperson()
    print(top_sales_p)

    # Prepare top sales bar chart and plot
    fig = plt.figure(figsize=(10, 5))
    plt.bar(top_sales_p.index, top_sales_p, color="maroon", width=0.4)

    plt.xlabel("Sales Representatives")
    plt.ylabel("No. of cars sold")
    plt.title("Total Sales Report (2023)")
    plt.savefig("./reports/tsp.png")
    plt.show()

    # Fetch top sales by car make from lib and print
    msc = most_sold_make()
    print(msc)

    # Create a pie chart for top sales by car make
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.pie(msc, labels=msc.index, autopct="%1.1f%%", startangle=90)
    ax.axis("equal")
    ax.set_title("Distribution of Car Makes")
    plt.savefig("./reports/msc.png")
    plt.show()

    # Fetch top sales by car model from lib and print
    msm = most_sold_model()
    print(msm)

    # Prepare and plot top sales by car make chart
    fig, ax = plt.subplots(figsize=(10, 5))

    ax.barh(msm.index, msm)
    # Add annotation to bars
    for i in ax.patches:
        plt.text(
            i.get_width() + 0.2,
            i.get_y() + 0.5,
            str(round((i.get_width()), 2)),
            fontsize=10,
            fontweight="bold",
            color="grey",
        )

    ax.set_title(
        "Most Sold Car Models",
        loc="left",
    )
    ax.set_xlabel("Number Sold")
    ax.set_ylabel("Car Models")
    plt.savefig("./reports/msm.png")
    plt.show()
