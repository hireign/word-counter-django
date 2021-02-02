from django.http import HttpResponse
from django.shortcuts import render
import re
import operator

# def home(request):
#     return render(request, 'home.html')


def home(request):
    try:
        fulltext = request.GET['fulltext']
    except:
        fulltext = ""
    filteredtext = re.sub('(\W+)', ' ', fulltext).lower()
    original_spaces = fulltext.count(' ')
    onelinetext = re.sub('\n', ' ', fulltext).lower()
    wordlist = onelinetext.split()
    newpara_pattern = "\n"
    if(re.search(newpara_pattern, fulltext)):
        print("new line!!")
    # worddict = dict()
    # for word in wordlist:
    #     if(word not in worddict.keys()):
    #         worddict[word] = 1
    #     else:
    #         worddict[word] += 1
    # sorted_items = sorted(
    #     worddict.items(), key=operator.itemgetter(1), reverse=True)
    words_total = len(wordlist)
    linebreaks = fulltext.count('\n')
    single_spaces = onelinetext.count(' ')
    all_total = len(onelinetext) - linebreaks
    char_total = all_total - single_spaces
    paragraphs = all_total-char_total-original_spaces-1
    return render(request, 'home.html', {'fulltext': fulltext, 'linebreaks': linebreaks, 'onelinetext': onelinetext, 'original_spaces': original_spaces, 'filteredtext': filteredtext, 'paragraphs': paragraphs, 'all_total': all_total, 'char_total': char_total, 'words_total': words_total})


# def about(request):
#     return render(request, 'about.html')
