from django.db import models


# Create your models here.
class ArmourPiece(models.Model):
    class ArmourType(models.IntegerChoices):
        HEAD = 0
        CHEST = 1
        ARMS = 2
        WAIST = 3
        LEGS = 4

    name = models.CharField(max_length=255, unique=True)
    rarity = models.IntegerField()
    min_defence = models.IntegerField()
    max_defence = models.IntegerField()
    fire_resistance = models.IntegerField()
    water_resistance = models.IntegerField()
    thunder_resistance = models.IntegerField()
    ice_resistance = models.IntegerField()
    dragon_resistance = models.IntegerField()
    no_of_one_slot_decorations = models.IntegerField()
    no_of_two_slot_decorations = models.IntegerField()
    no_of_three_slot_decorations = models.IntegerField()
    armour_type = models.IntegerField(ArmourType.choices)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def no_slots(self) -> bool:
        return (
            self.no_of_one_slot_decorations == 0
            and self.no_of_two_slot_decorations == 0
            and self.no_of_three_slot_decorations == 0
        )
