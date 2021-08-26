import asyncio

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from circle.apps.news.views import (async_get_latest_news,
                                    async_get_news_by_category,
                                    async_get_news_categories,
                                    async_get_news_categories_id)


class NewsByCategoryView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, cat_id, num_page):
        if request.method == 'GET':
            if cat_id and num_page is None:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"data": "Not found"})
            latest_news = asyncio.run(async_get_news_by_category(cat_id, num_page))
            if not latest_news:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"data": "Not found"})
            return Response(status=status.HTTP_200_OK, data={"data": latest_news})


class NewsCategoriesView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.method == 'GET':
            news_categories = asyncio.run(async_get_news_categories())
            if not news_categories:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"data": "Not found"})
            return Response(status=status.HTTP_200_OK, data={"data": news_categories})


class AllNewsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        if request.method == 'GET':
            latest_news = asyncio.run(async_get_latest_news())
            if not latest_news:
                return Response(status=status.HTTP_404_NOT_FOUND, data={"data": "Not found"})
            else:
                news_result = []
                list_cat = []
                for row in latest_news:
                    category = asyncio.run(async_get_news_categories_id(row['id']))
                    list_cat.append(category)
                    news_dict = dict()
                    news_dict['id'] = row['id']
                    news_dict['published'] = str(row['date']).replace('T', ' ')
                    news_dict['link'] = row['link']
                    news_dict['title'] = row['title']['rendered']
                    news_dict['image'] = row['jetpack_featured_media_url']
                    news_dict['category_id'] = category['id']
                    news_dict['category_name'] = category['name']
                    news_result.append(news_dict)
                return Response(status=status.HTTP_200_OK, data={"data": news_result})
