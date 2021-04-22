
class BaseSerialization:


    _model = None


    def serialize(self, instance):
        raise NotImplemented('Abstrat class serialize not implemented')


    def deserialize(self, data):
        raise NotImplemented('Abstrat class serialize not implemented')