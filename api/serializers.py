from rest_framework import serializers

class UuidSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
            str(instance.timestamp) : instance.uuid
        }