# ----------------------------------- 1 ----------------------------------------
'''
����������� ����� �����, �������-����������� �������� ������ ���������
���� � ���� ������ ������� �����-�����-���. � ������ ������ ����������� ��� ������.
������, � ����������� @classmethod, ������ ��������� �����, �����,
��� � ��������������� �� ��� � ���� ������. ������, � ����������� @staticmethod,
������ ��������� ��������� �����, ������ � ���� (��������, ����� � �� 1 �� 12).
��������� ������ ���������� ��������� �� �������� ������.
'''


class Data:
    def __init__(self, day_month_year):
        # self.day = day
        # self.month = month
        # self.year = year
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'All right'
                else:
                    return f'������������ ���'
            else:
                return f'������������ �����'
        else:
            return f'������������ ����'

    def __str__(self):
        return f'������� ���� {Data.extract(self.day_month_year)}'


today = Data('11 - 1 - 2001')
print(today)
print(Data.valid(11, 11, 2022))
print(today.valid(11, 13, 2011))
print(Data.extract('11 - 11 - 2011'))
print(today.extract('11 - 11 - 2020'))
print(Data.valid(1, 11, 2000))


# ----------------------------------- 2----------------------------------------'''

'''
�������� ����������� �����-����������, �������������� �������� ������� �� ����. 
��������� ��� ������ �� ������, �������� �������������. ��� ����� ������������� 
���� � �������� �������� ��������� ������ ��������� ���������� ��� �������� � 
�� ����������� � �������.
'''

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"������� �� ���� �����������")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))

# ----------------------------------- 3 ----------------------------------------
'''
�������� ����������� �����-����������, ������� ������ ��������� ���������� ������ 
�� ���������� ��������� ���� ������ � ������. ��������� ������ ���������� �� �������� �������. 
���������� ����������� � ������������ ������ � ��������� ������. 
�����-���������� ������ �������������� ���� ������ ��������� ������.
'''


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        # self.my_list = [int(i) for i in input('������� �������� ����� ������ ').split()]
        # val = int(input('������� �������� � ��������� Enter - '))
        # self.my_list.append(val)
        while True:
            try:
                val = int(input('������� �������� � ��������� Enter - '))
                self.my_list.append(val)
                print(f'������� ������ - {self.my_list} \n ')
            except:
                print(f"������������ �������� - ������ � ������")
                y_or_n = input(f'����������� ��� ���? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'�� �����'
                else:
                    return f'�� �����'

try_except = Error(1)
print(try_except.my_input())


# ----------------------------------- 4 ----------------------------------------
'''
������� ������ ��� �������� ������ ����������. �������� �����, ����������� �����. 
� ����� ����� �����������, ������� ����� ������� ��� �������-�����������. 
��� ������ � ���������� ���� ���������� (�������, ������, �������). 
� ������� ������ ���������� ���������, ����� ��� ����������� �����. 
� �������-����������� ����������� ���������, ���������� ��� ������� ���� ����������. 
'''

# ----------------------------------- 5 ----------------------------------------

'''
���������� ������ ��� ������ ��������. ����������� ������, ���������� �� ���� ���������� 
�� ����� � �������� � ������������ ������������� ��������. ��� �������� ������ 
� ������������ � ���������� ������ ����������, � ����� ������ ������, ����� ������������ 
����� ���������� ���������, �������� �������.
'''

# ----------------------------------- 6 ----------------------------------------
'''
���������� ������ ��� ������ ��������. ���������� �������� ��������� �������� 
������������� ������. ��������, ��� �������� ���������� ���������, ������������ 
�� �����, ������ ������������ ��������� ��� ������. 
���������: ������������ �� ����������� ����������� � ������� ������ ���������� 
�������� ������������, ��������� �� ������ �� ���.
'''


class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'������ ����������': self.name, '���� �� ��': self.price, '����������': self.quantity}

    def __str__(self):
        return f'{self.name} ���� {self.price} ���������� {self.quantity}'

    # @classmethod
    # @staticmethod
    def reception(self):
        # print(f'��� ������ - Q, ����������� - Enter')
        # while True:
        try:
            unit = input(f'������� ������������ ')
            unit_p = int(input(f'������� ���� �� �� '))
            unit_q = int(input(f'������� ���������� '))
            unique = {'������ ����������': unit, '���� �� ��': unit_p, '����������': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'������� ������ -\n {self.my_store}')
        except:
            return f'������ ����� ������'

        print(f'��� ������ - Q, ����������� - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'���� ����� -\n {self.my_store_full}')
            return f'�����'
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StoreMashines):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StoreMashines):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())


# ----------------------------------- 7 ----------------------------------------
'''
����������� ������ ��������� � ������������ �������. �������� ����� ������������ �����, 
���������� ���������� ������� �������� � ��������� ����������� �����. 
��������� ������ �������, ������ ���������� ������ (����������� �����) � 
�������� �������� � ��������� ��������� �����������. 
��������� ������������ ����������� ����������.
'''


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'����� z1 � z2 �����')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'������������ z1 � z2 �����')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)