# kb.py
from pyDatalog import pyDatalog

# --- CLEAR any previous facts/rules ---
pyDatalog.clear()

# --- CREATE ALL TERMS ---
pyDatalog.create_terms("""
    # Variables
    Pest, Chemical, Disease, Tool, Control, Group,

    # Predicates
    pest, disease, insecticide, miticide, fungicide,
    natural_solution, biopesticide, biocontrol,
    controls_pest, controls_disease,
    has_irac_group, has_frac_group,
    is_systemic, is_organic,
    find_pest_control, find_disease_control,
    is_ipm_choice, is_biological_or_natural,
    is_organic_control, is_ipm_tool
""")

# --- FACTS ---
def load_facts():
    assert_fact = pyDatalog.assert_fact

    # ---- PESTS ----
    for p in ['avocado_thrips', 'boring_beetles', 'ambrosia_beetles', 
              'polyphagous_shothole_borer', 'avocado_lace_bug', 'mites',
              'persea_mite', 'avocado_brown_mite', 'sixspotted_mite',
              'caterpillars', 'scale_insects', 'greenhouse_thrips']:
        assert_fact('pest', p)

    # ---- DISEASES ----
    for d in ['phytophthora_root_rot', 'laurel_wilt', 'anthracnose', 'cercospora_spot']:
        assert_fact('disease', d)

    # ---- CHEMICALS ----
    for i in ['abamectin', 'spinosad', 'spinetoram', 'imidacloprid']:
        assert_fact('insecticide', i)
    assert_fact('miticide', 'spirodiclofen')
    for f in ['copper', 'azoxystrobin']:
        assert_fact('fungicide', f)

    # ---- ASSOCIATIONS ----
    assert_fact('controls_pest', 'abamectin', 'avocado_thrips')
    assert_fact('controls_pest', 'spinosad', 'avocado_thrips')
    assert_fact('controls_pest', 'spirodiclofen', 'persea_mite')

    assert_fact('controls_disease', 'copper', 'anthracnose')
    assert_fact('controls_disease', 'azoxystrobin', 'anthracnose')

    # ---- PROPERTIES ----
    assert_fact('has_irac_group', 'abamectin', '6')
    assert_fact('has_frac_group', 'azoxystrobin', '11')
    assert_fact('is_systemic', 'imidacloprid')
    assert_fact('is_organic', 'spinosad')


# --- RULES ---
def load_rules():
    # RULE 1: Pest → Control
    find_pest_control(Pest, Chemical) <= pest(Pest) & controls_pest(Chemical, Pest)

    # RULE 2: Disease → Control
    find_disease_control(Disease, Chemical) <= disease(Disease) & controls_disease(Chemical, Disease)

    # RULE 3: IPM tools
    is_ipm_choice(Tool) <= is_ipm_tool(Tool)

    # RULE 4: Biological / Natural
    is_biological_or_natural(Control) <= natural_solution(Control)


# --- LOAD KB FUNCTION ---
def load_kb():
    """
    Clears pyDatalog, loads all terms, facts, and rules.
    Returns the pyDatalog module itself (optional, terms are global).
    """
    pyDatalog.clear()
    load_facts()
    load_rules()
    return pyDatalog


# Automatically load KB when imported
load_kb()
