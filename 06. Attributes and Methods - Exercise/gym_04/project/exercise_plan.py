class ExercisePlan:
    id_count = 0

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @staticmethod
    def get_next_id():
        ExercisePlan.id_count += 1
        next_id = ExercisePlan.id_count
        return next_id

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        duration = hours * 60
        return cls(trainer_id, equipment_id, duration)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"
