from exam_16aug.project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, type_h='Heavy', capacity=capacity*2, memory=memory*0.75)
