from rigidbody import RigidBody
from libs.vectors import Vector2
import pygame


class Entity:
    def __init__(self, position: Vector2, velocity: Vector2, sprite, rigidbody: RigidBody = None, mass=1, restitution=1,
                 dynamic=True, gravity=Vector2(0, 60)):
        self.position = position
        self.velocity = velocity
        self.mass = mass
        self.e = restitution
        self.rigidBody = rigidbody
        self.dynamic = dynamic
        self.gravity = gravity
        self.sprite = sprite
        self.rigidBodyEnabled = bool(self.rigidBody)

    def move(self):
        if not self.dynamic:
            self.velocity += self.gravity
        self.position += self.velocity

    def resize(self, size: tuple = None):
        if size is None:
            return

        self.sprite = pygame.transform.scale(self.sprite, size)

    def render(self, surface: pygame.surface):
        surface.blit(self.sprite, self.position.toTuple)

    def on_collision(self, collision):
        if not isinstance(collision, Entity):
            return

        if collision.rigidBodyEnabled:
            overlap = self.rigidBody.check_overlap(collision.rigidBody)
            if not overlap:
                return

            # direction = self.rigidBody.get_direction(collision.rigidBody)
            cached_collision_velocity = collision.velocity
            collision.velocity = (collision.velocity * collision.mass - self.mass *
                                  (self.velocity * (self.e - 1) - collision.velocity * self.e)) / \
                                 (collision.mass + self.mass)
            self.velocity = (self.velocity - cached_collision_velocity) * self.e + collision.velocity
