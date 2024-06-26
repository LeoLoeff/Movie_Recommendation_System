import streamlit as st

st.header('Advanced Models')
st.write("""
    We have tested deep learning techniques, implementing a Neural Collaborative Filtering (NCF) model to improve predictive performance.

    ### Neural Collaborative Filtering
    
    The NCF model is designed for collaborative filtering tasks and applies neural networks to predict user-item ratings. Here are some of the techniques used:

    - **Embeddings**:
        - User and item IDs were transformed into dense vector representations using embedding layers.
        - Additionally, a Word2Vec model was trained on tags from the dataset, transforming each tag into an embedding vector to capture semantic relationships.
    
    - **Dense Layers**:
        - Combined user and item embeddings were passed through several dense layers with ReLU (Rectified Linear Unit) activations to learn complex patterns.
    
    - **Dropout**:
        - Dropout layers were added to the network to prevent overfitting by randomly setting a fraction of input units to zero during training.
    
    - **Compilation**:
        - The model was compiled using the Adam optimizer, which adjusts the learning rate during training, and Mean Absolute Error (MAE) as the loss function.
    
    - **Hyperparameter Tuning**:
        - RandomizedSearchCV was used to explore different combinations of hyperparameters, including embedding dimensions, dropout rates, dense layer units, learning rates, and regularization strengths.
        - The best hyperparameters were identified and used to train the main NCF model.
    
    ### Results
    - The NCF model showed potential with promising results in preliminary tests, but it requires further refinement to consistently outperform classical methods.
    - When additional features such as tag embeddings and one-hot encoded genres were included, the updated NCF model showed slight improvements but also presented mixed results.

""")
st.image("images/img3.jpg", caption="Training NCF", width=550)