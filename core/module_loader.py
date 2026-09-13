import importlib
from pathlib import Path


class ModuleLoader:
    def __init__(self):
        self.modules_path = Path(__file__).resolve().parent.parent / "modules"

    def discover(self):
        modules = []

        if not self.modules_path.exists():
            return modules

        for item in self.modules_path.iterdir():
            if item.is_dir() and not item.name.startswith("_"):
                modules.append(item.name)

        return sorted(modules)

    def load(self, module_name):
        try:
            return importlib.import_module(
                f"modules.{module_name}"
            )
        except ImportError as error:
            print(f"[!] Could not load module '{module_name}': {error}")
            return None