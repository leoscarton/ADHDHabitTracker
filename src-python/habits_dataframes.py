import pandas as pd
import numpy as np

class HabitDataFrame():
    def __init__(self):
        self._habit_columns = ['Name', 'Group', 'Frequency (Number)', 'Frequency (Type)', 'Instances', 'Current Streak', 'Maximum Streak']
        self._habits = pd.DataFrame(columns=self._habit_columns)

    def add_habit(self, new_habit:dict):
        new_habit_df = pd.DataFrame([new_habit])
        new_habit_df = new_habit_df.reindex(columns=self._habit_columns)
        new_habit_df["Instances"] = new_habit_df["Instances"].fillna(0).astype(int)

        self._habits = pd.concat([self._habits, new_habit_df], ignore_index=True, axis=0)

class HabitInstanceDataFrame():
    def __init__(self):
        self._habit_instance_columns = ['Name', 'Group', 'Date', 'Status']
        self._habit_instances = pd.DataFrame(columns=self._habit_instance_columns)

    def add_habit_instance(self, new_instance:dict):
        new_instance_df = pd.DataFrame([new_instance])
        new_instance_df = new_instance_df.reindex(columns=self._habit_instance_columns)

        new_instance_df['Status'] = new_instance_df['Status'].fillna(False)

        self._habit_instances = pd.concat([self._habit_instances, new_instance_df], ignore_index=True, axis=0)

class EnvironmentConditions():
    def __init__(self):
        self._env_conditions = {
            "Emotional" : [],
            "Weather" : [],
            "Other" : []
        }