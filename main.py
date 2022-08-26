from datetime import datetime
from pyfiglet import Figlet
import pandas as pd

data = [
    {
        'registration_id': 1,
        'registration_date': '2021-01-26',
        'first_name': 'Andi',
        'last_name': 'Kim',
        'street_address': 'Jl. Soka Raya blok y no 1',
        'city': 'Bekasi',
        'zip_code': '17116',
        'sex': 'M',
        'age': 24,
        'blood_type': 'A',
        'phone_number': '082112609738',
        'created_at': '2021-04-26',
        'updated_at': '2021-04-26'
    },
    {
        'registration_id': 2,
        'registration_date': '2021-02-26',
        'first_name': 'Budi',
        'last_name': 'Park',
        'street_address': 'Jl. melati Raya blok y no 2',
        'city': 'Bogor',
        'zip_code': '16680',
        'sex': 'M',
        'age': 22,
        'blood_type': 'B',
        'phone_number': '082112609733',
        'created_at': '2021-04-26',
        'updated_at': '2021-04-26'
    },
    {
        'registration_id': 3,
        'registration_date': '2021-04-26',
        'first_name': 'Caca',
        'last_name': 'Lee',
        'street_address': 'Jl. melati 3 blok z no 1',
        'city': 'Jakarta',
        'zip_code': '15117',
        'sex': 'F',
        'age': 19,
        'blood_type': 'O',
        'phone_number': '082112609777',
        'created_at': '2021-04-26',
        'updated_at': '2021-04-26'
    },
]


def find_index(r):
    for i, d in enumerate(data):
        if d['registration_id'] == int(r):
            return i


def create():
    print('\nPlease select one of these options.')
    menus = ['Insert Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Enter your choice here : ")

    if (option == '1'):
        registration_id = input("\nEnter registration id : ")
        index = find_index(registration_id)
        if index != None:
            print("\nRegistration id already exist.")
            create()
        else:
            print('\nPlease fill in the patient form below.')
            forms = ['First Name', 'Last Name',
                     'Street Address', 'City', 'Zip Code', 'Sex', 'Age', 'Blood Type', 'Phone Number']
            temp = []

            for form in forms:
                answer = input(f"{form} : ")
                temp.append(answer)

            new_data = {
                'registration_id': registration_id,
                'registration_date': datetime.today().strftime('%Y-%m-%d'),
                'first_name': temp[0],
                'last_name': temp[1],
                'street_address': temp[2],
                'city': temp[3],
                'zip_code': temp[4],
                'sex': temp[5],
                'age': temp[6],
                'blood_type': temp[7],
                'phone_number': temp[8],
                'created_at': datetime.today().strftime('%Y-%m-%d'),
                'updated_at': datetime.today().strftime('%Y-%m-%d')
            }
            option = input("Saved data? (Yes/No): ")

            if option == 'Yes':
                data.append(new_data)
                print('\nData saved successfully.')
                create()
            else:
                create()
    else:
        main()


def read():
    print('\nPlease select one of these options.')
    menus = ['View All Data', 'View Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Enter your choice here : ")

    if (option == '1'):
        if data == []:
            print("\nDatabase is empty.")
            read()
        else:
            print('\n')
            print(pd.DataFrame(data).to_string(index=False))
            print('\n')
            read()

    elif (option == '2'):
        registration_id = int(input(
            '\nPlease enter the registration_id of the patient you want to see : '))

        index = find_index(registration_id)
        if index != None:
            print('\n')
            print(pd.DataFrame([data[index]]).to_string(index=False))
            print('\n')
            read()
        else:
            print("\nData doesn\'t exist.")
            read()
    else:
        main()


def update():
    print('\nPlease select one of these options.')
    menus = ['Update Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Enter your choice here : ")

    if (option == '1'):
        registration_id = input("\nEnter registration id : ")
        index = find_index(registration_id)
        if index == None:
            print("\nData doesn\'t exist.")
            update()
        else:
            print('\n')
            print(pd.DataFrame([data[index]]).to_string(index=False))
            print('\n')

            option = input("Continue update? (Yes/No) : ")

            if (option == 'Yes'):
                print('\nPlease select one of these options.')
                menus = ['first_name', 'last_name', 'street_address', 'city',
                         'zip_code', 'sex', 'age', 'blood_type', 'phone_number']
                for i, menu in enumerate(menus, start=1):
                    print(f'{i} : {menu}')
                option = int(input("Enter your choice here : "))-1

                new_data = input(
                    f'\nPlease input your new {menus[option]} data : ')

                proceed = input("Update data? (Yes/No): ")
                if proceed == 'Yes':
                    print(menus[option])
                    data[index][menus[option]] = new_data

                    print('\nData updated successfully!')
                    update()
                else:
                    update()
            else:
                update()
    else:
        main()


def delete():
    print('\nPlease select one of these options.')
    menus = ['Delete Data', 'Main Menu']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')
    option = input("Enter your choice here : ")

    if (option == '1'):
        registration_id = input("\nEnter registration id : ")
        index = find_index(registration_id)
        if index == None:
            print("\nData doesn\'t exist.")
            update()
        else:
            print('\n')
            print(pd.DataFrame([data[index]]).to_string(index=False))
            print('\n')

            option = input("Continue delete? (Yes/No) : ")

            if (option == 'Yes'):
                del data[index]

                print('\nData deleted successfully!')
                delete()
            else:
                delete()
    else:
        main()


def main():
    print('\nPlease select one of the menus below.')
    menus = ['Read data', 'Add new data',
             'Update existing data', 'Delete a data', 'Exit']
    for i, menu in enumerate(menus, start=1):
        print(f'{i} : {menu}')

    option = input("Enter your choice here : ")

    if (option == '1'):
        read()
    elif (option == '2'):
        create()
    elif (option == '3'):
        update()
    elif (option == '4'):
        delete()
    elif (option == '5'):
        print('\nGoodbye, have a nice day~!')
    elif (option == ''):
        print('\nYour option can\'t be empty!')
        main()
    else:
        print('\nThis menu doesn\'t exists!')
        main()


if __name__ == '__main__':
    # welcome message and menus
    result = Figlet(font='Slant')
    print(result.renderText("Hospital System!"))
    print('====Hello, welcome to the patient data portal!===\n')

    main()
