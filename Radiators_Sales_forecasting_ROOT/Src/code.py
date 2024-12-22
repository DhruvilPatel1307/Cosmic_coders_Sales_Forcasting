import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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

# 2. Sales Channel Distribution
plt.figure(figsize=(5, 5))
df['Sales Channel'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Sales Channel Distribution')
plt.ylabel('')
plt.tight_layout()
plt.show()
