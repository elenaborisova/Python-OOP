from exam_16aug.project.software.software import Software


class UnsuccessfulInstallException(Exception):
    pass


class Hardware:
    def __init__(self, name, type_h, capacity, memory):
        self.name = name
        self.type_h = type_h
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if self.capacity < software.capacity_consumption or self.memory < software.memory_consumption:
            raise UnsuccessfulInstallException('Software cannot be installed')

        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
