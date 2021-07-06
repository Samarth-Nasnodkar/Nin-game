from Entities.rigidbody import RigidBody
from libs.vectors import Vector2
import pygame


class Entity:
    def __init__(
            self,
            position: Vector2,
            velocity: Vector2,
            sprites: list,
            rigidbody: RigidBody = None,
            mass=1,
            restitution=1,
            dynamic=True,
            gravity=Vector2(0, 60),
            collisionFree=False,
            animated=False,
            frameDifference=0
    ):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.e = restitution
        self.rigidBody = rigidbody
        self.dynamic = dynamic
        self.gravity = gravity
        self.sprites = sprites
        self.collisionFree = collisionFree
        self.animated = animated
        self.fD = frameDifference
        self.fC = 0
        self.animCounter = 0
        self.rigidBodyEnabled = bool(self.rigidBody)

    def move(self, backwards=False):
        if not self.dynamic:
            self.velocity += self.gravity
        if not backwards:
            self.position += self.velocity
            self.rigidBody.startX += self.velocity.x
            self.rigidBody.endX += self.velocity.x
            self.rigidBody.startY += self.velocity.y
            self.rigidBody.endY += self.velocity.y
        else:
            self.position -= self.velocity
            self.rigidBody.startX -= self.velocity.x
            self.rigidBody.endX -= self.velocity.x
            self.rigidBody.startY -= self.velocity.y
            self.rigidBody.endY -= self.velocity.y

    def resize(self, size: tuple = None):
        if size is None:
            return
        for i in range(len(self.sprites)):
            self.sprites[i] = pygame.transform.scale(self.sprites[i], size)

    def move_to(self, position: tuple):
        self.position.x = position[0]
        self.position.y = position[1]
        self.rigidBody.move_to(position)

    def render(self, surface: pygame.surface):
        if not self.animated:
            surface.blit(self.sprites[0], self.position.toTuple)
        else:
            surface.blit(self.sprites[self.animCounter], self.position.toTuple)
            if self.fC >= self.fD:
                self.animCounter += 1
                self.fC = 0
            else:
                self.fC += 1
            if self.animCounter >= len(self.sprites):
                self.animCounter = 0

    def on_collision(self, collision):
        if not isinstance(collision, Entity):
            return

        if collision.rigidBodyEnabled:
            overlap = self.rigidBody.check_overlap(collision.rigidBody)
            if not overlap:
                return

            # direction = self.rigidBody.get_direction(collision.rigidBody)
            cached_collision_velocity = collision.velocity
            if not self.collisionFree:
                collision.velocity = (collision.velocity * collision.mass - self.mass * (
                        self.velocity * (self.e - 1) - collision.velocity * self.e)) / (collision.mass + self.mass)
                self.velocity = (self.velocity - cached_collision_velocity) * self.e + collision.velocity
            else:
                direction = self.rigidBody.get_direction(collision.rigidBody)
                if direction in ["u", "d"]:
                    collision.velocity.y = int(self.e * -1 * collision.velocity.y)
                elif direction in ["r", "l"]:
                    collision.velocity.x = int(self.e * -1 * collision.velocity.x)
