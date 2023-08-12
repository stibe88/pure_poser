import math

from . import representations


Matrix = representations.Matrix
Quaternion = representations.Quaternion
OPKDeg = representations.OPKDeg


class Converter(object):
    @staticmethod
    def matrix_to_opk_deg(
        matrix: Matrix
    ) -> OPKDeg:
        m = matrix
        phi = math.atan2(m.r13, (m.r23**2 + m.r33**2)**0.5)

        if not -1e-10 < math.cos(phi) < 1e-10:
            return OPKDeg(
                omega=math.degrees(math.atan2(-m.r23, m.r33)),
                phi=math.degrees(phi),
                kappa=math.degrees(math.atan2(-m.r12, m.r11))
            )
        return OPKDeg(
            omega=0.0,
            phi=math.degrees(phi),
            kappa=math.degrees(
                math.atan2(m.r32, m.r22) if phi == math.pi*0.5
                else math.atan2(-m.r32, m.r22)
            )
        )
    
    @staticmethod
    def opk_deg_to_matrix(
        opk_deg: OPKDeg,
    ) -> Matrix:
        so, sp, sk = (
            math.sin(math.radians(a))
            for a in (opk_deg.omega, opk_deg.phi, opk_deg.kappa)
        )
        co, cp, ck = (
            math.cos(math.radians(a))
            for a in (opk_deg.omega, opk_deg.phi, opk_deg.kappa)
        )
        return Matrix(
            r11=cp*ck,
            r12=-cp*sk,
            r13=sp,
            r21=co*sk + so*sp*ck,
            r22=co*ck - so*sp*sk,
            r23=-so*cp,
            r31=so*sk - co*sp*ck,
            r32=so*ck + co*sp*sk,
            r33=co*cp
        )
    
    @staticmethod
    def matrix_to_quaternion(
        matrix: Matrix
    ) -> Quaternion:
        m = matrix.as_tuple
        t = m[0][0] + m[1][1] + m[2][2]
        if t > 0.0:
            d = (t + 1)**0.5
            f = 0.5 / d
            return Quaternion(
                w=0.5 * d,
                x=(m[2][1] - m[1][2]) * f,
                y=(m[0][2] - m[2][0]) * f,
                z=(m[1][0] - m[0][1]) * f,
            )
        
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
        q[3] = (m[k][j] - m[j][k]) * f
        q[j] = (m[j][i] + m[i][j]) * f
        q[k] = (m[k][i] + m[i][k]) * f

        return Quaternion(
            w=q[3], x=q[0], y=q[1], z=q[2],
        )
    
    @staticmethod
    def quaternion_to_matrix(
        quaternion: Quaternion
    ) -> Matrix:
        q = quaternion.normalized()
        w, x, y, z = q.w, q.x, q.y, q.z
        wx2, wy2, wz2 = w*x*2, w*y*2, w*z*2
        xx2, xy2, xz2 = x*x*2, x*y*2, x*z*2
        yy2, yz2, zz2 = y*y*2, y*z*2, z*z*2
        return Matrix(
            r11=1 - yy2 - zz2,
            r12=xy2 - wz2,
            r13=xz2 + wy2,
            r21=xy2 + wz2,
            r22=1 - xx2 - zz2,
            r23=yz2 - wx2,
            r31=xz2 - wy2,
            r32=yz2 + wy2,
            r33=1 - xx2 - yy2,
        )
