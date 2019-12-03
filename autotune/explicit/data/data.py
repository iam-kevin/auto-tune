from typing import List


class Data(object):
    """Holds the Data from loading from some point"""

    # TODO: Add Generic typing
    pass

    @property
    def columns(self) -> List:
        """The columns of the contents"""

        raise NotImplementedError()

    def inspect(self, *args, **options):
        """For humans sake. To enable view of characteristics of the
        data, so that it can be used to find useful information
        about the data"""

        raise NotImplementedError()

    def __repr__(self) -> str:
        """The representation exposed on the loader.

        Should vary depending on the loader used"""
        raise NotImplementedError()
