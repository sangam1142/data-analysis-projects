import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Sales_Data_Analysis.csv")
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Monthly sales
df["Month"] = df["Order_Date"].dt.month
monthly_sales = df.groupby("Month")["Sales_Amount"].sum()

# Category-wise sales
category_sales = df.groupby("Category")["Sales_Amount"].sum()

# Plots
monthly_sales.plot(kind="line", title="Monthly Sales Trend")
plt.show()

category_sales.plot(kind="bar", title="Category-wise Sales")
plt.show()
