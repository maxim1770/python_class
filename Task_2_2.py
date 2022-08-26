import math
from abc import ABC, abstractmethod


class Home(ABC):

    @abstractmethod
    def __init__(self, width, height, length):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def SetPeople(self, number_people):
        pass

    @abstractmethod
    def SetLanguage(self, language):
        pass


class City(Home):

    @abstractmethod
    def __init__(self, width, height, length, number_people, language, number_houses):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def SetCount(self, number_houses):
        pass

    @abstractmethod
    def SetPeople(self, number_people):
        pass

    @abstractmethod
    def SetLanguage(self, language):
        pass


class Country(City):

    def __init__(self, width, height, length, number_people, language, number_houses, number_cities):
        self.width = width
        self.height = height
        self.length = length
        self.number_people = number_people
        self.language = language
        self.number_houses = number_houses
        self.number_cities = number_cities

    def print(self):
        print(self.width, self.height, self.length, self.number_people, self.language, self.number_houses,
              self.number_cities)

    def SetCount(self, number_houses):
        self.number_houses = number_houses

    def SetPeople(self, number_people):
        self.number_people = number_people

    def SetLanguage(self, language):
        self.language = language

    def CountPeople(self):
        return self.number_cities * self.number_houses * self.number_people
