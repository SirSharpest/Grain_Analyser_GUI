from ct_analysing_library.CTData import CTData


class CTGUIData(CTData):
    """
    This class provides much needed encapsulation between
    the library and the GUI being used
    """

    def __init__(self, folder, rachis):
        """
        Initialises the data structure to that of the
        parent library
        """
        super().__init__(folder, rachis)

    def download_data(self, save_location):
        self.df.to_csv(save_location)
