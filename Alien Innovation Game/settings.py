class Settings():
    def __init__(self, width = 1450, height = 750):
        self.screen_width = width
        self.screen_height = height
        self.bg_color = (230, 230, 230)

        self.ship_speed_factor = 1.5

        self.bullet_speed_factor = 3
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，-1表示向左移
        self.fleet_direction = 1

        self.alien_count = 0
