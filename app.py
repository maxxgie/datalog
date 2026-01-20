import streamlit as st
from kb_loader import load_kb
from kb_rules import Pest, Chemical, Disease, pest, disease, find_pest_control, find_disease_control
from kb_facts import is_organic

# Load KB
load_kb()

st.title("🥑 Avocado Pest & Disease Expert System")

# --- PEST CONTROLS ---
st.header("Find Pest Controls")
all_pests = sorted([p[0] for p in pest(Pest)])
selected_pest = st.selectbox("Select Pest", all_pests)

results = find_pest_control(selected_pest, Chemical)
if results:
    st.dataframe([{"Control": r[1]} for r in results])
else:
    st.info("No controls found.")

# --- DISEASE CONTROLS ---
st.header("Find Disease Controls")
all_diseases = sorted([d[0] for d in disease(Disease)])
selected_disease = st.selectbox("Select Disease", all_diseases)

disease_results = find_disease_control(selected_disease, Chemical)
if disease_results:
    st.dataframe([{"Control": r[1]} for r in disease_results])
else:
    st.info("No controls found.")
