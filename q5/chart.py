import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -----------------------------
# Synthetic customer engagement data
# -----------------------------
np.random.seed(42)

data = {
    "Time_on_Site": np.random.normal(5.5, 1.1, 400),
    "Pages_Viewed": np.random.normal(9, 2.5, 400),
    "Email_Clicks": np.random.normal(2.2, 1.0, 400),
    "App_Usage": np.random.normal(11, 3.2, 400),
    "Purchase_Frequency": np.random.normal(2.0, 0.6, 400),
    "Customer_Satisfaction": np.random.normal(4.3, 0.4, 400),
}

df = pd.DataFrame(data)
corr = df.corr()

# -----------------------------
# Seaborn styling
# -----------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -----------------------------
# Create EXACT 512x512 heatmap
# -----------------------------
plt.figure(figsize=(8, 8))  # 8 in × 64 dpi = 512 px

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    square=True,
    cbar_kws={"shrink": 0.7}
)

plt.title("Customer Engagement Correlation Heatmap", pad=20)
plt.tight_layout()

# -----------------------------
# Save EXACT 512×512 PNG
# -----------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()

print("chart.png created successfully (512x512)")
