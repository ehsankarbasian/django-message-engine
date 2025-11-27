from django.apps import AppConfig

import importlib.util
import pathlib
import sys


"""
Recommended structure for client's app:

my_app/
    message_engine_concrete/
        ** anything **
"""


class MessageEngineConfig(AppConfig):
    
    default_auto_field = "django.db.models.BigAutoField"
    name = "message_engine"
    
    
    def ready(self):
        base = pathlib.Path(__file__).parent / "message_engine_concrete"
        _AutoImporter.import_concrete_modules(base)


class _AutoImporter:

    @staticmethod
    def import_concrete_modules(base_path):
        """
        Recursively import all .py files inside message_engine_concrete/*
        No need for __init__.py inside subfolders.
        """

        base_path = pathlib.Path(base_path)

        for path in base_path.rglob("*.py"):
            if path.name == "__init__.py":
                continue

            module_name = _AutoImporter._filepath_to_module(path, base_path)
            _AutoImporter._import_module(module_name, path)


    @staticmethod
    def _filepath_to_module(filepath: pathlib.Path, base_path: pathlib.Path):
        # Example:
        #   base_path = .../message_engine_concrete
        #   filepath  = .../message_engine_concrete/senders/cmd_printer.py
        #
        # → module_name = "message_engine_concrete.senders.cmd_printer"

        rel = filepath.relative_to(base_path.parent)
        module_name = ".".join(rel.with_suffix("").parts)
        return module_name


    @staticmethod
    def _import_module(module_name: str, filepath: pathlib.Path):
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
