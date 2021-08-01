from rest_framework.reverse import reverse
from rest_framework import generics
from rest_framework.response import Response
from games.models import Game, GameCategory, PlayerScore, Player
from games.serializers import GameSerializer, GameCategorySerializer, PlayerSerializer, PlayerScoreSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import permissions
from games.permissions import IsOwnerOrReadOnly
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import FilterSet
from django_filters import NumberFilter, DateTimeFilter, AllValuesFilter

# 제네릭 클래스 기반 뷰의 활용

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'players': reverse(PlayerList.name, request=request),
            'game-categories': reverse(GameCategoryList.name, request=request),
            'games': reverse(GameList.name, request=request),
            'scores': reverse(PlayerScoreList.name, request=request),
            'users': reverse(UserList.name, request=request),
        })


class GameCategoryList(generics.ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail',
    throttle_scope = 'game-categories',
    throttle_classes = (ScopedRateThrottle,)


class GameList(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )
    # 필터, 검색, 정렬 기능에서 사용할 필드 지정
    filter_fields = (
        'name',
        'game_category',
        'release_date',
        'played',
        'owner',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'release_date',
    )

    def perform_create(self, serializer):
        # 요청으로 받은 사용자로 소유자를 설정하기 위해
        # create 메서드에 추가적인 owner 필드를 전달함
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'
    filter_fields = (
        'name',
        'gender',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreFilter(FilterSet):
    min_score = NumberFilter(
        name='score', lookup_expr='gte'
    )
    max_score = NumberFilter(
        name='score', lookup_expr='lte'
    )
    from_score_date = DateTimeFilter(
        name='score_date', lookup_expr='gte'
    )
    to_score_date = DateTimeFilter(
        name='score_date', lookup_expr='lte'
    )
    player_name = AllValuesFilter(
        name='player__name'
    )
    game_name = AllValuesFilter(
        name='game__name'
    )

    class Meta:
        model = PlayerScore
        fields = (
            'score',
            'from_score_date',
            'to_score_date',
            'min_score',
            'max_score',
            # player__name 에는 player_name으로 접근할 것
            'player_name',
            # game__name 에는 game_name으로 접근할 것
            'game_name'
        )


class PlayerScoreList(generics.ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list',
    filter_class = PlayerScoreFilter
    ordering_fields = (
        'score',
        'score_date',
    )


class PlayerScoreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'