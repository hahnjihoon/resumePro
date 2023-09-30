from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import tb_memo, YourForm

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

def index(request):
    data = tb_memo.objects.all()
    # logger.debug('****************************',data)
    return render(request, 'index.html', {'data':data})


def layout_static(request):
    return render(request, 'layout-static.html')

def layout_sidenav_light(request):
    return render(request, 'layout-sidenav-light.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def password(request):
    return render(request, 'password.html')

def e401(request):
    return render(request, '401.html')

def e404(request):
    return render(request, '404.html')

def e500(request):
    return render(request, '500.html')

def charts(request):
    return render(request, 'charts.html')

def tables(request):
    return render(request, 'tables.html')

def visitor(request):
    post_list = tb_memo.objects.all().order_by('-id')
    page = request.GET.get('page')

    paginator = Paginator(post_list, 5)

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        page_obj = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        page_obj = paginator.page(page)


    context = {
        'data': post_list,
        'current_page': page_obj,
        'paginator': paginator
    }

    return render(request, 'visitor.html', context)
    # logger.debug('****************************',data)
    # return render(request, 'visitor.html', {'data': data})


    # GET 요청 처리
    # if request.method == 'GET':
    #     # 데이터베이스에서 데이터 조회
    #     data = tb_memo.objects.all()
    #     # 사용자 정의 폼 초기화
    #     form = YourForm()
    #     return render(request, 'visitor.html', {'data': data, 'form': form})
    #
    # # POST 요청 처리
    # elif request.method == 'POST':
    #     # 사용자로부터의 POST 데이터를 폼으로 받음
    #     form = YourForm(request.POST)
    #     if form.is_valid():
    #         # 폼이 유효하면 데이터베이스에 저장
    #         name = form.cleaned_data['name']
    #         content = form.cleaned_data['content']
    #         tb_memo.objects.create(name=name, content=content)
    #         return redirect('visitor')  # 방문자 뷰로 리다이렉트
    #     else:
    #         # 폼이 유효하지 않으면 에러 메시지를 뷰에 전달
    #         data = tb_memo.objects.all()
    #         return render(request, 'visitor.html', {'data': data, 'form': form})

def get1(request):
    print('get1/ 요청들어옴')
    print(request.GET)
    # return HttpResponse('get1')

    # 사용자로부터의 POST 데이터를 폼으로 받음
    form = YourForm(request.GET)
    if form.is_valid():
        cleaned_data = form.cleaned_data
    name = form.cleaned_data['name']
    content = form.cleaned_data['content']
    tb_memo.objects.create(name=name, content=content)
    return redirect('visitor');