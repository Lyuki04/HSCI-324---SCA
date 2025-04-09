import streamlit as st

st.set_page_config(page_title="Autosomal Inheritance", page_icon="🧬", layout="wide")

# Title of the page
st.title("Understanding Autosomal Inheritance")

# Introduction to autosomal inheritance
st.markdown("""
Inheritance patterns determine how genetic traits or diseases are passed down from parents to offspring. Two common inheritance patterns are **autosomal dominant** and **autosomal recessive** inheritance.
<sup>1,2</sup>", unsafe_allow_html=True)
""")
with st.expander("🔑 Key Terms <sup>(1, 2)</sup>", unsafe_allow_html=True)
    st.markdown("""
    To understand inheritance patterns like autosomal dominant and recessive traits, it's essential to grasp a few foundational terms in genetics:

    ### 🧬 Genotype
    - The **genotype** refers to the underlying genetic makeup of an organism—the specific alleles it carries for a given gene.
    - For example: `YY`, `Yy`, or `yy` represent different genotypes.

    ### 🌱 Phenotype
    - The **phenotype** is the **observable** trait or characteristic that results from the genotype.
    - For example, whether an individual **has SCA** or is unaffected.

    ### 🧩 Homozygous vs. Heterozygous
    - **Homozygous** organisms have two identical alleles for a gene:
        - `YY` (homozygous dominant)
        - `yy` (homozygous recessive)
    - **Heterozygous** organisms have one dominant and one recessive allele: `Yy`

    These key terms form the basis for understanding **autosomal inheritance** patterns and how traits are passed from one generation to the next.
    """)




# Autosomal Dominant vs. Autosomal Recessive Inheritance
st.markdown("""
### Autosomal Dominant vs. Autosomal Recessive Inheritance<sup>1,2</sup>
""", unsafe_allow_html=True)

# Create a comparison table
st.markdown("""
| **Characteristic**             | **Autosomal Dominant**                                                                 | **Autosomal Recessive**                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Affected Genotypes**        | Heterozygous (Aa) or homozygous dominant (AA) individuals express the trait            | Only homozygous recessive (aa) individuals express the trait                            |
| **Carrier Individuals**       | Not applicable                                      | Heterozygous (Aa) individuals are carriers and typically do **not** show the trait      |
| **Trait Expression**          | One copy of the dominant allele is sufficient to express the trait                     | Two copies of the recessive allele are required for trait expression                    |
| **Inheritance Pattern**       | If one parent is affected (Aa), there is a **50% chance** the trait will be passed on  | The trait appears only when **both** parents are carriers or affected                   |
""")

with st.expander("References"):
    st.markdown("""
    1. Fowler, S., Roush, R., & Wise, J. (2025). Patterns of Inheritance. In Concepts of Biology. essay, OpenStax College. 
    2. Genetic Alliance, & The New York-Mid-Atlantic Consortium for Genetic and Newborn Screening Services. (2009, July 8). Understanding genetics: A New York, Mid-Atlantic guide for patients and health professionals (Appendix E, Inheritance patterns). Genetic Alliance. https://www.ncbi.nlm.nih.gov/books/NBK115561/")
    """)