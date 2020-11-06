from django.http import HttpResponse
from django.shortcuts import render
import re
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    filteredtext = re.sub('\W+',' ', fulltext).lower()
    wordlist = filteredtext.split()
    worddict = dict()
    for word in wordlist:
        if(word not in worddict.keys()):
            worddict[word] = 1
        else:
            worddict[word] += 1
    sorted_items = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'worddict':sorted_items})

def about(request):
    return render(request, 'about.html')
