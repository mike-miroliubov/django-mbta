from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Have a single dir for apps
#APPS_DIR = BASE_DIR.path("styleguide_example")
env = environ.Env()