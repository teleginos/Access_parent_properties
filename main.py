from classes.Sedan import Sedan

if __name__ == '__main__':
    vehicle1 = Sedan('Вася', 'Tesla', '500', 'White')

    vehicle1.print_info()

    vehicle1.set_color('Pink')
    vehicle1.set_color('Red')
    vehicle1.owner = 'Лена'

    vehicle1.print_info()