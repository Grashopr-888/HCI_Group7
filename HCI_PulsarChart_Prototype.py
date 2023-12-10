import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load your dataset
# Replace 'your_dataset.xlsx' with the path to your dataset file
data = pd.read_excel('gneres_test.xlsx')

# Selecting a subset of the dataset for a clearer visualization
subset_data = data.iloc[:15, :]

# Normalizing the data for better visual representation
normalized_data = (subset_data - subset_data.min()) / (subset_data.max() - subset_data.min())

# Generating the plot with 3D depth effect
fig, ax = plt.subplots(figsize=(15, 10))

# Setting background color for depth effect
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Plotting each normalized row with 3D depth effect
for index, row in normalized_data.iterrows():
    smooth_line = np.interp(np.linspace(0, len(row) - 1, 500), np.arange(len(row)), row)
    # Adding a shadow for each line to create a 3D effect
    for depth in np.linspace(0, 1, 10):
        ax.plot(smooth_line + index * 0.5 - depth, linewidth=1.2, color=(0.3, 0.3, 0.3, 0.3 - depth/10))

    ax.plot(smooth_line + index * 0.5, linewidth=1.2, color=sns.color_palette("tab10")[index % 10])

# Adding enhancements for clarity
plt.xlabel('Musical Attributes', fontsize=14, color='white', labelpad=20)
plt.ylabel('Normalized Values & Records', fontsize=14, color='white', labelpad=20)
plt.title('Pulsar-Style Visualization of Musical Attributes', fontsize=16, color='white', pad=20)
plt.xticks(ticks=np.linspace(0, 500, len(subset_data.columns)), labels=subset_data.columns, rotation=45, fontsize=12, color='white')
plt.yticks(color="grey", size=12)
plt.gca().invert_yaxis()  # Invert y-axis for visual style
plt.grid(True, linestyle='--', alpha=0.7, color='grey')  # Adding a grid for better readability
plt.tight_layout()  # Adjust layout

# Display the plot
plt.show()
