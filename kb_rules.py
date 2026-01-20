from pyDatalog import pyDatalog

# Create all terms needed for rules
pyDatalog.create_terms("""
    Pest, Chemical, Disease, Tool, Control,
    find_pest_control, find_disease_control,
    is_ipm_choice, is_biological_or_natural,
    is_ipm_tool, natural_solution
""")

# --- RULES (module-level) ---
# Pest -> Control
find_pest_control(Pest, Chemical) <= pyDatalog.pest(Pest) & pyDatalog.controls_pest(Chemical, Pest)

# Disease -> Control
find_disease_control(Disease, Chemical) <= pyDatalog.disease(Disease) & pyDatalog.controls_disease(Chemical, Disease)

# IPM tools
is_ipm_choice(Tool) <= pyDatalog.is_ipm_tool(Tool)

# Biological / Natural
is_biological_or_natural(Control) <= pyDatalog.natural_solution(Control)
