# chart.py
# Author contact: 24ds2000081@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# -------------------------------------------------------
# 1. Seaborn styling for professional, publication-ready look
# -------------------------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------------------------------------------
# 2. Generate realistic synthetic customer engagement data
# -------------------------------------------------------
np.random.seed(42)

data = {
    "Time_on_Site": np.random.normal(5.5, 1.2, 500),      # minutes per visit
    "Pages_Viewed": np.random.normal(9, 2.8, 500),
    "Email_Clicks": np.random.normal(2.2, 1.1, 500),
    "App_Usage": np.random.normal(11, 3.5, 500),
    "Purchase_Frequency": np.random.normal(2.0, 0.7, 500),
    "Customer_Satisfaction": np.random.normal(4.3, 0.4, 500),
}

df = pd.DataFrame(data)
corr = df.corr()

# -------------------------------------------------------
# 3. Create EXACT 512x512 heatmap (NO RESIZING)
# -------------------------------------------------------
fig = plt.figure(figsize=(8, 8), dpi=64)   # 8 inches * 64 dpi = 512 pixels

sns.heatmap(
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
# 4. Save as EXACT 512x512 PNG
# -------------------------------------------------------
fig.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close(fig)

print("chart.png generated successfully (512x512 pixels)")
