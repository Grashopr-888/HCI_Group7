import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to create and display a single spider chart with a darker background
def create_darker_spider_chart(csv_data):
    # Selecting random cells from column C and D
    random_row = csv_data.sample()
    music_terms = str(random_row.iloc[0]['music_categories']).split(', ')
    movie_terms = str(random_row.iloc[0]['movie_categories']).split(', ')

    # Finding the overlap and unique terms
    categories = list(set(music_terms).union(set(movie_terms)))
    num_vars = len(categories)
    
    # Combining the values to find the maximum value for each category (overlap)
    values_music = [1 if category in music_terms else 0 for category in categories]
    values_movie = [1 if category in movie_terms else 0 for category in categories]
    combined_values = [max(m, v) for m, v in zip(values_music, values_movie)]
    
    # Complete the loop for the chart
    combined_values += combined_values[:1]
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]

    # Plotting the spider chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#202020')  # Very dark grey background outside of the circle
    ax.set_facecolor('#202020')

    # Adding the combined layer
    ax.fill(angles, combined_values, color='blue', alpha=0.5)

    # Customizing the plot
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8, color='white')
    ax.set_yticklabels([])  # Hide the radial labels

    # Show the plot
    plt.show()

# Load your CSV data here
csv_data = pd.read_csv('combinedcategories_test2.csv')  # Make sure to replace with your actual CSV path

# Run the function to create and display a single spider chart with a darker background
create_darker_spider_chart(csv_data)
