"""
Customer Retention Rate - 2024 Quarterly Analysis
author: 24ds200081@ds.study.iitm.ac.in
"""

import matplotlib.pyplot as plt
import pandas as pd

# -----------------------------
# 1. Define the quarterly data
# -----------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Retention_Rate": [67.14, 72.50, 76.54, 71.57]
}

industry_target = 85.0

df = pd.DataFrame(data)

# -----------------------------
# 2. Basic analysis
# -----------------------------
average_retention = df["Retention_Rate"].mean()

print("Quarterly Retention Rates (2024):")
print(df)
print(f"\nCalculated Average Retention Rate: {average_retention:.2f}")
print(f"Industry Target Retention Rate: {industry_target:.2f}")

# -----------------------------
# 3. Visualization
# -----------------------------
plt.figure(figsize=(8, 5))

# Line plot of quarterly retention
plt.plot(df["Quarter"], df["Retention_Rate"], marker="o", linewidth=2, label="Customer Retention Rate")

# Horizontal line for industry target
plt.axhline(y=industry_target, color="red", linestyle="--", linewidth=2, label="Industry Target (85%)")

# Annotate each point
for x, y in zip(df["Quarter"], df["Retention_Rate"]):
    plt.text(x, y + 0.5, f"{y:.2f}%", ha="center", va="bottom", fontsize=9)

plt.title("Customer Retention Rate - 2024 Quarterly Trend vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.ylim(60, 90)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("retention_trend.png", dpi=150)
plt.close()
