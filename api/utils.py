import json
from enum import Enum


class EnumEx(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))


def get_three_state_bool(value: str) -> bool | None:
    if value:
        if value.lower() == 'true':
            return True
        elif value.lower() == 'false':
            return False
    return None


def format_error(error):
    return json.dumps({'error': f'{str(error)}'})
