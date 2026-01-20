from pyDatalog import pyDatalog
import streamlit as st
from kb_facts import load_facts
from kb_rules import load_rules

@st.cache_resource
def load_kb():
    pyDatalog.clear()

    # Declare variables
    pyDatalog.create_terms('Pest, Chemical, Disease, Tool, Control, Group, RuleName')

    # Declare predicates
    pyDatalog.create_terms("""
        pest, disease, insecticide, miticide, fungicide, natural_solution,
        biopesticide, biocontrol, controls_pest, controls_disease,
        has_irac_group, has_frac_group,
        is_systemic, is_translaminar, is_contact, is_stomach_poison,
        is_protectant, is_fungistat, is_post_harvest,
        is_selective, is_non_selective,
        application_method, is_organic, is_ipm_tool,
        find_pest_control, find_disease_control,
        is_ipm_choice, is_biological_or_natural,
        is_organic_control, is_high_resistance_risk,
        get_irac_group, get_frac_group,
        resistance_management_strategy,
        preferred_application, high_risk_application,
        ipm_cultural_rule,
        resistance_rule, application_rule,
        fungicide_rule, ipm_rule
    """)

    # Load facts & rules
    load_facts()
    load_rules()

    return pyDatalog
