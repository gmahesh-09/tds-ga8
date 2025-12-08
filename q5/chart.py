# chart.py
# Author: 24ds2000081@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from PIL import Image
import io

# -------------------------------------------------------
# 1. Professional Seaborn Styling
# -------------------------------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")

# -------------------------------------------------------
# 2. Generate Realistic Synthetic Customer Engagement Data
# -------------------------------------------------------
np.random.seed(42)

data = {
    "Time_on_Site": np.random.normal(5.5, 1.2, 500),
    "Pages_Viewed": np.random.normal(9, 2.7, 500),
    "Email_Clicks": np.random.normal(2.3, 1.0, 500),
    "App_Usage": np.random.normal(11, 3.3, 500),
    "Purchase_Frequency": np.random.normal(2.0, 0.6, 500),
    "Customer_Satisfaction": np.random.normal(4.3, 0.5, 500),
}

df = pd.DataFrame(data)
corr = df.corr()

# -------------------------------------------------------
# 3. Create a high-quality heatmap figure
# -------------------------------------------------------
fig = plt.figure(figsize=(8, 8), dpi=150)  # High DPI for crisp rendering

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
# 4. Render figure to memory buffer (PNG)
# -------------------------------------------------------
buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=150, bbox_inches="tight")
buf.seek(0)

# -------------------------------------------------------
# 5. Load into PIL and resize to EXACT 512×512
# -------------------------------------------------------
img = Image.open(buf)
img = img.resize((512, 512), Image.LANCZOS)
img.save("chart.png")

plt.close(fig)

print("chart.png saved successfully (exact 512x512 pixels)")
