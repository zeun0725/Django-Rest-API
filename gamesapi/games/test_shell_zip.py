# shell 에서 테스트 하는 코드 모음집

# serialize 테스트

from datetime import datetime
from django.utils import timezone
from six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from games.models import Game
from games.serializers import GameSerializer

gamedatetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
game1 = Game(name='Smurfs Jungle', release_date=gamedatetime, game_category='2D mobile arcade', played=False)
game1.save()
game2 = Game(name='Angry Birds RPG', release_date=gamedatetime, game_category='3D RPG', played=False)
game2.save()

game_serializer1 = GameSerializer(game1)
print(game_serializer1.data)
game_serializer2 = GameSerializer(game2)
print(game_serializer2.data)

# JSONRenderer => 딕셔너리를 json으로 변환해줌
renderer = JSONRenderer()
rendered_game1 = renderer.render(game_serializer1.data)
rendered_game2 = renderer.render(game_serializer2.data)
print(rendered_game1)
print(rendered_game2)
