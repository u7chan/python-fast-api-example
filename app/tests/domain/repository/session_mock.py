from abc import abstractmethod
from typing import Any, Self


class Mock:
    def __init__(self):
        self.__call_count: int = 0
        self.__args: tuple = ()
        self.__result: Any = None

    def called_count(self) -> int:
        return self.__call_count

    def called_with(self) -> tuple:
        return self.__args

    def return_value(self, value: Any):
        self.__result = value

    def increment(self, *args) -> Any:
        self.__args = args
        self.__call_count += 1
        return self.__result


class SessionMock:
    def __init__(self):
        self.query__mock = Mock()
        self.filter_by__mock = Mock()
        self.order_by__mock = Mock()
        self.limit__mock = Mock()
        self.one__mock = Mock()
        self.all__mock = Mock()
        self.add__mock = Mock()

    def query(self, class_type: Any) -> Self:
        self.query__mock.increment(class_type)
        return self

    def filter_by(self, **args: Any) -> Self:
        self.filter_by__mock.increment(args)
        return self

    def order_by(self, sort: Any) -> Self:
        self.order_by__mock.increment(sort)
        return self

    def limit(self, limit: Any) -> Self:
        self.limit__mock.increment(limit)
        return self

    def one(self) -> Any:
        return self.one__mock.increment()

    def all(self) -> list[Any]:
        return self.all__mock.increment()

    def add(self, data: Any):
        self.add__mock.increment(data)
