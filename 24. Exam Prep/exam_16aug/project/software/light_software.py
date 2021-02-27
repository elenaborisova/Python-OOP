from exam_16aug.project.software.software import Software


class LightSoftware(Software):
    def __init__(self, name, c_c, m_c):
        super().__init__(name, type_s='light', capacity_consumption=c_c*1.5, memory_consumption=m_c*0.5)
