from pyDatalog import pyDatalog

# Terms already created in kb_loader.py, but just in case
pyDatalog.create_terms("""
    Pest, Chemical, Disease, Tool, Control,
    find_pest_control, find_disease_control,
    is_ipm_choice, is_biological_or_natural,
    is_ipm_tool, natural_solution,
    pest, disease, controls_pest, controls_disease
""")

# RULES (module-level)
find_pest_control(Pest, Chemical) <= pest(Pest) & controls_pest(Chemical, Pest)
find_disease_control(Disease, Chemical) <= disease(Disease) & controls_disease(Chemical, Disease)
is_ipm_choice(Tool) <= is_ipm_tool(Tool)
is_biological_or_natural(Control) <= natural_solution(Control)
