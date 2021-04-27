from .models import City, State


class BaseSerialization:


    _model = None

    @classmethod
    def Model(cls):
        return cls._model

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


class CitySerializer(BaseSerialization):
    
    _model = City

    @classmethod
    def serialize(cls, instance):
        result = super().serialize(instance)


        result.update(
            name=instance.name,
            state=StateSerializer.serialize(instance.state)
        )

        return result

        
