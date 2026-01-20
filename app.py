import streamlit as st
from kb_loader import load_kb
from pyDatalog import pyDatalog

# Load KB
kb = load_kb()

# Import predicates
pest = pyDatalog.terms.pest
disease = pyDatalog.terms.disease
insecticide = pyDatalog.terms.insecticide
fungicide = pyDatalog.terms.fungicide
find_pest_control = pyDatalog.terms.find_pest_control
find_disease_control = pyDatalog.terms.find_disease_control
is_organic_control = pyDatalog.terms.is_organic_control
is_ipm_choice = pyDatalog.terms.is_ipm_choice

Pest = pyDatalog.terms.Pest
Chemical = pyDatalog.terms.Chemical
Disease = pyDatalog.terms.Disease
Control = pyDatalog.terms.Control
Tool = pyDatalog.terms.Tool

st.title("🥑 Avocado Pest & Disease Expert System")

# --- Pest Controls ---
st.header("Find Pest Controls")
pests = sorted([p[0] for p in pest(Pest)])
selected_pest = st.selectbox("Select Pest", pests)

results = find_pest_control(selected_pest, Chemical)
if results:
    st.dataframe([{"Control": r[1]} for r in results])
else:
    st.info("No controls found.")
