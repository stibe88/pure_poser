from dataclasses import dataclass
from typing import Union, Tuple, List

import poser

from . import representations
from . import converter


Point = poser.point.Point
Translation = poser.translation.Translation

Matrix = representations.Matrix
Quaternion = representations.Quaternion
OPKDeg = representations.OPKDeg

Converter = converter.Converter


@dataclass(init=False)
class Rotation(object):
    quaternion: Quaternion = None
    matrix: Matrix = None
    opk_deg: OPKDeg = None

    def __init__(
        self,
        rotation: Union[Quaternion, Matrix, OPKDeg] = Quaternion()
    ) -> None:
        if isinstance(rotation, Quaternion):
            self.quaternion = rotation
            self._update_from_quaternion()
        elif isinstance(rotation, Matrix):
            self.matrix = rotation
            self._update_from_matrix()
        elif isinstance(rotation, OPKDeg):
            self.opk_deg = rotation
            self._update_from_opk_deg()
        else:
            raise TypeError(
                f"rotation has an unsupported type: "
                f"{type(rotation)}"
            )
    
    def __invert__(
        self,
    ) -> "Rotation":
        return Rotation(
            rotation=~self.quaternion
        )
    
    def __mul__(
        self,
        other: "Rotation",
    ) -> "Rotation":
        return Rotation(
            rotation=self.quaternion * other.quaternion
        )
        
    @property
    def as_tuple(self) -> Tuple[Tuple[float]]:
        return self.matrix.as_tuple
    
    @as_tuple.setter
    def as_tuple(self, matrix: Tuple[Tuple[float]]):
        self.matrix.as_tuple = matrix
        self._update_from_matrix()

    @property
    def as_list(self) -> List[List[float]]:
        return self.matrix.as_list
    
    @as_list.setter
    def as_list(self, matrix: List[List[float]]):
        self.matrix.as_list = matrix
        self._update_from_matrix()

    def interpolated(
        self,
        other: "Rotation",
        factor: float,
    ) -> "Rotation":
        return Rotation(
            rotation=self.quaternion.interpolated(
                other=other.quaternion,
                factor=factor,
            )
        )
    
    def transform_point(
        self,
        point: Union[Point, Translation]
    ) -> None:
        self.matrix.transform_point(point=point)

    def transform_points(
        self,
        points: Union[list, tuple],
    ) -> None:
        self.matrix.transform_points(points=points)

    def transformed_point(
        self,
        point: Union[Point, Translation],
    ) -> Union[Point, Translation]:
        return self.matrix.transformed_point(point=point)
    
    def transformed_points(
        self,
        points: Union[list, tuple],
    ) -> Union[list, tuple]:
        return self.matrix.transformed_points(points=points)
        
    def _update_from_quaternion(self):
        self.matrix = Converter.quaternion_to_matrix(
            quaternion=self.quaternion,
        )
        self.opk_deg = Converter.matrix_to_opk_deg(
            matrix=self.matrix,
        )

    def _update_from_matrix(self):
        self.opk_deg = Converter.matrix_to_opk_deg(
            matrix=self.matrix,
        )
        self.quaternion = Converter.matrix_to_quaternion(
            matrix=self.matrix,
        )

    def _update_from_opk_deg(self):
        self.matrix = Converter.opk_deg_to_matrix(
            opk_deg=self.opk_deg,
        )
        self.quaternion = Converter.matrix_to_quaternion(
            matrix=self.matrix,
        )
        