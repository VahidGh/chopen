import sys
import os
import django

CHOPEN_PATH = os.path.dirname(os.path.realpath(__file__))

def django_setup():
    if CHOPEN_PATH not in sys.path:
        sys.path.append(CHOPEN_PATH)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "web_app.settings") # web_app should be an app on the chopen path.
    django.setup()
