import streamlit as st

st.title("Fitness and Selection")

# Set the page configuration for Streamlit

# Title of the page
st.subheader("Selection in Genetics and its Impact on Spinocerebellar Ataxia (SCA)")

# Introduction
st.markdown("""
**Selection** is a fundamental process in evolution where certain traits become more common in a population due to their advantageous nature in terms of survival and reproduction. In the context of genetic diseases like **Spinocerebellar Ataxia (SCA)**, selection plays a key role in determining how the disease allele(s) persist or diminish across generations.

In this section, we'll explore how selection acts on genetic alleles, specifically in dominant and recessive diseases, and how it affects the frequency of disease alleles over time.
""")

# Basic Explanation of Selection
st.subheader("What is Selection?")
st.markdown("""
Selection can be categorized into **natural selection** and **artificial selection**. In natural selection, certain genetic traits become more common because they contribute to the organism's ability to survive and reproduce in its environment. This can act to **increase the frequency of beneficial alleles** or **decrease the frequency of harmful alleles** over time.

In the case of genetic diseases like **SCA**, natural selection typically **reduces the frequency** of harmful alleles if they are associated with reduced fitness (e.g., homozygous affected individuals may not survive or reproduce).

Selection is not only about the presence or absence of a disease allele, but also how the disease allele interacts with the fitness of individuals in a population.
""")

# Selection Types and Impact on SCA
st.subheader("How Selection Affects SCA")
st.markdown("""
For diseases like **SCA**, the impact of selection depends on whether the disease allele is **dominant** or **recessive**. Here’s a breakdown of how selection operates for each type of inheritance:

### 1. **Dominant Inheritance** (e.g., **SCA1, SCA2, etc.**)
   - **Homozygous affected (AA)** and **heterozygous affected (Aa)** individuals both experience a reduction in fitness, leading to a **decrease in allele frequency**.
   - **Selection pressure** is strong because both types of affected individuals contribute to disease transmission.
   - Over time, the **frequency of the disease allele** can **decrease** significantly if the selection pressure is strong enough.

### 2. **Recessive Inheritance** (e.g., **SCA3, SCA7, etc.**)
   - Only **homozygous affected (aa)** individuals experience a fitness disadvantage, so the disease allele may persist in the population in **heterozygous carriers (Aa)** without reducing fitness.
   - Recessive alleles can be maintained at a **constant frequency** for many generations, even in the presence of selection, because carriers do not suffer from the disease.
   - Selection against **homozygous affected individuals** can still **reduce the allele frequency**, but the rate of decline is slower compared to dominant diseases.
""")