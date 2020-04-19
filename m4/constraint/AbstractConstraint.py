from abc import *


class AbstractConstraint(metaclass=ABCMeta):
    """
    Abstract Constraint
    """
    def __init__(self, constraint_id: str = "", constraint_name: str = "", constraint_type: str = ""):
        self.id: str = constraint_id
        self.name: str = constraint_name
        self.type: str = constraint_type

    @abstractmethod
    def check(self):
        pass
