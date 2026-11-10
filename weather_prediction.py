
# ============================================
# WEATHER PREDICTION USING MACHINE LEARNING
# Python, Pandas, NumPy, Seaborn, Matplotlib
# ============================================

# 1. Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Set visualization style
sns.set_style("whitegrid")


# 2. Create Weather Dataset

data = {
    'Day': range(1, 31),

    'Temperature': [
        25, 27, 29, 30, 28, 26, 24, 25, 28, 31,
        32, 30, 29, 27, 26, 28, 30, 33, 34, 32,
        31, 29, 27, 26, 25, 28, 30, 32, 33, 31
    ],

    'Humidity': [
        60, 62, 65, 70, 68, 63, 58, 61, 66, 72,
        75, 73, 70, 67, 64, 68, 72, 78, 80, 76,
        74, 70, 66, 62, 60, 67, 71, 77, 79, 75
    ],

    'Rainfall': [
        5, 0, 2, 0, 10, 15, 20, 5, 0, 0,
        0, 3, 5, 8, 12, 0, 0, 0, 2, 0,
        0, 5, 10, 15, 20, 3, 0, 0, 0, 5
    ],

    'WindSpeed': [
        10, 12, 15, 11, 9, 14, 18, 16, 12, 10,
        8, 9, 13, 15, 17, 12, 10, 8, 9, 11,
        14, 16, 18, 15, 12, 10, 9, 11, 13, 14
    ]
}

df = pd.DataFrame(data)


# 3. Display Dataset

print("\n========== WEATHER DATASET ==========")
print(df.head(10))

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# 4. Check Missing Values

print("\nMissing Values:")
print(df.isnull().sum())


# 5. DATA VISUALIZATION USING MATPLOTLIB

# Temperature Trend

plt.figure(figsize=(10, 5))

plt.plot(
    df['Day'],
    df['Temperature'],
    marker='o',
    linewidth=2
)

plt.title("Daily Temperature Trend")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()


# Rainfall Visualization

plt.figure(figsize=(10, 5))

plt.bar(
    df['Day'],
    df['Rainfall']
)

plt.title("Daily Rainfall Analysis")
plt.xlabel("Day")
plt.ylabel("Rainfall (mm)")
plt.show()


# Humidity Trend

plt.figure(figsize=(10, 5))

plt.plot(
    df['Day'],
    df['Humidity'],
    color='green',
    marker='o'
)

plt.title("Daily Humidity Trend")
plt.xlabel("Day")
plt.ylabel("Humidity (%)")
plt.show()


# 6. DATA VISUALIZATION USING SEABORN

# Temperature Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    df['Temperature'],
    kde=True,
    bins=8
)

plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.show()


# Temperature vs Humidity

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x='Humidity',
    y='Temperature',
    size='Rainfall',
    sizes=(30, 200)
)

plt.title("Temperature vs Humidity")
plt.show()


# Correlation Heatmap

plt.figure(figsize=(8, 6))

sns.heatmap(
    df.drop(columns=['Day']).corr(),
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Weather Parameters Correlation")
plt.show()


# Wind Speed Analysis

plt.figure(figsize=(8, 5))

sns.boxplot(
    y=df['WindSpeed']
)

plt.title("Wind Speed Distribution")
plt.ylabel("Wind Speed (km/h)")
plt.show()


# 7. MACHINE LEARNING MODEL

# Input Features
X = df[['Humidity', 'Rainfall', 'WindSpeed']]

# Target Variable
y = df['Temperature']


# Split Dataset

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Linear Regression Model

model = LinearRegression()

# Train Model
model.fit(X_train, y_train)


# 8. MAKE PREDICTIONS

predictions = model.predict(X_test)


print("\n========== MODEL PREDICTIONS ==========")

for actual, predicted in zip(y_test, predictions):
    print(
        f"Actual: {actual}°C | "
        f"Predicted: {predicted:.2f}°C"
    )


# 9. MODEL EVALUATION

mae = mean_absolute_error(y_test, predictions)

mse = mean_squared_error(y_test, predictions)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, predictions)


print("\n========== MODEL PERFORMANCE ==========")

print("Mean Absolute Error:", round(mae, 2))

print("Mean Squared Error:", round(mse, 2))

print("Root Mean Squared Error:", round(rmse, 2))

print("R2 Score:", round(r2, 2))


# 10. ACTUAL VS PREDICTED TEMPERATURE

plt.figure(figsize=(9, 5))

plt.plot(
    range(len(y_test)),
    y_test.values,
    marker='o',
    label='Actual Temperature'
)

plt.plot(
    range(len(predictions)),
    predictions,
    marker='s',
    label='Predicted Temperature'
)

plt.title("Actual vs Predicted Temperature")

plt.xlabel("Test Data")
plt.ylabel("Temperature (°C)")

plt.legend()
plt.grid(True)
plt.show()


# 11. PREDICT FUTURE TEMPERATURE

print("\n========== WEATHER PREDICTION ==========")

humidity = float(input("Enter Humidity (%): "))

rainfall = float(input("Enter Rainfall (mm): "))

wind_speed = float(input("Enter Wind Speed (km/h): "))


new_weather = pd.DataFrame({
    'Humidity': [humidity],
    'Rainfall': [rainfall],
    'WindSpeed': [wind_speed]
})


predicted_temperature = model.predict(new_weather)[0]


print("\n========== PREDICTED WEATHER ==========")

print(
    "Predicted Temperature:",
    round(predicted_temperature, 2),
    "°C"
)

if predicted_temperature >= 35:
    print("Weather Condition: Very Hot")

elif predicted_temperature >= 30:
    print("Weather Condition: Hot")

elif predicted_temperature >= 25:
    print("Weather Condition: Pleasant")

else:
    print("Weather Condition: Cool")


print("\nWeather Prediction Completed Successfully!")
