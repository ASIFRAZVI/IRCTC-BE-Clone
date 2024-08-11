from rest_framework import serializers
from apps.booking_app.models.booking_model import Train


class TrainGetSerializer(serializers.ModelSerializer):
    class Meta:
        model =Train
        fields="__all__"
    
    def validate(self, value):
        """validate date from and upto"""
        input_date_from=value['date_from']
        input_date_upto=value['date_upto']
        
        if input_date_from > input_date_upto:
            raise serializers.ValidationError("The date from should be lesser and date upto should be grater")
        pass
        return value