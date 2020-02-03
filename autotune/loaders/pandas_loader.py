# Importing necessary packages for the loader
import pandas as pd

from ..data.pandas import PandasData
from ..loaders.loader import Loader


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

    def load(self, file_path: str, **kwargs) -> PandasData:
        """Assumption, reading CSV files"""
        # TODO: Could add feature that select the type of
        #  reader depending on the file extension
        #  .csv -> read_csv, .xlsx -> read_excel ...

        # Update the kwargs for pandas
        self.set_opts.update(kwargs)

        return PandasData(pd.read_csv(file_path, **self.set_opts))
