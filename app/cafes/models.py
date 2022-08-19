from django.conf import settings
from django.db import models
from django.utils.functional import cached_property

User = settings.AUTH_USER_MODEL


class AddressLevelOne(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class AddressLevelTwo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    super_name = models.ForeignKey(AddressLevelOne, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AddressLevelThree(models.Model):
    name = models.CharField(max_length=20, unique=True)
    super_name = models.ForeignKey(AddressLevelTwo, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    name = models.CharField(max_length=30)
    address = models.ForeignKey(AddressLevelThree, on_delete=models.CASCADE)

    detail_address = models.CharField(max_length=50)
    detail_address_load = models.CharField(max_length=50)
    number = models.CharField(max_length=15)
    menu = models.ImageField(upload_to="cafe_menu", blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "detail_address"],
                name="unique cafes",
            )
        ]

    @cached_property
    def address_level1(self):
        return self.address_level2.super_name

    @cached_property
    def address_level2(self):
        return self.address.super_name

    @property
    def sum_address(self):
        return f"{self.address_level1} {self.address_level2} {self.address} {self.detail_address}"

    @property
    def like_count(self):
        return self.likes.count()

    @property
    def flag_count(self):
        return self.flags.count()


class CafeComplexity(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="complexities")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="cafe_complexity_image", blank=True)

    class Level(models.TextChoices):
        ONE = "Very low"
        TWO = "low"
        THREE = "middle"
        FOUR = "high"
        FIVE = "Very high"

    level = models.CharField(max_length=10, choices=Level.choices, blank=True)


class CafeTime(models.Model):
    class Day(models.TextChoices):
        SUN = "Sunday"
        MON = "Monday",
        TUE = "Tuesday",
        WED = "Wednesday",
        THU = "Thursday",
        FRI = "Friday",
        SAT = "Saturday",

    day = models.CharField(max_length=10, choices=Day.choices)
    start = models.TimeField()
    end = models.TimeField()
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)


class CafeTag(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    content = models.CharField(max_length=10)


class CafeImage(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="cafe_image")


class CafeLike(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class CafeFlag(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE, related_name="flags")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Reason(models.TextChoices):
        INCO = "Incorrect",
        MISS = "Miss",
        SPAM = "Spam",
        DIS = "Disturb",
        ETC = "Etc",

    reason = models.CharField(max_length=10, choices=Reason.choices)
    created = models.DateTimeField(auto_now_add=True)
