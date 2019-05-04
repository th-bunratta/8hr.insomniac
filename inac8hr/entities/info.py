import arcade
from inac8hr.gui import PaneTile, Point
from i18n.loc import LocalizedText
from inac8hr.globals import GAME_PREFS

VALID_PLACEMENT = 1
INVALID_PLACEMENT = 0


class UnitInfo:
    """
        Contains each Defender unit information
        (e.g. coverage radius, sprite assets, description)\n
        Also serves as a model of a Defender
    """
    def __init__(self, loc_name):
        self.unit_name = loc_name
        self.view_image = None
        self.strength = 1
        self.coverage_radius = 1
        self.descriptor = ""
        self.blueprint = None
        self.abilities = None
        self.thumbnail = arcade.load_texture("assets/images/chars/avail.png")


class PaperShredderUnitInfo(UnitInfo):
    def __init__(self):
        super().__init__(LocalizedText("Units/Def/PPS/Name"))
        self.strength = 1
        self.coverage_radius = 1
        self.description = LocalizedText("Units/Def/PPS/Desc")
        self.blueprint = UnitBlueprint(["assets/images/chars/unavail.png", "assets/images/chars/avail.png"], scaling=GAME_PREFS.scaling)
        self.abilities = None


class CalculatorUnitInfo(UnitInfo):
    def __init__(self):
        super().__init__(LocalizedText("Units/Def/Calc/Name"))
        self.strength = 1
        self.coverage_radius = 1
        self.description = LocalizedText("Units/Def/Calc/Desc")
        self.blueprint = UnitBlueprint(["assets/images/chars/avail.png", "assets/images/chars/unavail.png"], scaling=GAME_PREFS.scaling)
        self.abilities = None


class UnitBlueprint():
    "Minimum of 2 texture files"
    def __init__(self, texture_files: list, scaling=1, initial_loc=(0,0)):
        self.defender = None
        self.sprite = arcade.Sprite()
        self.texture_files = texture_files
        for file_name in texture_files:
            self.sprite.append_texture(arcade.load_texture(file_name))
        self.state = INVALID_PLACEMENT
        self.configure_texture()
        self.position = initial_loc

    def set_position(self, value):
        self.sprite.set_position(*value)

    def get_position(self):
        return self.sprite.position

    position = property(get_position, set_position)

    def rescale(self):
        self.configure_texture()

    def configure_texture(self):
        self.sprite.scale = GAME_PREFS.scaling
        self.sprite.set_texture(self.state)

    def change_state(self, state):
        self.state = state
        self.configure_texture()


class In8acUnitInfo:
    """
        Unit information instance of Insomni8 Game
    """
    INFO_LIST = [
        PaperShredderUnitInfo(),
        CalculatorUnitInfo()
    ]

    @classmethod
    def get_all(cls):
        return cls.INFO_LIST

    @classmethod
    def get_all_as_pane_tile(cls):
        return [PaneTile(Point(0, 0), model=i) for i in In8acUnitInfo.INFO_LIST]
