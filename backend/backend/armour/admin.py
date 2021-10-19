from django.contrib import admin

from .models import ArmourPiece

# Register your models here.


@admin.register(ArmourPiece)
class ArmourPieceAdmin(admin.ModelAdmin):
    model = ArmourPiece
