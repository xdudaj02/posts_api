import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Post
from .serializers import PostSerializer, PostPostSerializer, PostPutSerializer, PostPatchSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


def get_highest_post_id():
    item = Post.objects.order_by('-id').first()
    if item:
        return item.id
    else:
        return 0


def unexpected_keys(request_data, valid_data):
    if len(request_data.keys()) != len(valid_data.keys()):
        return True
    return False


@swagger_auto_schema(method='GET',
                     operation_id='get_post',
                     operation_summary='View a post',
                     operation_description='This endpoint returns the post with the given id.',
                     responses={200: openapi.Response(description='Post with given id successfully returned.',
                                                      schema=PostSerializer)})
@api_view(['GET'])
def get_post(request, post_id):
    try:
        result = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/' + str(post_id))
        if response.status_code != status.HTTP_200_OK:
            return Response(status=status.HTTP_404_NOT_FOUND)
        result = Post(**response.json())
        result.save()

    serializer = PostSerializer(result)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='GET',
                     operation_id='get_user_posts',
                     operation_summary='View all posts of a user',
                     operation_description='This endpoint returns all posts of the user with the given id.',
                     responses={200: openapi.Response(description='All posts published by user with given userId '
                                                                  'successfully returned.', schema=PostSerializer)})
@api_view(['GET'])
def get_user_posts(request, user_id):
    result = Post.objects.filter(userId__exact=user_id)

    serializer = PostSerializer(result, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='POST',
                     operation_id='post_post',
                     operation_summary='Create a post',
                     operation_description='This endpoint creates a new post. All fields must be specified. User id '
                                           'needs to be a valid id of a user registered at '
                                           'https://jsonplaceholder.typicode.com/.',
                     request_body=PostPostSerializer,
                     responses={200: openapi.Response(description='Post successfully created.', schema=PostSerializer),
                                400: 'Bad request.',
                                403: 'Unregistered user.'})
@api_view(['POST'])
def create_post(request):
    data = request.data

    serializer = PostPostSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    if unexpected_keys(request.data, data):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # if len(data) != 3 or 'userId' not in data or 'title' not in data or 'body' not in data:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    response = requests.get('https://jsonplaceholder.typicode.com/users/' + str(data['userId']))
    if response.status_code != status.HTTP_200_OK:
        return Response(status=status.HTTP_403_FORBIDDEN)

    post_id = max(101, get_highest_post_id() + 1)

    result = Post(id=post_id, **data)
    result.save()

    serializer = PostSerializer(result)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PATCH',
                     operation_id='patch_post',
                     operation_summary='Partially update a post',
                     operation_description='This endpoint updates the post with given id. Fields that can be updated '
                                           'are: title and body. Only changed fields need to be specified.',
                     request_body=PostPatchSerializer,
                     responses={200: openapi.Response(description='Post successfully updated.', schema=PostSerializer),
                                400: 'Bad request.',
                                404: 'Post with given id does not exist.'})
@api_view(['PATCH'])
def patch_post(request, post_id):
    data = request.data
    # for item in data:
    #     if item not in ['title', 'body']:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PostPatchSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    if unexpected_keys(request.data, data):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    items = Post.objects.filter(pk=post_id)
    if not items.first():
        return Response(status=status.HTTP_404_NOT_FOUND)

    items.update(**data)

    serializer = PostSerializer(items.first())
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='PUT',
                     operation_id='put_post',
                     operation_summary='Update a post',
                     operation_description='This endpoint updates the post with given id. Fields that cam be updated '
                                           'are: title and body. Both of these fields must be specified.',
                     request_body=PostPutSerializer,
                     responses={200: openapi.Response(description='Post successfully updated.', schema=PostSerializer),
                                400: 'Bad request.',
                                404: 'Post with given id does not exist.'})
@api_view(['PUT'])
def put_post(request, post_id):
    data = request.data
    # if len(data) != 2 or 'title' not in data or 'body' not in data:
    #     return Response(status=status.HTTP_400_BAD_REQUEST)

    serializer = PostPutSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    if unexpected_keys(request.data, data):
        return Response(status=status.HTTP_400_BAD_REQUEST)

    items = Post.objects.filter(pk=post_id)
    if not items.first():
        return Response(status=status.HTTP_404_NOT_FOUND)

    items.update(**data)

    serializer = PostSerializer(items.first())
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(method='DELETE',
                     operation_id='delete_post',
                     operation_summary='Delete a post',
                     operation_description='This endpoint deletes the post with given id.',
                     responses={200: 'Post successfully deleted.',
                                404: 'Post with given id does not exist.'})
@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        item = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        item.delete()
        return Response(status=status.HTTP_200_OK)

# todo: redo as class based
