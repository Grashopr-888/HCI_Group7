import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

def load_excel_data(file_path, sheet_names):
    return pd.read_excel(file_path, sheet_name=sheet_names)

def get_random_movie_terms(sheet, column_name, num_terms=3):
    return ', '.join(random.sample(list(sheet[column_name].dropna()), num_terms))

def find_best_match(sheet, categories_mapping, concatenated_terms):
    movie_terms_list = concatenated_terms.split(', ')
    movie_categories = set(categories_mapping.get(term.strip(), None) for term in movie_terms_list)
    movie_categories.discard(None)

    best_match_count = 0
    best_match_music_terms = ""

    for index, row in sheet.iterrows():
        music_terms_string = str(row['music_terms'])
        music_terms_list = music_terms_string.split(', ')
        music_categories = set(categories_mapping.get(term.strip(), None) for term in music_terms_list)
        music_categories.discard(None)

        match_count = len(movie_categories.intersection(music_categories))

        if match_count > best_match_count:
            best_match_count = match_count
            best_match_music_terms = music_terms_string

    return best_match_music_terms

def create_spider_chart(categories_list, movie_counts, music_counts, chart_title):
    num_categories = len(categories_list)
    angles = [n / float(num_categories) * 2 * np.pi for n in range(num_categories)]
    angles += angles[:1]

    movie_data = movie_counts + movie_counts[:1]
    music_data = music_counts + music_counts[:1]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True), facecolor='black')
    plt.xticks(angles[:-1], categories_list, color='white', size=12)
    ax.set_facecolor('black')
    ax.set_rlabel_position(0)
    plt.yticks([1, 2, 3], ["1", "2", "3"], color="white", size=7)
    plt.ylim(0, 3)

    ax.plot(angles, movie_data, linewidth=1, linestyle='solid', label='Movie Terms', color='blue')
    ax.fill(angles, movie_data, 'b', alpha=0.1)
    ax.plot(angles, music_data, linewidth=1, linestyle='solid', label='Music Terms', color='red')
    ax.fill(angles, music_data, 'r', alpha=0.1)

    plt.title(chart_title, size=20, color='white', y=1.1)
    plt.legend(loc='upper right', facecolor='darkgrey')
    plt.show()

def main():
    file_path = '/Users/trent/HCI_Prototype/cluster_categories_test (3).xlsx'  # Replace with your file path
    sheet_names = ['criterion_collection_ets', 'genres_test_with_music_terms', 'categories']
    excel_data = load_excel_data(file_path, sheet_names)

    movie_terms_sheet = excel_data['criterion_collection_ets']
    music_terms_sheet = excel_data['genres_test_with_music_terms']
    categories_sheet = excel_data['categories']

    categories_mapping = {term: category for category in categories_sheet.columns for term in categories_sheet[category].dropna().tolist()}
    random_movie_terms = get_random_movie_terms(movie_terms_sheet, 'movie_terms')
    best_music_match = find_best_match(music_terms_sheet, categories_mapping, random_movie_terms)

    movie_term_categories = [categories_mapping.get(term.strip(), "Other") for term in random_movie_terms.split(', ')]
    music_term_categories = [categories_mapping.get(term.strip(), "Other") for term in best_music_match.split(', ')]

    category_counts = {cat: [movie_term_categories.count(cat), music_term_categories.count(cat)] for cat in set(movie_term_categories + music_term_categories)}
    categories_list = list(category_counts.keys())
    movie_counts = [category_counts[cat][0] for cat in categories_list]
    music_counts = [category_counts[cat][1] for cat in categories_list]

    create_spider_chart(categories_list, movie_counts, music_counts, 'Categorical Matches: Movie vs Music Terms')

if __name__ == "HCI_Categorical_SpiderChart_Test":
    main()

