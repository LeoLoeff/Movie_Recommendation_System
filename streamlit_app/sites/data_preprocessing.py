import streamlit as st

st.header('Data Preprocessing')
st.write("""
    The preprocessing steps were carried out as follows:

    1. **Data Import**:
        - Imported necessary dataframes from the MovieLens 25M dataset.
        - Specifically utilized 'genome-scores', 'genome-tags', 'movies', and 'ratings' dataframes which contain essential information on movies, user ratings, and genome tags.
    
    2. **Data Merging**:
        - Merged the 'movies' dataframe with the 'genome-scores' dataframe on the 'movieId' column to combine movie details with their respective genome scores.
        - Next, merged the resulting dataframe with the 'genome-tags' dataframe on the 'tagId' column, integrating descriptive tags for each genome score.
        - Dropped the 'tagId' column as it was no longer necessary for further analysis.
    
    3. **Filtering Tags**:
        - Sorted the combined dataframe by 'movieId' and 'relevance' in descending order.
        - Retained only the top 40 tags for each movie, making the dataset more manageable and meaningful.
    
    4. **Aggregating Tags and Relevances**:
        - Grouped the dataframe by 'movieId', 'title', and 'genres'.
        - Aggregated 'relevance' and 'tag' values into lists within each group, maintaining a structured and compact form for each movie entry.
    
    5. **Merging with Ratings**:
        - Removed the 'timestamp' column in the 'ratings' dataframe as it was unnecessary for the analysis.
        - Merged the aggregated tags dataframe with the 'ratings' dataframe on the 'movieId' column, linking each movie's tag information with user ratings.
        - Dropped rows with missing values and converted 'userId' column to integer type for memory optimization.
    
    6. **Filtering by Movie Occurrences**:
        - Counted occurrences of each 'movieId' and retained only movies with 2000 or more ratings to ensure robustness.
    
    7. **Sampling**:
        - Defined a custom sampling function to reduce the number of rows while maintaining a representative sample.
        - Applied the sampling function to each 'movieId' group, resulting in a dataset with 5,273,559 entries.
    
    The final dataset, approximately 301.8 MB in memory usage, is ready for further analysis and modeling.
""")