
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
url = 'https://raw.githubusercontent.com/rashida048/Some-NLP-Projects/master/movie_dataset.csv'
movies = pd.read_csv(url)

# Check for null values and drop them
movies.dropna(inplace=True)

# Features to be considered for recommendation
features = ['keywords', 'cast', 'genres', 'director']

# Combine the selected features
def combine_features(row):
    return ' '.join(row[feature] for feature in features)

movies['combined_features'] = movies.apply(combine_features, axis=1)

# Convert text to vectors using CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(movies['combined_features'])

# Compute the cosine similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

# Function to get movie title from index
def get_title_from_index(index):
    return movies.iloc[index]['title']

# Function to get index from movie title
def get_index_from_title(title):
    result = movies[movies.title.str.lower() == title.lower()]
    return result.index[0] if not result.empty else None

# Recommend similar movies
def recommend_movies(movie_title):
    movie_index = get_index_from_title(movie_title)
    if movie_index is None:
        return "Movie not found in the dataset."

    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:6]

    recommendations = [get_title_from_index(i[0]) for i in sorted_similar_movies]
    return recommendations

# Example usage
movie_name = input("Enter a movie name: ")
recommended = recommend_movies(movie_name)
print("\nTop 5 similar movies to '{}':".format(movie_name))
for i, rec in enumerate(recommended, 1):
    print(f"{i}. {rec}")
