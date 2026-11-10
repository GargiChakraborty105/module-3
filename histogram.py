
# ============================================
# PENGUINS DATASET - HISTOGRAM VISUALIZATION
# Using Seaborn and Matplotlib
# ============================================

# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# 2. Load Penguins Dataset

df = sns.load_dataset('penguins')


# 3. Display Dataset

print("First Five Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())


# 4. Check Penguin Species

print("\nPenguin Species:")
print(df['species'].value_counts())


# ============================================
# 5. HISTOGRAM USING MATPLOTLIB
# ============================================

plt.figure(figsize=(8, 5))

plt.hist(
    df['flipper_length_mm'].dropna(),
    bins=15,
    color='skyblue',
    edgecolor='black'
)

plt.title("Penguin Flipper Length Distribution")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")

plt.grid(axis='y', alpha=0.3)
plt.show()


# ============================================
# 6. HISTOGRAM USING SEABORN
# ============================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x='body_mass_g',
    bins=15,
    color='orange',
    kde=True
)

plt.title("Penguin Body Mass Distribution")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Frequency")

plt.show()


# ============================================
# 7. BILL LENGTH HISTOGRAM
# ============================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x='bill_length_mm',
    bins=15,
    color='green',
    kde=True
)

plt.title("Penguin Bill Length Distribution")
plt.xlabel("Bill Length (mm)")
plt.ylabel("Frequency")

plt.show()


# ============================================
# 8. BILL DEPTH HISTOGRAM
# ============================================

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x='bill_depth_mm',
    bins=15,
    color='purple',
    kde=True
)

plt.title("Penguin Bill Depth Distribution")
plt.xlabel("Bill Depth (mm)")
plt.ylabel("Frequency")

plt.show()


# ============================================
# 9. HISTOGRAM BY PENGUIN SPECIES
# ============================================

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x='flipper_length_mm',
    hue='species',
    bins=15,
    kde=True
)

plt.title("Flipper Length by Penguin Species")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Frequency")

plt.show()


# ============================================
# 10. BODY MASS COMPARISON
# ============================================

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x='body_mass_g',
    hue='species',
    bins=15,
    element='step',
    kde=True
)

plt.title("Body Mass Comparison by Species")
plt.xlabel("Body Mass (grams)")
plt.ylabel("Frequency")

plt.show()


# ============================================
# 11. MULTIPLE HISTOGRAMS USING SUBPLOTS
# ============================================

fig, axes = plt.subplots(2, 2, figsize=(12, 9))

sns.histplot(
    data=df,
    x='bill_length_mm',
    bins=15,
    kde=True,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Bill Length Distribution")

sns.histplot(
    data=df,
    x='bill_depth_mm',
    bins=15,
    kde=True,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Bill Depth Distribution")

sns.histplot(
    data=df,
    x='flipper_length_mm',
    bins=15,
    kde=True,
    ax=axes[1, 0]
)
axes[1, 0].set_title("Flipper Length Distribution")

sns.histplot(
    data=df,
    x='body_mass_g',
    bins=15,
    kde=True,
    ax=axes[1, 1]
)
axes[1, 1].set_title("Body Mass Distribution")

plt.suptitle("Penguin Dataset - Histogram Analysis", fontsize=16)

plt.tight_layout()
plt.show()


# ============================================
# 12. FINAL DATA ANALYSIS
# ============================================

print("\n========== PENGUIN DATA ANALYSIS ==========")

print("\nAverage Body Mass by Species:")
print(df.groupby('species')['body_mass_g'].mean())

print("\nAverage Flipper Length by Species:")
print(df.groupby('species')['flipper_length_mm'].mean())

print("\nAverage Bill Length by Species:")
print(df.groupby('species')['bill_length_mm'].mean())


print("\nHistogram Visualization Completed!")
