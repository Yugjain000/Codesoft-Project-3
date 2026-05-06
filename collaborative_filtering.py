import math

# Dummy dataset: Users and their ratings for various movies (1-5 scale)
# A rating of None or missing key means the user hasn't seen the movie.
user_ratings = {
    'Alice': {
        'The Matrix': 5,
        'Inception': 4,
        'Interstellar': 4,
        'The Notebook': 1,
        'Titanic': 2
    },
    'Bob': {
        'The Matrix': 4,
        'Inception': 5,
        'The Notebook': 1,
        'Titanic': 2
        # Has not seen 'Interstellar'
    },
    'Charlie': {
        'The Notebook': 5,
        'Titanic': 4,
        'The Matrix': 2,
        'Inception': 1
    },
    'David': {
        'The Matrix': 5,
        'Inception': 4,
        'Interstellar': 5,
        'The Notebook': 1
    },
    'Eve': {
        'The Notebook': 4,
        'Titanic': 5,
        'La La Land': 5
    }
}

def calculate_similarity(user1, user2):
    """
    Calculate Euclidean distance-based similarity between two users.
    Returns a value between 0 and 1, where 1 means identical preferences.
    """
    movies1 = user_ratings.get(user1, {})
    movies2 = user_ratings.get(user2, {})

    # Find common movies
    common_movies = set(movies1.keys()).intersection(set(movies2.keys()))

    if not common_movies:
        return 0.0 # No similarity if they haven't rated any of the same movies

    # Calculate sum of squared differences
    sum_squared_diff = sum(
        pow(movies1[movie] - movies2[movie], 2) 
        for movie in common_movies
    )

    # Convert distance to a similarity score (1 / (1 + distance))
    distance = math.sqrt(sum_squared_diff)
    similarity = 1 / (1 + distance)
    return similarity

def recommend_movies(target_user, num_recommendations=2):
    """
    Recommend movies for a target user based on user-based collaborative filtering.
    """
    if target_user not in user_ratings:
        return f"User '{target_user}' not found in the dataset."

    target_movies = set(user_ratings[target_user].keys())
    similarities = []

    # Calculate similarity with all other users
    for user in user_ratings:
        if user != target_user:
            sim_score = calculate_similarity(target_user, user)
            similarities.append((user, sim_score))

    # Sort users by similarity descending
    similarities.sort(key=lambda x: x[1], reverse=True)

    recommendations = {}
    
    # We will use a weighted rating approach based on the most similar users
    for similar_user, sim_score in similarities:
        if sim_score <= 0:
            continue
            
        similar_user_movies = user_ratings[similar_user]
        
        for movie, rating in similar_user_movies.items():
            # Only consider movies the target user hasn't seen
            if movie not in target_movies:
                if movie not in recommendations:
                    recommendations[movie] = {'weighted_score': 0, 'sim_sum': 0}
                
                # Add similarity * rating to the score
                recommendations[movie]['weighted_score'] += rating * sim_score
                recommendations[movie]['sim_sum'] += sim_score

    # Calculate final estimated rating for each movie
    final_recommendations = []
    for movie, scores in recommendations.items():
        estimated_rating = scores['weighted_score'] / scores['sim_sum']
        final_recommendations.append((movie, estimated_rating))

    # Sort by estimated rating descending
    final_recommendations.sort(key=lambda x: x[1], reverse=True)

    return final_recommendations[:num_recommendations]

if __name__ == "__main__":
    print("--- User-Based Collaborative Filtering System ---")
    
    users_to_test = ['Bob', 'Eve', 'Charlie']
    
    for user in users_to_test:
        print(f"\nRecommendations for {user}:")
        recs = recommend_movies(user)
        
        if not recs:
            print("  No new movies to recommend.")
        else:
            for i, (movie, expected_rating) in enumerate(recs, 1):
                print(f"  {i}. {movie} (Estimated Rating: {expected_rating:.2f}/5.0)")
