#file created by sid
from django.http import HttpResponse
from django.shortcuts import render

# def siddhu(request):
#     return HttpResponse("<h1>Welcome to peronal Navigator</h1><br/>"
#                         "<h2>Your Favourite Links are here</h2><br/>"
#                         "<a href='https://www5.gowatchseries.bz/info/grimm-season-1-crp'>Grimm Season 1</a><br/>"
#                         "<a href='https://primewire.es'>Movie Website</a><br/>"
#                         "<a href='https://www.youtube.com/watch?v=5BDgKJFZMl8&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9'>Harry Django Playlist</a><br/>"
#                         "<a href='https://www.youtube.com/watch?v=UNREuwdJCw0'>AC4 Theme Song</a>")
#
#
# def about(request):
#     return HttpResponse("About")

def index(request):
    return render(request,'index2.html')

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    upper_text=request.POST.get('upper_text','off')
    new_line=request.POST.get('new_line','off')
    spacer = request.POST.get('spacer', 'off')
    char_counter = request.POST.get('char_counter', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext=analyzed
    if upper_text=="on":
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        djtext=analyzed
    if new_line=="on":
        analyzed=""
        for char in djtext:
            if char!='\n'and char!='\r' :
                analyzed = analyzed + char
        djtext=analyzed
    if spacer=="on":
        analyzed=""
        for char in djtext:
            if char!=' ':
                analyzed = analyzed + char
        djtext=analyzed
    if char_counter=="on":
        analyzed=0
        for char in djtext:
            analyzed=analyzed+1
        djtext=analyzed
    params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)


#MY LEARNING PROCESS CODES ARE BELOW
# def siddhu(request):
    # gaming={"Game":"AC4","Protagonist":"Edward James Kenway"}
    # return render(request,'index.html',gaming)
    # return HttpResponse("<h1>Welcome to peronal Navigator</h1><br/>"
    #                     "<h2>Your Favourite Buttons are here</h2><br/>"
    #                     '<form action="http://127.0.0.1:8000/father"><input type="submit" value="Father" /></form><br/>'
    #                     '<form action="http://127.0.0.1:8000/mother"><input type="submit" value="Mother" /></form><br/>'
    #                     '<form action="http://127.0.0.1:8000/brother"><input type="submit" value="Brother" /></form><br/>'
    #                     '<form action="http://127.0.0.1:8000/clan"><input type="submit" value="Clan" /></form><br/>'
    #                     '<form action="http://127.0.0.1:8000/surname"><input type="submit" value="Surname" /></form><br/>'
    #                     )

# def sumit(request):
#     return render(request,'brother.html')
#     # return HttpResponse("<p>Your brother is Arindam</p></br>"
#                         # '<form action="http://127.0.0.1:8000"><input type="submit" value="Go Back" /></form><br/>')

# def avijit(request):
#     return render(request,'father.html')
#     # return HttpResponse("Avijit is Your Father")
#
# def soma(request):
#     return render(request, 'mother.html')
#     # return HttpResponse("Soma is mom of Siddhartha and Sumit")
#
# def kuku(request):
#     return render(request, 'clan.html')
#     # return HttpResponse("Siddhu belongs to kuku clan")
#
#
# def bose(request):
#     return render(request, 'surname.html')

