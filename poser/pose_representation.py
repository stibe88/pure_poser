from dataclasses import dataclass
from typing import Tuple

from poser.rotation_handler import Rotation
from poser.translation_representation import Translation


@dataclass
class Pose(object):
    translation: Translation
    rotation: Rotation

    def __invert__(self) -> "Pose":
        inverted_rotation = ~self.rotation
        return Pose(
            translation=inverted_rotation.transformed_point(~self.translation),
            rotation=inverted_rotation,
        )
    
    def __mul__(self, other: "Pose"):
        return Pose(
            translation=self.translation + self.rotation.transformed_point(
                other.translation
            ),
            rotation=self.rotation * other.rotation,
        )
    
    @property
    def as_tuple(self) -> Tuple[Tuple[float]]:
        r = self.rotation.as_tuple
        t = self.translation.as_tuple
        return (
            (r[0][0], r[0][1], r[0][2], t[0],),
            (r[1][0], r[1][1], r[1][2], t[1],),
            (r[2][0], r[2][1], r[2][2], t[2],),
            (0.0, 0.0, 0.0, 1.0,),
        )
    
    @as_tuple.setter
    def as_tuple(self, matrix: Tuple[Tuple[float]]) -> None:
        self.rotation.as_tuple = (
            matrix[0][:3], matrix[1][:3], matrix[2][:3]
        )
        self.translation.as_tuple = (matrix[0][3], matrix[1][3], matrix[2][3])
