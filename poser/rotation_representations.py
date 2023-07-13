from typing import Tuple, List
from dataclasses import dataclass
import math


@dataclass
class RotationMatrix(object):
    r11: float = 1.0
    r12: float = 0.0
    r13: float = 0.0
    r21: float = 0.0
    r22: float = 1.0
    r23: float = 0.0
    r31: float = 0.0
    r32: float = 0.0
    r33: float = 1.0

    def __post_init__(self):
        if not isinstance(self.r11, float):
            self.r11 = float(self.r11)
        if not isinstance(self.r12, float):
            self.r12 = float(self.r12)
        if not isinstance(self.r13, float):
            self.r13 = float(self.r13)
        if not isinstance(self.r21, float):
            self.r21 = float(self.r21)
        if not isinstance(self.r22, float):
            self.r22 = float(self.r22)
        if not isinstance(self.r23, float):
            self.r23 = float(self.r23)
        if not isinstance(self.r31, float):
            self.r31 = float(self.r31)
        if not isinstance(self.r32, float):
            self.r32 = float(self.r32)
        if not isinstance(self.r33, float):
            self.r33 = float(self.r33) 
    
    def __invert__(
        self,
    ) -> "RotationMatrix":
        return RotationMatrix(
            r11=self.r11,
            r12=self.r21,
            r13=self.r31,
            r21=self.r12,
            r22=self.r22,
            r23=self.r32,
            r31=self.r13,
            r32=self.r23,
            r33=self.r33,
        )

    def __mul__(
        self,
        other: "RotationMatrix"
    ) -> "RotationMatrix":
        (
            (a11, a12, a13,),
            (a21, a22, a23,),
            (a31, a32, a33,),
        ) = self.as_tuple
        (
            (b11, b12, b13,),
            (b21, b22, b23,),
            (b31, b32, b33,),
        ) = other.as_tuple
        return RotationMatrix(
            r11=a11*b11 + a12*b21 + a13*b31,
            r12=a11*b12 + a12*b22 + a13*b32,
            r13=a11*b13 + a12*b23 + a13*b33,
            r21=a21*b11 + a22*b21 + a23*b31,
            r22=a21*b12 + a22*b22 + a23*b32,
            r23=a21*b13 + a22*b23 + a23*b33,
            r31=a31*b11 + a32*b21 + a33*b31,
            r32=a31*b12 + a32*b22 + a33*b32,
            r33=a31*b13 + a32*b23 + a33*b33,
        )
    
    @property
    def as_tuple(self) -> Tuple[Tuple[float]]:
        return (
            (self.r11, self.r12, self.r13,),
            (self.r21, self.r22, self.r23,),
            (self.r31, self.r32, self.r33,),
        )
    
    @as_tuple.setter
    def as_tuple(
        self,
        matrix: Tuple[Tuple[float]]
    ) -> None:
        self.r11 = matrix[0][0]
        self.r12 = matrix[0][1]
        self.r13 = matrix[0][2]
        self.r21 = matrix[1][0]
        self.r22 = matrix[1][1]
        self.r23 = matrix[1][2]
        self.r31 = matrix[2][0]
        self.r32 = matrix[2][1]
        self.r33 = matrix[2][2]

    @property
    def as_list(self) -> List[List[float]]:
        return [
            [self.r11, self.r12, self.r13,],
            [self.r21, self.r22, self.r23,],
            [self.r31, self.r32, self.r33,],
        ]
    
    @as_list.setter
    def as_list(
        self,
        matrix: List[List[float]]
    ) -> None:
        self.r11 = matrix[0][0]
        self.r12 = matrix[0][1]
        self.r13 = matrix[0][2]
        self.r21 = matrix[1][0]
        self.r22 = matrix[1][1]
        self.r23 = matrix[1][2]
        self.r31 = matrix[2][0]
        self.r32 = matrix[2][1]
        self.r33 = matrix[2][2]


@dataclass
class RotationQuaternion(object):
    w: float = 1.0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __post_init__(self):
        if not isinstance(self.w, float):
            self.w = float(self.w)
        if not isinstance(self.x, float):
            self.x = float(self.x)
        if not isinstance(self.y, float):
            self.y = float(self.y)
        if not isinstance(self.z, float):
            self.z = float(self.z)

    def __abs__(self) -> float:
        w, x, y, z = self.w, self.x, self.y, self.z
        return (w*w + x*x + y*y + z*z)**0.5
    
    def __invert__(self) -> "RotationQuaternion":
        self.normalize()
        return RotationQuaternion(
            w=self.w,
            x=-self.x,
            y=-self.y,
            z=-self.z,
        )
    
    def __mul__(
        self, 
        other: "RotationQuaternion",
    ) -> "RotationQuaternion":
        self.normalize()
        other.normalize()
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        return RotationQuaternion(
            w=w1*w2 - x1*x2 - y1*y2 - z1*z2,
            x=w1*x2 + x1*w2 + y1*z2 - z1*y2,
            y=w1*y2 - x1*z2 + y1*w2 + z1*x2,
            z=w1*z2 + x1*y2 - y1*x2 + z1*w2, 
        )
    
    def normalize(self) -> None:
        norm = abs(self)
        if norm == 1.0:
            return
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm

    def normalized(self) -> "RotationQuaternion":
        norm = abs(self)
        if norm == 1.0:
            return self
        return RotationQuaternion(
            w=self.w/norm,
            x=self.x/norm,
            y=self.y/norm,
            z=self.z/norm,
        )
    
    def interpolated(
        self,
        other: "RotationQuaternion",
        factor: float,
    ) -> "RotationQuaternion":
        self.normalize()
        other.normalize()
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        
        omega = math.acos(w1*w2 + x1*x2 + y1*y2 + z1*z2)
        sin_omega = math.sin(omega)
        
        f1 = math.sin((1 - factor)*omega) / sin_omega
        f2 = math.sin(factor*omega) / sin_omega
        
        return RotationQuaternion(
            w=f1*w1 + f2*w2,
            x=f1*x1 + f2*x2,
            y=f1*y1 + f2*y2,
            z=f1*z1 + f2*z2,
        ) 


@dataclass
class RotationOPKDeg(object):
    omega: float = 0.0
    phi: float = 0.0
    kappa: float = 0.0

    def __post_init__(self):
        if not isinstance(self.omega, float):
            self.omega = float(self.omega)
        if not isinstance(self.phi, float):
            self.phi = float(self.phi)
        if not isinstance(self.kappa, float):
            self.kappa = float(self.kappa)
