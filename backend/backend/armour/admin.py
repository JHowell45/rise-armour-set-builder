from django.contrib import admin

from .models import ArmourPiece, ArmourSet


# Register your models here.
@admin.register(ArmourPiece)
class ArmourPieceAdmin(admin.ModelAdmin):
    model = ArmourPiece

    list_display = [
        "id",
        "name",
        "set_name_name",
        "rarity",
        "min_defence",
        "max_defence",
        "fire_resistance",
        "water_resistance",
        "thunder_resistance",
        "ice_resistance",
        "dragon_resistance",
        "no_of_one_slot_decorations",
        "no_of_two_slot_decorations",
        "no_of_three_slot_decorations",
    ]

    list_editable = [
        "name",
        "rarity",
        "min_defence",
        "max_defence",
        "fire_resistance",
        "water_resistance",
        "thunder_resistance",
        "ice_resistance",
        "dragon_resistance",
        "no_of_one_slot_decorations",
        "no_of_two_slot_decorations",
        "no_of_three_slot_decorations",
    ]

    save_on_top = True

    def set_name_name(self, instance):
        return instance.set_name.name


@admin.register(ArmourSet)
class ArmourSetAdmin(admin.ModelAdmin):
    model = ArmourSet

    list_display = ["id", "name", "rarity", "date_created", "date_modified"]

    list_editable = ["name", "rarity"]
