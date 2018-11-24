from graphene import Node
from graphene_django.types import DjangoObjectType

from .models import *


class GenreNode(DjangoObjectType):

    class Meta:
        model = Genre
        interfaces = (Node, )


class UserNode(DjangoObjectType):

    class Meta:
        model = User
        interfaces = (Node, )


class ComicNode(DjangoObjectType):

    class Meta:
        model = Comic
        interfaces = (Node, )


class CommentNode(DjangoObjectType):

    class Meta:
        model = Comment
        interfaces = (Node, )
