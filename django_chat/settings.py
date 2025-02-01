import os

ENVIRONMENT = os.getenv("ENVIRONMENT")


if ENVIRONMENT == "production":
    from config.production import *

elif ENVIRONMENT == "development":
    from config.dev import *
