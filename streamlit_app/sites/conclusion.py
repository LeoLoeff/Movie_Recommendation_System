import streamlit as st

st.header('Conclusion')

st.write("""
        
    ### Key Takeaways
    - **Traditional Models**: Collaborative filtering techniques, particularly matrix factorization (SVD) and KNN-based models, demonstrated robust performance.
    - **Deep Learning Models**: The NCF model showed potential but needs more sophisticated techniques to achieve better results.
    - **Model Evaluation**: The best models provided reasonably close predictions, making them useful for generating relevant movie recommendations.
    
    ### Future Work
    - **Enhancing Data Preprocessing**: Reducing the extent of data reduction during preprocessing.
    - **Extended Parameter Tuning**: Conducting a more exhaustive grid search for better performance.
    - **Dynamic Thresholds**: Using dynamic thresholds for precision and recall to provide more personalized and reliable measures.
    
    Overall, the mixed methodology approach enabled us to leverage the strengths of different models, resulting in a solid and effective recommendation system.
""")