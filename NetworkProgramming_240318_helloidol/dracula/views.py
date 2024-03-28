from django.shortcuts import render

# Create your views here.

def show_sia(request) :
    return render(request, 'dracula/sia.html',
                  {'title' : '드라큘라', 'name' : '김준수', 'img' : 'https://www.ccnnews.co.kr/news/photo/202403/328559_409224_2639.jpg'})

def show_summer(request) :
    return render(request, 'dracula/summer.html',
                  {'title' : '미나', 'name' : '정선아', 'img' : 'https://flexible.img.hani.co.kr/flexible/normal/970/1298/imgdb/original/2024/0131/20240131501747.jpg'})
