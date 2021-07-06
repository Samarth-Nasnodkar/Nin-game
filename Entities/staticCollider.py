from Entities.rigidbody import RigidBody
from Entities.entity import Entity


class StaticCollider:
    def __init__(self, body: RigidBody) -> None:
        self.rigidBody = body

    def move_to(self, position: tuple):
        self.rigidBody.move_to(position)

    def on_collision(self, collider):
        if not isinstance(collider, StaticCollider) and not isinstance(collider, Entity):
            return
        overlap = self.rigidBody.check_static_overlap(collider.rigidBody)
        if not overlap:
            return

        _dir = self.rigidBody.get_direction(collider.rigidBody)
        print(_dir)
        buffer = 5
        if _dir == "l":
            # collider.rigidBody.endX = self.rigidBody.startX
            # collider.rigidBody.startX = (
            #     collider.rigidBody.endX - collider.rigidBody.xLength
            # )
            collider.move_to((self.rigidBody.startX - collider.rigidBody.xLength - buffer, collider.rigidBody.startY))

        elif _dir == "r":
            # collider.rigidBody.startX = self.rigidBody.endX
            # collider.rigidBody.endX = (
            #     collider.rigidBody.startX + collider.rigidBody.xLength
            # )
            collider.move_to((self.rigidBody.endX + buffer, collider.rigidBody.startY))
        elif _dir == "u":
            # collider.rigidBody.endY = self.rigidBody.startY
            # collider.rigidBody.startY = (
            #     collider.rigidBody.endY - collider.rigidBody.yLength
            # )
            collider.move_to((collider.rigidBody.startX, self.rigidBody.startY - collider.rigidBody.yLength - buffer))
        elif _dir == "d":
            # collider.rigidBody.startY = self.rigidBody.endY
            # collider.rigidBody.endY = (
            #     collider.rigidBody.startY + collider.rigidBody.yLength
            # )
            collider.move_to((collider.rigidBody.startX, self.rigidBody.endY + buffer))
