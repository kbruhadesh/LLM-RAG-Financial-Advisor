import streamlit as st

def update_memory(age=None, duration=None, risk=None):
    if "profile" not in st.session_state:
        st.session_state.profile = {
            "age": None,
            "duration": None,
            "risk": None
        }

    if age:
        st.session_state.profile["age"] = age
    if duration:
        st.session_state.profile["duration"] = duration
    if risk:
        st.session_state.profile["risk"] = risk


def get_profile():
    return st.session_state.get("profile", {
        "age": None,
        "duration": None,
        "risk": None
    })
