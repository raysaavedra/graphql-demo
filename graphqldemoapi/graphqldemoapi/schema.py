import graphene

from graphene import relay
from graphene_django.debug import DjangoDebug

from core.schema import *
from core.models import *


class Query(graphene.ObjectType):
    debug = graphene.Field(DjangoDebug, name='__debug')
    comics = graphene.List(ComicNode, title=graphene.String(required=False))

    def resolve_comics(self, info, **kwargs):
        title = kwargs.get('title')
        if title:
            return Comic.objects.filter(title=title)
        else:
            return Comic.objects.all()


schema = graphene.Schema(query=Query)