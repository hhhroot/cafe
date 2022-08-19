from rest_framework import serializers

from .models import Cafe, CafeComplexity, AddressLevelOne, AddressLevelTwo, AddressLevelThree, CafeLike


class CafeSerializer(serializers.ModelSerializer):
    full_address = serializers.CharField(write_only=True)

    class Meta:
        model = Cafe
        fields = [
            "pk",
            "name",
            "number",
            "sum_address",
            "full_address",
            "like_count",
            "flag_count",
        ]

    def validate(self, attrs):
        ret = super().validate(attrs)
        full_address = attrs.pop("full_address")
        address_level1, address_level2, address_level3, *details = full_address.split(" ")
        detail_address = " ".join(details)

        ret["address_level1"] = address_level1
        ret["address_level2"] = address_level2
        ret["address_level3"] = address_level3
        ret["detail_address"] = detail_address

        return ret

    def create(self, validated_data):
        address_level1 = validated_data.pop("address_level1")
        address_level2 = validated_data.pop("address_level2")
        address_level3 = validated_data.pop("address_level3")

        address_level1, _ = AddressLevelOne.objects.get_or_create(name=address_level1)
        address_level2, _ = AddressLevelTwo.objects.get_or_create(name=address_level2, super_name=address_level1)
        address_level3, _ = AddressLevelThree.objects.get_or_create(name=address_level3, super_name=address_level2)

        validated_data["address"] = address_level3

        return super().create(validated_data)


class CafeComplexitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CafeComplexity
        fields = [
            "cafe",
            "content",
            "created",
            "image",
            "level",
        ]

    def validate(self, attrs):
        ret = super().validate(attrs)
        user = self.context['request'].user
        ret['user'] = user

        return ret


class CafeDetailSerializer(serializers.ModelSerializer):
    complexities = CafeComplexitySerializer(many=True)
    is_flag = serializers.SerializerMethodField()
    is_like = serializers.SerializerMethodField()

    class Meta:
        model = Cafe
        fields = [
            "name",
            "number",
            "sum_address",
            "complexities",
            "is_flag",
            "is_like",
        ]

    def get_is_flag(self, obj):
        user = self.context['request'].user
        if obj.flags.filter(user=user).first():
            return True
        else:
            return False

    def get_is_like(self, obj):
        user = self.context['request'].user
        if obj.likes.filter(user=user).first():
            return True
        else:
            return False


class CafeLikeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="cafe.name")
    address = serializers.CharField(source="cafe.sum_address")
    call = serializers.CharField(source="cafe.number")

    class Meta:
        model = CafeLike
        fields = [
            "name",
            "address",
            "call",
            "created",
        ]