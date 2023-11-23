from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app_study_dream.models import Board

## hihi
# Create your views here.

@login_required(login_url='login')
def list_page(request):  # 메인 페이지 _로그인 기능 예정 ==> 특정 권한을 가진 사람만 객체에 넣고, 아니면 공백 리턴
    boards = {'boards': Board.objects.all()}
    return render(request, 'list.html', boards)

@login_required(login_url='login')
def write_post(request):
    if request.method == "POST":
        author = request.POST['author']
        title = request.POST['title']
        content = request.POST['content']
        board = Board(author=author, title=title, content=content)
        board.save()
        return HttpResponseRedirect(reverse('list_page'))
    else:
        return render(request, 'write_post.html')

@login_required(login_url='login')
def detail(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Board.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'detail.html', {'board': board})
