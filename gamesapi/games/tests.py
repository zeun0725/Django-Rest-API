from django.test import TestCase
from django.urls import reverse
from django.utils.http import urlencode
from rest_framework import status
from django.test import TestCase
from games.models import GameCategory

#===================================================================
#self.assertEqual = 응답의 속성을 검사해 응답의 json 본문이 포함된 데이터를 점검함
#===================================================================

class GameCategoryTests(TestCase):
    def create_game_category(self, name):
        url = reverse('gamecategory-list')
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response

    def test_create_and_retrieve_game_category(self):
        new_game_category_name = 'New Game Category'
        response = self.create_game_category(new_game_category_name)
        self.assertEqual(response.status_coode, status.HTTP_201_CREATED)
        self.assertEqual(GameCategory.objects.count(), 1)
        self.assertEqual(
            GameCategory.objects.get().name,
            new_game_category_name
        )
        print("PK {0}".format(GameCategory.objects.get().pk))

    def test_create_duplicated_game_category(self):
        # 고유한 제약으로 인해 같은 이름의 두 게임 카테고리를 생성할 수 없는지 여부를 테스트
        url =reverse('gamecategory-list')
        new_game_category_name = 'New Game Category'
        data = {'name': new_game_category_name}
        response1 = self.create_game_category(new_game_category_name)
        self.assertEqual(
            response1.status_code,
            status.HTTP_201_CREATED
        )
        response2 = self.create_game_category(new_game_category_name)
        self.assertEqual(
            response2.status_code,
            status.HTTP_400_BAD_REQUEST
        )

    def test_retrieve_game_categories_list(self):
        # 기본 키 또는 id로 특정 게임 카테고리를 얻을 수 있는 지 테스트
        new_game_category_name = 'New Game Category'
        self.create_game_category(new_game_category_name)
        url = reverse('gamecategory-list')
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.status_coode,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['count'],
            1
        )
        self.assertEqual(
            response.data['results'][0]['name'],
            new_game_category_name
        )

    def test_update_game_category(self):
        # 게임 카테고리 단일 필드 업데이트 테스트
        new_game_category_name = 'Initial Name'
        response = self.create_game_category(new_game_category_name)
        url = reverse(
            'gamecategory-detail',
            None,
            {response.data['pk']}
        )
        updated_game_category_name = 'Updated Game Category Name'
        data = {'name': updated_game_category_name}
        patch_response = self.client.patch(url, data, format='json')
        self.assertEqual(
            patch_response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            patch_response.data['name'],
            updated_game_category_name
        )

    def test_filter_game_category_by_name(self):
        # 게임 카테고리를 이름에 따라 필터링 할 수 있는 지 테스트
        game_category_name1 = 'First game category name'
        self.create_game_category(game_category_name1)
        game_category_name2 = 'Second game category name'
        self.create_game_category(game_category_name2)
        filter_by_name = {'name': game_category_name1}
        url = '{0}?{1}'.format(
            reverse('gamecategory-list'),
            urlencode(filter_by_name)
        )
        response = self.client.get(url, format='json')
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.data['count'],
            1
        )
        self.assertEqual(
            response.data['results'][0]['name'],
            game_category_name1
        )
