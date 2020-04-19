

class Policy(object):
    """
    Policy Object
    """

    # 1-1. Public Static

    # 1-2. Private Static
    _INIT_KEYWORD_ARGS: dict = {
        'DAILY': {},
        'WEEKLY': {},
        'CUSTOM': {}
    }

    _TYPES: list = [
        'DAILY',
        'WEEKLY',
        'CUSTOM'
    ]

    def __init__(self):
        """
        생성자 :
        """

        # 2-1. Public Member

        # 2-2. Private Member
        self._location: str = ""            # 'factory', 'machine', 'warehouse'
        self._cause: str = ""               #
        self._timeIntervals: list = []      #

    def init(self, type: str, **kwargs):
        if type not in Policy._INIT_KEYWORD_ARGS.keys():
            raise KeyError(
                f""
            )

    def _set_type(self, type_name: str):
        """
        str 형식의 값을 self._startDate 속성으로 할당합니다.
        :param type_name: str = 타입 종류
        :return: void
        """
        self._type = type_name
