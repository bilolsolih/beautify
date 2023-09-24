from datetime import timedelta

AUTH_USER_MODEL = 'accounts.User'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ]
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),

    'SLIDING_TOKEN_LIFETIME': timedelta(days=3),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=30),

    'UPDATE_LAST_LOGIN': False,
}

CKEDITOR_UPLOAD_PATH = 'uploads/'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'apps.accounts.authentication_backends.UsernamePhoneNumberAndEmailAuthenticationBackend'
]
