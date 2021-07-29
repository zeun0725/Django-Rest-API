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
```

### 슈퍼유저 만들기
python manage.py createsuperuser 
