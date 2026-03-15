import pandas as pd
import numpy as np
from habit_manager import HabitManager, Habit, HabitLog

def convert_habit_to_dataframe(habit:Habit):
    log_df = []
    for hlog in habit.habit_logs:
        log_element = {
            "Name":habit.name,
            "Group":habit.group,
            "Frequency (Number)":habit.frequency_number,
            "Frequency (Type)":habit.frequency_type,
            "Date":hlog.date,
            "Status":hlog.status
        }
        log_df.append(log_element)
    
    log_df = pd.DataFrame(log_df)
    return log_df

def convert_habit_list_to_dataframe(manager:HabitManager):
    df = []
    for h in manager.habit_groups.values().values():
        element = {
            "Name":h.name,
            "Group":h.group,
            "Frequency (Number)":h.frequency_number,
            "Frequency (Type)":h.frequency_type,
            "Log Count":h.log_count,
            "Current Streak":h.current_streak,
            "Maximum Streak":h.max_streak
        }
        df.append(element)
    
    df = pd.DataFrame(df)
    return df
