from abc import *
import datetime

from m4.process.Item import Item


class AbstractRouteNode(metaclass=ABCMeta):
    """
    Abstract Time Constraint
    """
    def __init__(self):
        pass

    @abstractmethod
    def check_availables(self):
        """
        check Available status
        """
        pass

    @abstractmethod
    def fetch(self):
        """
        get and remove item quantity
        """
        pass

    @abstractmethod
    def put(self):
        """
        put item
        """
        pass

    @abstractmethod
    def run(self):
        """
        tick이 발생했을때 aging 처리
        """
        pass
