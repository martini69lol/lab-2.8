#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

airport = []

def add_flight():
    race = input("Название пункта назначения рейса: ")
    number = input("Номер рейса: ")
    type = float(input("Тип самолёта: "))

    airports = {
        'race': race,
        'number': number,
        'type': type,
    }

    airport.append(airports)
    if len(airport) > 1:
        airport.sort(key=lambda item: item.get('race', ''))

def list_flights():
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 20
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^20} |'.format(
            "No",
            "Пункт",
            "Номер",
            "Тип самолёта"
        )
    )
    print(line)

    for idx, airports in enumerate(airport, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>20} |'.format(
                idx,
                airports.get('race', ''),
                airports.get('number', ''),
                airports.get('type', 0)
            )
        )

    print(line)

def select_flight(command):
    parts = command.split(' ', maxsplit=2)
    sel = parts[1]

    count = 0
    for airports in airport:
        if airports.get('type') == sel:
            count += 1
            print(
                '{:>4}: {}'.format(count, airports.get('race', ''))
            )
            print('Пункт:', airports.get('race', ''))
            print('Номер:', airports.get('number', ''))

    if count == 0:
        print("Тип самолета не найден.")

def help_menu():
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рейсов;")
    print("select <товар> - информация о рейсе;")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")

def main():
    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            add_flight()

        elif command == 'list':
            list_flights()

        elif command.startswith('select '):
            select_flight(command)

        elif command == 'help':
            help_menu()

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == '__main__':
    main()
