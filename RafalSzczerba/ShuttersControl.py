import time
import requests
import json

ipaddress = '95.155.88.228:1994'
apiKey = '000'

def ReadLevel():
    try:
        readLvl = requests.get(f'http://{ipaddress}/{apiKey}/get_open_level/').content
    except:
        print("Błąd połączenia program przerwano")
        exit()
    return readLvl
def MoveShutter(level):
    try:
        result = requests.get(f'http://{ipaddress}/{apiKey}/set_open_level/?level={level}&blocking_time=0').content
    except:
        print("Błąd połączenia program przerwano")
        exit()
    return result

if __name__ == '__main__':
    choosenOption = input("Co chcesz zrobić? \r\n 1). Odczytaj położenie rolety \r\n 2). Wysteruj roletę\r\n")
    if(choosenOption  == '1'):
        if(json.loads(ReadLevel())["status"]=="ok"):
            print("odczytano nastętujący poziom pokrycia okna: " + str(json.loads(ReadLevel())["level"] +"%"))
        else:
            print("zły klucz api")

    if(choosenOption == '2'):
        result = input("Ustaw procent odsłąnięcia rolety \r\n")
        if (json.loads(MoveShutter(result))["status"] == "ok"):
            print(f"procedura wykonana - przesłonięcie = {result} %")
        else:
            print("zły klucz api")
