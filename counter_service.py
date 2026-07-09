class CounterService:
    def __init__(self) -> None:
        self._counter = 0

    def increment(self) -> int:
        self._counter += 1
        return self._counter

    def get_current_value(self) -> int:
        return self._counter
