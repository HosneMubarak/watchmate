from rest_framework import serializers
from .models import WatchList, StreamPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchListSerializer(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"

# def name_validate(value):
#     if len(value) < 4:
#         raise serializers.ValidationError('name is two short')
#     else:
#         return value
#
#
# class WatchListSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_validate])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return WatchList.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.name)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('You are not allowed to use same name and description')
#         if WatchList.objects.filter(name=data['name']).exists():
#             raise serializers.ValidationError('Already using this name')
#         else:
#             return data
