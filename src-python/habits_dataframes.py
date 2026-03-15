import pandas as pd
import numpy as np

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