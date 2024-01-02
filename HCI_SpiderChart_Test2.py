import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Function to create and display a single spider chart with a 3D effect and a legend
def modified_create_3d_effect_spider_chart_with_legend(csv_data):
    # Selecting random cells from column C and D
    random_row = csv_data.sample()
    music_terms = str(random_row.iloc[0]['music_categories']).split(', ')
    movie_terms = str(random_row.iloc[0]['movie_categories']).split(', ')

    # Finding the overlap and unique terms
    categories = list(set(music_terms).union(set(movie_terms)))
    num_vars = len(categories)
    
    # Assigning values for music and movie categories
    values_music = [1 if category in music_terms else 0 for category in categories]
    values_movie = [1 if category in movie_terms else 0 for category in categories]
    
    # Complete the loop for the chart
    values_music += values_music[:1]
    values_movie += values_movie[:1]
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]

    # Plotting the spider chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#202020')  # Very dark grey background outside of the circle
    ax.set_facecolor('#202020')

    # Adding the music layer with a shadow for a 3D effect
    music_layer = ax.fill(angles, values_music, color='red', alpha=0.9)
    ax.fill(angles, [x+0.1 for x in values_music], color='darkred', alpha=0.3)  # Shadow for 3D effect

    # Adding the movie layer with a shadow for a 3D effect
    movie_layer = ax.fill(angles, values_movie, color='blue', alpha=0.9)
    ax.fill(angles, [x+0.1 for x in values_movie], color='darkblue', alpha=0.3)  # Shadow for 3D effect

    # Customizing the plot
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=8, color='white')
    ax.set_yticklabels([])  # Hide the radial labels

    # Adding a legend
    plt.legend([music_layer[0], movie_layer[0]], ['Music Categories', 'Movie Categories'], loc='upper right', bbox_to_anchor=(1.1, 1.1))

    # Show the plot
    plt.show()

# Load your CSV data here
csv_data = pd.read_csv('combinedcategories_test3.csv')  # Replace with your actual CSV file path

# Run the function to create and display a single spider chart with a 3D effect and a legend
modified_create_3d_effect_spider_chart_with_legend(csv_data)


