import streamlit as st

st.set_page_config(page_title="Autosomal Inheritance", page_icon="🧬", layout="wide")

# Title of the page
st.title("Understanding Autosomal Inheritance")

# Introduction to autosomal inheritance
st.markdown("""
Inheritance patterns determine how genetic traits or diseases are passed down from parents to offspring. The two most common autosomal inheritance patterns are **autosomal dominant** and **autosomal recessive** inheritance.
    
This page will help you understand the key differences between these two inheritance types, using simple descriptions and a comparison table.
""")

# Autosomal Dominant vs. Autosomal Recessive Inheritance
st.subheader("Autosomal Dominant vs. Autosomal Recessive Inheritance")

# Create a comparison table
st.markdown("""
| **Characteristic**                         | **Autosomal Dominant**                                      | **Autosomal Recessive**                                      |
|--------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|
| **Affected Genotypes**                     | Homozygous dominant (AA) or heterozygous (Aa) individuals are affected | Only homozygous recessive (aa) individuals are affected |
| **Carrier Individuals**                    | N/A | Heterozygous (Aa) individuals are carriers but do not show the trait |
| **Trait Expression**                       | One copy of the dominant allele is sufficient to express the trait | Both copies of the recessive allele must be present for the trait to be expressed |
| **Inheritance Pattern**                    | The trait is passed on with a 50% chance to offspring when one parent is affected | The trait is passed on only when both parents are carriers or affected |
| **Affected Parents**                       | Affected parents have a 50% chance of passing the allele to offspring | Affected parents (aa) must both pass the allele to an offspring for expression of the trait |
""")

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