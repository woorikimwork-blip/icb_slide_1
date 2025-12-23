import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the penguins dataset
df = sns.load_dataset('penguins')

# Basic analysis
print("Dataset Info:")
print(df.info())
print("\nDataset Description:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

# Visualization 1: Histogram of bill_length_mm
plt.figure(figsize=(8, 6))
sns.histplot(df['bill_length_mm'], kde=True)
plt.title('Histogram of Bill Length')
plt.savefig('hist_bill_length.png')
plt.close()

# Visualization 2: Histogram of bill_depth_mm
plt.figure(figsize=(8, 6))
sns.histplot(df['bill_depth_mm'], kde=True)
plt.title('Histogram of Bill Depth')
plt.savefig('hist_bill_depth.png')
plt.close()

# Visualization 3: Histogram of flipper_length_mm
plt.figure(figsize=(8, 6))
sns.histplot(df['flipper_length_mm'], kde=True)
plt.title('Histogram of Flipper Length')
plt.savefig('hist_flipper_length.png')
plt.close()

# Visualization 4: Histogram of body_mass_g
plt.figure(figsize=(8, 6))
sns.histplot(df['body_mass_g'], kde=True)
plt.title('Histogram of Body Mass')
plt.savefig('hist_body_mass.png')
plt.close()

# Visualization 5: Boxplot of bill_length_mm by species
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='bill_length_mm', data=df)
plt.title('Boxplot of Bill Length by Species')
plt.savefig('box_bill_length_species.png')
plt.close()

# Visualization 6: Boxplot of bill_depth_mm by species
plt.figure(figsize=(8, 6))
sns.boxplot(x='species', y='bill_depth_mm', data=df)
plt.title('Boxplot of Bill Depth by Species')
plt.savefig('box_bill_depth_species.png')
plt.close()

# Visualization 7: Scatter plot of bill_length_mm vs bill_depth_mm
plt.figure(figsize=(8, 6))
sns.scatterplot(x='bill_length_mm', y='bill_depth_mm', hue='species', data=df)
plt.title('Scatter Plot of Bill Length vs Bill Depth')
plt.savefig('scatter_bill_length_depth.png')
plt.close()

# Visualization 8: Scatter plot of flipper_length_mm vs body_mass_g
plt.figure(figsize=(8, 6))
sns.scatterplot(x='flipper_length_mm', y='body_mass_g', hue='species', data=df)
plt.title('Scatter Plot of Flipper Length vs Body Mass')
plt.savefig('scatter_flipper_body_mass.png')
plt.close()

# Visualization 9: Count plot of species (Bar chart)
plt.figure(figsize=(8, 6))
sns.countplot(x='species', data=df)
plt.title('Count of Species')
plt.savefig('count_species.png')
plt.close()

# For bar chart: Cross-tabulation and Pivot Table
cross_tab = pd.crosstab(df['species'], df['island'])
pivot_table = df.pivot_table(values='body_mass_g', index='species', columns='island', aggfunc='mean')

print("\nCross-tabulation of Species and Island:")
print(cross_tab)
print("\nPivot Table of Mean Body Mass by Species and Island:")
print(pivot_table)

# Visualization 10: Bar plot of mean body_mass_g by species
plt.figure(figsize=(8, 6))
sns.barplot(x='species', y='body_mass_g', data=df, estimator=np.mean)
plt.title('Mean Body Mass by Species')
plt.savefig('bar_body_mass_species.png')
plt.close()

# Visualization 11: Pair plot
sns.pairplot(df, hue='species')
plt.savefig('pairplot.png')
plt.close()

# Visualization 12: Violin plot of bill_length_mm by species
plt.figure(figsize=(8, 6))
sns.violinplot(x='species', y='bill_length_mm', data=df)
plt.title('Violin Plot of Bill Length by Species')
plt.savefig('violin_bill_length_species.png')
plt.close()

# Visualization 13: Heatmap of correlations
plt.figure(figsize=(8, 6))
numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.savefig('heatmap_corr.png')
plt.close()

# Visualization 14: Count plot of island
plt.figure(figsize=(8, 6))
sns.countplot(x='island', data=df)
plt.title('Count of Islands')
plt.savefig('count_island.png')
plt.close()

# Visualization 15: Boxplot of body_mass_g by island
plt.figure(figsize=(8, 6))
sns.boxplot(x='island', y='body_mass_g', data=df)
plt.title('Boxplot of Body Mass by Island')
plt.savefig('box_body_mass_island.png')
plt.close()

# Create Markdown content
markdown_content = f"""
# Penguins Dataset Analysis

## Dataset Overview
- **Shape**: {df.shape}
- **Columns**: {list(df.columns)}

## Basic Statistics
{df.describe().to_markdown()}

## Missing Values
{df.isnull().sum().to_markdown()}

## Visualizations

### 1. Histogram of Bill Length
![Histogram of Bill Length](hist_bill_length.png)

### 2. Histogram of Bill Depth
![Histogram of Bill Depth](hist_bill_depth.png)

### 3. Histogram of Flipper Length
![Histogram of Flipper Length](hist_flipper_length.png)

### 4. Histogram of Body Mass
![Histogram of Body Mass](hist_body_mass.png)

### 5. Boxplot of Bill Length by Species
![Boxplot of Bill Length by Species](box_bill_length_species.png)

### 6. Boxplot of Bill Depth by Species
![Boxplot of Bill Depth by Species](box_bill_depth_species.png)

### 7. Scatter Plot of Bill Length vs Bill Depth
![Scatter Plot of Bill Length vs Bill Depth](scatter_bill_length_depth.png)

### 8. Scatter Plot of Flipper Length vs Body Mass
![Scatter Plot of Flipper Length vs Body Mass](scatter_flipper_body_mass.png)

### 9. Count of Species (Bar Chart)
![Count of Species](count_species.png)

#### Cross-tabulation for Bar Chart (Species Count)
{cross_tab.to_markdown()}

#### Pivot Table for Bar Chart (Mean Body Mass by Species and Island)
{pivot_table.to_markdown()}

### 10. Mean Body Mass by Species (Bar Chart)
![Mean Body Mass by Species](bar_body_mass_species.png)

### 11. Pair Plot
![Pair Plot](pairplot.png)

### 12. Violin Plot of Bill Length by Species
![Violin Plot of Bill Length by Species](violin_bill_length_species.png)

### 13. Correlation Heatmap
![Correlation Heatmap](heatmap_corr.png)

### 14. Count of Islands (Bar Chart)
![Count of Islands](count_island.png)

### 15. Boxplot of Body Mass by Island
![Boxplot of Body Mass by Island](box_body_mass_island.png)
"""

# Save to Markdown file
with open('penguins_analysis.md', 'w') as f:
    f.write(markdown_content)

print("Analysis complete. Markdown file saved as 'penguins_analysis.md'")