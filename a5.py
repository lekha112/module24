import pandas as pd
import matplotlib.pyplot as plt

# Sample weather data
data = {
    'Date': pd.date_range(start='2024-01-01', periods=30, freq='D'),
    'Temperature (°C)': [30, 32, 31, 29, 28, 35, 33, 34, 36, 37,
                         36, 35, 34, 33, 32, 31, 30, 28, 29, 30,
                         31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    'Humidity (%)': [70, 65, 68, 72, 75, 60, 55, 58, 50, 45,
                     48, 50, 52, 54, 56, 60, 62, 65, 66, 68,
                     70, 72, 74, 76, 77, 78, 79, 80, 81, 82],
    'Precipitation (mm)': [0, 0, 5, 10, 0, 0, 0, 2, 0, 0,
                           0, 3, 0, 0, 0, 1, 2, 0, 0, 0,
                           0, 0, 5, 0, 0, 0, 0, 0, 0, 0]
}

# Creating a DataFrame
weather_df = pd.DataFrame(data)

# Plotting Temperature and Humidity
plt.figure(figsize=(14, 6))

# Temperature line plot
plt.subplot(1, 2, 1)
plt.plot(weather_df['Date'], weather_df['Temperature (°C)'], marker='o', color='red', label='Temperature (°C)')
plt.title('Daily Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()

# Humidity line plot
plt.subplot(1, 2, 2)
plt.plot(weather_df['Date'], weather_df['Humidity (%)'], marker='o', color='blue', label='Humidity (%)')
plt.title('Daily Humidity Over Time')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Bar plot for Precipitation
plt.figure(figsize=(10, 5))
plt.bar(weather_df['Date'], weather_df['Precipitation (mm)'], color='skyblue')
plt.title('Daily Precipitation Over Time')
plt.xlabel('Date')
plt.ylabel('Precipitation (mm)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()
