# app.py
import streamlit as st
from kb import load_kb, Pest, Chemical, Disease, pest, disease, find_pest_control, find_disease_control, is_organic_control

# Load KB (terms, facts, and rules)
load_kb()

st.set_page_config(page_title="🥑 Avocado Expert System", layout="wide")
st.title("🥑 Avocado Pest & Disease Expert System")

# --- Pest Controls Section ---
st.header("Find Pest Controls")

# Get all pests from KB
all_pests = sorted([p[0] for p in pest(Pest)])
selected_pest = st.selectbox("Select Pest", all_pests)

# Optional: Organic filter
organic_only = st.checkbox("Show only organic controls")

# Query controls
results = find_pest_control(selected_pest, Chemical)

# Filter organic if checkbox selected
if organic_only:
    results = [r for r in results if is_organic_control(r[1])]

if results:
    st.dataframe([{"Control": r[1]} for r in results])
else:
    st.info("No controls found for this pest.")

# --- Disease Controls Section ---
st.header("Find Disease Controls")

all_diseases = sorted([d[0] for d in disease(Disease)])
selected_disease = st.selectbox("Select Disease", all_diseases)

disease_results = find_disease_control(selected_disease, Chemical)

# Filter organic if checkbox selected
if organic_only:
    disease_results = [r for r in disease_results if is_organic_control(r[1])]

if disease_results:
    st.dataframe([{"Control": r[1]} for r in disease_results])
else:
    st.info("No controls found for this disease.")
