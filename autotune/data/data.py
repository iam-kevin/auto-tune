from typing import Iterable, Tuple, Generic, TypeVar

TData = TypeVar('TData')

import numpy as np
from autotune.data.components import AddableData


class Data(Generic[TData]):
    """[Aim] Object that is to store the data that is presented from the loaders

    Features to be present:
    - Allow Merging different types of Data

    The whole function will be making HEAVY use of numpy arrays

    Things to be overriden by this `Data` class.
    - columns?
    -
    """

    def __init__(self,
                 data: TData,
                 columns: Iterable = None):
        # This is the base data type to work with
        self._d: TData = data

        # Setting the columns for the application
        self._col = columns

        # To contain the references that are needed
        self.references: list = []

    @property
    def data(self) -> TData:
        return self._d

    @property
    def columns(self) -> Iterable:
        return self._col

    @property
    def shape(self) -> Tuple[int, ...]:
        """This attribute has to be implemented as a function with `@property` decorator"""
        return self._d.shape

    @property
    def row_count(self) -> int:
        """Obtain the number of rows (records) in the data object

        [ Can be overriden ]

        """
        return self._d.shape[0]

    def add_references(self, data_to_add: AddableData):
        """Merge the references of the addable datas added to the main Data.

        [ Can be overriden ]

        Upon adding the `AddableData` objects to the main data. It might help storing the references of the added data. This could be useful when attempting to do things like. Removing data for training, mainiting its location during random sampling or things as such
        """
        # Expected to hold the number of rows before updating
        pre_tt = self.row_count
        # ixrange = (ct, ct + data_to_add.row_count)

        # TODO: This should be replaced with an equivalent to a pd.IndexSlice
        #   Make it into a 'References' object or something like that
        ixrange = (slice(pre_tt, pre_tt + data_to_add.row_count, None),)
        reference = (data_to_add.name, ixrange)

        self.references.append(reference)

    def addition(self, other: AddableData):
        # Add reference, then update the values (don't change the order)
        self.add_references(other)
        self._d = self.update_merged(other)

    def add(self, data_to_add: AddableData):
        """[Can be overriden by advanced users]
        Not the issue of adding reference... you should find  way around this
        """

        # Add the 'addable' data to the main Data
        # Check if the data is `AddableData`
        if not isinstance(data_to_add, AddableData):
            raise TypeError(
                f'Argument must be a \'{AddableData.__name__}\', instead got \'{type(data_to_add).__name__}\'')

        # Using np.ndarray
        #   Append the data to the main class.
        #   Add the references of the values added

        # Ensure that the data added are in the same shape
        if len(data_to_add.shape) != len(self.shape):
            raise ValueError(f'The value of the added data doesn\'t have the same rank (len(shape))')

        if data_to_add.shape[-1] != self.shape[-1]:
            raise ValueError(
                f'Expected shape[-1] of added data to be {self.shape[-1]}, instead got {data_to_add.shape[-1]}')

        self.addition(data_to_add)

    def update_merged(self, other: AddableData) -> np.ndarray:
        """Creates the final form after merging the data"""
        return np.concatenate((self._d, other._d), axis=0)

    def inspect(self, *args, **options):
        """For humans sake. To enable view of characteristics of the
        data, so that it can be used to find useful information
        about the data"""

        raise NotImplementedError()

    def __repr__(self) -> str:
        """The representation exposed on the data.

        Should vary depending on the `Data` used"""
        raise NotImplementedError()
