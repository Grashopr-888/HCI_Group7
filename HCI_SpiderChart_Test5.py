import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def modified_create_3d_effect_spider_chart_with_random_values(csv_data):
    # Consistency Check: Ensure no null rows are selected
    csv_data = csv_data.dropna(subset=['music_categories', 'movie_categories'])
    
    # Selecting random cells from 'music_categories' and 'movie_categories'
    random_row = csv_data.sample()
    music_terms = str(random_row.iloc[0]['music_categories']).split(', ')
    movie_terms = str(random_row.iloc[0]['movie_categories']).split(', ')

    # Removing leading and trailing whitespaces
    music_terms = [term.strip() for term in music_terms if term]  # Ensure no empty terms
    movie_terms = [term.strip() for term in movie_terms if term]  # Ensure no empty terms

    # Finding the overlap and unique terms
    categories = list(set(music_terms).union(set(movie_terms)))
    num_vars = len(categories)

    # Safe function to find or generate valence and arousal
    def find_or_generate_value(term, category_list, column_name):
        if term in category_list:
            matched_rows = csv_data[csv_data['Categorical Term'] == term][column_name]
            if not matched_rows.empty and not pd.isnull(matched_rows.values[0]):
                return matched_rows.values[0]
        # Generate a random value rounded to the nearest 0.2
        return round(np.random.uniform(0.2, 1.0) * 5) / 5

    # Finding corresponding valence and arousal values for music and movie categories
    values_music_valence = [find_or_generate_value(category, music_terms, 'Valence_rounded') for category in categories]
    values_movie_valence = [find_or_generate_value(category, movie_terms, 'Valence_rounded') for category in categories]

    values_music_arousal = [find_or_generate_value(category, music_terms, 'Arousal_rounded') for category in categories]
    values_movie_arousal = [find_or_generate_value(category, movie_terms, 'Arousal_rounded') for category in categories]

    # Function to create a spider chart
    def create_spider_chart(fig, position, values_music, values_movie, title, explanation_text):
        angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist() + [0]
        ax = fig.add_subplot(1, 2, position, polar=True)
        ax.set_facecolor('#202020')

        # Adding the music layer with a shadow for a 3D effect
        music_layer = ax.fill(angles, values_music + [values_music[0]], color='red', alpha=0.9)
        ax.fill(angles, [x + 0.1 for x in values_music] + [values_music[0] + 0.1], color='darkred', alpha=0.3)

        # Adding the movie layer with a shadow for a 3D effect
        movie_layer = ax.fill(angles, values_movie + [values_movie[0]], color='blue', alpha=0.9)
        ax.fill(angles, [x + 0.1 for x in values_movie] + [values_movie[0] + 0.1], color='darkblue', alpha=0.3)

        # Customizing the plot
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories, size=8, color='white', rotation=45, ha='right')  # Rotate labels to avoid overlap

        # Setting the numerical labels for the concentric circles
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'], color='white')

        # Adding a legend and title
        ax.legend([music_layer[0], movie_layer[0]], ['Music Categories', 'Movie Categories'], loc='upper right', bbox_to_anchor=(1.1, 1.1))
        ax.set_title(title, color='white', size=14)

        # Adding a text box below the graph to explain Valence and Arousal
        plt.text(0.5, -0.2, explanation_text, ha='center', va='center', fontsize=12, color='white', transform=ax.transAxes)

    # Creating the figure with adjusted size
    fig = plt.figure(figsize=(14, 10))  # Adjusted figure size to accommodate text boxes and prevent overlap
    fig.patch.set_facecolor('#202020')

    # Valence and Arousal explanation texts
    valence_text = "Valence represents the positivity or negativity of the emotion evoked by a category."
    arousal_text = "Arousal indicates the intensity of emotion provoked by a category."

    # Creating the Valence chart with explanation
    create_spider_chart(fig, 1, values_music_valence, values_movie_valence, 'Valence', valence_text)

    # Creating the Arousal chart with explanation
    create_spider_chart(fig, 2, values_music_arousal, values_movie_arousal, 'Arousal', arousal_text)

    # Adjust layout to prevent overlap
    plt.tight_layout(pad=2.0)
    plt.show()

# Load your CSV data
csv_data = pd.read_csv('combinedcategories_test6.csv')  # Replace with your actual CSV file path

# Run the function to create and display the spider charts with a 3D effect and a legend
modified_create_3d_effect_spider_chart_with_random_values(csv_data)


