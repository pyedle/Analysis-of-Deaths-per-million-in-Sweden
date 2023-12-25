import pandas as pd
import matplotlib.pyplot as plt

# Load data from Excel file
file_path = '/kaggle/input/deaths-per-million-in-sweden/000005JV_20231225-191442.xlsx'  
df = pd.read_excel(file_path)

# Extract the years and sum the number of deaths for each year
years = df.columns[1:]  # Exclude the first column (as they are not years)
yearly_sums = {}

for year in years:
    # Select columns for the current year
    columns_for_year = df[year]
    
    # Sum the number of deaths for each year
    yearly_sums[year] = columns_for_year.sum()/1000000
    
x_labels = [2015,2016,2017,2018,2019,2020]
    
# Plot the results
fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(yearly_sums.keys(), yearly_sums.values(), width=0.5)
ax.set_title('Total Number of Deaths for Each Year')
ax.set_xlabel('Year')
ax.set_ylabel('Deaths per million')
ax.set_xticklabels(x_labels)

plt.show()
