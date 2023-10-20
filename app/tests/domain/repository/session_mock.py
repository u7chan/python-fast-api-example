from typing import Any, Self


class SessionMock:
    raise_query: Any = None

    one_return_value: Any = None
    all_return_value: list[Any] = []
    add_value: Any = None

    query_call_count = 0
    filter_by_count = 0
    order_by_call_count = 0
    limit_call_count = 0
    one_call_count = 0
    all_call_count = 0
    add_call_count = 0
    commit_call_count = 0

    def query(self, class_type: Any) -> Self:
        self.query_call_count += 1
        if not self.raise_query is None:
            raise self.raise_query
        return self

    def filter_by(self, **args: Any) -> Self:
        self.filter_by_count += 1
        return self

    def order_by(self, sort: Any) -> Self:
        self.order_by_call_count += 1
        return self

    def limit(self, limit: Any) -> Self:
        self.limit_call_count += 1
        return self

    def one(self) -> Any:
        self.one_call_count += 1
        return self.one_return_value

    def all(self) -> list[Any]:
        self.all_call_count += 1
        return self.all_return_value

    def add(self, data: Any):
        self.add_call_count += 1
        self.add_value = data

    def commit(self):
        self.commit_call_count += 1
