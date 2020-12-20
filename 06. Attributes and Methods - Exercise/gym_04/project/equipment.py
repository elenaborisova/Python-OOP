class Equipment:
    id_count = 0

    def __init__(self, name: str):
        self.name = name
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        Equipment.id_count += 1
        next_id = Equipment.id_count
        return next_id

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
