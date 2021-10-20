from django.db import models


# Create your models here.
class ArmourSet(models.Model):
    name = models.CharField(max_length=255, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)


class ArmourPiece(models.Model):
    class ArmourType(models.IntegerChoices):
        HEAD = 0
        CHEST = 1
        ARMS = 2
        WAIST = 3
        LEGS = 4

    name = models.CharField(max_length=255, unique=True)
    set_name = models.ForeignKey(ArmourSet, on_delete=models.CASCADE)
    rarity = models.IntegerField()
    min_defence = models.IntegerField()
    max_defence = models.IntegerField(null=True, blank=True)
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

    def is_low_rank(self) -> bool:
        return self.rarity < 4

    def is_high_rank(self) -> bool:
        return 4 <= self.rarity < 7

    def is_master_rank(self) -> bool:
        return self.rarity > 7
