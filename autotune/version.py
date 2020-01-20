"""
The package versioning loosely follows:

Semantic Versioning 1.0.0
Site: https://semver.org/spec/v1.0.0.html

Used keyword:
MAJOR, MINOR, PATCH

The version format may be subjected to change
"""

_MAJOR, _MINOR, _PATCH, _LABEL = 0, 1, 0, 'dev'


VERSION = f"{_MAJOR}.{_MINOR}.{_PATCH}-{_LABEL}"
