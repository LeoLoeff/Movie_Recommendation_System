# ProjectTemplate

## Explanations and Instructions

This repository contains the files needed to initialize a project for your [DataScientest](https://datascientest.com/) training.

It contains mainly the present README.md file and an application template [Streamlit](https://streamlit.io/).

**README**

The README.md file is a central element of any git repository. It allows you to present your project, its objectives, and to explain how to install and launch the project, or even how to contribute to it.

You will have to modify different sections of this README.md to include the necessary informations.

- Complete the sections (`## Presentation and Installation` `## Streamlit App`) following the instructions in these sections.
- Delete this section (`## Explanations and Instructions`)

**Streamlit Application**

A [Streamlit] application template (https://streamlit.io/) is available in the [streamlit_app](streamlit_app) folder. You can use this template to start with your project.

## Presentation and Installation

Complete this section with a brief description of your project, the context (including a link to the DataScientest course), and the objectives.

You can also add a brief presentation of the team members with links to your respective networks (GitHub and/or LinkedIn for example).

**Example:**

This repository contains the code for our project **Movie Recommendation System**, developed during our [Data Scientist training](https://datascientest.com/en/data-scientist-course) at [DataScientest](https://datascientest.com/).

The goal of this project is to create a recommendation system based on the MovieLens 25M dataset using collaborative filtering and model optimization through Deep Learning algorithms.

This project was developed by the following team :

- Lena Ametsbichler ([GitHub](https://github.com/) / [LinkedIn](http://linkedin.com/))
- Leonhard Löffler ([GitHub](https://github.com/) / [LinkedIn](http://linkedin.com/))

You can browse and run the [notebooks](./notebooks). 

You will need to download the data from [MovieLens](https://files.grouplens.org/datasets/movielens/ml-25m.zip) and extract/save it to the directory data/raw:

├── data               <- Should be in your computer but not on Github (only in .gitignore)
│   ├── dataframes     <- Pre-processed data for Streamlit app.
│   ├── models         <- Pre-calculated models for Streamlit app.
│   ├── processed      <- The final, canonical data sets for modeling; Should be on your computer but not on Github (only in .gitignore)
│   ├── raw            <- The original, immutable data dump; Should be on your computer but not on Github (only in .gitignore)
│   └── visualization  <- Pre-calculated charts for Streamlit app.

You will need to install the dependencies (in a dedicated environment) :

```
pip install -r requirements.txt
```

## Streamlit App

**Add explanations on how to use the app.**

To run the app (be careful with the paths of the files in the app):

```shell
conda create --name my-awesome-streamlit python=3.9
conda activate my-awesome-streamlit
pip install -r requirements.txt
streamlit run app.py
```

The app should then be available at [localhost:8501](http://localhost:8501).
