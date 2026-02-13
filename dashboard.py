import pandas as pd
import matplotlib.pyplot as plt

# Load Data (Make sure cleaned_sales.csv is in SAME folder)
df = pd.read_csv("cleaned_sales.csv")

# -------- Monthly Sales --------
monthly_sales = df.groupby("Month")["SALES"].sum()

plt.figure()
monthly_sales.plot(kind="bar")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
print("Saved monthly_sales.png")
plt.close()

# -------- Top 5 Customers --------
top_customers = df.groupby("CUSTOMERNAME")["SALES"].sum().sort_values(ascending=False).head(5)

plt.figure()
top_customers.plot(kind="bar")
plt.title("Top 5 Customers")
plt.xlabel("Customer")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("top_customers.png")
print("Saved top_customers.png")
plt.close()

# -------- Country Wise Sales --------
country_sales = df.groupby("COUNTRY")["SALES"].sum()

plt.figure()
country_sales.plot(kind="bar")
plt.title("Country Wise Sales")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("country_sales.png")
print("Saved country_sales.png")
plt.close()

print("Dashboard Graphs Saved Successfully!")
