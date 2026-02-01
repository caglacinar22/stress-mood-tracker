# Stress and Mood Self-Tracking Web App

## Overview
This project explores the design and implementation of a simple web application for daily stress and mood tracking to support self-reflection and awareness.  
The goal is to help users notice patterns in their stress and mood over time through lightweight interaction and visualization.

This project is intended for educational and research purposes and does not provide medical advice or diagnosis.

---

## Features
- Log daily mood and stress using sliders
- Annotate entries with contextual tags (sleep, study, social, exercise)
- Add optional notes for each day
- Visualize trends over time in a dashboard
- Export personal data as a CSV file
- Local data storage using CSV

---

## Users
**Target users:** University students

A small usability study was conducted with 3–5 participants to evaluate ease of use and clarity of the interface.

---

## Evaluation
Participants were asked to:
- Log their mood and stress for a day
- Add contextual tags
- Interpret their weekly trend from the dashboard

Feedback indicated that:
- Fast and simple input was important
- Visual trends helped users reflect on their habits
- Contextual tags made entries more meaningful

Based on feedback, the interface was refined for clarity and ease of use.

---

## Tech Stack
- Python
- Streamlit
- Pandas
- Matplotlib

---

## Project Structure
-stress-mood-tracker/
-app.py
-requirements.txt
-README.md
-data/


---

## How to Run

1. Clone the repository:
git clone <your-repo-url>
cd stress-mood-tracker


2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run the app:
streamlit run app.py


Then open the local URL shown in the terminal (usually http://localhost:8501).

---

## Limitations and Ethics
- This application does not diagnose or treat any mental health condition.
- Data is self-reported and may be subjective.
- The usability study involved a small number of participants.
- Personal mental health data should be stored and handled carefully to protect user privacy.

---

## Author
Cagla CINAR



