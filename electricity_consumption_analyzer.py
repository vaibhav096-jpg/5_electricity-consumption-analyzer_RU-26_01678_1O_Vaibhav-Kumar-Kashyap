import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("usage.csv")
print(data)

original_units=data["Units"].copy()

data["Units"]=pd.to_numeric(data["Units"], errors='coerce')
invalid_units = data["Units"].isna()

for index in data[invalid_units].index:
    print("Row", index + 1," skipped: invalid Units" ,original_units[index])

negative_units = data["Units"] < 0

for index in data[negative_units].index:
    print("Row", index + 1," skipped: Units cannot be negative.")
valid_data=data[data["Units"].notna() & (data["Units"]>=0)]
print(valid_data)

units=valid_data["Units"].to_numpy()
total=np.sum(units)
print("Valid rows:", len(valid_data))
print("Total :", total,"units")

avg=np.mean(units)
maximum = np.max(units)
highest_month = valid_data[valid_data["Units"] == maximum]
minimum = np.min(units)
lowest_month = valid_data[valid_data["Units"] == minimum]
std_dev = np.std(units)

above_average = valid_data[valid_data["Units"] > avg]

plt.bar(valid_data["Month"], valid_data["Units"])
plt.title("Monthly Consumption")
plt.xlabel("Month")
plt.ylabel("Units")
plt.show()

plt.plot(valid_data["Month"], valid_data["Units"], marker="o")
plt.title("Monthly Consumption Trend")
plt.xlabel("Month")
plt.ylabel("Units")
plt.show()

while True:
    print("\n1. Summary")
    print("2. Above Average Months")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        print("\nTotal :", total, "units")
        print("Average:", round(avg, 2), "units")
        print("Highest:",highest_month.iloc[0]["Month"], maximum, "units")
        print("Lowest:",lowest_month.iloc[0]["Month"], minimum, "units")
        print("Standard Deviation:", round(std_dev, 2), "units")
    elif choice == "2":
        print("\nMonths Above Average:")
        print(above_average)
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

