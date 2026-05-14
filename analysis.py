import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Automobile.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Replace missing values
df.replace("?", pd.NA, inplace=True)

# Convert columns to numeric
cols = ["horsepower", "weight", "displacement", "mpg"]

for col in cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove missing values
df = df.dropna()

# ---------------- BASIC ANALYSIS ----------------

print("Average MPG:", df["mpg"].mean())
print("Highest Horsepower:", df["horsepower"].max())

print("\nAverage MPG by Cylinders:")
print(df.groupby("cylinders")["mpg"].mean())

# ---------------- GRAPHS ----------------

# MPG Distribution
plt.hist(df["mpg"])
plt.title("MPG Distribution")
plt.xlabel("MPG")
plt.ylabel("Count")
plt.show()

# Horsepower vs MPG
plt.scatter(df["horsepower"], df["mpg"])
plt.title("Horsepower vs MPG")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()

# Weight vs MPG
plt.scatter(df["weight"], df["mpg"])
plt.title("Weight vs MPG")
plt.xlabel("Weight")
plt.ylabel("MPG")
plt.show()