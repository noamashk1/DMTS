# Column names constants for DMTS experiment
# This file centralizes all column name definitions to ensure consistency across the application

class ColumnNames:
    """Central definition of all column names used in the DMTS experiment"""
    
    # Main table columns (first table in levels_table_creating.py)
    LEVEL_NAME = "Level Name"
    NUMBER_OF_STIMULI = "Number of Stimuli"
    
    # Stimuli table columns (second table in levels_table_creating.py and GUI_sections.py)
    STIM_PATH = "stim path"
    VALUE = "value"
    P_GO = "P(go)"
    P_STIM = "P(stim)"
    IS_NEUROLUX = "is neurolux"
    P_NEUROLUX = "P(neurolux)"
    INDEX = "index"
    
    # CSV header columns (for saving files)
    @classmethod
    def get_csv_headers(cls):
        """Returns the CSV headers in the correct order"""
        return [cls.LEVEL_NAME, cls.STIM_PATH, cls.VALUE, cls.P_GO, cls.P_STIM, cls.IS_NEUROLUX, cls.P_NEUROLUX, cls.INDEX]
    
    # Treeview columns (for GUI_sections.py)
    @classmethod
    def get_treeview_columns(cls):
        """Returns the treeview columns tuple"""
        return (cls.LEVEL_NAME, cls.STIM_PATH, cls.VALUE, cls.P_GO, cls.P_STIM, cls.IS_NEUROLUX, cls.P_NEUROLUX, cls.INDEX)
    
    # Column widths for GUI
    COLUMN_WIDTHS = {
        LEVEL_NAME: 100,
        STIM_PATH: 200,
        VALUE: 80,
        P_GO: 70,
        P_STIM: 70,
        IS_NEUROLUX: 90,
        P_NEUROLUX: 90,
        INDEX: 50
    }
