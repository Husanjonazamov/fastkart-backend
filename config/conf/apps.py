from config.env import env

APPS = [
    "channels",
    "cacheops",
    "rosetta",
    "django_ckeditor_5",
    "drf_spectacular",
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_redis",
    "rest_framework_simplejwt",
    "django_core",
    "core.apps.accounts.apps.AccountsConfig",
    
    # create apps
    'core.apps.api',
    'core.apps.cart',
    'core.apps.content',
    'core.apps.core',
    'core.apps.orders',
    'core.apps.payments',
    'core.apps.product',
    'core.apps.address',
]

if env.str("PROJECT_ENV") == "debug":
    APPS += [
        "silk",
    ]