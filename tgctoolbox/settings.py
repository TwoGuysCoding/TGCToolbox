import logging
import os

import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

BASE_FILES = [
    os.path.join("configuration", "base.yaml"),
    os.path.join("configuration", "local.yaml"),
    os.path.join("configuration", "production.yaml"),
]


class Settings:
    """Class to manage application settings."""

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, config_files=None, reload=False):
        """
        Initialize Settings object.

        Args:
            config_files (list): List of YAML configuration files.
            reload (bool): Whether to reload settings.
        """
        if not hasattr(self, "_initialized") or reload:
            self._settings = {}
            config_files = config_files or BASE_FILES
            self._load_from_yaml(config_files)
            self._load_from_env()
            self._initialized = True

    def _load_from_yaml(self, config_files):
        """Load settings from YAML files."""
        loaded_settings = {}
        settings_names = []
        if config_files:
            for file in config_files:
                try:
                    with open(file, "r") as f:
                        settings = yaml.safe_load(f)
                        if settings:
                            loaded_settings.update(settings)
                            settings_names.extend(settings.keys())
                except FileNotFoundError:
                    logger.warning(f"Configuration file not found: {file}")
                    continue
                except yaml.YAMLError:
                    logger.warning(f"Error loading configuration file: {file}")
                    continue
        self._settings.update(loaded_settings)
        logger.info("Following settings were loaded from YAML files:")
        for name in settings_names:
            logger.info(f"  - {name}")

    def _load_from_env(self):
        """Load settings from environment variables."""
        settings_names = []
        for key, value in os.environ.items():
            if key.startswith("VAR_"):
                keys = key.split("_")[1:]  # Remove 'VAR_' prefix
                settings_names.append(keys[-1])
                current_level = self._settings
                for k in keys[:-1]:
                    current_level = current_level.setdefault(k, {})
                current_level[keys[-1]] = value
        logger.info("Following settings were loaded from environment variables:")
        for name in settings_names:
            logger.info(f"  - {name}")

    def get(self, key, default=None):
        """
        Get the value of a setting.

        Args:
            key (str): The key of the setting.
            default: Default value if setting not found.

        Returns:
            The value of the setting if found, otherwise default value.
        """
        value = self._settings
        for k in key.split("."):
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value


# Example usage:
if __name__ == "__main__":
    settings = Settings()
    settings2 = Settings()

    # Accessing settings
    app_port = settings.get("app.port")
    print(f"App Port: {app_port}")
    print(settings is settings2)
