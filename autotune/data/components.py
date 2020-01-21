"""
This data contains the components (that may heavily use `numpy`)
that are used with the main Data

The `Imputed` and `OverSampled`/`UnderSampled` should contain the references
(rather than the values themselves... Of the values)
"""
import numpy as np


class AddableData(object):
    def __init__(self, data: np.ndarray):
        self._d = data

    @property
    def row_count(self) -> int:
        """Returns the number of row (records) in the data

        [Can be overriden]

        """
        return self._d.shape[-2]

    @property
    def shape(self):
        return self._d.shape

    @property
    def name(self) -> str:
        """Can be overriden"""
        return 'AddableData'


# This class represented computed 'missing' values
class Imputed(AddableData):
    """Contains the data that is added by an Imputator."""
    pass


# This class represents the values that are a result of sampling
class Sampled(AddableData):
    pass


class OverSampled(Sampled):
    pass


class UnderSampled(Sampled):
    pass
