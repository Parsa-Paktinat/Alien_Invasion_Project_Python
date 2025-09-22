class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (150, 150, 150)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (50, 50, 50)
        self.bullets_allowed = 70

        # Alien settings
        self.aliens_drop_speed = 10

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 3.5
        self.bullet_speed = 6.0
        self.alien_speed = 1.0
        self.fleet_direction = 1 # 1: right, -1: left

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = 50