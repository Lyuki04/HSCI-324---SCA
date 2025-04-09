from PIL import Image
import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Spinocerebellar Ataxia (SCA)", page_icon="🧬", layout="wide") 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/c50d0c64-6bbb-4b3d-ae0b-ef3e54b1c4ee/p1gEOM5mJy.json"


left_column, right_column = st.columns((5,3))
with left_column:
    st.title("Spinocerebellar Ataxia (SCA)")
with right_column:
    st_lottie(lottie_coding, height=200, key="Brain")


img_cerebellum = Image.open("Images/cerebellum.jpg")
img_CAG = Image.open("Images/CAG repeat.png")


with st.container():
    st.write("---")
    st.markdown("### What is Spinocerebellar Ataxia (SCA)?<sup>1,2</sup>", unsafe_allow_html=True)
    left_column, right_column = st.columns((4,4))
    with left_column:
       st.markdown("""
- **Ataxia**: Loss of coordination affecting movement, balance, and speech 
- **Spinocerebellar Ataxia (SCA)**: A group of inherited, progressive neurodegenerative disorders caused by mutations  
- Primarily impacts the **cerebellum**, but may affect other areas like the **spinal cord** and **nerves**  
- **Onset** varies widely by type and genetics
""")
    with right_column: 
        st.image(img_cerebellum)
        st.markdown("_Note: Cerebellum is highlighted in red. (Source: https://storymd.com/journal/6weno3vc5w-spinocerebellar-ataxia-type-1)_")

with st.container():
    st.write("---")
    st.subheader("Types of Spinocerebellar Ataxia<sup>1,2</sup>", unsafe_allow_html=True)
    st.markdown("SCAs differ by **symptoms** and **inheritance patterns**.")
    st.page_link("pages/2_Inheritance Types.py", label="***Learn More About Inheritance Patterns***")
    with st.expander("Autosomal Dominant SCA"):
        st.markdown("""
        - Inherited in a **dominant** manner
        - Most common type of SCA 
        - Includes:  
         - **Type 1**: Ataxia + oculomotor, cognitive, and speech issues  
         - **Type 2**: Similar to Type 1 + **retinal degeneration**  
         - **Type 3**: Mainly **cerebellar ataxia** + possible tremors, stiffness
        """)

with st.expander("Autosomal Recessive SCA"):
    st.markdown("""
        - Inherited in a **recessive** manner  
        - Formally grouped under **autosomal recessive cerebellar ataxias (ARCAs)**  
        - Specific ARCA's can be in an informal, descriptive sense be called SCA as they can affect spinocerrebellar pathways
        - More **numerous** and **genetically diverse** than dominant SCAs  
        - Further classification is challenging due to overlapping, inconsistent, and varied symptoms  
        
        - May involve additional features such as:  
            - Intellectual disability  
            - Seizures  
            - Muscle weakness or coordination problems  
            - Other neurological or systemic complications
     """)


with st.container():
    st.write("---")
    st.subheader("SCA and ARCA Genetics") 
    st.markdown("#### Overview of Genetic Causes of Dominant SCA")
    
    # Create the table using markdown formatting
    st.markdown("""
    | **Type of Mutation**         | **Example SCAs**        | **Genetic Mechanism**                              |
    |-----------------------------|-------------------------|-----------------------------------------------------|
    | CAG repeat expansions       | SCA1, SCA2, SCA3, SCA6, SCA7, SCA17 | Toxic polyglutamine tracts → protein aggregation, impaired folding, **neuronal dysfunction**, and **cell death**, especially in **cerebellar neurons** |
    | Missense/nonsense mutations | SCA13, SCA14, SCA28            | Altered protein structure or function → **neurodegeneration** through disrupted protein function, signaling, or cellular maintenance |
    | Other structural mutations  | Rare/less common SCAs   | Disrupted splicing, altered gene expression, or impaired cellular roles → **progressive neuronal damage** and **loss of motor coordination** |
    """)


    st.markdown("_Note: Dominant SCAs caused by CAG repeats often display anticipation (earlier and more severe onset in successive generations) due to repeat expansion during inheritance._")
    
    left_column, right_column = st.columns((0.389,4))
    with right_column:
        st.image(img_CAG)
        st.markdown("_Note: (Source:)_")

st.markdown("#### Overview of Genetic Causes of Recessive Ataxias")
    
st.markdown("""
    **Autosomal recessive cerebellar ataxias (ARCAs)** are more **numerous and genetically diverse** than dominant forms. They are caused by a wide variety of mutations affecting genes involved in:

    - DNA repair  
    - Mitochondrial function  
    - Lipid metabolism  
    - Neuronal signaling and survival  

    These disorders often begin in **childhood or adolescence** and tend to have **systemic features** beyond the nervous system.

    Unlike dominant SCAs, ARCAs typically do **not** involve repeat expansions, and instead arise from **loss-of-function mutations** inherited from both parents.
    """)

st.markdown("""
    | **Mechanism**                     | **Example ARCAs**                                      | **Genetic Features**                                                 |
    |----------------------------------|--------------------------------------------------------|----------------------------------------------------------------------|
    | Loss-of-function mutations       | Friedreich's ataxia (*FXN*)                            | GAA repeat expansion → mitochondrial iron overload → **neuronal degeneration**, particularly in the cerebellum and dorsal column |
    | Defects in DNA repair            | Ataxia-telangiectasia (*ATM*)                          | Impaired DNA damage response → genomic instability → **neuronal apoptosis**, especially in cerebellar neurons |
    | Mitochondrial dysfunction        | CoQ10 deficiency (*COQ8A*, others), ARSACS (*SACS*)     | Disrupted mitochondrial function → energy failure in neurons → **cerebellar atrophy** and **motor dysfunction** |
    | Lipid/metabolic pathway defects  | Cerebrotendinous xanthomatosis (*CYP27A1*)             | Defective bile acid synthesis → accumulation of lipids in neurons → **neurodegeneration**, including cerebellar regions |
    | Synaptic/axon function defects   | AOA1 (*APTX*), AOA2 (*SETX*)                           | Faulty DNA repair → defective axonal maintenance → neurodegeneration → **progressive ataxia** affecting coordination |
    """)




st.markdown("_Note: Recessive ataxias are highly heterogeneous and often have overlapping features with metabolic or neurodegenerative syndromes._")


    
with st.container():
    st.subheader("References")
    st.write("1. Bhandari, J., Thada, P. K., & Samanta, D. (2023, September 15). Spinocerebellar ataxia. In StatPearls. StatPearls Publishing. https://www.ncbi.nlm.nih.gov/books/NBK557816/")
    st.write("2. Klockgether, T., Mariotti, C., & Paulson, H. L. (2019). Spinocerebellar ataxia. Nature Reviews. Disease Primers, 5(1), 24–24. https://doi.org/10.1038/s41572-019-0074-3")
