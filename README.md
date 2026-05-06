# Codesoft-Project-3

# Simple Movie Recommendation System

This project contains two simple implementations of recommendation systems in Python. It serves as an educational starting point to understand how different recommendation algorithms work.

## Features

This repository includes two different approaches to recommending movies:

1. **Collaborative Filtering (`collaborative_filtering.py`)**:
   - **Type**: User-Based Collaborative Filtering.
   - **How it works**: It finds users who have similar tastes to you by calculating the Euclidean distance between your ratings and theirs. It then recommends movies that those similar users rated highly, but you haven't seen yet.
   - **Dependencies**: None (Pure Python).

2. **Content-Based Filtering (`content_based_filtering.py`)**:
   - **Type**: Item-Based Content Filtering.
   - **How it works**: It looks at the properties of the items themselves (in this case, movie genres and plot descriptions). It uses TF-IDF to process the text and calculates the Cosine Similarity between movies. If you like a specific movie, it recommends other movies with similar descriptions.
   - **Dependencies**: `pandas`, `scikit-learn`.

## Prerequisites

To run the content-based filtering script, you will need to install a few external libraries. You can do this using `pip`:

```bash
pip install -r requirements.txt
```

*(Note: The collaborative filtering script requires no external installations and runs on standard Python.)*

## Usage

You can run either script directly from your terminal or command prompt.

**To run the Collaborative Filtering script:**
```bash
python collaborative_filtering.py
```

**To run the Content-Based Filtering script:**
```bash
python content_based_filtering.py
```

### Experimenting with Your Own Data

Both scripts use small, hardcoded dummy datasets to make it easy to understand the core concepts without dealing with complex data loading. 

Feel free to open the files in your text editor and modify the `user_ratings` dictionary (for collaborative filtering) or the `data` dictionary (for content-based filtering) to add your own users, movies, and ratings!

## Future Improvements
- Integrate larger, real-world datasets (e.g., MovieLens).
- Implement a Hybrid Recommendation System that combines both collaborative and content-based approaches.
- Add a user interface (CLI or Web UI).
