from django.http import HttpResponse
from django.shortcuts import render  # allows us to return templates
import operator

def homepage(request):
    return render(request, "home.html", {"hithere": "this is me"})  # passing dictionary, cant have whitespaces in keys names
# can't pass default strings for some reason

def hellopage(request):  # request contains all info about user etc (e.g cookies)
    return HttpResponse("Hello")  # you can't simply return a string you need to return hhtp response

def eggspage(request):
    return HttpResponse("<b>Eggs</b>")  # passing html strings like that isn't a great idea

def count(request):
    fulltext = request.GET["fulltext"]  # accessing info that goes after "fulltext"
    wordslist = fulltext.split(" ")
    counted_words = {}
    for word in wordslist:
        if word not in counted_words:
            counted_words[word] = 1
        else:
            counted_words[word] += 1

    final_op = sorted(counted_words.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {"passed_text": fulltext, "counted_words": final_op})

def about(request):
    return render(request, "about.html")
