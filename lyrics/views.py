from django.shortcuts import render,redirect
from .forms import  LyricsForm
from extensions.lyrics import find_lyrics
#--------------------------------Lyrics Page---------------------------------
def lyrics(request):
    global lyrics_text
    if request.method == "POST":
        song_name =  request.POST.get("song_name",False)
        artist_name =  request.POST.get("artist_name",False)
        lyrics_text = find_lyrics(song_name, artist_name)
        return redirect ("/result/")
    else:
        form = LyricsForm()
    return render(request,"lyrics/home.html",{'form':LyricsForm,"lyrics":lyrics})
#--------------------------------Results Page---------------------------------
def result(request):
    return render(request,"lyrics/result.html",{"lyrics":lyrics_text})
#-----------------------------------------------------------------------------

