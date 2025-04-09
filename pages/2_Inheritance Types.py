import streamlit as st

st.set_page_config(page_title="Autosomal Inheritance", page_icon="🧬", layout="wide")

# Title of the page
st.title("Understanding Autosomal Inheritance")

# Introduction to autosomal inheritance
st.markdown("""
Inheritance patterns determine how genetic traits or diseases are passed down from parents to offspring. Two common inheritance patterns are **autosomal dominant** and **autosomal recessive** inheritance.
""")

with st.expander("🔑 Key Terms"):
    st.markdown("""
    To understand inheritance patterns like autosomal dominant and recessive traits, it's essential to grasp a few foundational terms in genetics:

    ### 🧬 Genotype
    - The **genotype** refers to the underlying genetic makeup of an organism—the specific alleles it carries for a given gene.
    - For example: `YY`, `Yy`, or `yy` represent different genotypes for a gene controlling seed color.

    ### 🌱 Phenotype
    - The **phenotype** is the **observable** trait or characteristic that results from the genotype.
    - For instance, both `YY` and `Yy` genotypes produce **yellow seeds** as a phenotype in Mendel’s pea plant experiments.

    ### 🔠 Dominant vs. Recessive Alleles
    - A **dominant allele** (e.g., `Y`) is expressed in the phenotype if at least one copy is present.
    - A **recessive allele** (e.g., `y`) is only expressed when both copies are recessive (`yy`).

    ### 🧩 Homozygous vs. Heterozygous
    - **Homozygous** organisms have two identical alleles for a gene:
        - `YY` (homozygous dominant)
        - `yy` (homozygous recessive)
    - **Heterozygous** organisms have one dominant and one recessive allele: `Yy`

    ### Example: Seed Color in Pea Plants
    - `Y` = Yellow seed allele (dominant)
    - `y` = Green seed allele (recessive)
    - `YY` and `Yy` → **Yellow seeds** (phenotype)
    - `yy` → **Green seeds** (phenotype)

    These key terms form the basis for understanding **autosomal inheritance** patterns and how traits are passed from one generation to the next.
    """)


# Autosomal Dominant vs. Autosomal Recessive Inheritance
st.subheader("Autosomal Dominant vs. Autosomal Recessive Inheritance")

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
    st.write("1. Genetic Alliance, & The New York-Mid-Atlantic Consortium for Genetic and Newborn Screening Services. (2009, July 8). Understanding genetics: A New York, Mid-Atlantic guide for patients and health professionals (Appendix E, Inheritance patterns). Genetic Alliance. https://www.ncbi.nlm.nih.gov/books/NBK115561/")
    """)