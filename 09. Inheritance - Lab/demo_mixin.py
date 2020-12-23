class PrintStateMixin:
    def print_state(self):
        print(f"--- {self.__class__} ---")
        for key, value in self.__dict__.items():
            print(f"{key}={value}")

        print(f"----------")


class DebugAttributesSetterMixin:
    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        print(f"{self.__class__}, {key}={value}")
