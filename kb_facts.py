from pyDatalog import pyDatalog

def load_facts():
    assert_fact = pyDatalog.assert_fact

    # ---- PESTS ----
    assert_fact('pest', 'avocado_thrips')
    assert_fact('pest', 'boring_beetles')
    assert_fact('pest', 'ambrosia_beetles')
    assert_fact('pest', 'polyphagous_shothole_borer')
    assert_fact('pest', 'avocado_lace_bug')
    assert_fact('pest', 'mites')
    assert_fact('pest', 'persea_mite')
    assert_fact('pest', 'avocado_brown_mite')
    assert_fact('pest', 'sixspotted_mite')
    assert_fact('pest', 'caterpillars')
    assert_fact('pest', 'scale_insects')
    assert_fact('pest', 'greenhouse_thrips')

    # ---- DISEASES ----
    assert_fact('disease', 'phytophthora_root_rot')
    assert_fact('disease', 'laurel_wilt')
    assert_fact('disease', 'anthracnose')
    assert_fact('disease', 'cercospora_spot')

    # ---- CHEMICALS ----
    assert_fact('insecticide', 'abamectin')
    assert_fact('insecticide', 'spinosad')
    assert_fact('insecticide', 'spinetoram')
    assert_fact('insecticide', 'imidacloprid')
    assert_fact('miticide', 'spirodiclofen')
    assert_fact('fungicide', 'copper')
    assert_fact('fungicide', 'azoxystrobin')

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
