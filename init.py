from drawer import LevelDrawer
from manager import GameManager
import arcade

GAME_TITLE = 'Insom8ia'
SCREEN_WIDTH = 800#18*40
SCREEN_HEIGHT = 600#12*40

class InsomniaGame(arcade.Window):
    def __init__(self, width, height, title, fullscreen=True):
        super().__init__(width, height, title, fullscreen)
        self.manager = GameManager(resolution=(width,height))
        self.manager.load_sprites()
        self.manager.fullscreen = fullscreen

    def on_draw(self):
        #arcade.set_background_color(arcade.color.WHEAT)    
        arcade.start_render()
        self.manager.draw()

    def on_resize(self, width: float, height: float):
        if width >= 1920 or width == 800:
            super().on_resize(width, height)
            self.manager.reset_scaling(width, height)
            self.manager.load_sprites()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.F11:
            self.manager.fullscreen = not self.manager.fullscreen
            self.set_fullscreen(self.manager.fullscreen)
        self.manager.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.manager.on_key_release(key, modifiers)
    
    def on_mouse_motion(self, x, y, dx, dy):
        self.manager.on_mouse_motion(x, y, dx, dy)

    def update(self, delta):
        self.manager.update(delta)

if __name__ == '__main__':
    game = InsomniaGame(SCREEN_WIDTH, SCREEN_HEIGHT, GAME_TITLE)
    arcade.run()

