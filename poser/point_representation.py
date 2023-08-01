from dataclasses import dataclass
from typing import Tuple, List


@dataclass
class Point(object):
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __post_init__(self):
        if not isinstance(self.x, float):
            self.x = float(self.x)
        if not isinstance(self.y, float):
            self.y = float(self.y)
        if not isinstance(self.z, float):
            self.z = float(self.z)

    @property
    def as_tuple(self) -> Tuple[float]:
        return (self.x, self.y, self.z,)
    
    @as_tuple.setter
    def as_tuple(
        self,
        point: Tuple[float]
    ) -> None:
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.__post_init__()

    @property
    def as_list(self) -> List[float]:
        return [self.x, self.y, self.z]
    
    @as_list.setter
    def as_list(
        self,
        point: List[float]
    ) -> None:
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.__post_init__()
