from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = dict()
    for word in wordlist:
        if(word not in worddict.keys()):
            worddict[word] = 0
        else:
            worddict[word] += 1
    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'worddict':worddict})
