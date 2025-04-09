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
    st.markdown("### What is Spinocerebellar Ataxia (SCA)?<sup>3,7,12</sup>", unsafe_allow_html=True)
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
    st.markdown("### Types of Spinocerebellar Ataxia<sup>2,3,4,6,7,10,11,12,13,14</sup>", unsafe_allow_html=True)
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
    st.markdown("#### Overview of Genetic Causes of Dominant SCA<sup>2,6,8,9,10,11,13</sup>", unsafe_allow_html=True)
    
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
        st.markdown("_Note: (Source:https://www.nature.com/articles/s41572-019-0074-3)_")

st.markdown("#### Overview of Genetic Causes of Recessive Cerebellar Ataxias<sup>1,4,6,10,12</sup>", unsafe_allow_html=True)
    
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


st.subheader("References")

with st.expander(""):
    st.markdown("""
    1. Beaudin, M., Matilla-Dueñas, A., Soong, B. W., Pedroso, J. L., Barsottini, O. G., Mitoma, H., Tsuji, S., Schmahmann, J. D., Manto, M., Rouleau, G. A., Klein, C., & Dupre, N. (2019). The Classification of Autosomal Recessive Cerebellar Ataxias: a Consensus Statement from the Society for Research on the Cerebellum and Ataxias Task Force. Cerebellum (London, England), 18(6), 1098–1125. https://doi.org/10.1007/s12311-019-01052-2
    2. Benomar, A., Le Guern, E., Dürr, A., Ouhabi, H., Stevanin, G., Yahyaoui, M., Chkili, T., Agid, Y., & Brice, A. (1994). Autosomal-dominant cerebellar ataxia with retinal degeneration (ADCA type II) is genetically different from ADCA type I. Annals of neurology, 35(4), 439–444. https://doi.org/10.1002/ana.410350411
    3. Bhandari, J., Thada, P. K., & Samanta, D. (2023, September 15). Spinocerebellar ataxia. In StatPearls. StatPearls Publishing. https://www.ncbi.nlm.nih.gov/books/NBK557816/
    4. Fogel, B. L., & Perlman, S. (2007). Clinical features and molecular genetics of autosomal recessive cerebellar ataxias. The Lancet. Neurology, 6(3), 245–257. https://doi.org/10.1016/S1474-4422(07)70054-6
    5. Fujioka, S., Sundal, C., & Wszolek, Z. K. (2013). Autosomal dominant cerebellar ataxia type III: a review of the phenotypic and genotypic characteristics. Orphanet journal of rare diseases, 8, 14. https://doi.org/10.1186/1750-1172-8-14
    6. Jayadev, S., & Bird, T. D. (2013). Hereditary ataxias: overview. Genetics in medicine : official journal of the American College of Medical Genetics, 15(9), 673–683. https://doi.org/10.1038/gim.2013.28
    7. Klockgether, T., Mariotti, C., & Paulson, H. L. (2019). Spinocerebellar ataxia. Nature Reviews. Disease Primers, 5(1), 24–24. https://doi.org/10.1038/s41572-019-0074-3
    8. Matilla-Dueñas, A., Sánchez, I., Corral-Juan, M., Dávalos, A., Alvarez, R., & Latorre, P. (2010). Cellular and molecular pathways triggering neurodegeneration in the spinocerebellar ataxias. Cerebellum (London, England), 9(2), 148–166. https://doi.org/10.1007/s12311-009-0144-2
    9. Orr, H. T., & Zoghbi, H. Y. (2007). Trinucleotide repeat disorders. Annual review of neuroscience, 30, 575–621. https://doi.org/10.1146/annurev.neuro.29.051605.113042
    10. Palau, F., & Espinós, C. (2006). Autosomal recessive cerebellar ataxias. Orphanet journal of rare diseases, 1, 47. https://doi.org/10.1186/1750-1172-1-47
    11. Shakkottai, V. G., & Fogel, B. L. (2013). Clinical neurogenetics: autosomal dominant spinocerebellar ataxia. Neurologic clinics, 31(4), 987–1007. https://doi.org/10.1016/j.ncl.2013.04.006
    12. Sun, Y.-M., Lu, C., & Wu, Z.-Y. (2016). Spinocerebellar ataxia: relationship between phenotype and genotype - a review. Clinical Genetics, 90(4), 305–314. https://doi.org/10.1111/cge.12808
    13. Synofzik, M., & Schüle, R. (2017). Overcoming the divide between ataxias and spastic paraplegias: Shared phenotypes, genes, and pathways. Movement disorders : official journal of the Movement Disorder Society, 32(3), 332–345. https://doi.org/10.1002/mds.26944
    14. Whaley, N. R., Fujioka, S., & Wszolek, Z. K. (2011). Autosomal dominant cerebellar ataxia type I: A review of the phenotypic and genotypic characteristics. Orphanet Journal of Rare Diseases, 6, 33. https://doi.org/10.1186/1750-1172-6-33
    """)