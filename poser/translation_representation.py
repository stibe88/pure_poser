from typing import Union
from dataclasses import dataclass

from poser.point_representation import Point


@dataclass
class Translation(Point):
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
    
    def interpolated(
        self,
        other: "Translation",
        factor: float,
    ) -> "Translation":
        return Translation(
            x=self.x * (1.0-factor) + other.x * factor,
            y=self.y * (1.0-factor) + other.y * factor,
            z=self.z * (1.0-factor) + other.z * factor,
        )
        
    def transform_point(
        self,
        point: Union[Point, "Translation"]
    ) -> None:
        if not isinstance(point, (Point, self)):
            raise TypeError(
                "point is neither a Point nor a Translation instance."
            )
        point.as_tuple = self._translate(
            x=point.x,
            y=point.y,
            z=point.z,
            tx=self.x,
            ty=self.y,
            tz=self.z,
        )
    
    def transform_points(
        self,
        points: Union[list, tuple],
    ) -> None:
        (x, y, z,) = self.as_tuple
        for point in points:
            if not isinstance(point, (Point, self)):
                raise TypeError(
                    "point is neither a Point nor a Translation instance."
                )
            point.as_tuple = self._translate(
                x=point.x,
                y=point.y,
                z=point.z,
                tx=x,
                ty=y,
                tz=z,
            )

    def transformed_point(
        self,
        point: Union[Point, "Translation"],
    ) -> Union[Point, "Translation"]:
        if isinstance(point, Point):
            return Point(
                *self._translate(
                    x=point.x,
                    y=point.y,
                    z=point.z,
                    tx=self.x,
                    ty=self.y,
                    tz=self.z,
                )
            )
        elif isinstance(point, Translation):
            return Translation(
                *self._translate(
                    x=point.x,
                    y=point.y,
                    z=point.z,
                    tx=self.x,
                    ty=self.y,
                    tz=self.z,
                )
            )
        else:
            raise TypeError(
                "point is neither a Point nor a Translation instance."
            )

    def transformed_points(
        self,
        points: Union[list, tuple]
    ) -> Union[list, tuple]:
        (x, y, z) = self.as_tuple
        if isinstance(points, tuple):
            return tuple(
                Point(
                    *self._translate(
                        x=point.x,
                        y=point.y,
                        z=point.z,
                        tx=x,
                        ty=y,
                        tz=z,
                    )
                ) if isinstance(point, Point) else
                Translation(
                    *self._translate(
                        x=point.x,
                        y=point.y,
                        z=point.z,
                        tx=x,
                        ty=y,
                        tz=z,
                    )
                )
                for point in points
                if (isinstance(point, Point) or isinstance(point, Translation))
            )
        elif isinstance(points, list):
            return [
                Point(
                    *self._translate(
                        x=point.x,
                        y=point.y,
                        z=point.z,
                        tx=x,
                        ty=y,
                        tz=z,
                    )
                ) if isinstance(point, Point) else
                Translation(
                    *self._translate(
                        x=point.x,
                        y=point.y,
                        z=point.z,
                        tx=x,
                        ty=y,
                        tz=z,
                    )
                )
                for point in points
                if (isinstance(point, Point) or isinstance(point, Translation))
            ]
        
    @staticmethod
    def _translate(
        x: float,
        y: float,
        z: float,
        tx: float,
        ty: float,
        tz: float,
    ) -> (float, float, float):
        return(
            x + tx,
            y + ty,
            z + tz,
        )
        