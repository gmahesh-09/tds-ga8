# chart.py
# Author email: aa@abc.com

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------------------------------
# 1. Seaborn styling for publication-ready visualization
# -------------------------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------------------------------------------
# 2. Generate realistic synthetic customer engagement data
# -------------------------------------------------------
np.random.seed(42)

data = {
    "Time_on_Site": np.random.normal(5.5, 1.2, 300),     # minutes
    "Pages_Viewed": np.random.normal(8, 2.5, 300),
    "Email_Clicks": np.random.normal(2, 1.0, 300),
    "App_Usage": np.random.normal(10, 3.0, 300),
    "Purchase_Frequency": np.random.normal(1.8, 0.6, 300),
    "Customer_Satisfaction": np.random.normal(4.2, 0.5, 300)
}

df = pd.DataFrame(data)
corr = df.corr()

# -------------------------------------------------------
# 3. Create 512x512 heatmap using Seaborn
# -------------------------------------------------------
plt.figure(figsize=(8, 8))   # 8 inches * 64 dpi = 512 px

heatmap = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5,
    square=True,
    cbar_kws={"shrink": 0.7}
)

plt.title("Customer Engagement Correlation Matrix", pad=20)

# -------------------------------------------------------
# 4. Save exact 512x512 PNG
# -------------------------------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
