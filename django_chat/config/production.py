from base import *
import os

DEBUG = False
IP_REDIS = os.getenv("IP_REDIS")
PORT_REDIS = os.getenv("PORT_REDIS")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.RedisChannelLayer",
        "CONFIG": {"hosts": [(IP_REDIS, PORT_REDIS)]},
    },
}
