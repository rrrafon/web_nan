from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import author, authorInfo


def main_page(request):
    pageTitle = 'Portfolio'
    author_name  = author.objects.get(pk = 1)
    author_bio = authorInfo.objects.get(pk = 1)
    # should be dictionary, this is where you put variables
    context = {
        'var_title': pageTitle,
        'var_authorName': author_name.author_name,
        'var_authorBio': author_bio.author_bio,
        'var_profilePhoto': author_bio.author_photo,

    }
    # this code automatically look inside the templates folder
    return render(request, 'main/main_index.html', context)


