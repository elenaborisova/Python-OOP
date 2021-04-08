from exam_19dec.project.medicine.medicine import Medicine
from exam_19dec.project.medicine.painkiller import Painkiller
from exam_19dec.project.medicine.salve import Salve
from exam_19dec.project.supply.food_supply import FoodSupply
from exam_19dec.project.supply.supply import Supply
from exam_19dec.project.supply.water_supply import WaterSupply
from exam_19dec.project.survivor import Survivor


class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_supplies = [s for s in self.supplies if isinstance(s, FoodSupply)]
        if not food_supplies:
            raise IndexError('There are no food supplies left!')
        return food_supplies

    @property
    def water(self):
        water_supplies = [s for s in self.supplies if isinstance(s, WaterSupply)]
        if not water_supplies:
            raise IndexError('There are no water supplies left!')
        return water_supplies

    @property
    def painkillers(self):
        painkillers = [m for m in self.medicine if isinstance(m, Painkiller)]
        if not painkillers:
            raise IndexError('There are no painkillers left!')
        return painkillers

    @property
    def salves(self):
        salves = [m for m in self.medicine if isinstance(m, Salve)]
        if not salves:
            raise IndexError('There are no salves left!')
        return salves

    def add_survivor(self, survivor: Survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply: Supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine: Medicine):
        self.medicine.append(medicine)

    def heal(self, survivor: Survivor, medicine_type: str):
        if survivor.needs_healing:
            medicine = [m for m in self.medicine if m.__class__.__name__ == medicine_type][-1]
            self.medicine.remove(medicine)
            medicine.apply(survivor)
            return f'{survivor.name} healed successfully with {medicine_type}'

    def sustain(self, survivor: Survivor, sustenance_type: str):
        if survivor.needs_sustenance:
            sustenance = [s for s in self.supplies if s.__class__.__name__ == sustenance_type][-1]
            self.supplies.remove(sustenance)
            sustenance.apply(survivor)
            return f'{survivor.name} sustained successfully with {sustenance_type}'

    def next_day(self):
        for survivor in self.survivors:
            survivor.needs -= survivor.age * 2
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
