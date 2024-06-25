import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.header('Data Exploration')


### general information about the dataset

st.subheader('The MovieLens 25M Dataset')

st.write('Data volume: 25 million ratings, 62,000 movies, and 162,000 users')
st.write('Time frame covered: January 1995 - November 2019')

ml = pd.DataFrame({"table name": ['movies.csv','links.csv','ratings.csv','tags.csv','genome-scores.csv','genome-tags.csv'],
                  "columns": ['movieId, title, genres','movieId, imdbId, tmdbId','userId, movieId, rating, timestamp','userId, movieId, tag, timestamp','movieId, tagId, relevance','tagId, tag'],
                  "length": [62423,62423,25000095,1093360,15584448,1128]})
                #   "length": ['62,423','62,423','25,000,095','1,093,360','15,584,448','1,128']})
                  
st.dataframe(ml, hide_index=True)


### loading data and calculations
@st.cache_data
def load_df_movies():
    df = pd.read_csv('../../movie_recommendation/data/raw/ml-25m/movies.csv')
    return df
df_movies = load_df_movies()

# hot-one encoding to split genres in separate columns using pandas strin method
df_movies = pd.concat([df_movies, df_movies['genres'].str.get_dummies(sep='|')], axis=1)
# removing unnecessary columns
df_movies.drop(['title','genres'], axis=1, inplace=True)
# rename column to avoid spaces
df_movies.rename(columns={'(no genres listed)':'no_genre_listed'}, inplace=True)

frequency_genres = df_movies.iloc[:,1:].sum()

@st.cache_data
def load_genre_ratings():
    df = pd.read_parquet('../data/dataframes/genre_ratings.parquet.gzip')
    return df
genre_ratings = load_genre_ratings()

@st.cache_data
def load_user_rating_avg():
    df = pd.read_parquet('../data/dataframes/user_rating_avg.parquet.gizp')
    return df
user_rating_avg = load_user_rating_avg()

@st.cache_data
def load_user_rating_sum():
    df = pd.read_parquet('../data/dataframes/user_rating_sum.parquet.gizp')
    return df
user_rating_sum = load_user_rating_sum()

# genre_ratings = pd.read_parquet('../data/dataframes/genre_ratings.parquet.gzip')
# user_rating_avg = pd.read_parquet('../data/dataframes/user_rating_avg.parquet.gizp')
# user_rating_sum = pd.read_parquet('../data/dataframes/user_rating_sum.parquet.gizp')

# genre_ratings = pd.read_parquet('../data/dataframes/genre_ratings.parquet.gzip')

stat_user_rating_sum = user_rating_sum.describe()
stat_user_rating_avg = user_rating_avg.describe()

### definition of table style / highlight

def higlight_mmm(s):
    is_min = s.index == 'min'
    is_median = s.index == '50%'
    is_max = s.index == 'max'
    return ['background-color: lightblue' if m else 'background-color: lightblue' if n else 'background-color: lightblue' if o else '' for m,n,o in zip(is_min, is_median, is_max)]

styled_stat_user_rating_sum = stat_user_rating_sum.style.apply(higlight_mmm, axis=0)
styled_stat_user_rating_avg = stat_user_rating_avg.style.apply(higlight_mmm, axis=0)

### generation of charts

# pie chart Proportion of genres
fig_pie = go.Figure()
fig_pie.add_trace(go.Pie(labels=frequency_genres.index, values=frequency_genres, direction='clockwise'))
fig_pie.update_layout(legend_title = 'Genres', title='Proportions of genres', title_x=0.45, title_y=0.95)
fig_pie.update_layout(autosize=False, width=600, height=600)

# boxplot rating distribution per genre
@st.cache_data
def chart_box():
    fig_box = plt.figure(figsize=(10, 6))
    sns.boxplot(genre_ratings.replace({0:np.nan}).iloc[:,1:-2], fliersize=1)
    plt.title('Distribution movie rating per genre')
    plt.xticks(rotation=75);
    return fig_box
fig_box = chart_box()

### display of charts

# checkbox for displaying plots
if st.checkbox('Show DataViz'):
    st.subheader('Genre distribution and rating')
    st.plotly_chart(fig_pie)
    st.pyplot(fig_box)

    st.subheader('Rating behaviour')
    st.markdown('**Basic statistics**')

    left_column, right_column = st.columns(2)
    left_column.write('Number of movies rated by each user:')
    left_column.table(styled_stat_user_rating_sum)
    
    # left_column.markdown('- minimum = 20 ratings')
    # left_column.markdown('- median = 71 ratings')
    # left_column.markdown('- maximum > 32.000 ratings')

    right_column.write('Average rating per user:')
    right_column.table(styled_stat_user_rating_avg)
    # right_column.markdown('- median = 3.7')
    # right_column.markdown('- There are users with an average rating of 0.5 as well as users with 5.0 --> their ratings have a standard deviation of 0')
