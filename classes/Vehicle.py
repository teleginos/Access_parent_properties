from colorama import Fore, init

init(autoreset=True)


class Vehicle:
    __COLOR_VARIANTS = ["Blue", "White", "Black", "Red", "Green", "Yellow"]

    def __init__(self, owner, model, engine_power, color):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color

    def print_info(self):
        print(f"{Fore.BLUE}Модель: {self.get_model()}\n"
              f"Мощность двигателя: {self.get_horsepower()}\n"
              f"Цвет: {Fore.GREEN + self.get_color()}\n"
              f"{Fore.BLUE}Владелец: {Fore.GREEN + self.owner}")

    def set_color(self, new_color):
        if new_color.capitalize() in self.__COLOR_VARIANTS:
            self.__color = new_color.capitalize()
        else:
            print(f"{Fore.RED}Цвет {new_color} не предусмотрен производителем")
