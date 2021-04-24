from .models import State


class BaseSerialization:


    _model = None


    @classmethod
    def serialize(cls, instance):
        return {
            'pk':instance.pk,
            'description': str(instance)
        }


    @classmethod
    def deserialize(cls, data):
        return cls._model(**data)
    

class StateSerializer(BaseSerialization):
    
    _model = State

    @classmethod
    def serialize(cls, instance):
        result = super().serialize(instance)


        result.update(
            name=instance.name,
            abbreviation=instance.abbreviation
        )

        return result

        
