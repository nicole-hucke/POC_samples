# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 16:48:35 2023

@author: tacob
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read the first CSV file into a DataFrame
df1 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P1(1).csv')
df2 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P2(1).csv')
df3 = pd.read_csv('C:/Users/tacob/OneDrive - University of Idaho/Summer Work 23/Raw CSV/P3(1).csv')

# Print the first DataFrame
print(df1)
print(df2)
print(df3)

# Convert the 'date' column to datetime format for both DataFrames
df1['Date/time'] = pd.to_datetime(df1['Date/time'])
df2['Date/time'] = pd.to_datetime(df2['Date/time'])
df3['Date/time'] = pd.to_datetime(df3['Date/time'])

# Sort the first DataFrame by the 'date' column
df1.sort_values('Date/time', inplace=True)
df2.sort_values('Date/time', inplace=True)
df3.sort_values('Date/time', inplace=True)

# Set the desired time frame
start_date = pd.to_datetime('2022-03-01')
end_date = pd.to_datetime('2022-05-31')

# Filter the first DataFrame based on the time frame
df1_filtered = df1[(df1['Date/time'] >= start_date) & (df1['Date/time'] <= end_date)]
df2_filtered = df2[(df2['Date/time'] >= start_date) & (df2['Date/time'] <= end_date)]
df3_filtered = df3[(df3['Date/time'] >= start_date) & (df3['Date/time'] <= end_date)]

# Create the line graph
plt.figure(figsize=(200, 50))
plt.plot(df1_filtered['Date/time'], df1_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 1')
plt.plot(df2_filtered['Date/time'], df2_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 2')  # Add the line for the second DataFrame
plt.plot(df3_filtered['Date/time'], df3_filtered['Depth'], linewidth=2, alpha=1, label='Piezometer 3')

# Set labels for the axes
plt.xlabel('Date', fontsize=45)
plt.ylabel('Depth', fontsize=45)

# Set a title for the graph
plt.title('Flow Depth over Time \n March - May 2022', fontsize=70)

# Rotate x-axis labels for better readability (optional)
plt.xticks(rotation=45)
plt.xticks(ticks=plt.xticks()[0][::1])
plt.xticks(fontsize=35)

plt.yticks(fontsize=35)

plt.grid(True)
plt.legend(fontsize=45, prop={'size': 70})

# Display the graph
plt.show()
