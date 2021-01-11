from .objects import Entity
from .map import Wall
from kivy.core.window import Window
from kivy.vector import Vector as vec


class Mob(Entity):
    def __init__(self, pos, game, speed=150):
        super(Mob, self).__init__()
        self.source = "assets/images/enemy/enemy.png"
        self._speed = speed
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.game = game
        self.game.bind(on_frame=self.move_step)

    def stop_callbacks(self):
        self.game.unbind(on_frame=self.move_step)

    def move_step(self, dt):
        step_size = self._speed * dt
        cur_x = self.pos[0]
        cur_y = self.pos[1]
        if "up" in self.game.keys_pressed:
            cur_y += step_size
        if "down" in self.game.keys_pressed:
            cur_y -= step_size
        if "left" in self.game.keys_pressed:
            cur_x -= step_size
        if "right" in self.game.keys_pressed:
            cur_x += step_size
        self.pos = (cur_x, cur_y)


class Player(Entity):
    def __init__(self, game, pos, speed=200):
        super(Player, self).__init__()
        self._speed = speed
        self.pos = vec(pos)
        self.vel = vec(0, 0)
        self.game = game
        self.game.bind(on_frame=self.update)
        self.source = "assets/images/player/digger_front.png"
        self._bullets = set()

    def _make_step(self, dt):
        step_size = self._speed * dt
        self.vel = vec(0, 0)
        if "up" in self.game.keys_pressed:
            self.vel.y = step_size
        elif "down" in self.game.keys_pressed:
            self.vel.y = -step_size
        elif "left" in self.game.keys_pressed:
            self.vel.x = -step_size
        elif "right" in self.game.keys_pressed:
            self.vel.x = +step_size
        else:
            self.vel = vec(0, 0)
        self.pos = self.pos + self.vel

    def stop_callbacks(self):
        self.game.unbind(on_frame=self.update)

    def update(self, widget, dt):
        if "space" in self.game.keys_pressed:
            print("SHOT!!!")
            self.make_shot(Bullet(self, self.pos, self.vel))

        if self.check_collision():
            print("No Collision!!!")
            self._make_step(dt)
        else:
            print("Collision!")

    def check_collision(self):
        # Check for collisions
        print(self.game.colliding_entities(self))
        for e in self.game.colliding_entities(self):
            if isinstance(e, Wall):
                return False
        return True

    def make_shot(self, bullet):
        self._bullets.add(bullet)
        self.game.add_etinity(bullet)

    def remove_bullet(self, bullet):
        self.game.remove_etinity(bullet)
        self._bullets.remove(bullet)


class Bullet(Entity):
    def __init__(self, player, pos, vel, speed=300):
        super(Bullet, self).__init__()
        # self.source = "assets/images/player/bullet/bullet.png"
        self._speed = speed
        self.player = player
        self.pos = pos
        self.vel = vel
        self.player.game.bind(on_frame=self.update)

    def stop_callbacks(self):
        self.player.game.unbind(on_frame=self.update)

    def update(self, widget, dt):
        if self.check_collision():
            self._make_step(dt)

    def _make_step(self, dt):
        step_size = self._speed * dt
        self.vel.x = (self.vel.x + step_size) if self.vel.x != 0 else 0
        self.vel.y = (self.vel.y + step_size) if self.vel.y != 0 else 0
        self.pos += self.vel

    def check_collision(self):
        # Check for collisions

        if self.pos.x > Window.width or self.pos[1] > Window.height:
            self.stop_callbacks()
            self.player.remove_bullet(self)
            return
        for e in self.player.game.colliding_entities(self):
            if isinstance(e, Mob):
                self.stop_callbacks()
                self.player.remove_bullet(self)
                e.stop_callbacks()
                self.player.game.remove_etinity(e)
                return
