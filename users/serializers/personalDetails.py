from users.models.personalDetails import Personal_Details
from rest_framework import serializers


class Persona_Details_Serializers(serializers.ModelSerializer):
    dob = serializers.DateField(
        format='%d/%m/%Y',  # format for output
        input_formats=['%d/%m/%Y']  # format for input
    )
    class Meta:
        model=Personal_Details
        fields="__all__"

    def create(self, validated_data):
        return Personal_Details.objects.create(**validated_data)