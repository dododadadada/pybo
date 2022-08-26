from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import pandas as pd
from .models import Circle
from django.core.paginator import Paginator

def index(request):
    return render(request, 'circle/circle_main.html')


def downloadCircle(request):
    filename = 'C:\Korea university\데이터톤\장고\동아리전체데이터.csv'
    df = pd.read_csv(filename, encoding="cp949", na_values='nan')

    category_list = []
    for i in range(len(df)):
        # 프로그램 데이터 db에 저장
        Circle.objects.create(name=df["동아리명"][i],
                              category=df["분과"][i],
                              tag=df["해시태그"][i],
                              content=df["동아리설명"][i],
                              type=df["소속"][i])

    return HttpResponse(f'''
    <html>
    <body>
        <h1>카테고리 이름</h1>
        <h1>Download Complete</h1>
        {df}
        <h2>Data Types</h2>
        {df.dtypes}
    </body>
    </html>
    ''')

def showCirclelist(request):
    page = request.GET.get('page', '1')  # 페이지
    program_list = Circle.objects.order_by('name')
    paginator = Paginator(program_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'circle_list': page_obj}
    return render(request, 'circle/circle_list.html', context) # 객체 있으면 세번째 parameter: context

def detail(request, circle_id):
    circle = get_object_or_404(Circle, pk=circle_id)
    context = {'circle': circle}
    return render(request, 'circle/circle_detail.html', context)