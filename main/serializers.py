from main.models import Coards, PerevalAdd, PerevalImages, User, PerevalUser
from rest_framework import serializers
from rest_framework.response import Response

from django.core.exceptions import ValidationError


def file_size(value):  # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')


class CoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coards
        # exclude = (id,)
        # fields = ("latitude", "longitude", "height")
        fields = ("beautyTitle",
                  "title",
                  "other_titles",
                  "connect",
                  "coards",
                  "level_winter",
                  "level_summer",
                  "level_autumn",
                  "level_spring",
                  )


class PerevalUpdSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalAdd
        fields = (
            "status",
            "photos",
            "title",
            "beautyTitle",
            "other_titles",
            "connect",
            "level_winter",
            "level_summer",
            "level_autumn",
            "level_spring",
            "latitude",
            "longitude",
            "height",
            "date_added",
            "add_time",
            # "users",
        )


class PerevalsSerializer(serializers.ModelSerializer):
    # coards = serializers.PrimaryKeyRelatedField(queryset=Coards.objects.all())

    class Meta:
        model = PerevalAdd
        fields = (
            "id",
            "status",
            "title",
            "date_added",
            "add_time",
        )


class PerevalSerializer(serializers.ModelSerializer):
    # photos = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title'
    # )
    # photos = serializers.StringRelatedField(many=True)
    # photos = serializers.PrimaryKeyRelatedField(many=True, queryset=PerevalImages.get(pereval_id=))
    photos = serializers.PrimaryKeyRelatedField(many=True, queryset=PerevalImages.objects.all())

    class Meta:
        model = PerevalAdd
        exclude = ("status", )  # все поля кроме статуса


class PhotoDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = "__all__"


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerevalImages
        fields = "__all__"


class PhotoAddSerializer(serializers.ModelSerializer):
    img = serializers.ImageField(max_length=None, use_url=True, validators=[file_size])

    class Meta:
        model = PerevalImages
        fields = (
            "img",
            "title",
            "date_added",
            "pereval"
        )


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class UserDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "fname", "lname")


class UserAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")


class PerevalUserSerializer:
    class Meta:
        model = PerevalUser
        fields = "__all__"
