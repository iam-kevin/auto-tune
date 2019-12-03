from autotune.explicit.loaders.loader import Loader
from typing import Dict, Any

# Importing necessary packages for the loader
import numpy as np
import pandas as pd

from autotune.explicit.data.pandas_data import PandasData


class PandasLoader(Loader):
    """
    Attributes
        set_opts (`Dict[str, Any]`): options that are used in
            configuring the PandasData objects
    """
    _default_kwargs = dict(index_col=0)

    def __init__(self, default: bool = True):
        if default:
            # Options to set when loading the data
            self.set_opts = PandasLoader._default_kwargs
        else:
            self.set_opts = {}

    @classmethod
    def load(cls, file_path: str, **kwargs) -> PandasData:
        """Assumption, reading CSV files"""
        # TODO: Could add feature that select the type of
        #  reader depending on the file extension
        #  .csv -> read_csv, .xlsx -> read_excel ...

        return PandasData(pd.read_csv(file_path, **kwargs))