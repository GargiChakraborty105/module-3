
# =================================================
# PENGUINS DATASET - RELATIONSHIP BETWEEN VARIABLES
# Using Python, Seaborn and Matplotlib
# =================================================

# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visualization style
sns.set_style("whitegrid")


# 2. Load Dataset

df = sns.load_dataset("penguins")


# 3. Explore Dataset

print("FIRST FIVE ROWS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())


# 4. Select Numerical Variables

numeric_df = df.select_dtypes(include=np.number)


# 5. PAIRPLOT
# Relationship between all numerical variables

sns.pairplot(
    data=df,
    hue="species",
    diag_kind="hist"
)

plt.suptitle(
    "Relationship Between Penguin Variables",
    y=1.02
)

plt.show()


# 6. CORRELATION HEATMAP
# Identify correlation between variables

plt.figure(figsize=(9, 6))

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5,
    fmt=".2f"
)

plt.title("Penguins Dataset Correlation Heatmap")

plt.show()


# 7. SCATTER PLOT
# Bill Length vs Bill Depth

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    s=80
)

plt.title("Bill Length vs Bill Depth")

plt.xlabel("Bill Length (mm)")
plt.ylabel("Bill Depth (mm)")

plt.show()


# 8. SCATTER PLOT
# Flipper Length vs Body Mass

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species",
    s=80
)

plt.title("Flipper Length vs Body Mass")

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (grams)")

plt.show()


# 9. REGRESSION PLOT
# Show relationship and trend

plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    scatter_kws={"alpha": 0.5},
    line_kws={"color": "red"}
)

plt.title("Flipper Length vs Body Mass Regression")

plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (grams)")

plt.show()


# 10. BOX PLOT
# Compare body mass by species

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="species",
    y="body_mass_g",
    hue="species"
)

plt.title("Body Mass Comparison by Penguin Species")

plt.xlabel("Penguin Species")
plt.ylabel("Body Mass (grams)")

plt.show()


# 11. VIOLIN PLOT
# Compare flipper length distribution

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="species",
    y="flipper_length_mm",
    hue="species"
)

plt.title("Flipper Length Distribution by Species")

plt.xlabel("Penguin Species")
plt.ylabel("Flipper Length (mm)")

plt.show()


# 12. JOINT PLOT
# Analyze two variables together

sns.jointplot(
    data=df,
    x="bill_length_mm",
    y="bill_depth_mm",
    hue="species",
    kind="scatter"
)

plt.show()


# 13. CORRELATION VALUES

print("\n========== CORRELATION VALUES ==========")

print(correlation)


# 14. STRONGEST CORRELATION

print("\n========== VARIABLE RELATIONSHIP ==========")

corr_pairs = correlation.unstack()

corr_pairs = corr_pairs[
    corr_pairs.index.get_level_values(0) !=
    corr_pairs.index.get_level_values(1)
]

corr_pairs = corr_pairs.drop_duplicates()

print("Strongest Correlation:")
print(corr_pairs.abs().idxmax())

print("Correlation Value:")
print(corr_pairs.loc[corr_pairs.abs().idxmax()])


# 15. FINAL SUMMARY

print("\n========== SPECIES-WISE ANALYSIS ==========")

print(
    df.groupby("species")[
        ["bill_length_mm",
         "bill_depth_mm",
         "flipper_length_mm",
         "body_mass_g"]
    ].mean()
)

print("\nRelationship Visualization Completed!")
