import streamlit as st

st.title("Movie Recommender System")
st.text("")  # Add empty text for spacing
st.image("images/img1.jpg", caption=" ", width=650)
st.markdown("""
    <p style="line-height: 2;">     
    Recommendation systems are important tools, enhancing customer experience and boosting revenue by providing personalized product or service suggestions.
    Our project focuses on developing a collaborative filtering-based movie recommendation system. We utilized the MovieLens 25M dataset to train and evaluate various models.
    </p>
    
    ## Introduction to the Project
    
    ### Overview
    - **Data Analysis and Preprocessing**: Initial data analysis and preprocessing were conducted to create a manageable dataset for further analysis and model building.
    - **Model Evaluation**: Various models were trained and fine-tuned, with the best-performing models evaluated for their effectiveness.
    - **Collaborative Filtering**: The project employs collaborative filtering, focusing on similarities between users and/or items to provide recommendations.
""", unsafe_allow_html=True)