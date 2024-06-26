import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go

st.header('Classical Models')


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

metric = st.radio('**Select metric**', ('mae', 'mse', 'rmse'))

fig = go.Figure()
fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results[f'test_{metric}']['mean'], 
                     error_y=dict(type = 'data', array = agg_cv_results[f'test_{metric}']['std'], visible = True), name = 'testset', orientation='v')) 
fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results[f'train_{metric}']['mean'], 
                     error_y=dict(type = 'data', array = agg_cv_results[f'train_{metric}']['std'], visible = True), name = 'trainset', orientation='v')) 

fig.update_layout(title = f'Average {metric} from 5-fold cross-validation of Surprise models with optimized parameters',  
                  xaxis_title = 'Model', yaxis_title = f'Average {metric} (cv=5)') # Title and axis titles
fig.update_layout(autosize=False, width=1000, height=400) #,legend=dict(orientation="h", y=-0.1)) # Figure size
fig.update_layout(legend=dict(x=0, y=1))

# sort ascending
order = agg_cv_results[f'test_{metric}']['mean'].sort_values().index
fig.update_xaxes(categoryorder='array', categoryarray= order)


st.plotly_chart(fig)


### chart cv times

sorting = st.radio('**Select model sorting**', ('like chart above', 'fit_time', 'test_time'))
if sorting == 'like chart above': sorting = f'test_{metric}'

fig = go.Figure()
fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results['test_time']['mean'], 
                     error_y=dict(type = 'data', array = agg_cv_results['test_time']['std'], visible = True), name = 'test time', orientation='v')) 
fig.add_trace(go.Bar(x = agg_cv_results.index, y = agg_cv_results['fit_time']['mean'], 
                     error_y=dict(type = 'data', array = agg_cv_results['fit_time']['std'], visible = True), name = 'fit time', orientation='v')) 

fig.update_layout(title = 'Average fit and test times in 5-fold cross-validation', 
                  xaxis_title = 'Model', yaxis_title = 't [s]') # Title and axis titles
fig.update_layout(autosize=False, width=1000, height=400) #,legend=dict(orientation="h", y=-0.1)) # Figure size
fig.update_layout(legend=dict(x=0, y=1))

# sort like other graph
order = agg_cv_results[sorting]['mean'].sort_values().index
fig.update_xaxes(categoryorder='array', categoryarray= order)

st.plotly_chart(fig)