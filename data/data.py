from dataclasses import dataclass


@dataclass
class Person:
    full_name : str = None
    firstname : str = None
    lastname : str = None
    email : str = None
    age : int = None
    salary : int = None
    department : str = None
    current_address : str = None
    permanent_address : str = None
    mobile : str = None

@dataclass
class Color:
    color_name: list = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None

@dataclass
class SelectMenu:
    select_value: list = None
    select_title: list = None
    multiselect_color: list = None
    car_select: list = None