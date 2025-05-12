# Single Responsibility Principle

from unittest import result


class ArrayValidator():
    def validate(self, array):
        assert type(array) == list, ValueError('Please, Insert a List')
        assert len(array) > 1, ValueError(
            'the list need have more than 1 element')


class ArrayToStringTransformer():
    def transform(self, array):
        return [str(i) for i in array]


class ArrayConcatenator():
    def __init__(self, validator: ArrayValidator, strTransformator: ArrayToStringTransformer):
        self.validator = validator
        self.toStr = strTransformator

    def concatenate(self, array: list) -> str:
        self.validator.validate(array)
        array = self.toStr.transform(array)
        return ' '.join(array)


arrayConcatenator = ArrayConcatenator(
    validator=ArrayValidator(),
    strTransformator=ArrayToStringTransformer())

if __name__ == '__main__':

    myString = 'POO is cool, bro'
    mySecondString = 'i love it!'

    myArray = [myString, mySecondString]

    result: str = arrayConcatenator.concatenate(
        array=[myString, mySecondString])

    print(result)
