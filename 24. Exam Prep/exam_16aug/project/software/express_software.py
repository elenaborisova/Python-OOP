from exam_16aug.project.software.software import Software


class ExpressSoftware(Software):
    def __init__(self, name, c_c, m_c):
        super().__init__(name, type_s='Express', capacity_consumption=c_c, memory_consumption=m_c*2)
