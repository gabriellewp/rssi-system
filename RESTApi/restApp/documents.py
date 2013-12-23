from mongoengine import Document, StringField, FloatField, DateTimeField, \
                    IntField, FileField
                    


class InheritableDocument(Document):
    """ Inhertibale document is extended from mongoengin document
        which povides meta object to update document."""
    meta = {
        'abstract': True,
        'allow_inheritance': True,
    }

class watchRecords(InheritableDocument):
    """ watchRecords document is extended from InheritableDocument
        it holds the fields for watchRecors collection for mongoDB."""
    
    x = FloatField()
    y = FloatField()
    insertedAt = DateTimeField()
    mapId = IntField()
    watchId = StringField()
            

class mapRecords(InheritableDocument):
    """ mapRecords document is extended from InheritableDocument
        it holds the fields for mapRecords collection for mongoDB."""
        
    mapId = IntField()
    receiverId = IntField()
    image = FileField()
    width = IntField()
    height = IntField()
    scalingX = FloatField()
    scalingY = FloatField()
    offsetX = IntField()
    offsetY = IntField()
    updateTime = DateTimeField()
    
    
class receiverRecords(InheritableDocument):
    """ receiverRecords document is extended from InheritableDocument
        it holds the fields for receiverRecords collection for mongoDB."""
        
    receiverId = IntField()
    mapId = IntField()
    x = FloatField()
    y = FloatField()
    
    
	

