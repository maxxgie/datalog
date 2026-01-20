from pyDatalog import pyDatalog
import streamlit as st
from kb_facts import load_facts
from kb_rules import *  # Rules are loaded at module level

@st.cache_resource
def load_kb():
    """
    Clears pyDatalog and loads facts.
    Rules are already loaded when kb_rules.py is imported.
    """
    pyDatalog.clear()
    load_facts()
    return pyDatalog
