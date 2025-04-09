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
""")

# Expanders for more detail on each inheritance pattern
with st.expander("Autosomal Dominant Inheritance"):
    st.markdown("""
    - **One copy of the dominant allele (A)** is enough for an individual to express the dominant trait. 
    - Individuals with the genotype **AA** (homozygous dominant) or **Aa** (heterozygous) will show the disease or trait.
    - There is a **50% chance** of passing the dominant allele to each child if one parent is affected (heterozygous or homozygous dominant).
    - **No carriers** in the classic sense,individuals who inherit the dominant allele will express the trait.
   """)

with st.expander("🧬 Autosomal Dominant Inheritance"):
    st.markdown("""
    - The trait is expressed when **at least one copy** of the dominant allele (**A**) is present.
    - Individuals with **AA** (homozygous dominant) or **Aa** (heterozygous) genotypes **express the trait**.
    - Only individuals with **aa** (homozygous recessive) do **not** show the trait.
    - An affected parent (Aa) has a **50% chance** of passing the dominant allele to each child.
    - If **both parents are affected** (e.g., Aa x Aa), there is a:
        - **75% chance** the child will be affected (AA or Aa),
        - **25% chance** the child will be unaffected (aa).
    """)