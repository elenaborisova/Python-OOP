# The Singleton pattern is used when we want to guarantee that only one instance of a given class exists during runtime

def singleton(cls):
    instance = [None]

    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class DataImporter:
    def __init__(self):
        pass


importer1 = DataImporter()
print(importer1)
importer2 = DataImporter()
print(importer2)
print(importer1 == importer2)

# same id's same objects; they are equal
# everytime I create a new instance I need to receive the same object

# singleton restricts us from having static and class methods in the class
