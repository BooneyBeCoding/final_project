# final_project

## RESEARCH QUESTION AND PROPOSAL:
- The 3 most prominent subreddits whose communities are built around the topic of stock market investing each have different constructions of culture. 
- By running a sentiment-gauging cross-analysis over the headline/title of posts of each, can we teach a Machine Learning model to discern which of the subreddits was most likely the subreddit of origin?


### Description 
We would like to investigate whether sentiment analysis data, generated by VADER, can be used in a basic machine learning model to predict post origins 
across multiple Reddit discussion groups (subreddits) that share similar topics but different cultures.

We have an initial dataset comprised of basic post information (title, subreddit origin, upvote score, post link url, comment number, body text, and post date)
for a selection of the top posts (by score) of the three most popular stock investing subreddits (/r/wallstreetbets, /r/investing, and /r/stocks), roughly 1000 
posts per subreddit. Some data points, such as upvote score and comment number, are likely highly correlated to overall subreddit size. It is generally held 
that different subreddits have different cultures, or "feels", and that that is reflected in the types of posts that are successful in a given subreddit. You 
might write a title differently to gain attention successfully, depending on the specific subreddit. To test this at a basic level, we will use the VADER 
sentiment analysis package to assign a score to each post title in our dataset. VADER (Valence Aware Dictionary for Sentiment Reasoning) takes a string, and 
based on an emotion intensities dictionary model, returns four values: negative, neutral, positive, and compound (a normalized value of the three scores). 

We will feed this generated data into a simple machine learning model and see if we can train it to identify the origin of a given post, based on just 
this sentiment information. One approach would be to use a Supervised Logistic Regression model for single element membership. An example of this would be 
that /r/wallstreetbets is generally considered the most divergent of the stock trading subreddits, so the output label for the given input data could be a 
simple Y/N of whether the model thinks the sample post is from /r/wallstreet bets. If we generate a simple five element data set from the original 
data set (the four VADER outputs, plus a "WSB?" column), the rough outline of the model would look like test_Reddit_VADER.ipynb (we don't yet have the 
VADER outputs built, so it doesn't have a data set to run against yet).

It may also be worth feeding the same generated VADER dataset into an unstructured model and see if set to three clusters, if it can pick out the three 
subreddits with any sort of accuracy. 

It might also be interesting to pursue the same line of inquiry with a slightly different dataset. There are two main Game of Thrones subreddits, /r/gameofthrones
and /r/freefolk. If we could generate a similar dataset, we could generate a similar VADER output and run similar ML models to see if it were able to successfully
identify posts based purely on the sentiment analysis. 

### TECHNOLOGIES and METHODOLOGIES LIST:
1. Kaggle - datasets
2. Jupyter - virtual environment
3. Github - version management
4. Python - scripting language
5. Quickbase App - ERD
6. SQLite and SQLAlchemy - database housing and management
7. Vader - Python package for Sentiment Analysis
8. Tableau - visualization
9. VS Code Basic - file creation, idea structure, and organization

## Machine Learning Model
Utilizing VADER Sentiment Analysis on the titles of each subreddit post and a Logistic Regression model to analyse the VADER scores to determine if a post came from WallStreetBets or not.  The model ran at 100% initially, but this was due to biased fields.

### Data PreProcessing for MLM
The Dataset we are utilizing is very well formatted and uniform.  For preprosessing, we removed the "Body" column from the dataframe as it was not always utilized by the post, and not necessary for what we are wanting to train the model on. As well, after adding 4 columns to the DF for the Vader analysis, we modified the "subreddit" column to return a 1 if the post was from r/WallStreetBets and a 0 if the post was from r/stocks or r/investing.
### Feature Engineering & Selection
As mentioned above, we have chosen to utilize [VADER Sentiment Analysis](https://github.com/cjhutto/vaderSentiment) to read the "title" of each post and return a sentiment score for positive, negative, neutral, and compound.  We chose Vader as it is an Georgia Tech created open source sentiment analysis tool that specializes in social media. It generates the four element score based on both lexicon and rule-based criteria. For more information, see here:

Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text. Eighth International Conference on Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.

Once run on each post, these scores were then added to each post in the dataframe.

![](https://github.com/BooneyBeCoding/final_project/blob/main/Images/sum%20of%20Vader%20for%20each%20subreddit.PNG)

### Data Spliting
The data splitting is set to randomizing the test and train datasets, and an 80/20 train/test split.  
### Model Choice
Since we are training our model to determine if posts are from r/wallstreetbets or not through the Sentiment Analysis, we are utilizing Logistic Regression for our Machine Learning Model.  This model has the benefit of being quick to run and rather easy to understand yet has some limitation when it comes to what pieces of the dataset can be utilized as to not throw off the model.
### Changes Made to the model from seg 2 to 3
One of the main changes from segment 2 to segment 3 is the removal of the "Score" and "Number of Comments" columns from the training and testing datasets.  We found that both of those columns had much higher totals for r/wallstreetbets than it did for the 2 other subreddits, thus causing our model to see that and be able to return a 100% accuracy score.

![](https://github.com/BooneyBeCoding/final_project/blob/main/Images/MLM%20total%20100%20percent.PNG)

Upon further evaluation, we realized the model was marking everything at 0 "not WSB" and getting a 2/3rd score (67%) as that is basically what the dataset breaks down to be. One of the reasons for this was that the r/stocks and r/WallStreetBets sentiment scores were remarkably similar.  As well the dataset was skewed to have 1/3 be from WSB and 2/3 be from not WSB.

![](https://github.com/BooneyBeCoding/final_project/blob/main/Images/MLM%20total%2068%20percent.PNG)

After removing the r/stocks sets from the DF, we received a score of 50%, though you could now see the model trying to guess.

With the additions of added Neural Nets, and optimizations, we were able to raise the accuracy up to 64%.

As well, after adding back in the "Score" and "Number of Comments" tabs, the original model was running at a 50% accuracy, when adding a neural net to the model, the accuracy grew to 90%+, but this would defeat the point of the evaluation, given the strong size bias of those two fields.

### Conclusion of Model
In conclusion we found that our model was insufficiant and could not reach our hypothesis.  With more time we would pull data directly from the Reddit API for a more fleshed out source of data with more points to train our model on.  As well we sould also potentially use a different model with more subreddit's involved.

## Slide Presentation

https://docs.google.com/presentation/d/1OHD0zEzcUYN0IbASrJJ2OZe9RWMEJugxxqiC2-yn4fM/edit?usp=sharing

## Dasboard
https://public.tableau.com/profile/paul.smith1805#!/vizhome/final_projectGroup6/final_projectGroup6

![](https://github.com/BooneyBeCoding/final_project/blob/main/Images/dashboard_final.PNG)
