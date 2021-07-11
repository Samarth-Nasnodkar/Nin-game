from libs.vectors import Vector2, toDegrees
from math import atan


class RigidBody:
    def __init__(self, coords: tuple, tag=None):
        self.tag = None
        self.startX = coords[0]
        self.startY = coords[1]
        self.endX = coords[2]
        self.endY = coords[3]
        self.xLength = abs(self.startX - self.endX)
        self.yLength = abs(self.startY - self.endY)

    def get_extreme_angles(self):
        rto = self.yLength / self.xLength if self.xLength != 0 else 10000
        return toDegrees(atan(abs(rto)))

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
        return abs(dist.x) < self.xLength + body.xLength and abs(dist.y) < self.yLength + body.yLength

    def check_static_overlap(self, body) -> bool:
        if not isinstance(body, RigidBody):
            return False

        self_center = Vector2(
            int((self.startX + self.endX) / 2), int((self.startY + self.endY) / 2)
        )
        body_center = Vector2(
            int((body.startX + body.endX) / 2), int((body.startY + body.endY) / 2)
        )
        dist = self_center - body_center
        return dist.x ** 2 + dist.y ** 2 < self.xLength ** 2 + self.yLength ** 2 and \
               dist.x ** 2 + dist.y ** 2 < body.xLength ** 2 + body.yLength ** 2

    def move_to(self, position: tuple):
        self.startX = position[0]
        self.startY = position[1]
        self.endX = self.startX + self.xLength
        self.endY = self.startY + self.yLength

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
        print(ang)
        if -e_ang <= ang <= e_ang:
            return "r"
        elif e_ang <= ang <= 180 - e_ang:
            return "u"
        elif -e_ang >= ang >= e_ang - 180:
            return "d"
        else:
            return "l"
