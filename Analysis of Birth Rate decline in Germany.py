import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from Excel file
file_path = '/kaggle/input/d/priyankayedle/germany-birth-rate/germany-birth-rate.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Map months to quarters
month_to_quarter = {'January': 1, 'February': 1, 'March': 1, 'April': 2, 'May': 2, 'June': 2,
                    'July': 3, 'August': 3, 'September': 3, 'October': 4, 'November': 4, 'December': 4}
df['Quarter'] = df['Months'].map(month_to_quarter)

# Output rows with Quarter 3 and 4 and Year 2023
filtered_df = df[(df['Year'] == 2023) & (df['Quarter'].isin([3, 4]))]
# Output every row in df except filtered_df
df = df.loc[~df.index.isin(filtered_df.index)]

# Clean and convert 'In total' column to numeric, handling spaces and commas
df['In total'] = df['In total'].replace({',': '', ' ': ''}, regex=True).astype(int)

# Pivot the DataFrame to have years as columns
pivot_df = df.pivot_table(index='Quarter', columns='Year', values='In total', aggfunc='sum')

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))  

# Increase spacing between bars and quarters
bar_width = 0.5
quarters = pivot_df.index
total_quarters = len(quarters)
total_years = len(pivot_df.columns)
group_width = total_years * bar_width + (total_years - 1) * 0.5
bar_positions = np.arange(0, total_quarters * group_width, group_width)

# Define colors for each year
colors = ['#1f78b4', '#1f78b4', '#1f78b4', '#1f78b4', '#e31a1c', '#e31a1c']

# Plot each year's data for each quarter with specified colors
for i, (year, color) in enumerate(zip(pivot_df.columns, colors)):
    data = pivot_df[year]
    ax.bar(bar_positions + i * (bar_width + 0.1), data, width=bar_width, label=year, align='edge', color=color)


# Set ticks and labels
ax.set_xticks(bar_positions + (total_years - 1) * (bar_width + 0.1) / 2)
ax.set_xticklabels(quarters)

plt.title('Total Births for Each Year of Each Quarter')
plt.xlabel('Quarter')
plt.ylabel('Number of births in Geramny')


# Adjust legend position outside the plot
plt.legend(title='Year', loc='upper left', bbox_to_anchor=(1, 1))

# Add values on top of each bar 
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points', fontsize=5.25)

plt.show()
