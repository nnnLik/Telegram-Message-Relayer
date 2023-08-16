from . import const

DATABASES = {
    "default": {
        "ENGINE": const.DB_ENGINE,
        "NAME": const.DB_NAME,
        "USER": const.DB_USER,
        "PASSWORD": const.DB_PASSWORD,
        "HOST": const.DB_HOST,
        "PORT": const.DB_PORT,
    }
}
