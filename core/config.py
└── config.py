from pathlib import Path
import json


class Config:
    ROOT_DIR = Path(__file__).resolve().parent.parent
    CONFIG_DIR = ROOT_DIR / "config"
    SETTINGS_FILE = CONFIG_DIR / "settings.json"

    DEFAULTS = {
        "name": "Payload",
        "version": "0.1.0",
        "theme": {
            "primary": "pink",
            "secondary": "green"
        }
    }

    def __init__(self):
        self.settings = self.load()

    def load(self):
        if not self.SETTINGS_FILE.exists():
            return self.DEFAULTS.copy()

        try:
            with open(self.SETTINGS_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return self.DEFAULTS.copy()

    def get(self, key, default=None):
        return self.settings.get(key, default)