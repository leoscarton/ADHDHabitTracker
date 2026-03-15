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
    
    def remove_habit(self, habit_to_remove:str):
        self._habits.drop([self._habits['Name'] == habit_to_remove], axis=0, inplace=True)
        self._habits.reset_index()

class HabitInstanceDataFrame():
    def __init__(self):
        self._habit_instance_columns = ['Name', 'Group', 'Date', 'Status']
        self._habit_instances = pd.DataFrame(columns=self._habit_instance_columns)

    def add_habit_instance(self, new_instance:dict):
        new_instance_df = pd.DataFrame([new_instance])
        new_instance_df = new_instance_df.reindex(columns=self._habit_instance_columns)

        new_instance_df['Status'] = new_instance_df['Status'].fillna(False)

        self._habit_instances = pd.concat([self._habit_instances, new_instance_df], ignore_index=True, axis=0)

    def remove_habit_instance(self, instance_to_remove):
        self._habit_instances.drop([(self._habit_instances['Name'] == instance_to_remove['Name']) & (self._habit_instances['Date'] == instance_to_remove['Date'])])
        self._habit_instances.reset_index()

class EnvironmentConditions():
    def __init__(self):
        self._env_conditions = {
            "Emotional" : [],
            "Weather" : [],
            "Other" : []
        }