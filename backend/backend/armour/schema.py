"""Use this file to define the model schemas for GraphQL."""
import graphene
from graphene_django import DjangoObjectType

from . import models


class ArmourPieceType(DjangoObjectType):
    class Meta:
        model = models.ArmourPiece
