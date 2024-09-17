from django.shortcuts import render
import sys
sys.path.append('D:\django\mum_site\mum_site\articles')


def index(request):

    return render(request, 'main/index.html')

