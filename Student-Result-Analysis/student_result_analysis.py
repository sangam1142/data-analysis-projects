import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Student_Result_Data.csv")

# Calculate total and average
df["Total"] = df[["Maths", "Science", "English"]].sum(axis=1)
df["Average"] = df["Total"] / 3

# Pass / Fail
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Topper
topper = df.loc[df["Total"].idxmax()]
print("Topper:", topper["Name"], topper["Total"])

# Subject-wise average
subject_avg = df[["Maths", "Science", "English"]].mean()

# Plot
subject_avg.plot(kind="bar", title="Subject-wise Average Marks")
plt.show()
