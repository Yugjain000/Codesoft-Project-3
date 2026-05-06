import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Dummy dataset: Movies and their descriptions/genres
data = {
    'movie_id': [1, 2, 3, 4, 5, 6],
    'title': [
        'The Matrix', 
        'Inception', 
        'The Notebook', 
        'Titanic', 
        'Interstellar', 
        'La La Land'
    ],
    'description': [
        'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers. Sci-Fi Action',
        'A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O. Sci-Fi Thriller',
        'A poor yet passionate young man falls in love with a rich young woman, giving her a sense of freedom, but they are soon separated because of their social differences. Romance Drama',
        'A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic. Romance Drama',
        'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival. Sci-Fi Adventure',
        'While navigating their careers in Los Angeles, a pianist and an actress fall in love while attempting to reconcile their aspirations for the future. Romance Musical'
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

def create_similarity_matrix(df):
    """
    Creates a cosine similarity matrix based on the movie descriptions.
    """
    # Initialize the TF-IDF Vectorizer
    # Remove all english stop words such as 'the', 'a', etc.
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Construct the required TF-IDF matrix by fitting and transforming the data
    tfidf_matrix = tfidf.fit_transform(df['description'])
    
    # Compute the cosine similarity matrix
    # linear_kernel is equivalent to cosine similarity since TF-IDF vectors are already normalized
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    return cosine_sim

# Build the similarity matrix
cosine_sim_matrix = create_similarity_matrix(df)

# Construct a reverse map of indices and movie titles
indices = pd.Series(df.index, index=df['title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim_matrix, df=df):
    """
    Function that takes in movie title as input and outputs most similar movies.
    """
    if title not in indices:
        return f"Movie '{title}' not found in the dataset."
        
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwise similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 2 most similar movies (ignoring the first one since it is the movie itself)
    sim_scores = sim_scores[1:3]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 2 most similar movies
    return df['title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    print("--- Content-Based Filtering System ---")
    
    movies_to_test = ['The Matrix', 'The Notebook']
    
    for movie in movies_to_test:
        print(f"\nBecause you watched '{movie}':")
        recommendations = get_recommendations(movie)
        
        for i, rec_movie in enumerate(recommendations, 1):
            print(f"  {i}. {rec_movie}")
