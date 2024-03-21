# helloidol

---

1. `startproject helloidol`
   1. `phython -m pip install django~=4.2` : 4.2의 최신 버전 설치
   2. `django-admin startproject _helloidol_ .` : 현재 위치에서 장고 프로젝트 생성
   3. `python manage.py migrate` 
   4. `python manage.py runserver`
2. `startapp _playground_`
   1. Terminal
      1. `python manage.py start app _playground_`
   2. helloidol/settings.py
      1. `'playground',` in INSTALLED_APPS : 앱등록
3. playground/
   - 정보 전달 : urls -> views -> (models -> ) templates
   - 코드 작성 : ( models -> ) views -> templates -> urls 
   1. views
      1. `_say_hello()_`
   2. urls
      1. `_playground/hello/_` -> `_say_hello()_`와 연결
4. Django 프로젝트 설정
   1. `Settings` -> `Languages&FrameWork` -> `Django` 
   2. `Enable Django Support` -> `root`에 현재 파일 추가 -> `settings`에 settings.py 추가