# Getting started!

# Because I'm a pleb, this exploration (not official EDA) will be 
# in a vanilla .py file instead of a nice Jupyter notebook.

'''
Two Sigma Financial News Competition

Predict stock price movement based on market state and news articles.
Projections are 10 days into the future using history and a refreshed 
market and news state.

! Limitations:
You can only submit from Kaggle Kernels, and you may not use other 
data sources, GPU, or internet access.

! This is a two-stage competition. In Stage One you can edit your Kernels
and improve your model, where Public Leaderboard scores are based on their 
predictions relative to past market data. At the beginning of Stage Two, 
your Kernels are locked, and we will re-run your Kernels over the next six months, 
scoring them based on their predictions relative to live data as those six months 
unfold.


! Must use custom kaggle.competitions.twosigmanews Python module. The purpose of this 
module is to control the flow of information to ensure that you are not using future 
data to make predictions for the current trading day.

! Structure of this file:
Section chunk by chunk and explain what the code does. We'll have our actual EDA be 
presented nicely in a Jupyter notebook. This file is just for learning to pull 
the data and run some basic scripts.
'''

from kaggle.competitions import twosigmanews
# You can only call make_env() once, so don't lose it!
env = twosigmanews.make_env()
print('Done!')

(market_train_df, news_train_df) = env.get_training_data()

print("MARKET TRAIN DF")
print("Dimension set: ", list(market_train_df))
print("GG, shape of df is ... ", market_train_df.shape)

print("NEWS TRAIN DF")
print("Dimension set: ", list(news_train_df))
print("GG, shape of df is ... ", news_train_df.shape)

'''
get_prediction_days function¶

! Generator which loops through each "prediction day" (trading day) and provides all 
market and news observations which occurred since the last data you've received. Once you 
call predict to make your future predictions, you can continue on to the next prediction day.

! Yields:

While there are more prediction day(s) and predict was called successfully since the last 
yield, yields a tuple of:

market_observations_df: DataFrame with market observations for the next prediction day.
news_observations_df: DataFrame with news observations for the next prediction day.
predictions_template_df: DataFrame with assetCode and confidenceValue columns, prefilled with confidenceValue = 0, to be filled in and passed back to the predict function.
If predict has not been called since the last yield, yields None.
'''
