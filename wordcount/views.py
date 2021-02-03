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
    onelinetext = re.sub('\n', ' ', fulltext).lower()

    original_spaces = fulltext.count(' ')
    linebreaks = fulltext.count('\n')
    single_spaces = onelinetext.count(' ')
    tabs = onelinetext.count('\t')


    wordlist = onelinetext.split()
    words_total = len(wordlist) - tabs

    # number of total characters with white space
    all_total = len(onelinetext) - linebreaks
    # number of total characters without white space
    char_total = all_total - single_spaces - tabs

    # total paragraphs in the input
    splitedtext = " ".join(onelinetext.split())
    splited_spaces = splitedtext.count(' ')
    paragraphs = splited_spaces-original_spaces+1

    # newpara_pattern = "\n"
    # if(re.search(newpara_pattern, fulltext)):
    #     print("new line!!")
    # worddict = dict()
    # for word in wordlist:
    #     if(word not in worddict.keys()):
    #         worddict[word] = 1
    #     else:
    #         worddict[word] += 1
    # sorted_items = sorted(
    #     worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'home.html', {'fulltext': fulltext, 'linebreaks': linebreaks, 'onelinetext': onelinetext, 'original_spaces': original_spaces, 'filteredtext': filteredtext, 'paragraphs': paragraphs, 'all_total': all_total, 'char_total': char_total, 'words_total': words_total})
