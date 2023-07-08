import math
from typing import Tuple


class Rotation(object):

    def __init__(
        self, 
        w: float = 1.0,
        x: float = 0.0, 
        y: float = 0.0,
        z: float = 0.0,
    ) -> None:
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self._normalize()

    def __mul__(
        self, 
        other: "Rotation"
    ) -> "Rotation":
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        return Rotation(
            w=w1*w2 - x1*x2 - y1*y2 - z1*z2,
            x=w1*x2 + x1*w2 + y1*z2 - z1*y2,
            y=w1*y2 - x1*z2 + y1*w2 + z1*x2,
            z=w1*z2 + x1*y2 - y1*x2 + z1*w2, 
        )
    
    def __abs__(self) -> float:
        w, x, y, z = self.w, self.x, self.y, self.z
        return (w*w + x*x + y*y + z*z)**0.5
    
    def __invert__(self) -> "Rotation":
        return Rotation(
            w=self.w,
            x=-self.x,
            y=-self.y,
            z=-self.z,
        )
    
    @property
    def matrix(self) -> Tuple[Tuple[float]]:
        w, x, y, z = self.w, self.x, self.y, self.z
        xx2, yy2, zz2 = x*x*2, y*y*2, z*z*2
        wx2, wy2, wz2 = w*x*2, w*y*2, w*z*2
        xy2, xz2, yz2 = x*y*2, x*z*2, y*z*2
        return (
            (1.0-yy2-zz2, xy2-wz2, xz2+wy2,),
            (xy2+wz2, 1.0-xx2-zz2, yz2-wx2,),
            (xz2-wy2, yz2+wx2, 1.0-xx2-yy2,),
        )
    
    @matrix.setter
    def matrix(
        self, 
        matrix: Tuple[Tuple[float]]
    ) -> None:
        m = matrix
        t = m[0][0] + m[1][1] + m[2][2]
        if t > 0.0:
            d = (t + 1)**0.5
            
            self.w = 0.5 * d
            f = 0.5 / d
            self.x = (m[2][1] - m[1][2]) * f
            self.y = (m[0][2] - m[2][0]) * f
            self.z = (m[1][0] - m[0][1]) * f
            return
        
        # estimate indices
        i = 0
        if (m[1][1] > m[0][0]):
            i = 1
        if (m[2][2] > m[i][i]):
            i = 2
        j = (i + 1) % 3
        k = (j + 1) % 3
        
        d = (m[i][i] - m[j][j] - m[k][k] + 1)**0.5
        q = [0.0, 0.0, 0.0, 0.0]
        
        q[i] = 0.5 * d
        f = 0.5 / d
        self.w = (m[k][j] - m[j][k]) * f
        q[j] = (m[j][i] + m[i][j]) * f
        q[k] = (m[k][i] + m[i][k]) * f

        self.x = q[0]
        self.y = q[1]
        self.z = q[2]

    def interpolate(
        self,
        other: "Rotation",
        factor: float,
    ) -> "Rotation":
        w1, x1, y1, z1 = self.w, self.x, self.y, self.z
        w2, x2, y2, z2 = other.w, other.x, other.y, other.z
        
        omega = math.acos(w1*w2 + x1*x2 + y1*y2 + z1*z2)
        sin_omega = math.sin(omega)
        
        f1 = math.sin((1 - factor)*omega) / sin_omega
        f2 = math.sin(factor*omega) / sin_omega
        
        return Rotation(
            w=f1*w1 + f2*w2,
            x=f1*x1 + f2*x2,
            y=f1*y1 + f2*y2,
            z=f1*z1 + f2*z2,
        )
    
    def _normalize(self) -> None:
        norm = abs(self)
        if norm == 1.0:
            return
        self.w /= norm
        self.x /= norm
        self.y /= norm
        self.z /= norm
        