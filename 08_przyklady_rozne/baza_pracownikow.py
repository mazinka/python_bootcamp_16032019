import json

try:
    with open('python_employees.py') as file:
        employes = json.load(file)

except FileNotFoundError:
    employes =[]

action = input('co chcesz zrobić[d-dodaj, w-wypisz]')



if action == 'd':
    name = input ('podaj imie')
    last_name = input('podaj nazwisko')
    salary = input('pensja')

    employee ={
        'name': name,
        'last_name': last_name,
        'salary': salary
    }

    employes.append(employee)
    with open('python_employees.py','w') as fp:
        json.dump(employes, fp)

elif action =="w":
    for i, e in enumerate(employes, start=1):
        print(f'-[{i}] {e["name"]} {e["last_name"]}, pensja: {e["salary"]}')
