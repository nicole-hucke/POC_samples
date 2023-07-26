# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 13:26:47 2023

@author: tacob
"""

import pandas as pd
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Read the first CSV file into a DataFrame
df1 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P4(2).csv')
#df2 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P5(2).csv')
df3 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P6(2).csv')
df4 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/Sample Data 4 Python.csv')  # New CSV file with points

# Print the first DataFrame
print(df1)
#print(df2)
print(df3)
print(df4)

# Convert the 'date' column to datetime format for both DataFrames
df1['Date/time'] = pd.to_datetime(df1['Date/time'])
#df2['Date/time'] = pd.to_datetime(df2['Date/time'])
df3['Date/time'] = pd.to_datetime(df3['Date/time'])
df4['Date/time'] = pd.to_datetime(df4['Date/time'])

# Sort the first DataFrame by the 'date' column
df1.sort_values('Date/time', inplace=True)
#df2.sort_values('Date/time', inplace=True)
df3.sort_values('Date/time', inplace=True)
df4.sort_values('Date/time', inplace=True)

# Set the desired time frame
start_date = pd.to_datetime('2022-07-12')
end_date = pd.to_datetime('2022-08-31')

# Filter the DataFrame based on the time frame
df1_filtered = df1[(df1['Date/time'] >= start_date) & (df1['Date/time'] <= end_date)]
#df2_filtered = df2[(df2['Date/time'] >= start_date) & (df2['Date/time'] <= end_date)]
df3_filtered = df3[(df3['Date/time'] >= start_date) & (df3['Date/time'] <= end_date)]

# Filter the fourth DataFrame (with points) based on the time frame
df4_filtered = df4[(df4['Date/time'] >= start_date) & (df4['Date/time'] <= end_date)]

# Create the line graph
plt.figure(figsize=(200, 50))
plt.plot(df1_filtered['Date/time'], df1_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 4')
#plt.plot(df2_filtered['Date/time'], df2_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 5')  # Add the line for the second DataFrame
plt.plot(df3_filtered['Date/time'], df3_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 6')

# Create the scatter plot for the points
plt.scatter(df4_filtered['Date/time'], df4_filtered['Depth'], c='red', marker='o', s=500, label='Sample Dates')

# Set labels for the axes
plt.xlabel('\n Date \n', fontsize=70)
plt.ylabel('\n Depth (Meters) \n', fontsize=70)

# Set a title for the graph
plt.title('\n Upstream Flow Depth over Time \n July - August 2022 \n', fontsize=80)

# Rotate x-axis labels for better readability (optional)
date_ticks = pd.date_range(start=start_date, end=end_date, freq='5D')
plt.xticks(date_ticks, rotation=55, fontsize=55)

plt.yticks(fontsize=45)

plt.grid(True)
plt.legend(fontsize=65, prop={'size': 90})

# Add labels to the points
labels = df4_filtered['Sample Number']
texts = []
for x, y, label in zip(df4_filtered['Date/time'], df4_filtered['Depth'], labels):
    texts.append(plt.text(x, y, label, fontsize=35, ha='left', va='bottom', color='blue'))
    
adjust_text(texts, force_text=2, expand_text=(1.5, 1.5), arrowprops=dict(arrowstyle="-", color='black'))

# Display the graph
plt.show()
