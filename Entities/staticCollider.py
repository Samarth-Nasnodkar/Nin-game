from Entities.rigidbody import RigidBody
from Entities.entity import Entity


class staticCollider:
    def __init__(self, body: RigidBody) -> None:
        self.rigidBody = body

    def on_collision(self, collider):
        if not isinstance(collider, staticCollider) and not isinstance(
            collider, Entity
        ):
            return
        overlap = self.rigidBody.check_overlap(collider.rigidBody)
        if not overlap:
            return

        _dir = collider.rigidBody.get_direction(self.rigidBody)
        print(_dir)
        if _dir == "l":
            collider.rigidBody.endX = self.rigidBody.startX
            collider.rigidBody.startX = (
                collider.rigidBody.endX - collider.rigidBody.xLength
            )
        elif _dir == "r":
            collider.rigidBody.startX = self.rigidBody.endX
            collider.rigidBody.endX = (
                collider.rigidBody.startX + collider.rigidBody.xLength
            )
        elif _dir == "u":
            collider.rigidBody.endY = self.rigidBody.startY
            collider.rigidBody.startY = (
                collider.rigidBody.endY - collider.rigidBody.yLength
            )
        elif _dir == "d":
            collider.rigidBody.startY = self.rigidBody.endY
            collider.rigidBody.endY = (
                collider.rigidBody.startY + collider.rigidBody.yLength
            )
