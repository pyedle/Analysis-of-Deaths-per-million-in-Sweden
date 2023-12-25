import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/kaggle/input/excess-deaths-in-europe/nn.csv')  

# Task 1: Calculate the sum of 'value' for weeks 14 to 52 for each year from 2017 to 2021
filtered_df_task1 = df[(df['year'].between(2017, 2021)) & (df['week'].between(14, 52))]
sum_by_year = filtered_df_task1.groupby('year')['value'].sum().reset_index()
print("Task 1: Sum of 'value' for Weeks 14 to 52 for each year from 2017 to 2021")
print(sum_by_year)

# Task 2: Calculate the average of 'value' for weeks 14 to 52 for the combined years 2017 to 2019
filtered_df_task2 = df[(df['year'].between(2017, 2019)) & (df['week'].between(14, 52))]
print(filtered_df_task2.shape)
average_value_2017_2019= filtered_df_task2['value'].sum()
total = average_value_2017_2019/3
print("\nTask 2: Average Value for Weeks 14 to 52 (2017-2019):", total)

# Task 3: Calculate the excess percentage for each year compared to the average of 2017 to 2019
sum_by_year['excess_percentage'] = ((sum_by_year['value'] - total) / total) * 5
print("\nTask 3: Excess Percentage for each year compared to 2017-2019 average")
print(sum_by_year[['year', 'excess_percentage']])
# Round off excess percentage to 2 digits
sum_by_year['excess_percentage'] = round(sum_by_year['excess_percentage'], 2)
print(sum_by_year)

plt.bar(sum_by_year['year'], sum_by_year['excess_percentage'])
plt.axhline(y=0, color='black', linestyle='--', linewidth=1)
plt.xlabel('Year')
plt.ylabel('Excess Percentage')
plt.title('Excess Percentage for each year compared to 2017-2019 average')
plt.show()
