import arcade, math
from inac8hr.utils import LocationUtil
from inac8hr.levels import Level
from inac8hr.globals import *

VALID_PLACEMENT = 1
INVALID_PLACEMENT = 0

class BaseTool():
    pass

class PlacementAvailabilityTool(BaseTool):
    registered_inputs = [MOUSE_PRESS, MOUSE_MOTION]
    def __init__(self, level: Level):
        self.unit_blueprint = UnitBlueprint(["assets/images/chars/unavail.png", "assets/images/chars/avail.png"])
        self.unit_blueprint.sprite.center_x = 0
        self.unit_blueprint.sprite.center_y = 0
        self.unit_blueprint.sprite.scale = 0.7
        self.level = level

    def update_blueprint_state(self, x, y):
        if self.eval_availability(x, y):
            self.unit_blueprint.change_state(1)
        else:
            self.unit_blueprint.change_state(0)
    
    def eval_availability(self, x, y):
        if self.eval_proximity(x, y):
            r, c = LocationUtil.get_plan_position(x, y)
            r, c = int(round(abs(r),0)), int(round(abs(c),0))
            if self.level.map_plan.is_wall_at((r, c)):
                return True
        else:
            return False

    def eval_proximity(self, x, y):
        r, c = LocationUtil.get_plan_position(x, y)
        if ( 0 <=  abs( c - math.floor(c)) <= 0.1 or 0.92 <=  abs( c - math.floor(c)) < 1) and (0 <= abs( r - math.floor(r)) <= 0.1 or 0.92 <=  abs( r - math.floor(r)) < 1):
            return True #self.unit_blueprint.change_state(1)
        else:
            return False #self.unit_blueprint.change_state(0)

    def dispatch_mouse_motion(self, args: tuple):
        x, y = args
        self.unit_blueprint.sprite.set_position(x, y)
        self.update_blueprint_state(x, y)
        #self.eval_proximity(x, y)

    def dispatch_mouse_press(self, args: tuple):
        x, y = args
        if self.eval_availability(x, y):
            self.unit_blueprint.location = LocationUtil.get_plan_position(x,y, True)
            r, c = self.unit_blueprint.location
            self.level.place_defender(r, c)
    
    def draw(self):
        pass

class UnitBlueprint():
    "Minimum of 2 texture files"
    def __init__(self, texture_files: list):
        self.defender = None
        self.location = 0, 0
        self.sprite = arcade.Sprite()
        for file_name in texture_files:
            self.sprite.append_texture(arcade.load_texture(file_name))
        self.state = INVALID_PLACEMENT
        self.configure_texture()
    
    def configure_texture(self):
        self.sprite.set_texture(self.state)

    def change_state(self, state):
        self.state = state
        self.configure_texture()


class UnitPlacement():

    def check_availability(self):
        pass