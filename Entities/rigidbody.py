from libs.vectors import Vector2
from math import pi, atan


def toDegrees(x):
    return int(x * 180 / pi)


def absolute(x):
    return x if x >= 0 else -x


class RigidBody:
    def __init__(self, coords: tuple):
        self.startX = coords[0]
        self.startY = coords[1]
        self.endX = coords[2]
        self.endY = coords[3]
        self.xLength = absolute(self.startX - self.endX)
        self.yLength = absolute(self.startY - self.endY)

    def get_extreme_angles(self):
        rto = self.yLength / self.xLength if self.xLength != 0 else 10000
        return toDegrees(atan(absolute(rto)))

    def check_overlap(self, body) -> bool:
        if not isinstance(body, RigidBody):
            return False

        # return ((self.startX <= body.startX <= self.endX or body.startX <= self.endX <= body.endX) and
        #         body.startY <= self.startY <= body.endY) or \
        #        ((body.startX <= self.startX <= body.endX or self.startX <= body.endX <= self.endX) and
        #         self.startY <= body.startY <= self.endY)

        self_center = Vector2(
            int((self.startX + self.endX) / 2), int((self.startY + self.endY) / 2)
        )
        body_center = Vector2(
            int((body.startX + body.endX) / 2), int((body.startY + body.endY) / 2)
        )
        dist = self_center - body_center
        return (
            absolute(dist.x) < self.xLength + body.xLength
            and absolute(dist.y) < self.yLength + body.yLength
        )

    def get_direction(self, body) -> str:
        if not isinstance(body, RigidBody):
            return ""

        self_center = Vector2(
            int((self.startX + self.endX) / 2), int((self.startY + self.endY) / 2)
        )
        body_center = Vector2(
            int((body.startX + body.endX) / 2), int((body.startY + body.endY) / 2)
        )
        # if body_center.x > self_center.x and self.startY <= body_center.y <= self.endY:
        #     return "r"
        # elif body_center.y < self_center.y and self.startX <= body_center.x <= self.endX:
        #     return "u"
        # elif body_center.x < self_center.x and self.startY <= body_center.y <= self.endY:
        #     return "l"
        # elif body_center.y > self_center.y and self.startX <= body_center.x <= self.endX:
        #     return "d"
        dist = body_center - self_center
        ang = dist.angle
        e_ang = self.get_extreme_angles()
        if -e_ang <= ang <= e_ang:
            return "r"
        elif e_ang - 180 <= ang < 180 or -180 < ang <= 180 - e_ang:
            return "l"
        elif e_ang <= ang <= 180 - e_ang:
            return "d"
        else:
            return "u"
