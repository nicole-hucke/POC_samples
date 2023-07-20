# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:48:35 2023

@author: tacob
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read the first CSV file into a DataFrame
df1 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P1(3).csv')
df2 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P2(2).csv')
df3 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P3(2).csv')
df4 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/Sample Data 4 Python.csv')  # New CSV file with points

# Print the first DataFrame
print(df1)
print(df2)
print(df3)
print(df4)

# Convert the 'date' column to datetime format for both DataFrames
df1['Date/time'] = pd.to_datetime(df1['Date/time'])
df2['Date/time'] = pd.to_datetime(df2['Date/time'])
df3['Date/time'] = pd.to_datetime(df3['Date/time'])
df4['Date/time'] = pd.to_datetime(df4['Date/time'])

# Sort the first DataFrame by the 'date' column
df1.sort_values('Date/time', inplace=True)
df2.sort_values('Date/time', inplace=True)
df3.sort_values('Date/time', inplace=True)
df4.sort_values('Date/time', inplace=True)

# Set the desired time frame
start_date = pd.to_datetime('2023-03-01')
end_date = pd.to_datetime('2023-05-31')

# Filter the DataFrame based on the time frame
df1_filtered = df1[(df1['Date/time'] >= start_date) & (df1['Date/time'] <= end_date)]
df2_filtered = df2[(df2['Date/time'] >= start_date) & (df2['Date/time'] <= end_date)]
df3_filtered = df3[(df3['Date/time'] >= start_date) & (df3['Date/time'] <= end_date)]

# Filter the fourth DataFrame (with points) based on the time frame
df4_filtered = df4[(df4['Date/time'] >= start_date) & (df4['Date/time'] <= end_date)]

# Create the line graph
plt.figure(figsize=(200, 50))
plt.plot(df1_filtered['Date/time'], df1_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 1')
plt.plot(df2_filtered['Date/time'], df2_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 2')  # Add the line for the second DataFrame
plt.plot(df3_filtered['Date/time'], df3_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 3')

# Create the scatter plot for the points
plt.scatter(df4_filtered['Date/time'], df4_filtered['Depth'], c='red', marker='o', s=500, label='Sample Dates')

# Set labels for the axes
plt.xlabel('\n Date \n', fontsize=70)
plt.ylabel('\n Depth \n', fontsize=70)

# Set a title for the graph
plt.title('\n Flow Depth over Time \n March - May 2023 \n', fontsize=80)

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=55)
plt.xticks(ticks=plt.xticks()[0][::1])
plt.xticks(fontsize=55)

plt.yticks(fontsize=45)

plt.grid(True)
plt.legend(fontsize=65, prop={'size': 90})

# Display the graph
plt.show()
