import pandas as pd
import numpy as np

import logging

logging.basicConfig(level=logging.INFO)

##########################################################################
                        # CSVHandler Class
        # Separate class for handling CSV operations
##########################################################################


class CSVHandler:
    def __init__(self, filename:str = "habits.csv", df:pd.DataFrame = None, columns:list = None):
        # Storing the filename and DataFrame
        self._filename = filename
        self._columns = columns or ['Name', 'Type', 'Weekly Frequency', 'Instances']
        if df is not None:
            self._dataframe = df
        else:
            self._dataframe = pd.DataFrame(columns=self._columns)

    # Setters and getters
    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename:str):
        assert filename.endswith('.csv'), "Filename must end with .csv"   
        self._filename = filename
    
    @property
    def dataframe(self):
        return self._dataframe
    
    @dataframe.setter
    def dataframe(self, df:pd.DataFrame):
        assert isinstance(df, pd.DataFrame), "Data must be a pandas DataFrame."
        self._dataframe = df
    
    # Method for saving the DataFrame to a CSV file
    def save_to_csv(self):
        if not self._filename.endswith('.csv'):
            raise ValueError("Filename must end with .csv")
        if self._dataframe.empty:
            print("DataFrame is empty. Nothing to save.")
            return
        self._dataframe.to_csv(self._filename, index=False, encoding='utf-8')

    # Method for loading the DataFrame from a CSV file
    def load_from_csv(self):
        try:
            self._dataframe = pd.read_csv(self._filename, encoding='utf-8')
        except FileNotFoundError:
            print(f"File {self._filename} not found. Creating a new one.")
            self._dataframe = pd.DataFrame(columns=['Name', 'Type', 'Weekly Frequency', 'Instances'])
        except Exception as e:
            logging.error(f"An error occurred while loading the file '{self._filename}': {e}")
        

##########################################################################
            # Habit and HabitInstance Classes
##########################################################################

class HabitDataFrame():
    def __init__(self):
        self._habit_columns = ['Name', 'Group', 'Frequency (Number)', 'Frequency (Type)', 'Instances']
        self._habits = pd.DataFrame(columns=self._habit_columns)

    def add_habit(self, new_habit:dict):
        new_habit_df = pd.DataFrame(new_habit)
        new_habit_df = new_habit_df.reindex(columns=self._habit_columns)
        new_habit_df["Instances"] = new_habit_df["Instances"].fillna(0).astype(int)

        self._habits = pd.concat([self._habits, new_habit_df], ignore_index=True, axis=0)

'''
class Habit():
    def __init__(self, name:str, type:str, freq:int = 7, instances:int = 0):
        # Initializing the variables
        self._name = name
        self._type = type
        self._week_frequency = freq
        self._instances = instances

    # String representation of the Habit class
    def __repr__(self):
        return f"Habit Data:\n Name: {self._name}\n Type: {self._type}\n Weekly Frequency: {self._week_frequency}\n Instances: {self._instances}"

    #Name Setter and Getter
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name:str):
        assert new_name is not None and (len(new_name) > 0), "New name must not be empty."
        assert new_name != self._name, "New name must be different from the current name."
        
        self._name = new_name

    #Type Setter and Getter
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type:str):
        assert new_type is not None and (len(new_type) > 0), "New type must not be empty."
        assert new_type != self._type, "New type must be different from the current type."
        
        self._type = new_type

    #Frequency Setter and Getter 
    @property
    def week_frequency(self):
        return self._week_frequency
    
    @week_frequency.setter
    def change_frequency(self, new_freq:int):
        assert isinstance(new_freq, int), "New frequency must be an integer."
        assert new_freq > 0, "New frequency must be greater than zero."
        assert new_freq != self._week_frequency, "New frequency must be different from the current frequency."
        
        self._week_frequency = new_freq

    #Instances Setter and Getter
    @property
    def instances(self):
        return self._instances
    
    @instances.setter
    def change_instances(self, new_instances:int):
        assert isinstance(new_instances, int), "New instances must be an integer."
        assert new_instances >= 0, "New instances must be greater than or equal to zero."
        
        self._instances = new_instances

  #  def increment_instances(self):
  #      self._instances += 1

    # Method to alter the habit's properties
    # Allows changing name, type, frequency, and instances
    def alter_habit(self, new_name:str = None, new_type:str = None, new_freq:int = None, new_instances:int = None):
        if new_name is not None:
            self.name(new_name)
        if new_type is not None:
            self.type(new_type)
        if new_freq is not None:
            self.week_frequency(new_freq)
        if new_instances is not None:
            self.instances(new_instances)


class HabitInstance():
    def __init__(self, habit:Habit, date:str, check:bool = False, out_of_control:bool = False):
        # Initializing the variables
        self._habit = habit
        self._date = pd.to_datetime(date)
        self._check = check
        self._out_of_control = out_of_control

    # Setters and getters
    @property
    def date(self):
        date_string = self._date.strftime("%d/%m/%Y")
        return date_string

    @property
    def habit(self):
        return self._habit.__repr__()

    @property
    def check(self):
        return self._check
    
    @check.setter
    def change_check(self, new_check:bool):
        assert isinstance(new_check, bool), "New check must be a boolean."        
        self._check = new_check

    @property
    def out_of_control(self):
        return self._out_of_control
    
    @out_of_control.setter
    def out_of_control(self, new_out_of_control:bool):
        assert isinstance(new_out_of_control, bool), "New out_of_control must be a boolean."
        self._out_of_control = new_out_of_control

    # String representation of the HabitInstance class
    def __repr__(self):
        return f"Habit Instance Data:\n Habit: {self.habit}\n Date: {self.date_string}\n Done?: {'Yes' if self._check else 'No'}"
'''