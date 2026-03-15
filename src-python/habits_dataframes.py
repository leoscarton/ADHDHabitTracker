import pandas as pd
import numpy as np

'''
class HabitInstance():
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
'''

class Habit():
    def __init__(self, new_habit:dict):
        self._habit_attributes = ['Name', 'Group', 'Frequency (Number)', 'Frequency (Type)', 'Instances', 'Current Streak', 'Maximum Streak']

        self._habit_data = {k: new_habit.get(k) for k in self._habit_attributes}

        #self._habit_instance_attributes = ['Name', 'Group', 'Date', 'Status']
        self._habit_log_attributes = ['Date', 'Status']
        

    def autofill_incomplete_habit(self):
        for k in self._habit_data.keys():
            if k not in ['Name', 'Group', 'Frequency (Type)']:
                self._habit_data[k] = 0

    '''
    def add_habit_log(self, new_instance:dict):
        new_instance_df = pd.DataFrame([new_instance])
        new_instance_df = new_instance_df.reindex(columns=self._habit_instance_attributes)

        new_instance_df['Status'] = new_instance_df['Status'].fillna(False)

        self._habit_instances = pd.concat([self._habit_instances, new_instance_df], ignore_index=True, axis=0)
    
        
    def remove_habit(self, habit_to_remove:str):
        self._habits.drop([self._habits['Name'] == habit_to_remove], axis=0, inplace=True)
        self._habits.reset_index()
    '''
'''
class EnvironmentConditions():
    def __init__(self):
        self._env_conditions = {
            "Emotional" : [],
            "Weather" : [],
            "Other" : []
        }
'''

class HabitManager():
    def __init__(self):
        self._habit_groups = {}

    def add_new_habit(self, new_habit:dict, group:str):
        habit = Habit(new_habit=new_habit)
        
        self._habit_groups.setdefault(group, {})
        self._habit_groups[group].setdefault(habit['Name'], habit)

    def remove_habit(self, habit_name:str, habit_group:str):
        if habit_group in self._habit_groups.keys():
            self._habit_groups[habit_group].pop(habit_name, None)