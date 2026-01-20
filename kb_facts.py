from pyDatalog import pyDatalog

def load_facts():
    # ---- PESTS ----
    + pyDatalog.terms.pest('avocado_thrips')
    + pyDatalog.terms.pest('boring_beetles')
    + pyDatalog.terms.pest('ambrosia_beetles')
    + pyDatalog.terms.pest('polyphagous_shothole_borer')
    + pyDatalog.terms.pest('avocado_lace_bug')
    + pyDatalog.terms.pest('mites')
    + pyDatalog.terms.pest('persea_mite')
    + pyDatalog.terms.pest('avocado_brown_mite')
    + pyDatalog.terms.pest('sixspotted_mite')
    + pyDatalog.terms.pest('caterpillars')
    + pyDatalog.terms.pest('scale_insects')
    + pyDatalog.terms.pest('greenhouse_thrips')

    # ---- DISEASES ----
    + pyDatalog.terms.disease('phytophthora_root_rot')
    + pyDatalog.terms.disease('laurel_wilt')
    + pyDatalog.terms.disease('anthracnose')
    + pyDatalog.terms.disease('cercospora_spot')

    # ---- CHEMICALS ----
    + pyDatalog.terms.insecticide('abamectin')
    + pyDatalog.terms.insecticide('spinosad')
    + pyDatalog.terms.insecticide('spinetoram')
    + pyDatalog.terms.insecticide('imidacloprid')
    + pyDatalog.terms.miticide('spirodiclofen')
    + pyDatalog.terms.fungicide('copper')
    + pyDatalog.terms.fungicide('azoxystrobin')

    # ---- ASSOCIATIONS ----
    + pyDatalog.terms.controls_pest('abamectin', 'avocado_thrips')
    + pyDatalog.terms.controls_pest('spinosad', 'avocado_thrips')
    + pyDatalog.terms.controls_pest('spirodiclofen', 'persea_mite')

    + pyDatalog.terms.controls_disease('copper', 'anthracnose')
    + pyDatalog.terms.controls_disease('azoxystrobin', 'anthracnose')

    # ---- PROPERTIES ----
    + pyDatalog.terms.has_irac_group('abamectin', '6')
    + pyDatalog.terms.has_frac_group('azoxystrobin', '11')
    + pyDatalog.terms.is_systemic('imidacloprid')
    + pyDatalog.terms.is_organic('spinosad')
