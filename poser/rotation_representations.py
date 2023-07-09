from typing import Tuple
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

    @property
    def matrix(self) -> Tuple[Tuple[float]]:
        return (
            (self.r11, self.r12, self.r13,),
            (self.r21, self.r22, self.r23,),
            (self.r31, self.r32, self.r33,),
        )
    
    @matrix.setter
    def matrix(
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

    def __mul__(
        self,
        other: "RotationMatrix"
    ) -> "RotationMatrix":
        m1 = self
        m2 = other
        return RotationMatrix(
            r11=m1.r11*m2.r11 + m1.r12*m2.r21 + m1.r13*m2.r31,
            r12=m1.r11*m2.r12 + m1.r12*m2.r22 + m1.r13*m2.r32,
            r13=m1.r11*m2.r13 + m1.r12*m2.r23 + m1.r13*m2.r33,
            r21=m1.r21*m2.r11 + m1.r22*m2.r21 + m1.r23*m2.r31,
            r22=m1.r21*m2.r12 + m1.r22*m2.r22 + m1.r23*m2.r32,
            r23=m1.r21*m2.r13 + m1.r22*m2.r23 + m1.r23*m2.r33,
            r31=m1.r31*m2.r11 + m1.r32*m2.r21 + m1.r33*m2.r31,
            r32=m1.r31*m2.r12 + m1.r32*m2.r22 + m1.r33*m2.r32,
            r33=m1.r31*m2.r13 + m1.r32*m2.r23 + m1.r33*m2.r33,
        )
    
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


@dataclass
class RotationQuaternion(object):
    w: float = 1.0
    x: float = 0.0
    y: float = 0.0
    z: float = 0.0

    def __abs__(self) -> float:
        w, x, y, z = self.w, self.x, self.y, self.z
        return (w*w + x*x + y*y + z*z)**0.5
    
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
    
    def __invert__(self) -> "RotationQuaternion":
        self.normalize()
        return RotationQuaternion(
            w=self.w,
            x=-self.x,
            y=-self.y,
            z=-self.z,
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
