import asyncio

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from circle.apps.news.views import (async_get_latest_news,
                                    async_get_news_categories)

from rest_framework.permissions import IsAuthenticated


class AllNewsView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    # def get(self, request):
    #     content = {'data': 'Healthy!'}
    #     return Response(content)

    def get(self, request):
        if request.method == 'GET':
            latest_news = asyncio.run(async_get_latest_news())
            if not latest_news:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"data": "Not found"})
            else:
                news_result = []
                list_cat = []
                for row in latest_news:
                    category = asyncio.run(async_get_news_categories(row['id']))
                    list_cat.append(category)
                    news_dict = dict()
                    news_dict['id'] = row['id']
                    news_dict['link'] = row['link']
                    news_dict['title'] = row['title']['rendered']
                    news_dict['img'] = row['jetpack_featured_media_url']
                    news_dict['category'] = category['name']
                    news_result.append(news_dict)
                return Response(status=status.HTTP_200_OK, data={"data": news_result})
