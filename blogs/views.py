from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .utils import * 


class BlogList(APIView):

    def get(self, request):
        """
        API to get bloglist
        params: offset, limit
        """
        params = request.GET
        response = get_blog_list(params)
        return Response(data=response, status=status.HTTP_200_OK)


class Blog(APIView):

    def get(self, request):
        """
        API to get blog details
        """
        blog_number = request.GET.get('blog_number')
        response = get_blog(blog_number)
        return Response(data=response, status=status.HTTP_200_OK)

    def post(self, request):
        """
        API to create a new blog
        """
        params = request.data
        response = create_blog(params, request)
        return Response(data=response, status=status.HTTP_200_OK)


class Comment(APIView):

 def post(self, request):
        """
        API to add a comment to a blog's paragraph
        :param params: paragraph_number, message
        """
        params = request.data
        response = add_comment(params, request)
        return Response(data=response, status=status.HTTP_200_OK)
