from autotune.explicit.processes.build_process import BuildProcess
from autotune.explicit.data.pandas_data import PandasData


class PandasProcess(BuildProcess):
    """Sets up to invoke subroutines to `PandasData`

    Attributes
        pandas_data (`PandasData`): Data that is bound with the object
    """

    def __init__(self, pandas_data: PandasData):
        self.data = pandas_data
