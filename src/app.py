import os
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
from kivy.uix.label import CoreLabel
from src.map import Map
from src.objects import Player, Wall
import src.settings as settings


class GameWidget(Widget):
    def __init__(self, **kwargs):
        super(GameWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)
        self._score_label = CoreLabel(text="Score: 0")
        self._score_label.refresh()
        self._score = 0
        self._entities = set()
        self._tilesize = settings.TILESIZE
        self.game_over = False
        self.keys_pressed = set()
        self.register_event_type("on_frame")
        self.map = Map(os.path.join(settings.MAPS_DIR, "map2.txt"), 50)
        self.map_set = set()

        with self.canvas:
            self._load_data()

        Clock.schedule_interval(self._on_frame, 0)
        # self.sound = SoundLoader.load("music.wav")
        # self.sound.play()

    def _on_frame(self, dt):
        self.dispatch("on_frame", dt)

    def on_frame(self, dt):
        pass

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        text = keycode[1]
        self.keys_pressed.add(text)

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keys_pressed:
            self.keys_pressed.remove(text)

    def _load_data(self):
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == "1":
                    self.add_entity(Wall((col * self._tilesize, row * self._tilesize)))
                    print(self._entities)
                if tile.lower() == "p":
                    self.player = Player(self, pos=(col * 50, row * 50))
                    self.add_entity(self.player)

        self._score_instruction = Rectangle(
            texture=self._score_label.texture,
            pos=(20, Window.height - 30),
            size=self._score_label.texture.size,
        )

    def add_entity(self, entity):
        self._entities.add(entity)
        self.canvas.add(entity._instruction)

    def remove_entity(self, entity):
        if entity in self._enemies:
            self._entities.remove(entity)
            self.canvas.remove(entity._instruction)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        self._score = value
        self._score_label.text = f"Score: {self._score}"
        self._score_instruction.texture = self._score_label.texture
        self._score_instruction.size = self._score_label.texture.size

    # def move_step(self, dt):
    #     step_size = 100 * dt
    #     cur_x = self.player.pos[0]
    #     cur_y = self.player.pos[1]
    #     if "up" in self.keys_pressed:
    #         cur_y += step_size
    #     if "down" in self.keys_pressed:
    #         cur_y -= step_size
    #     if "left" in self.keys_pressed:
    #         cur_x -= step_size
    #     if "right" in self.keys_pressed:
    #         cur_x += step_size
    #     self.player.pos = (cur_x, cur_y)

    @staticmethod
    def collides(e1, e2):
        r1x = e1.pos[0]
        r1y = e1.pos[1]
        r2x = e2.pos[0]
        r2y = e2.pos[1]
        r1w = e1.size[0]
        r1h = e1.size[1]
        r2w = e2.size[0]
        r2h = e2.size[1]

        if r1x < r2x + r2w and r1x + r1w > r2x and r1y < r2y + r2h and r1y + r1h > r2y:
            return True
        else:
            return False

    def colliding_entities(self, entity):
        result = set()
        for e in self._entities:
            if self.collides(e, entity):
                result.add(e)
        return result


game = GameWidget()


class GameApp(App):
    def build(self):
        return game


def main():
    GameApp().run()


if __name__ == "__main__":
    main()
