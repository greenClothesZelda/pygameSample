GRAVITY: float = 3

class Fallable:
    def __init__(self, position: dict[str:float]):
        self.is_falling: bool = False
        self.position: dict[str: float] = position


    def fall(self, gravity: float) -> None:
        if self.is_falling:
            # 중력에 의해 위치를 업데이트
            self.position['dy'] += gravity
