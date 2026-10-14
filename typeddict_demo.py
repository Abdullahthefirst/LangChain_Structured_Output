from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person :Person = {'name':'abdullah' , 'age':19}
#the type is helpful for coding in IDE, but doesn't validate it at runtime