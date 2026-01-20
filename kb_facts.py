from pyDatalog import pyDatalog

# Create all terms needed for facts
pyDatalog.create_terms("""
    pest, disease, insecticide, miticide, fungicide,
    controls_pest, controls_disease,
    has_irac_group, has_frac_group,
    is_systemic, is_organic,
    natural_solution, biopesticide, biocontrol
""")

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
