from dataclasses import dataclass
from typing import Tuple, List, Optional, Union

import poser
import poser.rotation.rotation


Point = poser.point.Point
Translation = poser.translation.Translation
Rotation = poser.rotation.rotation.Rotation


@dataclass
class Pose(object):
    translation: Optional[Translation] = None
    rotation: Optional[Rotation] = None

    def __post_init__(self) -> None:
        if not self.translation:
            self.translation = Translation()
        if not self.rotation:
            self.rotation = Rotation()

    def __invert__(self) -> "Pose":
        inverted_rotation = ~self.rotation
        return Pose(
            translation=inverted_rotation.transformed_point(
                ~self.translation
            ),
            rotation=inverted_rotation,
        )
    
    def __mul__(self, other: "Pose"):
        return Pose(
            translation=(
                self.translation 
                + self.rotation.transformed_point(
                    other.translation
                )
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
        self.translation.as_tuple = (
            matrix[0][3], matrix[1][3], matrix[2][3]
        )

    @property
    def as_list(self) -> List[List[float]]:
        r = self.rotation.as_list
        t = self.translation.as_list
        return [
            r[0] + [t[0]],
            r[1] + [t[1]],
            r[2] + [t[2]],
            [0.0, 0.0, 0.0, 1.0],
        ]        

    @as_list.setter
    def as_list(self, matrix: List[List[float]]) -> None:
        self.rotation.as_list = (
            matrix[0][:3], matrix[1][:3], matrix[2][:3]
        )
        self.translation.as_list = (
            matrix[0][3], matrix[1][3], matrix[2][3]
        )

    def interpolated(
        self,
        other: "Pose",
        factor: float,
    ) -> "Pose":
        return Pose(
            translation=self.translation.interpolated(
                other=other.translation, 
                factor=factor,
            ),
            rotation=self.rotation.interpolated(
                other=other.rotation,
                factor=factor,
            ),
        )
    
    def transform_point(
        self,
        point: Union[Point, Translation],
    ) -> None:
        self.rotation.transform_point(point=point)
        self.translation.transform_point(point=point)

    def transform_points(
        self,
        points: Union[list, tuple],
    ) -> None:
        self.rotation.transform_points(points=points)
        self.translation.transform_points(points=points)

    def transformed_point(
        self,
        point: Union[Point, Translation],
    ) -> Union[Point, Translation]:
        return self.translation.transformed_point(
            point=self.rotation.transformed_point(
                point=point,
            )
        )
    
    def transformed_points(
        self,
        points: Union[list, tuple],
    ) -> Union[list, tuple]:
        return self.translation.transformed_points(
            points=self.rotation.transformed_points(
                points=points,
            )
        )
