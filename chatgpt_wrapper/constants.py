# Constants used across the modules are stored here.

import os
import tempfile

# Backend speciifc constants
RENDER_MODELS = {
    "default": "text-davinci-002-render-sha",
    "legacy-paid": "text-davinci-002-render-paid",
    "legacy-free": "text-davinci-002-render"
}

OPENAPI_CHAT_RENDER_MODELS = {
    "default": "gpt-3.5-turbo",
    "turbo": "gpt-3.5-turbo",
    "turbo-0301": "gpt-3.5-turbo-0301",
}
OPENAPI_MAX_TOKENS = 4096
OPENAPI_DEFAULT_MIN_SUBMISSION_TOKENS = 1
OPENAPI_DEFAULT_MAX_SUBMISSION_TOKENS = 4000

OPENAPI_DEFAULT_TEMPERATURE = 1
OPENAPI_TEMPERATURE_MIN = 0
OPENAPI_TEMPERATURE_MAX = 2

OPENAPI_DEFAULT_TOP_P = 1
OPENAPI_TOP_P_MIN = 0
OPENAPI_TOP_P_MAX = 1

OPENAPI_DEFAULT_PRESENCE_PENALTY = 0
OPENAPI_PRESENCE_PENALTY_MIN = -2
OPENAPI_PRESENCE_PENALTY_MAX = 2

OPENAPI_DEFAULT_FREQUENCY_PENALTY = 0
OPENAPI_FREQUENCY_PENALTY_MIN = -2
OPENAPI_FREQUENCY_PENALTY_MAX = 2

# Config specific constants.
DEFAULT_PROFILE = 'default'
DEFAULT_CONFIG_DIR = 'chatgpt-wrapper'
DEFAULT_DATABASE_BASENAME = 'storage'
CONFIG_PROFILES_DIR = 'profiles'
DEFAULT_CONFIG = {
    'backend': 'chatgpt-browser',
    'database': None,
    'browser': {
        'provider': 'firefox',
        'debug': False,
    },
    'chat': {
        'model': 'default',
        'model_customizations': {
            'temperature': OPENAPI_DEFAULT_TEMPERATURE,
            'top_p': OPENAPI_DEFAULT_TOP_P,
            'presence_penalty': OPENAPI_DEFAULT_PRESENCE_PENALTY,
            'frequency_penalty': OPENAPI_DEFAULT_FREQUENCY_PENALTY,
            'max_submission_tokens': OPENAPI_DEFAULT_MAX_SUBMISSION_TOKENS,
        },
        'streaming': False,
        'log': {
            'enabled': False,
            'filepath': 'chatgpt.log',
        },
    },
    'log': {
        'console': {
            'level': 'error',
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'debug': {
        'log': {
            'enabled': False,
            'filepath': '%s%schatgpt-debug.log' % (tempfile.gettempdir(), os.path.sep),
            'level': 'debug',
            'format': '%(name)s - %(asctime)s - %(levelname)s - %(message)s',
        },
    },
}

# Shell specific constants.
COMMAND_LEADER = '/'
LEGACY_COMMAND_LEADER = '!'
DEFAULT_COMMAND = 'ask'
COMMAND_HISTORY_FILE = '/tmp/repl_history.log'
DEFAULT_HISTORY_LIMIT = 20

# Interface-specific constants.
NO_TITLE_TEXT = "No title"
SYSTEM_MESSAGE_DEFAULT = "You are a helpful assistant."
