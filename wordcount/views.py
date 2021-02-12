from django.http import HttpResponse
from django.shortcuts import render
import re
import operator


def home(request):
    try:
        full_text = request.GET['full_text']
    except:
        full_text = ""

    # finding words and putting them in a list
    word_list = re.findall(r'[\w@#$%^&*/\’\-_.]+\b', full_text)
    # counting the number of words in the word_list
    words_total = len(word_list)

    # number of total characters with white space
    all_total = len(re.findall('.', full_text))
    # number of total characters without white space
    char_total = len(re.findall('\S', full_text))

    # total sentences
    sentences = len(re.findall('[\.!]+(\s|\[|$)', full_text))

    # total paragraphs in the input
    paragraphs = len(re.findall('\n\s*\S+', full_text)) + 1

    # worddict = dict()
    # for word in wordlist:
    #     if(word not in worddict.keys()):
    #         worddict[word] = 1
    #     else:
    #         worddict[word] += 1
    # sorted_items = sorted(
    #     worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'home.html', {'full_text': full_text, 'all_total': all_total, 'char_total': char_total, 'words_total': words_total, 'sentences': sentences, 'paragraphs': paragraphs, })
