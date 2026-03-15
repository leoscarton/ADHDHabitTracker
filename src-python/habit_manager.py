import pandas as pd
from dataclasses import dataclass, field
from typing import Dict, List
from enum import StrEnum
from pydantic import Field

class Weather(StrEnum):
    sunny = "Sunny"
    cloudy = "Cloudy"
    rainy = "Rainy"

class PhysicalHealthStatus(StrEnum):
    excellent = "Excellent"
    good = "Good"
    regular = "Regular"
    bad = "Bad"
    terrible = "Terrible"

@dataclass
class EnvironmentalFactors:
    energy:int = Field(ge=0, le=100)
    anxiety:int = Field(ge=0, le=100)
    weather:Weather = "Sunny"
    physical_health_status:PhysicalHealthStatus = "Good"
    health_conditions:List[str] = field(default_factory=list)
    other:List[str] = field(default_factory=list)

    

@dataclass
class HabitLog:
    date:pd.Timestamp
    status:bool = False
    env_factors:EnvironmentalFactors

    def __init__(self, timestamp:pd.Timestamp):
        self.date = timestamp

    def invert_status(self):
        self.status = not self.status

@dataclass
class Habit:
    name:str
    group:str
    frequency_number:int = 0
    frequency_type:str = "Week"
    log_count:int = 0
    current_streak:int = 0
    max_streak:int = 0
    habit_logs: List[HabitLog] = field(default_factory=list)

    def __init__(self, new_habit:dict):
        self.name = new_habit.get('Name')
        self.group = new_habit.get('Group')
        self.frequency_number = new_habit.get('Frequency (Number)', 0)
        self.frequency_type = new_habit.get('Frequency (Type)', 'Week')
        self.log_count = new_habit.get('Log Count', 0)
        

    def add_new_habit_log(self, new_log_timestamp:pd.Timestamp):
        if new_log_timestamp in self.habit_logs.keys():
            raise AssertionError("There is already another habit scheduled for this date and time.")
        else:
            self.habit_logs.setdefault(new_log_timestamp, HabitLog(new_log_timestamp))


@dataclass
class HabitManager:
    habit_groups:Dict[str, Dict[str, Habit]] = field(default_factory=dict)

    def add_new_habit(self, new_habit:dict, group:str):
        habit = Habit(new_habit=new_habit)
        
        self.habit_groups.setdefault(group, {})
        self.habit_groups[group].setdefault(habit['Name'], habit)

    def remove_habit(self, habit_name:str, habit_group:str):
        if habit_group in self.habit_groups.keys():
            self.habit_groups[habit_group].pop(habit_name, None)