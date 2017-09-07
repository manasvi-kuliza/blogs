import uuid
import os

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .exceptions import GenericException
from .constants import *


def get_blog_list(params):
    """
    method to create a new blog
    :param params: limit, offset, 
    :return:
    """
    try:
        offset = int(params.get('offset', DEFAULT_OFFSET))
        limit = int(params.get('limit', DEFAULT_LIMIT))
        blogs = Blog.objects.filter(is_deleted=False).order_by('created_at').values('blog_number', 'title')
        upper_count = offset + limit
        upper_count = blogs.count() if upper_count > blogs.count() else upper_count
        return blogs[offset:upper_count]
    except Exception as e:
        raise GenericException(detail=repr(e))


def create_blog(params, request):
    """
    method to create a new blog
    :param params: title, body, 
    :param request:
    :return:
    """
    try:
        title = params['title']
        message = params['body']
        if not message:
            raise KeyError()

        blog_number = str(uuid.uuid4())
        blog = Blog.objects.create(blog_number=blog_number, title=title)
        params['blog'] = blog
        create_paragraphs(params)
        return {"message": "Blog created successfully "}
    except KeyError as e:
        raise GenericException(detail="Title/Body can not be blank")
    except GenericException as e:
        raise GenericException(detail=e.detail)
    except Exception as e:
        raise GenericException(detail=repr(e))


def create_paragraphs(params):
    """
    method to creaate a paragraph
    :param params: blog object, body 
    :return:
    """
    try:
        # paragraphs = [s.strip() for s in message.splitlines() if s]
        # If neccesarily 2 lines
        message = params['body']
        paragraphs = message.split('\n\n')
        paras = []
        for seq, paragraph in enumerate(paragraphs):
            paragraph_number = str(uuid.uuid4())
            para = Paragraph(blog=params['blog'], paragraph_number=paragraph_number,
                             sequence=seq, body=paragraph)
            paras.append(para)
        Paragraph.objects.bulk_create(paras)
        return
    except KeyError as e:
        raise GenericException(detail="Body can not be blank")
    except Exception as e:
        raise GenericException(detail=repr(e))


def get_blog(blog_number):
    """
    method to get a blog with comments
    :param params: blog_number 
    :return:
    """
    try:
        blog = Blog.objects.get(blog_number=blog_number, is_deleted=False)
        result = {}
        result['blog_number'] = blog.blog_number
        result['title'] = blog.title
        result['paragraphs'] = []
        paragraphs = blog.paragraph_set.filter(is_deleted=False)
        for paragraph in paragraphs:
            temp = {}
            temp['sequence'] = paragraph.sequence
            temp['body'] = paragraph.body
            temp['paragraph_number'] = paragraph.paragraph_number
            temp['comments'] = paragraph.comment_set.values('message')
            result['paragraphs'].append(temp)
        return result
    except ObjectDoesNotExist as e:
        raise GenericException(detail="Blog not found")
    except Exception as e:
        raise GenericException(detail=repr(e))


def add_comment(params, request):
    """
    method to add a new comment
    :param params: paragraph_number, message, 
    :param request:
    :return:
    """
    try:
        message = params['message']
        paragraph_number = params['paragraph_number']
        paragraph = Paragraph.objects.get(paragraph_number=paragraph_number,
                                          is_deleted=False)
        Comment.objects.create(paragraph=paragraph, message=message)
        return {"message": "Comment added successfully"}
    except KeyError as e:
        raise GenericException(detail="Body can not be blank")
    except ObjectDoesNotExist as e:
        raise GenericException(detail="Paragraph not found")
    except Exception as e:
        raise GenericException(detail=repr(e))