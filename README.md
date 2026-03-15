# ADHD Habit Tracker

A WIP for a simple Habit Tracker focused on common struggles for people with Attention Deficit/Hyperactivity Disorder (ADHD) with an easy-to-use GUI.

## Problem

Many people with ADHD and other conditions (namely, Depression, Anxiety, Autism Spectrum Disorder and so on) suffer with **Executive Dysfunction**, a range of deficits in the so called Executive Functions of the human brain.
In summary, these functions are the reason humans can, amongst other things, control their impulses and emotions, focus on demanding tasks, plan ahead, manage time and complex tasks.
An impairment in Executive Functions make it harder for individuals to commit to habit building and long-term goals in general.

## Solution

This project aims to build a simple and intuitive desktop application where individuals can organize habits and other behaviors they intend to reinforce and become consistent in. The user will be able to add whichever habits in whichever frequency (Ex.: 3 times a week, 2 times a day, etc) they desire in a few clicks and afterwards track their consistency.

The main difference is that the application will (with the user's consent) request and store (locally) data about external and internal conditions that preceeded and suceeded the completion or avoidance of each task. The data will later be used to draw insights on what factors contribute to each behavior done by the user, using statistical data analysis and simple Machine Learning models.

----------------------------------------------------------------------------

## Summary of Tools Used

### Back-End

- Main Language: Python
- Basic data analysis: Pandas and NumPy
- Simple Machine Learning Models: Scikit-learn
- Data Storage: SQLite + SQLModel
- API Connection with Front-End: FastAPI

### Front-End

- Main Language: TypeScript
- UI Framework: React + Vite
- Desktop Runtime: Tauri v2
- Packaging of Python Script: PyInstaller

**NOTE:** Each tool's version will be provided in the future.

------------------------------------------------------------------------------------

Further details will be announced soon.