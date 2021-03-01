from exam_10apr.project.medicine.medicine import Medicine
from exam_10apr.project.medicine.painkiller import Painkiller
from exam_10apr.project.medicine.salve import Salve
from exam_10apr.project.supply.food_supply import FoodSupply
from exam_10apr.project.supply.supply import Supply
from exam_10apr.project.supply.water_supply import WaterSupply
from exam_10apr.project.survivor import Survivor


class Bunker:
    survivors = []
    supplies = []
    medicine = []

    @property
    def food(self):
        food_objects = [s for s in Bunker.supplies if isinstance(s, FoodSupply)]
        if not food_objects:
            raise IndexError('There are no food supplies left!')
        return food_objects

    @property
    def water(self):
        water_objects = [s for s in Bunker.supplies if isinstance(s, WaterSupply)]
        if not water_objects:
            raise IndexError('There are no water supplies left!')
        return water_objects

    @property
    def painkillers(self):
        painkiller_objects = [m for m in Bunker.medicine if isinstance(m, Painkiller)]
        if not painkiller_objects:
            raise IndexError('There are no painkillers left!')
        return painkiller_objects

    @property
    def salves(self):
        salves_objects = [m for m in Bunker.medicine if isinstance(m, Salve)]
        if not salves_objects:
            raise IndexError('There are no salves left!')
        return salves_objects

    @staticmethod
    def add_survivor(survivor: Survivor):
        if survivor in Bunker.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        Bunker.survivors.append(survivor)

    @staticmethod
    def add_supply(supply: Supply):
        Bunker.supplies.append(supply)

    @staticmethod
    def add_medicine(medicine: Medicine):
        Bunker.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            if medicine_type == 'Painkiller':
                med = self.painkillers[-1]
            elif medicine_type == 'Salve':
                med = self.salves[-1]

            Bunker.medicine.remove(med)
            med.apply(survivor)
            return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            if sustenance_type == 'FoodSupply':
                supply = self.food[-1]
            elif sustenance_type == 'WaterSupply':
                supply = self.water[-1]

            Bunker.supplies.remove(supply)
            supply.apply(survivor)
            return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in Bunker.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
