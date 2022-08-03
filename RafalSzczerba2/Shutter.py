import requests
from abc import ABC, abstractmethod

class Shutter(ABC):
    level = None
    def __init__(self,ip,apiKey):
        self.ip = ip
        self.apiKey = apiKey

    @abstractmethod
    def ReadLevel(self):
        pass

    @abstractmethod
    def MoveShutter(self,level):
        pass

class ShutterLivingRomm(Shutter):
    # Wywołanie metody init jest tu zbędne - masz taką samą w klasie z której dziedziczysz :) Gdybyś coś zmieniał, to wtedy tak.
    #def __init__(self,ip,apiKey):
    #    self.ip = ip
    #    self.apiKey = apiKey

    def ReadLevel(self):
        try:
            readLvl = requests.get(f'http://{self.ip}/{self.apiKey}/get_open_level/').content
        except:
            print("Błąd połączenia program przerwano")
            exit()
        return readLvl

    def MoveShutter(self, level):
        try:
            result = requests.get(f'http://{self.ip}/{self.apiKey}/set_open_level/?level={level}&blocking_time=0').content
        except:
            print("Błąd połączenia program przerwano")
            exit()
        return result










