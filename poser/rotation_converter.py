import math

import poser

class RotationConverter(object):
    @classmethod
    def matrix_to_opk_deg(
        matrix: "poser.RotationMatrix" 
    ) -> "poser.RotationOPKDeg":
        m = matrix
        phi = math.atan2(m.r13, (m.r32**2 + m.r33**2)**0.5)

        if math.cos(phi) != 0.0:
            return poser.RotationOPKDeg(
                omega=math.degrees(math.atan2(-m.r23, m.r33)),
                phi=math.degrees(phi),
                kappa=math.degrees(math.atan2(-m.r12, m.r11))
            )
        return poser.RotationOPKDeg(
            omega=0.0,
            phi=math.degrees(phi),
            kappa=math.degrees(
                math.atan2(m.r32, m.r22) if phi == math.pi*0.5
                else -math.atan2(m.r32, m.r22)
            )
        )
    
    @classmethod
    def opk_deg_to_matrix(
        opk_deg: "poser.RotationOPKDeg",
    ) -> "poser.RotationMatrix":
        so, sp, sk = (
            math.sin(math.radians(a))
            for a in (opk_deg.omega, opk_deg.phi, opk_deg.kappa)
        )
        co, cp, ck = (
            math.cos(math.radians(a))
            for a in (opk_deg.omega, opk_deg.phi, opk_deg.kappa)
        )
        return poser.RotationMatrix(
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
    
    @classmethod
    def matrix_to_quaternion(
        matrix: "poser.RotationMatrix"
    ) -> "poser.RotationQuaternion":
        m = matrix.matrix
        t = m[0][0] + m[1][1] + m[2][2]
        if t > 0.0:
            d = (t + 1)**0.5
            f = 0.5 / d
            return poser.RotationQuaternion(
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

        return poser.RotationQuaternion(
            w=q[3], x=q[0], y=q[1], z=q[2],
        )
    
    @classmethod
    def quaternion_to_matrix(
        quaternion: "poser.RotationQuaternion"
    ) -> "poser.RotationMatrix":
        q = quaternion.normalized()
        wx2, wy2, wz2 = q.w*q.x*2, q.w*q.y*2, q.w*q.z*2
        xx2, xy2, xz2 = q.x*q.x*2, q.x*q.y*2, q.x*q.z*2
        yy2, yz2, zz2 = q.y*q.y*2, q.y*q.z*2, q.z*q.z*2
        return poser.RotationMatrix(
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