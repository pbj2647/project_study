from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from app_study_dream.models import Board
from django.db import connection

## hihi
# Create your views here.

@login_required(login_url='login')
def list_page(request):  # 메인 페이지 _로그인 기능 예정 ==> 특정 권한을 가진 사람만 객체에 넣고, 아니면 공백 리턴
    with connection.cursor() as cursor:
        sql = "SELECT * FROM app_study_dream_board"
        cursor.execute(sql)
        datas = cursor.fetchall()
        lists = []
        for i in datas:
            row = {'id': i[0],
                    'title': i[1],
                    'author': i[2],
                    'created_date': i[4]}
            lists.append(row)
        return render(request, 'list.html', {'lists': lists})

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


# @login_required(login_url='login')
# def list_page(request):  # 메인 페이지 _로그인 기능 예정 ==> 특정 권한을 가진 사람만 객체에 넣고, 아니면 공백 리턴
#     # boards = {'boards': Board.objects.all()}
#     with connection.cursor() as cursor:
#         sql = "SELECT * FROM app_study_dream_board"
#         cursor.execute(sql)
#         datas = cursor.fetchone()
#         boards = []
#         for data in datas:
#             print(data)
#             row = {'id': datas[0],
#                     'title': datas[1],
#                     'author': datas[2],
#                     'created_date': datas[3]}
#             boards.append(row)
#     # print("boards :", boards)
#     # print("row :", row)
#     return render(request, 'list.html', { 'boards' : boards})