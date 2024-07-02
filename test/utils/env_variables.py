import os

try:
    BW_USERNAME = os.environ['BW_USERNAME']
    BW_PASSWORD = os.environ['BW_PASSWORD']
    BW_ACCOUNT_ID = os.environ['BW_ACCOUNT_ID']
    BW_MESSAGING_APPLICATION_ID = os.environ['BW_MESSAGING_APPLICATION_ID']
    BW_VOICE_APPLICATION_ID = os.environ['BW_VOICE_APPLICATION_ID']
    BASE_CALLBACK_URL = os.environ['BASE_CALLBACK_URL']
    BW_NUMBER = os.environ['BW_NUMBER']
    VZW_NUMBER = os.environ['VZW_NUMBER']
    ATT_NUMBER = os.environ['ATT_NUMBER']
    T_MOBILE_NUMBER = os.environ['T_MOBILE_NUMBER']
    USER_NUMBER = os.environ['USER_NUMBER']
    FORBIDDEN_USERNAME = os.environ['BW_USERNAME_FORBIDDEN']
    FORBIDDEN_PASSWORD = os.environ['BW_PASSWORD_FORBIDDEN']
    MANTECA_ACTIVE_NUMBER = os.environ['MANTECA_ACTIVE_NUMBER']
    MANTECA_IDLE_NUMBER = os.environ['MANTECA_IDLE_NUMBER']
    MANTECA_BASE_URL = os.environ['MANTECA_BASE_URL']
    MANTECA_STATUS_URL = MANTECA_BASE_URL + 'tests/'
    MANTECA_APPLICATION_ID = os.environ['MANTECA_APPLICATION_ID']
    PYTHON_VERSION = os.environ['PYTHON_VERSION']
    OPERATING_SYSTEM = os.environ['OPERATING_SYSTEM']
    RUNNER_OS = os.environ['RUNNER_OS']

except KeyError as e:
    raise Exception('Environmental variables not found')
