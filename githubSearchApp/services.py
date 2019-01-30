import requests, dateutil.parser
from django.utils import timezone


def timeDifference(createdAt):
    #To calculate time difference between current date and date of creation

    currentDate = timezone.now()
    createdAtUtc = dateutil.parser.parse(createdAt)
    diff = currentDate - createdAtUtc
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600 
    return([diff.days,hours])


def querryResults(owner, repository):
    #This function will make a search request at GitHub Api to get all the open issues
    #It'll then return the required data

    searchURL = "https://api.github.com/search/issues?q=repo:{}/{}+is:issue+is:open+&sort=created&order=dsc"
    response = requests.get(searchURL.format(owner, repository))
    responseJson = response.json()
    totalCount = responseJson['total_count']
    openedInLast24Hours = 0
    openedBetween24HoursAnd7Days = 0
    openedBefore7days = 0

    if totalCount!=0:
        for item in responseJson['items']:
            createdAt = item["created_at"]
            [days, hours] = timeDifference(createdAt)
            if hours <= 24:
                openedInLast24Hours += 1
            elif hours > 24 and days < 7:
                openedBetween24HoursAnd7Days +=1
            else:
                openedBefore7days = totalCount - (openedBetween24HoursAnd7Days + openedInLast24Hours)
                break
        return([totalCount, openedInLast24Hours, openedBetween24HoursAnd7Days, openedBefore7days])
    else:
        return([0, 0, 0, 0])