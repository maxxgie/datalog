from pyDatalog import pyDatalog

# Create all terms needed for rules
pyDatalog.create_terms("""
    Pest, Chemical, Disease, Tool, Control, Group,
    find_pest_control, find_disease_control, is_ipm_choice, is_biological_or_natural,
    is_ipm_tool, natural_solution
""")

def load_rules():
    # RULE 1: Pest → Control
    find_pest_control(Pest, Chemical) <= pest(Pest) & controls_pest(Chemical, Pest)

    # RULE 2: Disease → Control
    find_disease_control(Disease, Chemical) <= disease(Disease) & controls_disease(Chemical, Disease)

    # RULE 3: IPM tools
    is_ipm_choice(Tool) <= is_ipm_tool(Tool)

    # RULE 4: Biological / Natural
    is_biological_or_natural(Control) <= natural_solution(Control)
