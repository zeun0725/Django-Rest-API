# RESTful 파이썬 웹 서비스 제작

### 원본 소스
**https://github.com/PacktPublishing/Building-RESTful-Python-Web-Services**


### postgreSQL
```
psql --username=test --dbname=games --command="\dt"
psql --username=test --dbname=games --command="SELECT * FROM games_gamecategory;"
psql --username=test --dbname=games --command="SELECT * FROM games_game;"
psql --username=test --dbname=games --command="SELECT * FROM games_player;"
psql --username=test --dbname=games --command="SELECT * FROM games_playerscore;"
psql --username=test --dbname=games --command="SELECT id FROM auth_user WHERE username = 'root';"
```

### 슈퍼유저 만들기
python manage.py createsuperuser
superuser: root
 

### 의존 패키지
pip install django-filter  
pip install django-crispy-forms  
**단위테스트 설정**    
pip install covarage
pip install django-nose

### 장애 대응
```
 NumberFilter(
        field_name='score', lookup_expr='gte')
 # name 이 아니라 field_name 임
 ```

### 단위 테스트 실행
python manage.py test -v 2  
coverage report -m  
coverage html  

Name: 파이썬 모듈 이름  
Stmts: 파이썬 모듈의 실행 가능 문 개서  
Miss: 누락된 실행 가능 문 수, 즉 실행되지 않은 문 수  
Cover: 실행 가능 문의 커버리지(백분율로 표시)  

