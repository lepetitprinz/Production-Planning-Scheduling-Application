from m4.transfer.AbstractConstraint import AbstractConstraint


class CapaConstraint(AbstractConstraint):
    """
    Capa Constraint Object
    Capacity (일별 보관 가능량 혹은 처리 가능량)에 관한 제약을 담당
    """

    # Static 변수들
    staticVar2: object = None               # Comment

    # Static Constants
    CONSTANT_VARIABLE2: object = None       # Comment

    def __init__(self):

        # 1. AbstractConstraint 클래스에 정의된 멤버 변수들을 상속
        super().__init__()

        # 1. Public
        self.memberVar1: object = None

        # 2. Private
        self._privateVar: object = None

    def set_constraint(self):
        pass
