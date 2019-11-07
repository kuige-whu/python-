class Settings():
    def __init__(self):
        """初始化游戏的设置"""

    # 屏幕设置
        self.screen_width = 900
        self.screen_height = 650

        self.bg_color = (220, 220, 220)
     #   self.ship_speed_factor = 0.8

     #   self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10
     #   self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 5
        # fleet_direction为1表示向右移，为-1表示向左移
      #  self.fleet_direction = 1
        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        #self.alien_points = 50


    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""

        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.2
        # fleet_direction为1表示向右；为-1表示向左
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

