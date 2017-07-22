from django.http import HttpResponse
from django.shortcuts import render

VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def home(request):
    return render(request, 'home.html')


def translate(request):
    original = request.GET['originaltext']
    translation = ''
    for word in original.lower().split():
        if word.startswith(VOWELS):  # starts with vowel
            translation += word + 'yay '
        else:  # starts with consonant
            translation += word[1:] + word[0] + 'ay '

    return render(request, 'translate.html', {'original': original, 'translation': translation})
