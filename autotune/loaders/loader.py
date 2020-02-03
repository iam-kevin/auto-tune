import os

# TODO: Make typing generic Loader<T>
from autotune.data.data import Data


class Loader(object):
    """Loads content

    This can vary depending on the implementation. It can be loaded
    from a file. Or from a passed list. Or even a link

    Primarily: This is to load Kaggle/Zindi Styled contents"""

    @classmethod
    def _load(cls, file_path: str) -> Data:
        """Method used by the `load` helper function"""
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} doesn't exist.")

        return cls.load(file_path)

    @classmethod
    def load(cls, file_path: str, **options) -> Data:
        """Loads the file contents.

        Sub-routines are executed before loading the file"""

        raise NotImplementedError()

    def __repr__(self) -> str:
        """The representation exposed on the loader.

        Should vary depending on the loader used"""
        raise NotImplementedError()
