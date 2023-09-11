from kiosksvc.models import CheckInLog, Participant
from rest_framework import serializers


class CheckInLogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CheckInLog
        fields = ['tokenId', 'checkedInAt', 'participant']

class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ['id', 'name', 'email', 'affilation', 'role', 'qrUrl', 'couponDetail']

class PasscodeCheckInSerializer(serializers.Serializer):
    passcode = serializers.CharField(max_length=200)