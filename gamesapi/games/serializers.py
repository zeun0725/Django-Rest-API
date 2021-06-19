from rest_framework import serializers
from games.models import Game


class GameSerializer(serializers.Serializer):
    # 직렬화할 필드를 나타내는 속성을 선언
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    release_date = serializers.DateTimeField()

    game_category = serializers.CharField(max_length=200)
    played = serializers.BooleanField(required=False)

    def create(self, validated_data):
        # validated_data : 유효 데이터를 받고 새로운 Game 인스턴스 생성
        return Game.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # 기존 인스턴스와 새로운 유효한 데이터를 받아옴
        instance.name = validated_data.get('name', instance.name)
        instance.release_date = validated_data.get('release_date', instance.release_date)
        instance.game_category = validated_data.get('game_category', instance.game_category)
        instance.played = validated_data.get('played', instance.played)
        instance.save()
        return instance