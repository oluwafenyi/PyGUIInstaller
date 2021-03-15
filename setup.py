import os


class Setup:
    def __init__(self, platform):
        self.platform = platform
        # todo: darwin

    def get_default_install_location(self):
        if self.platform == "Linux":
            return "/usr/lib/"
        if self.platform == "Windows":
            return os.getenv("SystemDrive")

