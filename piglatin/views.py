from django.http import HttpResponse
from django.shortcuts import render

VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

def home(request):
    return render(request, 'home.html')


def translate(request):
    original = request.GET['originaltext'].lower()
    result = ''
    for word in original.split():
        if word.startswith(VOWELS):  # starts with vowel
            result += word + 'yay '
        else:  # starts with consonant
            result += word[1:] + word[0] + 'ay '

    return render(request, result)
