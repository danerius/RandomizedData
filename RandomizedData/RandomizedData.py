
from turtle import color
from xmlrpc.client import UNSUPPORTED_ENCODING
import matplotlib.pyplot as plt
import pandas as pd
import random
from scipy.signal import savgol_filter

# Use the dark background style
plt.style.use('dark_background')

# Adjust font properties (optional)
plt.rcParams['font.size'] = 10
plt.rcParams['font.family'] = 'Consolas' 

# Generate 500 random numbers between 0 and 100
random_numbers = [random.randint(0,100) for _ in range(500)]

# Set the window size
plt.figure(figsize=(15,5))

# Compute the rolling average using pandas
s = pd.Series(random_numbers)
rolling_avg = s.rolling(window=10).mean()

# Apply Savitzky-Golay filter
savgol = savgol_filter(random_numbers, window_length=9, polyorder=2)

# Plotting
plt.figure(figsize=(10,5))
plt.style.use('dark_background')
plt.plot(random_numbers, color='lightgray', linewidth=2, label='Original Data')
plt.plot(rolling_avg, color='yellow', linewidth=2, label='Rolling Average')
plt.plot(savgol, color='cyan', linewidth=2, label='Savitzky-Golay')
plt.title('Smoothing Techniques Comparison')
plt.xlabel('Index')
plt.ylabel('Value')
plt.legend()
plt.show()

#Den gillade tydligen inte "pandas" så den importen får jag kolla upp