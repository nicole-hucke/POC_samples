# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 15:40:36 2023

@author: tacob
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P2(2).csv')

# Print the DataFrame
print(df)

# Convert the 'date' column to datetime format
df['Date/time'] = pd.to_datetime(df['Date/time'])

# Sort the DataFrame by the 'date' column
df.sort_values('Date/time', inplace=True)

# Set the desired time frame
start_date = pd.to_datetime('2022-07-01')
end_date = pd.to_datetime('2022-08-31')

# Filter the DataFrame based on the time frame
df_filtered = df[(df['Date/time'] >= start_date) & (df['Date/time'] <= end_date)]

# Create the line graph
plt.figure(figsize=(200, 50))
plt.plot(df_filtered['Date/time'], df_filtered['Depth'], linewidth=2, alpha=1)

# Set labels for the axes
plt.xlabel('Date', fontsize=45)
plt.ylabel('Depth', fontsize=45)

# Set a title for the graph
plt.title('Flow Depth over Time \n July - August 2022', fontsize=70)

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)
plt.xticks(ticks=plt.xticks()[0][::1])
plt.xticks(fontsize=35)

plt.yticks(fontsize=35)

plt.grid(True)

# Display the graph
plt.show()