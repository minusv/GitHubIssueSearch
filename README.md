# GitHubIssueSearch
[Check it Out!](http://manasvi.pythonanywhere.com/)

## Features:
For a given GitHub Repository Url, this app will show:
- Total number of open issues
- Number of open issues that were opened in the last 24 hours
- Number of open issues that were opened more than 24 hours ago but less than 7 days ago
- Number of open issues that were opened more than 7 days ago 

## About
This app is created using [Django=1.11](https://docs.djangoproject.com/en/2.1/releases/1.11/).
[GitHub Search API](https://developer.github.com/v3/search/) is used to search the repository.
The logic for the same can be found in [services.py](https://github.com/minusv/GitHubIssueSearch/blob/master/githubSearchApp/services.py) and [views.py](https://github.com/minusv/GitHubIssueSearch/blob/master/githubSearchApp/views.py).

### [Services.py](https://github.com/minusv/GitHubIssueSearch/blob/master/githubSearchApp/services.py)
This file contains the main logic for this application. The enetered repository is searched, for every open issue returned, it's date of creation is compared with the current date to increment the respective count.

I've tried my best to make the code understandable and have documented it wherever necessary.

## To Do
- Implement a check mechanism while taking the input url.
- Exploit the full potential of Github Search API.
