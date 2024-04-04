from django.shortcuts import render

# Create your views here.

group = {
    'members': [
        {
            'title': '드라큘라',
            'name': '김준수',
            'img' : 'dracula/images/sia.png'
            # 'img': 'https://www.ccnnews.co.kr/news/photo/202403/328559_409224_2639.jpg'
        },
        {
            'title': '미나',
            'name': '정선아',
            'img' : 'dracula/images/summer.png'
            # 'img': 'https://flexible.img.hani.co.kr/flexible/normal/970/1298/imgdb/original/2024/0131/20240131501747.jpg'
        }
    ]
}


def show_sia(request):
    context = list(filter(lambda member: '김준수' in member['name'], group['members']))[0]
    # context = group['members'][0]
    return render(request, 'dracula/member.html', context=context)


def show_summer(request):
    context = list(filter(lambda member: '정선아' in member['name'], group['members']))[0]
    # context = group['members'][1]
    return render(request, 'dracula/member.html', context=context)


def show_member(request, mem):
    context = list(filter(lambda member: mem in member['name'], group['members']))[0]
    return render(request, 'dracula/member.html', context=context)
