import random

from data.data import Person, Color, Date, SelectMenu
from faker import Faker

faker_ru = Faker('ru_RU')
faker_en = Faker('En')
Faker.seed()

def generated_person():
    yield Person(
        full_name= faker_ru.first_name() + ' ' + faker_ru.last_name() + ' ' + faker_ru.middle_name(),
        firstname= faker_ru.first_name(),
        lastname= faker_ru.last_name(),
        age= random.randint(10,80),
        salary= random.randint(10000,80000),
        department= faker_ru.job(),
        email= faker_ru.email(),
        current_address= faker_ru.address(),
        permanent_address= faker_ru.address(),
        mobile= faker_ru.msisdn(),
    )

def generated_file():
    path = f'/Users/leonidlobanov/PycharmProjects/aqc/filetest{random.randint(1,19)}.txt'
    file = open(path, 'w+')
    file.write(f'Hi man, Success - {random.randint(1,19)}')
    file.close()
    return file.name, path

def generated_subject():
    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return random.choice(subjects)

def generated_choose_state():
    states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
    return random.choice(states)

def generated_choose_city():
    city = generated_choose_state()
    NCR = ["Delhi", "Gurgaon", "Noida"]
    Uttar_Pradesh = ['Agra', "Lucknow", "Merrut"]
    Haryana = ["Karnal", "Panipat"]
    Rajasthan = ["Jaipur", "Jaiselmer"]
    if city == 'NcR':
        return random.choice(NCR)
    elif city == "Uttar Pradesh":
        return random.choice(Uttar_Pradesh)
    elif city == "Haryana":
        return random.choice(Haryana)
    elif city == "Rajasthan":
        return random.choice(Rajasthan)
    else:
        return False

def generated_color():
    yield Color(
        color_name=["Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )

def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:00'
    )

def generated_select_menu():
    yield SelectMenu(
        select_value=["Group 1, option 1", "Group 1, option 2", "Group 2, option 1", "Group 2, option 2", "A root option", "Another root option"],
        select_title=["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"],
        multiselect_color=["Green", "Blue", "Black", "Red"],
        car_select=["Volvo", "Saab", "Opel", "Audi"]
    )

