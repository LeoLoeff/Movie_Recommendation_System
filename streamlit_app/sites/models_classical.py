import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

st.header('Classical Models')

# counter for automated chart number updates
n_chart = 0

st.subheader('Methodology')
st.markdown('FILL WITH TEXT')


################################## parameter tuning section #########################################

st.subheader('Surprise models: parameter tuning and cross-validation')
st.markdown('''**Surprise** is a Python library for recommender systems, which focuses on collaborative filtering.''')
            # Its toolkit is derived from scikit-learn and comprises, among others, of well known functions like *train_test_split*, *GridSearchCV* and *cross_validate*. 
            # Surprise provides manifold prediction algorithms like four different versions of *k-nearest-neighbor* (*KNN*) and 
            # matrix factorization algorithms like *SVD* and *NMF* (non-negative matrix factorization).  
st.markdown('''Benchmark: *NormalPredictor* model, which randomly predicts ratings between 0.5 and 5.0, based on the rating distribution in the training set.''')


default_metrics = joblib.load('../data/models/surp_metrics_default_models.pkl')

# create empty DataFrame with columns according to metrics
keys = list(default_metrics.keys()) # list of keys, which hold the model names
# df_metrics = pd.DataFrame(default_metrics, index=['MAE','MSE','RMSE']).T # e.g. use first model to retrieve coumns
df_metrics = pd.DataFrame(default_metrics, index=['mae','mse','rmse']).T # e.g. use first model to retrieve coumns

with st.expander('See MAE, MSE and RMSE for Surprise models with default* parameters'):
    n_chart = n_chart + 1

    metric = 'mae'
    metric2 = 'mse'
    metric3 = 'rmse'

    fig = go.Figure()
    fig.add_trace(go.Bar(x = df_metrics.index, y = df_metrics[f'{metric}'], name = f'{metric}', orientation='v')) 
    fig.add_trace(go.Bar(x = df_metrics.index, y = df_metrics[f'{metric2}'], name = f'{metric2}', orientation='v')) 
    fig.add_trace(go.Bar(x = df_metrics.index, y = df_metrics[f'{metric3}'], name = f'{metric3}', orientation='v')) 

    fig.update_layout(xaxis_title = 'Model', yaxis_title = 'Error') # axis titles
    fig.update_layout(legend=dict(x=0, y=1))

    # sort ascending
    order = df_metrics[f'{metric}'].sort_values().index
    fig.update_xaxes(categoryorder='array', categoryarray= order)

    st.plotly_chart(fig)
    st.caption(f'Chart {n_chart}: Different performance metrics for default Surprise models.')


################################## cross-validation section #########################################

### data import and preparation

cv_results = joblib.load('../data/models/surp_cv_results.json')

# create empty DataFrame with columns according to cv_results
keys = list(cv_results.keys()) # list of keys, which hold the model names
df_cv_results = pd.DataFrame(columns=cv_results[keys[0]].keys()) # e.g. use first model to retrieve coumns

# iterate over keys to fill df_cv_results successively
for model in keys:
    df = pd.DataFrame.from_dict(cv_results[model])
    df['model'] = model[3:] # write model name in new column, starting at position 3 to drop "cv_"
    df_cv_results = pd.concat([df_cv_results, df], axis=0, ignore_index=True) # append df to df_cv_results

# rename 'rand' to 'NormalPredictor'
df_cv_results['model'].loc[df_cv_results.model == 'rand'] = 'NormalPredictor'

agg_cv_results = df_cv_results.groupby(by=['model']).agg(['mean','std']) #, as_index=False


### char cv results
n_chart = n_chart + 1

with st.sidebar.container(border=True):
    st.markdown(f'### Chart {n_chart} options')
    metric = st.radio('**Select metric:**', ('mae', 'mse', 'rmse'))
    comparison_tuned = st.checkbox('result after tuning')

fig = go.Figure()
fig.add_trace(go.Bar(x = df_metrics.index, y = df_metrics[f'{metric}'], name = f'{metric} before optimization', orientation='v'))
# fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results[f'test_{metric}']['mean'], 
#                      error_y=dict(type = 'data', array = agg_cv_results[f'test_{metric}']['std'], visible = True), name = 'testset', orientation='v')) 
# fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results[f'train_{metric}']['mean'], 
#                      error_y=dict(type = 'data', array = agg_cv_results[f'train_{metric}']['std'], visible = True), name = 'trainset', orientation='v'))
if comparison_tuned:
    # fig.add_trace(go.Bar(x = df_metrics.index, y = df_metrics[f'{metric}'], name = f'{metric} before optimization', orientation='v'))
    fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results[f'test_{metric}']['mean'], 
                     error_y=dict(type = 'data', array = agg_cv_results[f'test_{metric}']['std'], visible = True), 
                     name = f'average {metric} after optimization (cv=5)', orientation='v')) 

fig.update_layout(xaxis_title = 'Model', yaxis_title = 'Error') # axis titles
fig.update_layout(legend=dict(x=0, y=1))

# sort ascending
order = agg_cv_results[f'test_{metric}']['mean'].sort_values().index
fig.update_xaxes(categoryorder='array', categoryarray= order)


st.plotly_chart(fig)
st.caption(f'Chart {n_chart}: Average {metric} from 5-fold cross-validation of optimized Surprise models.')

st.markdown('''*GridSearchCV* was applied to all elegible models (*SlopeOne* and *NormalPredictor* do not take arguments).
            Performance was measured in 5-fold *cross-validation*.''')

### chart cv times
with st.expander('See train and test time per model'):
    n_chart = n_chart + 1

    with st.sidebar.container(border=True):
        st.markdown(f'### Chart {n_chart} options')
        sorting = st.radio('**Select model sorting:**', (f'like chart {n_chart-1}', 'fit_time', 'test_time'))
        if sorting == f'like chart {n_chart-1}': sorting = f'test_{metric}'

    fig = go.Figure()
    fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results['test_time']['mean'], 
                        error_y=dict(type = 'data', array = agg_cv_results['test_time']['std'], visible = True), name = 'test time', orientation='v')) 
    fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results['fit_time']['mean'], 
                        error_y=dict(type = 'data', array = agg_cv_results['fit_time']['std'], visible = True), name = 'fit time', orientation='v')) 

    fig.update_layout(xaxis_title = 'Model', yaxis_title = 't [s]') # axis titles
    fig.update_layout(legend=dict(x=0, y=1))

    # sort like other graph
    order = agg_cv_results[sorting]['mean'].sort_values().index
    fig.update_xaxes(categoryorder='array', categoryarray= order)

    st.plotly_chart(fig)
    st.caption(f'Chart {n_chart}: Average fit and test times during 5-fold cross-validation of optimized Surprise models.')

# with st.expander('See learnings'):
box =  st.container(border=True)
box.markdown('#### Learnings from classical model training')
box.markdown('- All Surprise models perform significantly better than benchmark (random predictor).')
box.markdown('- Parameter tuning with GridSearchCV provided slight improvement of model performance, most significantly for KNNBasic (MAE was reduced by 7%).')
box.markdown('- The top 3 classical models are KNNBaseline, SVD and KNNZScore.')