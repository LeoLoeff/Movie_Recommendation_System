import streamlit as st

st.set_page_config(page_title="Movie Recommender System", page_icon=":material/edit:")

intro_page = st.Page("sites/intro.py", title="Introduction")
data_exploration_page = st.Page("sites/data_exploration.py", title="Data Exploration")
data_prep_page = st.Page("sites/data_preprocessing.py", title="Data Preprocessing")
models_page = st.Page("sites/models.py", title="Models")
results_page = st.Page("sites/results.py", title="Results")
outlook_page = st.Page("sites/challenges_outlook.py", title="Challenges & Outlook")
conclusion_page = st.Page("sites/conclusion.py", title="Conclusion")
about_page = st.Page("sites/about.py", title="About")


pg = st.navigation([intro_page,
                    data_exploration_page,
                    data_prep_page,
                    models_page,
                    results_page,
                    outlook_page,
                    conclusion_page,
                    about_page])

## navigation with sub-groups
# pg = st.navigation({"Getting started": [intro_page],
#                     "Data": [data_exploration_page, data_prep_page],
#                     "Modeling": [models_page],
#                     "Discussion": [results_page, outlook_page],
#                     "": [conclusion_page],
#                     "_____": [about_page]})


pg.run()

