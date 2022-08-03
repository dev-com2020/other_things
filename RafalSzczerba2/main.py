import json
from Shutter import ShutterLivingRomm

ipaddress = '95.155.8.228:1994'
apiKey = '000'
if __name__ == '__main__':
    shutterLR = ShutterLivingRomm(ipaddress,apiKey)
    choosenOption = input("Co chcesz zrobić? \r\n 1). Odczytaj położenie rolety \r\n 2). Wysteruj roletę\r\n")
    if(choosenOption  == '1'):
        if(json.loads(shutterLR.ReadLevel())["status"]=="ok"):
            print("odczytano nastętujący poziom pokrycia okna: " + str(json.loads(shutterLR.ReadLevel())["level"] +"%"))
        else:
            print("zły klucz api")

    if(choosenOption == '2'):
        result = input("Ustaw procent odsłąnięcia rolety \r\n")
        if (json.loads(shutterLR.MoveShutter(result))["status"] == "ok"):
            print(f"procedura wykonana - przesłonięcie = {result} %")
        else:
            print("zły klucz api")
