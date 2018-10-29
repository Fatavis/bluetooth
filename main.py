from tableur import ReadSpreadsheet
from bluetooth import Bluetooth
import time
from pprint import pprint

if __name__ == '__main__':
    stop = ["stop","stop"]
    spreadsheet = ReadSpreadsheet("tableau.csv")
    bluetooth = Bluetooth("COM9", 9600)
    #bluetooth.send_data("start")

    print("Début de l'envoie")
    print("bon nom")

    print("Bonnes syllabes 2")

    for syllable,index in zip(spreadsheet.good_syllable, spreadsheet.index_good_syllable):
        a = 1
        data_received = ""
        while a == 1:
            data_sent = syllable + "-" + str(index)
            bluetooth.send_data(data_sent)
            data_received = bluetooth.receive_data().strip()
            print("La donnée reçue est   : " + data_received)
            print("La donnée envoyée est : " + syllable + "-" + str(index))
            if data_received == data_sent:
                a = 0
            else:
                a = 1

    time.sleep(1)

    #Send the good name
    for name,index in zip(spreadsheet.good_name, spreadsheet.index_good_name):
        a = 1
        data_received = ""
        while a == 1:
            data_sent = name + "-" + str(index)
            bluetooth.send_data(data_sent)
            data_received = bluetooth.receive_data().strip()
            print("La donnée reçue est   : " + data_received)
            print("La donnée envoyée est : " + name + "-" + str(index))
            if data_received == data_sent:
                a = 0
            else:
                a = 1

    time.sleep(1)

    bluetooth.kick()
    bluetooth.close_communication()
    time.sleep(6)
    bluetooth2 = Bluetooth("COM9", 9600)

    for name in spreadsheet.bad_name1:
        a = 1
        data_received = ""
        while a == 1:
            data_sent = name
            bluetooth2.send_data(data_sent)
            data_received = bluetooth2.receive_data().strip()
            print("La donnée reçue est   : " + data_received)
            print("La donnée envoyée est : " + name)
            print(data_received == data_sent)
            if data_received == data_sent:
                a = 0
            else:
                a = 1

    time.sleep(1)

    bluetooth2.kick()
    bluetooth2.close_communication()
    time.sleep(6)
    bluetooth3 = Bluetooth("COM9", 9600)

    print("mauvais nom 2")

    for name in spreadsheet.bad_name2:
        a = 1
        data_received = ""
        while a == 1:
            data_sent = name
            bluetooth3.send_data(data_sent)
            data_received = bluetooth3.receive_data().strip()
            print("coucou1")
            print("La donnée reçue est   : " + data_received)
            print("La donnée envoyée est : " + data_sent)
            print(data_received == data_sent)
            if data_received == data_sent:
                a = 0
                print("coucou2")
            else:
                a = 1

    time.sleep(2)


    results_name = []
    results_syllables = []

    while bluetooth3.receive_data().strip() != "end":
        results_name.append(bluetooth3.receive_data().strip())
        print(bluetooth2.receive_data().strip())

    while bluetooth2.receive_data().strip() != "end":
        results_syllables.append(bluetooth3.receive_data().strip())
        print(bluetooth3.receive_data().strip())

    for data in results_name:
        print(data)

    for data in results_syllables:
        print(data)

    print(bluetooth.receive_data())
    bluetooth.close_communication()