import os
from datetime import datetime

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stress & Mood Tracker", layout="centered")

DATA_DIR = "data"
CSV_PATH = os.path.join(DATA_DIR, "entries.csv")

# Ensure data folder exists
os.makedirs(DATA_DIR, exist_ok=True)


def load_data() -> pd.DataFrame:
    if os.path.exists(CSV_PATH):
        df = pd.read_csv(CSV_PATH)
        # Parse timestamp safely
        df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
        return df
    return pd.DataFrame(columns=["timestamp", "mood", "stress", "tags" "note"])


def save_entry(mood: int, stress: int, tags: list[str], note: str) -> None:
    row = {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "mood": mood,
        "stress": stress,
        "tags": ", ".join(tags),
        "note": note.strip()
    }
    df = load_data()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    df.to_csv(CSV_PATH, index=False)


st.title("🧠 Stress & Mood Tracker")
st.caption("A simple self-tracking tool for awareness and reflection (not medical advice).")

tab_log, tab_dash = st.tabs(["Log", "Dashboard"])

with tab_log:
    st.subheader("Daily Check-in")
    mood = st.slider("Mood (1 = very low, 5 = very good)", 1, 5, 3)
    stress = st.slider("Stress (1 = very low, 5 = very high)", 1, 5, 3)

    st.write("What influenced your day?")
    tags = []
    if st.checkbox("Sleep"):
        tags.append("sleep")
    if st.checkbox("Study"):
        tags.append("study")
    if st.checkbox("Social"):
        tags.append("social")
    if st.checkbox("Exercise"):
        tags.append("exercise")

    note = st.text_area("Optional note (extra details)", height=100)

    if st.button("Save entry"):
        save_entry(mood, stress, tags, note)
        st.success("Saved ✅")

    st.markdown("---")
    st.subheader("Recent entries")
    df = load_data().sort_values("timestamp", ascending=False)
    st.dataframe(df.head(10), width="stretch")

with tab_dash:
    st.subheader("Trends (last 14 days)")
    df = load_data().dropna(subset=["timestamp"]).sort_values("timestamp")

    # Export CSV button
    if not df.empty:
        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download my data (CSV)",
            data=csv,
            file_name="stress_mood_data.csv",
            mime="text/csv"
        )

    if df.empty:
        st.info("No entries yet. Add a few in the Log tab.")
    else:
        df["date"] = df["timestamp"].dt.date
        recent = df[df["timestamp"] >= (pd.Timestamp.now() - pd.Timedelta(days=14))]

        if recent.empty:
            st.info("No entries in the last 14 days. Add new ones in the Log tab.")
        else:
            # Aggregate by day
            daily = recent.groupby("date", as_index=False).agg(
                mood=("mood", "mean"),
                stress=("stress", "mean")
            )

            # Plot
            fig, ax = plt.subplots()
            ax.plot(daily["date"], daily["mood"], marker="o", label="Mood (avg)")
            ax.plot(daily["date"], daily["stress"], marker="o", label="Stress (avg)")
            ax.set_xlabel("Date")
            ax.set_ylabel("Score")
            ax.set_ylim(1, 5)
            ax.legend()
            plt.xticks(rotation=30, ha="right")
            st.pyplot(fig)

            # Simple insights
            avg_mood = daily["mood"].mean()
            avg_stress = daily["stress"].mean()
            max_stress_day = daily.loc[daily["stress"].idxmax(), "date"]
            min_mood_day = daily.loc[daily["mood"].idxmin(), "date"]

            st.markdown("### Quick insights")
            st.write(f"- Average mood (14 days): **{avg_mood:.2f}/5**")
            st.write(f"- Average stress (14 days): **{avg_stress:.2f}/5**")
            st.write(f"- Highest stress day: **{max_stress_day}**")
            st.write(f"- Lowest mood day: **{min_mood_day}**")

            st.markdown("### Notes")
            st.write("This is a lightweight self-tracking tool for reflection. It does not diagnose or treat any condition.")
