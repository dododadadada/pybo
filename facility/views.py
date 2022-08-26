from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
import pandas as pd
from .models import Facility, Category
import json
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def map(request):
    return render(request, 'facility/test.html')

def downloadFacilities(request):
    with open('C:\Korea university\데이터톤\장고\전체시설정보.json', encoding='utf-8') as json_file:
        facility = json.load(json_file)
        category_list = []

        for i in range(len(facility)):
            Facility.objects.create(
                cate_1 = facility[i]['구분'],
                name = facility[i]['시설명'],
                lat = facility[i]['lat'],
                lng = facility[i]['lng'],
                dong = facility[i]['행정동'],
                cate_2 = facility[i]['분류체계'],
                content = facility[i]['시설정보'],
                url = facility[i]['링크']
            )
            if facility[i]["구분"] not in category_list:
                Category.objects.create(name=facility[i]["구분"])
                category_list.append(facility[i]["구분"])

    return HttpResponse(f'''
        <html>
        <body>
            <h1>Download Complete</h1>
            {facility}
        </body>
        </html>
        ''')


def showFacilities(request):
    facilities = Facility.objects.all
    context = {'facilities': facilities}
    return render(request, 'facility/default.html', context)


def getlocation(request):
    location_input = request.GET.get('location_input', '')
    facilities = Facility.objects.all
    context = {'facilities': facilities, 'location_input': location_input}
    return render(request, 'facility/get_location.html', context)

def showFacilitylist(request):
        context = {}

        # 사이트에서 필터 선택 여부 받아오기
        b = request.GET.get('b', '')
        f = request.GET.getlist('f')
        facility_list = Facility.objects.order_by('name')

        ########## 카테고리 리스트 ###############
        category_list = Category.objects.all()
        context['category_list'] = category_list

        if b:
            facility_list = facility_list.filter(
                Q(name__icontains=b) |
                Q(category__icontains=b)
            ).distinct()

        if f:
            print(f)
            query = Q()
            for i in f:
                query = query | Q(category__icontains=i)
            facility_list = facility_list.filter(query)

        # 필터링 된 결과 개수
        context['facility_number'] = facility_list.count()

        # 페이징 처리 시작
        page = request.GET.get('page', '1')  # 페이지
        paginator = Paginator(facility_list, 10)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context['facility_list'] = page_obj

        return render(request, 'facility/facility_list.html', context)


def detail(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    context = {'facility': facility}
    return render(request, 'facility/facility_detail.html', context)


