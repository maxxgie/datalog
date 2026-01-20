from pyDatalog import pyDatalog

def load_rules():
    Pest, Chemical, Disease, Tool, Control, Group = pyDatalog.terms(
        'Pest, Chemical, Disease, Tool, Control, Group'
    )

    # RULE 1: Pest → Control
    pyDatalog.terms.find_pest_control(Pest, Chemical) <= \
        pyDatalog.terms.pest(Pest) & \
        pyDatalog.terms.controls_pest(Chemical, Pest)

    # RULE 2: Disease → Control
    pyDatalog.terms.find_disease_control(Disease, Chemical) <= \
        pyDatalog.terms.disease(Disease) & \
        pyDatalog.terms.controls_disease(Chemical, Disease)

    # RULE 3: IPM tools
    pyDatalog.terms.is_ipm_choice(Tool) <= \
        pyDatalog.terms.is_ipm_tool(Tool)

    # RULE 4: Biological / Natural
    pyDatalog.terms.is_biological_or_natural(Control) <= \
        pyDatalog.terms.natural_solution(Control)
