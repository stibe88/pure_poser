from dataclasses import dataclass


@dataclass
class Translation(object):
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

    def __invert__(self) -> "Translation":
        return Translation(
            x=-self.x,
            y=-self.y,
            z=-self.z,
        )
    
    def __abs__(self) -> float:
        return (
            self.x**2 + self.y**2 + self.z**2
        )**0.5
    
    def __add__(
        self, 
        other: "Translation",
    ) -> "Translation":
        return Translation(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z,
        )
    
