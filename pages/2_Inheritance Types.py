import streamlit as st

st.set_page_config(page_title="Autosomal Inheritance", page_icon="🧬", layout="wide")

# Title of the page
st.title("Understanding Autosomal Inheritance")

# Introduction to autosomal inheritance
st.markdown("""
Inheritance patterns determine how genetic traits or diseases are passed down from parents to offspring. Two common inheritance patterns are **autosomal dominant** and **autosomal recessive** inheritance.
""")

# Autosomal Dominant vs. Autosomal Recessive Inheritance
st.subheader("Autosomal Dominant vs. Autosomal Recessive Inheritance")

# Create a comparison table
st.markdown("""
| **Characteristic**             | **Autosomal Dominant**                                                                 | **Autosomal Recessive**                                                                  |
|-------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| **Affected Genotypes**        | Heterozygous (Aa) or homozygous dominant (AA) individuals express the trait            | Only homozygous recessive (aa) individuals express the trait                            |
| **Carrier Individuals**       | Not applicable – carriers also express the trait                                       | Heterozygous (Aa) individuals are carriers and typically do **not** show the trait      |
| **Trait Expression**          | One copy of the dominant allele is sufficient to express the trait                     | Two copies of the recessive allele are required for trait expression                    |
| **Inheritance Pattern**       | If one parent is affected (Aa), there is a **50% chance** the trait will be passed on  | The trait appears only when **both** parents are carriers or affected                   |
| **Carrier Offspring Risk**    | Offspring are either affected or unaffected (no silent carriers)                       | Carrier parents have a **25% chance** of an affected child and **50% chance** of a carrier |


# Expanders for more detail on each inheritance pattern
with st.expander("Autosomal Dominant Inheritance"):
    st.markdown("""
    - **One copy of the dominant allele (A)** is enough for an individual to express the dominant trait. 
    - Individuals with the genotype **AA** (homozygous dominant) or **Aa** (heterozygous) will show the disease or trait.
    - There is a **50% chance** of passing the dominant allele to each child if one parent is affected (heterozygous or homozygous dominant).
    - **No carriers** in the classic sense—individuals who inherit the dominant allele will express the trait.
   """)

with st.expander("Autosomal Recessive Inheritance"):
    st.markdown("""
    - **Two copies of the recessive allele (aa)** are required for the individual to express the recessive trait.
    - Individuals with **AA** or **Aa** genotypes do not express the trait but may be carriers if they have the **Aa** genotype.
    - Both parents must be carriers or affected for a child to inherit two copies of the recessive allele and express the disease.
    - **Carrier individuals** (Aa) do not show the trait but have a 50% chance of passing the recessive allele to their children.
   """)