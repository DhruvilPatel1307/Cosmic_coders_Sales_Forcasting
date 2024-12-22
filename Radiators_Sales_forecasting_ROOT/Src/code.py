import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('/content/dairy_dataset.csv')

# 1. Total Revenue by Product and Location
plt.figure(figsize=(10, 6))
revenue_data = df.groupby(['Product Name', 'Location'])['Approx. Total Revenue(INR)'].sum().unstack()
revenue_data.plot(kind='bar', stacked=True, colormap='viridis', figsize=(10, 6))
plt.title('Total Revenue by Product and Location')
plt.xlabel('Product Name')
plt.ylabel('Total Revenue (INR)')
plt.xticks(rotation=45)
plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
for container in plt.gca().containers:
    plt.gca().bar_label(container, fmt='%.0f', label_type='center', fontsize=8)
plt.tight_layout()
plt.show()


# 2. Compare Two Locations (Interactive)
def compare_locations(location1, location2):
    if location1 not in df['Location'].values or location2 not in df['Location'].values:
        print("One or both locations are not in the dataset.")
        return
    filtered_data = df[df['Location'].isin([location1, location2])]
    comparison_data = filtered_data.groupby(['Product Name', 'Location'])['Approx. Total Revenue(INR)'].sum().unstack()
    comparison_data.plot(kind='bar', colormap='coolwarm', figsize=(10, 6))
    plt.title(f'Revenue Comparison: {location1} vs {location2}')
    plt.xlabel('Product Name')
    plt.ylabel('Total Revenue (INR)')
    plt.xticks(rotation=45)
    plt.legend(title='Location', bbox_to_anchor=(1.05, 1), loc='upper left')
    for container in plt.gca().containers:
        plt.gca().bar_label(container, fmt='%.0f', label_type='center', fontsize=8)
    plt.tight_layout()
    plt.show()

# List available locations
available_locations = df['Location'].unique()
print("Available Locations:")
for i, loc in enumerate(available_locations, start=1):
    print(f"{i}. {loc}")

# Example usage: User selects locations to compare
try:
    loc1_index = int(input("Select the first location by number: ")) - 1
    loc2_index = int(input("Select the second location by number: ")) - 1
    if not (0 <= loc1_index < len(available_locations)) or not (0 <= loc2_index < len(available_locations)):
        print("Invalid selection. Please select valid location numbers.")
    else:
        compare_locations(available_locations[loc1_index], available_locations[loc2_index])
except ValueError:
    print("Please enter a valid number.")
