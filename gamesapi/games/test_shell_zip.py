# tests.py 단위테스트 실행할 때 이 파일때문에 에러가 남 그래서 주석처리해줌


# # shell 에서 테스트 하는 코드 모음집
#
# # serialize 테스트
#
# from datetime import datetime
# from django.utils import timezone
# from six import BytesIO
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from games.models import Game
# from games.serializers import GameSerializer
#
# gamedatetime = timezone.make_aware(datetime.now(), timezone.get_current_timezone())
# game1 = Game(name='Smurfs Jungle', release_date=gamedatetime, game_category='2D mobile arcade', played=False)
# game1.save()
# game2 = Game(name='Angry Birds RPG', release_date=gamedatetime, game_category='3D RPG', played=False)
# game2.save()
#
# game_serializer1 = GameSerializer(game1)
# print(game_serializer1.data)
# game_serializer2 = GameSerializer(game2)
# print(game_serializer2.data)
#
# # JSONRenderer => 딕셔너리를 json으로 변환해줌
# renderer = JSONRenderer()
# rendered_game1 = renderer.render(game_serializer1.data)
# rendered_game2 = renderer.render(game_serializer2.data)
# print(rendered_game1)
# print(rendered_game2)
#
# json_string_for_new_game = '{"name":"Tomb Raider Extreme Edition" ,"release_date":"2021-07-07T00:58:00", "game_category":"3D RPG", "played": false}'
# json_bytes_for_new_game = bytes(json_string_for_new_game, encoding="UTF-8")
# stream_for_new_game = BytesIO(json_bytes_for_new_game)
# parser = JSONParser()
# parsed_new_game = parser.parse(stream_for_new_game)
# print(parsed_new_game)
#
# new_game_serializer = GameSerializer(data=parsed_new_game)
# if new_game_serializer.is_valid():
#     new_game = new_game_serializer.save()
#     print(new_game.name)
#
#
# # ==================
# # create game model
# # http POST 0.0.0.0:8000/games/ name='Tetris Reloaded' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Puzzle Craft' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Blek' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Scribblenauts Unlimited' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Cut the Rope: Magic' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Tiny Dice Dungeon' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='A Dark Room' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Bastion' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Welcome to the Dungeon' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
# # http POST 0.0.0.0:8000/games/ name='Dust: An Elysian Tail' game_category='2D mobile arcade' played=false release_date='2021-07-27T00:00:00'
