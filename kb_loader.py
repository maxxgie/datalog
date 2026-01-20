from pyDatalog import pyDatalog
import streamlit as st
from kb_facts import load_facts
from kb_rules import load_rules

@st.cache_resource
def load_kb():
    pyDatalog.clear()  # Clear previous facts/rules

    # Create all terms used globally
    pyDatalog.create_terms("""
        Pest, Chemical, Disease, Tool, Control, Group,
        pest, disease, insecticide, miticide, fungicide,
        natural_solution, biopesticide, biocontrol,
        controls_pest, controls_disease,
        has_irac_group, has_frac_group,
        is_systemic, is_organic,
        find_pest_control, find_disease_control,
        is_ipm_choice, is_biological_or_natural,
        is_organic_control, is_ipm_tool
    """)

    load_facts()
    load_rules()

    return pyDatalog
