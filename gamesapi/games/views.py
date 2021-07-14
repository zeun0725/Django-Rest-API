from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import status
from games.models import Game
from games.serializers import GameSerializer


# 내용을 Json으로 렌더링
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        # 수신된 데이터를 json으로 렌더링 후 반환된 바이트 문자열은 content에 저장
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        # 베이스 클래스의 초기자 호출
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def game_list(request):
    # 모든 게임을 나열하거나 새 게임 생성
    if request.method == 'GET':
        games = Game.objects.all()
        games_serializer = GameSerializer(games, many=True)
        return JSONResponse(games_serializer.data)

    elif request.method == 'POST':
        game_data = JSONParser().parse(request)
        game_serializer = GameSerializer(data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(game_serializer.data, status=status.HTTP_201_CREATED)
        return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def game_detail(request, pk):
    # 기존 게임을 검색, 업데이트, 삭제함
    try:
        game = Game.objects.get(pk=pk)
    except Game.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        game_serializer = GameSerializer(game)
        return JSONResponse(game_serializer.data)

    elif request.method == 'PUT':
        game_data = JSONParser().parse(request)
        # 기존 데이터(game_data)를 대체할 검색된 데이터로 인스턴스 생성
        game_serializer = GameSerializer(game, data=game_data)
        if game_serializer.is_valid():
            game_serializer.save()
            return JSONResponse(game_serializer.data)
        return JSONResponse(game_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        game.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)