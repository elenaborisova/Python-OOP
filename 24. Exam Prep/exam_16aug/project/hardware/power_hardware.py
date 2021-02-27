from exam_16aug.project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, type_h='Power', capacity=capacity*0.25, memory=memory*1.75)
