from libs.vectors import Vector2


class RigidBody:
    def __init__(self, coords: tuple):
        self.startX = coords[0]
        self.startY = coords[1]
        self.endX = coords[2]
        self.endY = coords[3]

    def check_overlap(self, body) -> bool:
        if not isinstance(body, RigidBody):
            return False

        return ((self.startX <= body.startX <= self.endX or body.startX <= self.endX <= body.endX) and
                body.startY <= self.startY <= body.endY) or \
               ((body.startX <= self.startX <= body.endX or self.startX <= body.endX <= self.endX) and
                self.startY <= body.startY <= self.endY)

    def get_direction(self, body) -> str:
        if not isinstance(body, RigidBody):
            return ""

        self_center = Vector2(int((self.startX + self.endX) / 2), int((self.startY + self.endY) / 2))
        body_center = Vector2(int((body.startX + body.endX) / 2), int((body.startY + body.endY) / 2))
        if body_center.x > self_center.x and self.startY <= body_center.y <= self.endY:
            return "r"
        elif body_center.y < self_center.y and self.startX <= body_center.x <= self.endX:
            return "u"
        elif body_center.x < self_center.x and self.startY <= body_center.y <= self.endY:
            return "l"
        elif body_center.y > self_center.y and self.startX <= body_center.x <= self.endX:
            return "d"
