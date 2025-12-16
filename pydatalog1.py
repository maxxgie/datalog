import streamlit as st
from pyDatalog import pyDatalog

# Initialize the knowledge base only once
@st.cache_resource
def load_kb():
    pyDatalog.clear()

    # 1. Declare all your variables
    pyDatalog.create_terms('Pest, Chemical, Disease, Tool, Control, Group, RuleName')

    # 2. Declare all your predicates (function/table names)
    pyDatalog.create_terms('pest, disease, insecticide, miticide, fungicide, natural_solution')
    pyDatalog.create_terms('biopesticide, biocontrol, controls_pest, controls_disease, has_irac_group')
    pyDatalog.create_terms('has_frac_group, is_systemic, is_translaminar, is_contact, is_stomach_poison')
    pyDatalog.create_terms('is_protectant, is_fungistat, is_post_harvest, is_selective, is_non_selective')
    pyDatalog.create_terms('application_method, is_organic, is_ipm_tool, find_pest_control')
    pyDatalog.create_terms('find_disease_control, is_ipm_choice, is_biological_or_natural')
    pyDatalog.create_terms('is_organic_control, is_high_resistance_risk, get_irac_group, get_frac_group')
    pyDatalog.create_terms('resistance_management_strategy, preferred_application, high_risk_application')
    pyDatalog.create_terms('is_fungicide_protectant, is_physical_control, ipm_cultural_rule')
    pyDatalog.create_terms('resistance_rule, application_rule, fungicide_rule, ipm_rule')

    # --- ENTITIES ---

    # PESTS (INSECTS & MITES)
    + pest('avocado_thrips')
    + pest('boring_beetles')
    + pest('ambrosia_beetles')
    + pest('polyphagous_shothole_borer')
    + pest('avocado_lace_bug')
    + pest('mites')
    + pest('persea_mite')
    + pest('avocado_brown_mite')
    + pest('sixspotted_mite')
    + pest('caterpillars')
    + pest('western_avocado_leafroller')
    + pest('omnivorous_looper')
    + pest('scale_insects')
    + pest('greenhouse_thrips')

    # DISEASES (FUNGICIDE-RELATED)
    + disease('phytophthora_root_rot')
    + disease('laurel_wilt')
    + disease('anthracnose')
    + disease('cercospora_spot')

    # INSECTICIDES & MITICIDES (CHEMICAL & BOTANICAL)
    + insecticide('abamectin')
    + insecticide('spinetoram')
    + insecticide('spinosad')
    + insecticide('spirotetramat')
    + insecticide('imidacloprid')
    + insecticide('dinotefuran')
    + insecticide('sabadilla')
    + insecticide('emamectin_benzoate')
    + insecticide('pyrethroids')
    + insecticide('permethrin')
    + insecticide('bifenthrin')
    + insecticide('malathion')
    + insecticide('fenpropathrin')
    + insecticide('pyrethrin')
    + miticide('spirodiclofen')

    # FUNGICIDES
    + fungicide('phosphonates')
    + fungicide('fosetyl_al')
    + fungicide('potassium_phosphite')
    + fungicide('metalaxyl')
    + fungicide('propiconazole')
    + fungicide('copper')
    + fungicide('azoxystrobin')
    + fungicide('strobilurin')
    + fungicide('prochloraz')

    # BIOLOGICALS & NATURAL SOLUTIONS
    + natural_solution('horticultural_oil')
    + natural_solution('insecticidal_soap')
    + natural_solution('neem_oil')
    + natural_solution('wettable_sulfur')
    + biopesticide('bt')
    + biopesticide('beauveria_bassiana')
    + biocontrol('predatory_mites')
    + biocontrol('parasitic_wasps')
    + biocontrol('generalist_predators')

    # --- ASSOCIATIONS (FACTS) ---

    # PEST -> CONTROL ASSOCIATIONS
    + controls_pest('abamectin', 'avocado_thrips')
    + controls_pest('spinetoram', 'avocado_thrips')
    + controls_pest('spinosad', 'avocado_thrips')
    + controls_pest('spirotetramat', 'avocado_thrips')
    + controls_pest('imidacloprid', 'avocado_thrips')
    + controls_pest('dinotefuran', 'avocado_thrips')
    + controls_pest('sabadilla', 'avocado_thrips')
    + controls_pest('emamectin_benzoate', 'boring_beetles')
    + controls_pest('pyrethroids', 'boring_beetles')
    + controls_pest('malathion', 'boring_beetles')
    + controls_pest('fenpropathrin', 'boring_beetles')
    + controls_pest('sanitation', 'polyphagous_shothole_borer')
    + controls_pest('imidacloprid', 'avocado_lace_bug')
    + controls_pest('pyrethrin', 'avocado_lace_bug')
    + controls_pest('neem_oil', 'avocado_lace_bug')
    + controls_pest('abamectin', 'persea_mite')
    + controls_pest('spirodiclofen', 'persea_mite')
    + controls_pest('horticultural_oil', 'mites')
    + controls_pest('wettable_sulfur', 'mites')
    + controls_pest('predatory_mites', 'mites')
    + controls_pest('bt', 'caterpillars')
    + controls_pest('spinosyns', 'caterpillars')
    + controls_pest('pyrethroids', 'caterpillars')
    + controls_pest('natural_enemies', 'scale_insects')
    + controls_pest('horticultural_oil', 'scale_insects')
    + controls_pest('insecticidal_soap', 'scale_insects')
    + controls_pest('parasitic_wasps', 'scale_insects')
    + controls_pest('beauveria_bassiana', 'ambrosia_beetles')
    + controls_pest('beauveria_bassiana', 'avocado_thrips')
    + controls_pest('trichogramma', 'caterpillars')

    # DISEASE -> CONTROL ASSOCIATIONS
    + controls_disease('phosphonates', 'phytophthora_root_rot')
    + controls_disease('metalaxyl', 'phytophthora_root_rot')
    + controls_disease('cultural_control_mulch', 'phytophthora_root_rot')
    + controls_disease('cultural_control_drainage', 'phytophthora_root_rot')
    + controls_disease('cultural_control_gypsum', 'phytophthora_root_rot')
    + controls_disease('propiconazole', 'laurel_wilt')
    + controls_disease('sanitation', 'laurel_wilt')
    + controls_disease('copper', 'anthracnose')
    + controls_disease('azoxystrobin', 'anthracnose')
    + controls_disease('prochloraz', 'anthracnose')
    + controls_disease('cultural_control_pruning', 'anthracnose')
    + controls_disease('copper', 'cercospora_spot')

    # CHEMICAL PROPERTIES (MODE OF ACTION)
    + has_irac_group('abamectin', '6')
    + has_irac_group('emamectin_benzoate', '6')
    + has_irac_group('spinosad', '5')
    + has_irac_group('spinetoram', '5')
    + has_irac_group('spirotetramat', '23')
    + has_irac_group('spirodiclofen', '23')
    + has_irac_group('imidacloprid', '4A')
    + has_irac_group('dinotefuran', '4A')
    + has_irac_group('pyrethroids', '3A')
    + has_irac_group('permethrin', '3A')
    + has_irac_group('bifenthrin', '3A')
    + has_irac_group('fenpropathrin', '3A')
    + has_irac_group('pyrethrin', '3A')
    + has_irac_group('malathion', '1B')
    + has_irac_group('bt', '11A')
    + has_irac_group('sabadilla', 'UN')
    + has_frac_group('phosphonates', 'P07')
    + has_frac_group('metalaxyl', '4')
    + has_frac_group('propiconazole', '3')
    + has_frac_group('prochloraz', '3')
    + has_frac_group('copper', 'M01')
    + has_frac_group('azoxystrobin', '11')
    + has_frac_group('strobilurin', '11')

    # CHEMICAL & APPLICATION ATTRIBUTES
    + is_systemic('spirotetramat')
    + is_systemic('imidacloprid')
    + is_systemic('dinotefuran')
    + is_systemic('emamectin_benzoate')
    + is_systemic('phosphonates')
    + is_systemic('propiconazole')
    + is_translaminar('abamectin')
    + is_contact('pyrethroids')
    + is_contact('malathion')
    + is_contact('fenpropathrin')
    + is_contact('spirodiclofen')
    + is_contact('horticultural_oil')
    + is_contact('insecticidal_soap')
    + is_stomach_poison('sabadilla')
    + is_protectant('copper')
    + is_protectant('azoxystrobin')
    + is_fungistat('phosphonates')
    + is_post_harvest('prochloraz')
    + is_selective('bt')
    + is_non_selective('horticultural_oil')
    + application_method('foliar_spray')
    + application_method('aerial_application')
    + application_method('soil_drench')
    + application_method('trunk_injection')
    + is_organic('spinosad')
    + is_organic('sabadilla')
    + is_organic('pyrethrin')
    + is_organic('horticultural_oil')
    + is_organic('wettable_sulfur')
    + is_organic('bt')
    + is_organic('neem_oil')
    + is_organic('insecticidal_soap')
    + is_ipm_tool('bt')
    + is_ipm_tool('horticultural_oil')
    + is_ipm_tool('insecticidal_soap')
    + is_ipm_tool('neem_oil')
    + is_ipm_tool('predatory_mites')
    + is_ipm_tool('parasitic_wasps')
    + is_ipm_tool('beauveria_bassiana')

    # --- FACTS FOR RULES ---
    + resistance_rule('r1', 'Rotate between different IRAC/FRAC Modes of Action (MoA) groups.')
    + application_rule('r1', 'Foliar sprays pose high risk to beneficials.')
    + application_rule('r2', 'Aerial application increases cost and drift risk.')
    + fungicide_rule('r1', 'Most fungicides are protectants, not curatives.')
    + ipm_rule('r4', 'Dust control is critical for conserving natural enemies.')
    + ipm_rule('r5', 'Ants must be controlled as they protect pests.')

    # --- RULES ---

    # RULE 1: Find a chemical control for a given pest.
    find_pest_control(Pest, Chemical) <= \
        pest(Pest) & \
        controls_pest(Chemical, Pest)

    # RULE 2: Find a chemical control for a given disease.
    find_disease_control(Disease, Chemical) <= \
        disease(Disease) & \
        controls_disease(Chemical, Disease)

    # RULE 3: Identify an IPM-compatible tool.
    is_ipm_choice(Tool) <= \
        is_ipm_tool(Tool)

    # RULE 4: Identify a biological or natural control.
    is_biological_or_natural(Control) <= natural_solution(Control)
    is_biological_or_natural(Control) <= biopesticide(Control)
    is_biological_or_natural(Control) <= biocontrol(Control)

    # RULE 5: Identify an organically certified control.
    is_organic_control(Control) <= \
        is_organic(Control)

    # RULE 6: Identify chemicals with high resistance risk.
    is_high_resistance_risk(Chemical) <= \
        has_irac_group(Chemical, '6')
    is_high_resistance_risk(Chemical) <= \
        has_irac_group(Chemical, '5')
    is_high_resistance_risk(Chemical) <= \
        has_frac_group(Chemical, '11')

    # RULE 7: Find the IRAC (insecticide) group for a chemical.
    get_irac_group(Chemical, Group) <= \
        has_irac_group(Chemical, Group)

    # RULE 8: Find the FRAC (fungicide) group for a chemical.
    get_frac_group(Chemical, Group) <= \
        has_frac_group(Chemical, Group)

    # RULE 9: General resistance management rule.
    resistance_management_strategy('rotate_moa_groups') <= \
        resistance_rule('r1', 'Rotate between different IRAC/FRAC Modes of Action (MoA) groups.')

    # RULE 10: Identify preferred application method.
    preferred_application(Chemical, 'trunk_injection') <= \
        is_systemic(Chemical) & insecticide(Chemical)
    preferred_application(Chemical, 'trunk_injection') <= \
        is_systemic(Chemical) & fungicide(Chemical)

    # RULE 11: Identify application method as high-risk for beneficials.
    high_risk_application('foliar_spray') <= \
        application_rule('r1', 'Foliar sprays pose high risk to beneficials.')

    # RULE 14: Identify critical IPM cultural rules.
    ipm_cultural_rule('dust_control') <= \
        ipm_rule('r4', 'Dust control is critical for conserving natural enemies.')
    ipm_cultural_rule('ant_control') <= \
        ipm_rule('r5', 'Ants must be controlled as they protect pests.')

    return pyDatalog

# Load the knowledge base
kb = load_kb()

# Import predicates into global scope for querying
from pyDatalog import pyDatalog
pest = pyDatalog.terms.pest
disease = pyDatalog.terms.disease
insecticide = pyDatalog.terms.insecticide
fungicide = pyDatalog.terms.fungicide
find_pest_control = pyDatalog.terms.find_pest_control
find_disease_control = pyDatalog.terms.find_disease_control
is_organic_control = pyDatalog.terms.is_organic_control
is_ipm_choice = pyDatalog.terms.is_ipm_choice
is_biological_or_natural = pyDatalog.terms.is_biological_or_natural
get_irac_group = pyDatalog.terms.get_irac_group
get_frac_group = pyDatalog.terms.get_frac_group
is_systemic = pyDatalog.terms.is_systemic
is_organic = pyDatalog.terms.is_organic

# Create named variables for queries
Pest = pyDatalog.terms.Pest
Chemical = pyDatalog.terms.Chemical
Disease = pyDatalog.terms.Disease
Tool = pyDatalog.terms.Tool
Control = pyDatalog.terms.Control
Group = pyDatalog.terms.Group

# ----------------------------------------------------------------------
#  BUILD THE STREAMLIT USER INTERFACE (UI)
# ----------------------------------------------------------------------

st.title("🥑 Avocado Pest & Disease Knowledge Base")
st.write("An expert system using Datalog to find control methods.")

# --- UI SECTION 1: FIND PEST CONTROLS ---
st.header("1. Find Pest Controls")

# Get all pests
all_pests = [p[0] for p in pest(Pest)]
selected_pest = st.selectbox("Select a Pest:", options=sorted(all_pests))

# Run the Datalog query
pest_controls_result = find_pest_control(selected_pest, Chemical)

# Display results
st.write(f"**Controls for {selected_pest}:**")
if pest_controls_result:
    control_list = [{"Control Method": item[1]} for item in pest_controls_result]
    st.dataframe(control_list, use_container_width=True)
else:
    st.info("No controls found in the knowledge base.")

# --- UI SECTION 2: FIND DISEASE CONTROLS ---
st.header("2. Find Disease Controls")

all_diseases = [d[0] for d in disease(Disease)]
selected_disease = st.selectbox("Select a Disease:", options=sorted(all_diseases))

disease_controls_result = find_disease_control(selected_disease, Chemical)

st.write(f"**Controls for {selected_disease}:**")
if disease_controls_result:
    control_list = [{"Control Method": item[1]} for item in disease_controls_result]
    st.dataframe(control_list, use_container_width=True)
else:
    st.info("No controls found in the knowledge base.")

# --- UI SECTION 3: QUERY BY CONTROL TYPE ---
st.header("3. Query by Control Type")

col1, col2, col3 = st.columns(3)

if col1.button("Show All Organic Controls"):
    st.subheader("Organic Controls")
    results = is_organic_control(Control)
    if results:
        control_list = [{"Control": item[0]} for item in results]
        st.dataframe(control_list, use_container_width=True)
    else:
        st.info("No organic controls found.")

if col2.button("Show All IPM Tools"):
    st.subheader("IPM Tools")
    results = is_ipm_choice(Tool)
    if results:
        tool_list = [{"Tool": item[0]} for item in results]
        st.dataframe(tool_list, use_container_width=True)
    else:
        st.info("No IPM tools found.")

if col3.button("Show Bio/Natural Controls"):
    st.subheader("Biological & Natural Controls")
    results = is_biological_or_natural(Control)
    if results:
        control_list = [{"Control": item[0]} for item in results]
        st.dataframe(control_list, use_container_width=True)
    else:
        st.info("No biological/natural controls found.")

# --- UI SECTION 4: CHEMICAL PROPERTIES ---
st.header("4. Check Chemical Properties")

# Get all chemicals
all_insecticides = [c[0] for c in insecticide(Chemical)]
all_fungicides = [f[0] for f in fungicide(Chemical)]
all_chemicals = sorted(list(set(all_insecticides + all_fungicides)))

selected_chemical = st.selectbox("Select a Chemical:", options=all_chemicals)

# Run multiple queries
irac_group_result = get_irac_group(selected_chemical, Group)
frac_group_result = get_frac_group(selected_chemical, Group)
is_systemic_check = list(is_systemic(selected_chemical))
is_organic_check = list(is_organic(selected_chemical))

# Display properties
st.write(f"**Properties for {selected_chemical}:**")
properties_found = False

if irac_group_result:
    st.info(f"**IRAC Group:** {irac_group_result[0][1]}")
    properties_found = True
    
if frac_group_result:
    st.info(f"**FRAC Group:** {frac_group_result[0][1]}")
    properties_found = True
    
if is_systemic_check:
    st.success("**Systemic:** Yes")
    properties_found = True
    
if is_organic_check:
    st.success("**Organic:** Yes")
    properties_found = True
    
if not properties_found:
    st.write("No specific properties found in KB for this chemical.")