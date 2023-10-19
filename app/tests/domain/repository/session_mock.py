class SessionMock:
    all_value: list[any] = []
    raise_query: any = None

    def query(self, _class) -> "SessionMock":
        if not self.raise_query is None:
            raise self.raise_query
        return self

    def order_by(self, _sort) -> "SessionMock":
        return self

    def limit(self, _limit) -> "SessionMock":
        return self

    def all(self) -> any:
        return self.all_value
