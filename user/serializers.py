from rest_framework import serializers
from user.models import ActivityPeriod, User

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time','end_time')


class UserDataSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True)

    class Meta:
        model = User
        fields = ('id','real_name','tz','activity_periods')
        