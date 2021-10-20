"""Use this file to define the model schemas for GraphQL."""
import graphene
from graphene_django import DjangoObjectType

from . import models


class ArmourPieceType(DjangoObjectType):
    class Meta:
        model = models.ArmourPiece


class Query(graphene.ObjectType):
    all_armour = graphene.List(ArmourPieceType)
    all_by_rarity = graphene.List(ArmourPieceType, rarity=graphene.Int)
    all_head_pieces = graphene.List(ArmourPieceType)
    all_chest_pieces = graphene.List(ArmourPieceType)
    all_arms_pieces = graphene.List(ArmourPieceType)
    all_waist_pieces = graphene.List(ArmourPieceType)
    all_legs_pieces = graphene.List(ArmourPieceType)

    def resolve_all_armour(root, info):
        return models.ArmourPiece.objects.all()

    def resolve_all_by_rarity(root, info, rarity: int):
        return models.ArmourPiece.objects.filter(rarity=rarity)

    def resolve_all_head_pieces(root, info):
        return models.ArmourPiece.objects.filter(
            armour_type=models.ArmourPiece.ArmourType.HEAD
        )

    def resolve_all_chest_pieces(root, info):
        return models.ArmourPiece.objects.filter(
            armour_type=models.ArmourPiece.ArmourType.CHEST
        )

    def resolve_all_arms_pieces(root, info):
        return models.ArmourPiece.objects.filter(
            armour_type=models.ArmourPiece.ArmourType.ARMS
        )

    def resolve_all_waist_pieces(root, info):
        return models.ArmourPiece.objects.filter(
            armour_type=models.ArmourPiece.ArmourType.WAIST
        )

    def resolve_all_legs_pieces(root, info):
        return models.ArmourPiece.objects.filter(
            armour_type=models.ArmourPiece.ArmourType.LEGS
        )


schema = graphene.Schema(query=Query)
