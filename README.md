# final_project

## RESEARCH QUESTION AND PROPOSAL:
- The 3 most prominent subreddits whose communities are built around the topic of stock market investing each have different constructions of culture. 
- By running a sentiment-gauging cross-analysis over the headline/title of posts of each, can we teach a Machine Learning model to discern which of the subreddits was most likely the subreddit of origin?


### Description 
We would like to investigate whether or not sentiment analysis data, generated by VADER, can be used in a basic machine learning model to predict post origins 
across multiple Reddit discussion groups (subreddits) that share similar topics but different cultures.

We have an initial dataset comprised of basic post information (title, subreddit origin, upvote score, post link url, comment number, body text, and post date)
for a selection of the top posts (by score) of the three most popular stock investing subreddits (/r/wallstreetbets, /r/investing, and /r/stocks), roughly 1000 
posts per subreddit. Some data points, such as upvote score and comment number, are likely highly correlated to overall subreddit size. It is generally held 
that different subreddits have different cultures, or "feels", and that that is reflected in the types of posts that are successful in a given subreddit. You 
might write a title differently to gain attention successfully, depending on the specific subreddit. To test this at a basic level, we will use the VADER 
sentiment analysis package to assign a score to each post title in our dataset. VADER (Valence Aware Dictionary for Sentiment Reasoning) takes a string, and 
based on an emotion intensities dictionary model, returns four values: negative, neutral, positive, and compound (an normalized value of the three scores). 

We will feed this generated data into a simple machine learning model, and see if we can can train it to identify the origin of a given post, based on just 
this sentiment information. One approach would be to use a Supervised Logistic Regression model for single element membership. An example of this would be 
that /r/wallstreetbets is generally considered the most divergent of the stock trading subreddits, so the output label for the given input data could be a 
simple Y/N of whether or not the model thinks the sample post is from /r/wallstreet bets. If we generate a simple five element data set from the original 
data set (the four VADER outputs, plus a "WSB?" column), the rough outline of the model would look similar to test_Reddit_VADER.ipynb (we don't yet have the 
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
6. PostgreSQL - database housing and management
7. Vader - Python package for Sentiment Analysis
8. Tableau - visualization
9. HTML & CSS - visualization
10. VS Code Basic - file creation, idea structure, and organization

### Communication Pattern
Have created Slack Group & Text Chain for rapid communication.

As well, will be meeing both Tuesday & Thursday during class time, as well as a check in on Sunday morning.

### Machine Learning Model
Utilizing Vader Sentiment Analysisn on the titles of each subreddit post and a Logistic Regression model to analyse the vader scores to determine if a post came from WallStreetBets or not.  The model runs at 100% currently.  In the next segment we may be able to analyse specific words for each of the 3 subreddits to see if there are  common terms that would trigger the accuracy.

### Slide Presentation

https://docs.google.com/presentation/d/1OHD0zEzcUYN0IbASrJJ2OZe9RWMEJugxxqiC2-yn4fM/edit?usp=sharing
