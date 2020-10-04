class WareHouse:
    def __init__(self, name):
        self.name = name



class OfficeEquipment:
    def __init__(self, name):
        self.name = name


class WareHouseUnit(WareHouse):
    def __init__(self, name, unit):
        super().__init__(name)
        self.name = name
        self.unit = unit
        self.dic_equipment = {}

    def add_equip(self, key, val):
        self.dic_equipment.setdefault(key, val)

    def remove_equip(self, key):
        self.dic_equipment.pop(key)



class Scaner(OfficeEquipment):
    def __init__(self, name, colore, key):
        super().__init__(name)
        self.name = name
        self.colore = colore
        self.key = key



class Comp(OfficeEquipment):
    def __init__(self, name, colore, key):
        super().__init__(name)
        self.name = name
        self.colore = colore
        self.key = key




class PrinterCls(OfficeEquipment):
    def __init__(self, name, colore, key):
        super().__init__(name)
        self.name = name
        self.colore = colore
        self.key = key




printer_1 = PrinterCls("Принтер 1", 'Белый',"1")
scan_1 = Scaner("Сканер 1", 'Черный',"2")
сomp_1 = Comp("Компьютер 1", 'Синий',"3")

wrh_1 = WareHouseUnit("Склад 1", "Подразделение 1")
wrh_1.add_equip(printer_1.key,printer_1)
wrh_1.add_equip(scan_1.key,scan_1)
wrh_1.add_equip(сomp_1.key,сomp_1)

print(f'На складе {wrh_1.name} в подразделении {wrh_1.unit} имеется следующий товар:')
for el in wrh_1.dic_equipment.values():
    print(f'Наименование: {el.name}')
    print('*'*20)
    print(f'Цвет товара: {el.colore}')
    print(f'Код товара: '+el.key)
    print('_'*20+'\n')

wrh_1.remove_equip(сomp_1.key)
wrh_1.remove_equip(scan_1.key)

print(f'На складе {wrh_1.name} в подразделении {wrh_1.unit} имеется следующий товар:')
for el in wrh_1.dic_equipment.values():
    print(f'Наименование: {el.name}')
    print('*'*20)
    print(f'Цвет товара: {el.colore}')
    print(f'Код товара: '+el.key)
    print('_'*20+'\n')


