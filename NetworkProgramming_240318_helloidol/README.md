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
      2. `_say_hello_html()_`
      3. `_say_bye_html()_`
      4. -> templates에 context 전달 
      5. show_멤버()
      6. image link -> image file(static)
   2. urls
      1. `_playground/hello/_` -> `_say_hello()_`와 연결
      2. `_playtround/hello_html/` -> `_say_hello_html()_`
   3. templates/playground/
      1. hello.html
      2. bye.html
4. helloidol/
   1. urls, plyground/urls
      1. `_playground/_` -> `_hello/_` -> `_say_hello()_`
      2. `_playground/` -> `_hello_html/_` -> `_say_hello_html()_`
      3. `_playground/_` -> `_bye_html/_` -> `_say_hello_html()_`

--- 
5. startapp 드라큘라  
   1. Terminal 
      1. python manage.py startapp 드라큘라
   2. helloidol/settings.py
      1. '드라큘라', in INSTALLED_APPS
6. 드라큘라/
   1. views
      1. ~~show_준수()~~
      2. ~~show_선아()~~
      3. -> teplates에 context 전달
      4. 정보를 하나로 묶고, 거기에서 꺼내오자
      5. show_멤버()
      6. image link -> image file(static)
      7. show_멤버리스트()
   2. templates/드라큘라/
      1. ~~준수.html~~
         1. title : 드라큘라 - 김준수
         2. h1 : 드라큘라
         3. h2 : 김준수
         4. img : 프로필 사진
            1. border-radius : 50%
      2. ~~선아.html~~
         1. title : 미나 - 정선아
         2. h1 : 미나
         3. h2 : 정선아
         4. img : 프로필 사진
      3. 멤버.html
         1. group_name, name, img_src
         2. `{ %load static % } <img src="{%static img_src %}">`
         3. ```
             {% extends 'base.html %}
             {% block title %}{% endblock %}
             {% block css %}{% endblock %}
             {% block content %}{% content %}
            ```
      4. 멤버리스트.html
         1. {% url '앱이름:path이름' %}
         2. {% url '앱이름:path이름' 변수=값 %}
         3.  ```
             {% extends 'base.html %}
             {% block title %}{% endblock %}
             {% block css %}{% endblock %}
             {% block content %}{% content %}
            ```
      

   3. urls
      1. ~~드라큘라/ -> 준수/ -> show_준수()~~
      2. ~~드라큘라/ -> 선아/ -> show_선아()~~
      3. 드라큘라/ -> <멤버>/ -> show_멤버(멤버)
      4. 드라큘라/ -> 멤버리스트 -> show_멤버리스트()
      5. static/dracula/images/
         1. sia.png, sia2.png, summer.png'
7. templates/
   1. base.html
   ```
   {% extends 'base.html %}
   {% block title %}{% endblock %}
   {% block css %}{% endblock %}
   {% block content %}{% content %}
   ```
---
8. helloidol/
   1. in TEMPLATES in settings.py
      1. 'DIR' : [BASE_DIR] / 'templates',


6. Django 프로젝트 설정
   1. `Settings` -> `Languages&FrameWork` -> `Django` 
   2. `Enable Django Support` -> `root`에 현재 파일 추가 -> `settings`에 settings.py 추가


