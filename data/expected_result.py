"""
This section contains the main code statuses and other result from API methods
"""


class ExpectedRequestsResult:
    STATUS_CODE_OK = 200
    NOT_FOUND = 404
    CREATED = 201
    NO_CONTENT = 204
    BAD_REQUEST = 400


class ExpectedCountUserList:
    COUNT_USERS = 22


class ExpectedMessage:
    msg_not_password = {
        "error": "Missing password"
    }

    msg_about_defined_users = {
        'error': 'Note: Only defined users succeed registration'
    }
