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

st.markdown("### Overview of Fitness<sup>1,2</sup>", unsafe_allow_html=True)

st.markdown("""
| **Topic**                           | **Key Point**                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------|
| What is Fitness?                     | The ability of an organism to survive, reproduce, and pass on its genes to the next generation. |
| Fitness and Dominant Inheritance     | Dominant mutations are more likely to impact fitness immediately since they are expressed with one copy of the mutation. |
| Fitness and Recessive Inheritance    | Recessive mutations often don't impact fitness unless both copies of the mutated gene are present (homozygous). |
| Fitness and SCA                      | In Spinocerebellar Ataxia (SCA), mutations can affect fitness over generations, with the mutation spreading or declining due to fitness effects. |
| Selection and Fitness                | Natural selection acts on the fitness of mutations, increasing or decreasing their frequency based on their effect on survival or reproduction. |
""")

st.subheader("Learn More About Fitness")

with st.expander("Influence of Fitness on Dominant vs. Recessive Inheritance"):
    st.markdown("""
    | **Factor**                      | **Dominant Inheritance**                                      | **Recessive Inheritance**                                      |
    |----------------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
    | **Expression of Mutation**       | Only **one copy** of the mutated gene is needed to express the disease. | **Two copies** of the mutated gene (one from each parent) are needed for expression. |
    | **Impact of Fitness**            | More **prone to being selected against** if the mutation is harmful, as it expresses in heterozygotes or homozygotes. | More **stable in the population** since carriers don't express the disease, and the gene can persist at low frequencies without being selected against. |
    | **Prevalence Change**            | Can **increase or decrease rapidly** in the population if the mutation is beneficial or harmful. The fitness of heterozygotes can influence the rate of change. | Mutations can **remain in the population** for longer periods without expressing the disease, but can still decrease over generations if they are harmful to homozygotes. |
    | **Effect on Population**         | Changes in gene frequency are **immediately visible** because the mutation expresses in individuals with one copy, affecting fitness. | Effects on the population are **slower to be visible** because carriers do not express the disease and don't suffer the fitness costs of homozygotes. |
    | **Persistence in the Population**| Dominant mutations **don’t persist as long** at low frequencies because they are expressed in the heterozygotes and can be subject to selection if harmful. | Recessive mutations can **persist for longer** in carriers without being expressed and can stay in the population even at low frequencies if there is no strong selection against them. |
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

st.subheader("Reference List")
with st.expander("References"):
    st.markdown("""
    1. Griffiths, A. J. F., Wessler, S. R., Carroll, S. B., & Doebley, J. (2019). *Introduction to genetic analysis* (12th ed.). W.H. Freeman and Company.
    2. Hartl, D. L., & Clark, A. G. (2007). *Principles of population genetics* (4th ed.). Sinauer Associates.
    3. LaBar, T., & Adami, C. (2017). Evolution of drift robustness in small populations. Nature communications, 8(1), 1012. https://doi.org/10.1038/s41467-017-01003-7
    4. Kliman, R., Sheehy, B., & Schultz, J. (2008). Genetic drift and effective population size. Nature Education, 1(3), 3.
    5. Mathur, S., Tomeček, J. M., Tarango-Arámbula, L. A., Perez, R. M., & DeWoody, J. A. (2023). An evolutionary perspective on genetic load in small, isolated populations as informed by whole genome resequencing and forward-time simulations. Evolution, 77(3), 690–704. https://doi.org/10.1093/evolut/qpac061
    6. Understanding Evolution. (n.d.). Bottlenecks and founder effects. Understanding Evolution. University of California Museum of Paleontology. Retrieved April 6, 2025, from https://evolution.berkeley.edu/bottlenecks-and-founder-effects/​
    """)