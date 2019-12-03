from autotune.explicit.data.data import Data
from typing import List, Dict

import numpy as np
import pandas as pd

_INSPECT_OUTPUT_FORMAT = ['jupyter', 'html']
_DEFAULT_INSPECT_OPTS = dict(style={"full_width": True})


class PandasData(Data):
    """Allows storing and manipulating pandas objects

    Primarily: This is to load Kaggle/Zindi Styled contents"""

    def __init__(self, df: pd.DataFrame):
        self.df: pd.DataFrame = df

    @property
    def columns(self) -> List:
        """Loads the columns of the DataFrame object"""
        return self.df.columns

    @property
    def _num_columns(self) -> List:
        """Loads the columns of the DataFrame object"""
        return self.df.shape[1]

    def inspect(self, output_format='jupyter', **profiling_options):
        """Human inspection of data, using pandas-profiling

        Args:
            output_format (str): Format options for inspecting the contents of the file.
                Options are `jupyter` and `html`
            **profiling_options: These are the options that include those which are passed to
             the `pd.DataFrame.profile_report()` method, as well as custom options such as

                output_file (str): File path (*.html) for storing the pandas profiling
                    output

        """
        if output_format not in _INSPECT_OUTPUT_FORMAT:
            raise ValueError(f"The option {output_format} isn't "
                             f"among the allowed options '{_INSPECT_OUTPUT_FORMAT}'")

        # Setting options for profiling
        prof_opts = _DEFAULT_INSPECT_OPTS
        prof_opts.update(profiling_options)

        if output_format == 'jupyter':
            self.df.profile_report(**prof_opts)

        elif output_format == 'html':
            if 'output_file' not in prof_opts:
                raise RuntimeError(f"'output_format' set to 'html', but param 'output_file' is missing")

            profile = self.df.profile_report(title='Pandas Profiling Report')
            profile.to_file(output_file="output.html")
            print(f"[INFO] Save profiling in \'{prof_opts['output_file']}.\'")

    def extra_str(self) -> Dict[str, str]:
        """Contains contents to show as outputs when printing the object"""

        # Check the number of columns
        if self._num_columns > 2:
            col_out = f"{self.columns[0]}, ..., {self.columns[-1]}"
        else:
            col_out = ", ".join(self.columns)

        return {"columns": f"(count={len(self._num_columns)}, view=[{col_out}])"}

    def __str__(self) -> str:
        """Prints a good looking output on `print(PandasData)`"""

        extra_output = ",\n ".join(["%s=%s" % (k, v) for k, v in self.extra_str()])
        return f"PandasData({extra_output}\n)"

    def __repr__(self) -> str:
        return self.df.__repr__()
