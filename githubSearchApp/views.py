from django.shortcuts import render,redirect
from .forms import UserInputForm
from .services import querryResults

def home(request):
    form = UserInputForm(request.POST or None)
    
    context = {
        'form':form,
    }

    if form.is_valid():
        url = form.cleaned_data.get("url")
        
        #GitHub Repository URL convention: https://github.com/[owner]/[repositoryName]
        #On spliting the URL the 3rd and 4th value of the list will give owner and repositoryName

        owner = url.split('/')[3]
        repository = url.split('/')[4]
        result = querryResults(owner, repository)
        context = {
            "totalOpenIssues" : result[0],
            "openedInLast24Hours" : result[1],
            "openedBetween24HoursAnd7Days" : result[2],
            "openedBefore7days" : result[3],
        }
        return render(request, 'result.html', context)

    return render(request, 'home.html', context)