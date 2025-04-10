import streamlit as st

st.title("Fitness and Selection")

# Set the page configuration for Streamlit

# Title of the page
st.subheader("Selection in Genetics and its Impact on Spinocerebellar Ataxia (SCA)")

# Introduction
st.markdown("""
**Selection** is a fundamental evolutionary process where traits increase in frequency due to their advantage in survival and reproduction. In genetic diseases like **Spinocerebellar Ataxia (SCA)**, selection influences how disease alleles persist or diminish across generations. This section explores how selection acts on genetic alleles, particularly in dominant and recessive diseases, and its impact on allele frequencies over time.
""")

# Basic Explanation of Selection
st.subheader("What is Selection?")
st.markdown("""
Selection can be categorized into **natural selection** and **artificial selection**. In natural selection, advantageous traits become more common, while harmful ones tend to decrease in frequency. For diseases like **SCA**, natural selection typically **reduces the frequency** of harmful alleles, particularly those that affect fitness (e.g., homozygous affected individuals may not survive or reproduce).

Selection is not just about the presence or absence of a disease allele, but how the allele interacts with fitness, influencing whether it persists or diminishes in a population.
""")

# Overview of Fitness
st.markdown("### Overview of Fitness<sup>1,2</sup>", unsafe_allow_html=True)
st.markdown("""
| **Topic**                           | **Key Point**                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------|
| What is Fitness?                     | The ability of an organism to survive, reproduce, and pass on its genes.      |
| Fitness and Dominant Inheritance     | Dominant mutations impact fitness immediately since they are expressed with one copy. |
| Fitness and Recessive Inheritance    | Recessive mutations often don't affect fitness unless both copies are mutated (homozygous). |
| Fitness and SCA                      | SCA mutations can affect fitness over generations, potentially spreading or declining depending on their impact. |
| Selection and Fitness                | Natural selection increases or decreases the frequency of alleles based on their effect on survival or reproduction. |
""")

# Expandable Section on Fitness Impact
st.subheader("Learn More About Fitness")

with st.expander("Influence of Fitness on Dominant vs. Recessive Inheritance"):
    st.markdown("""
    | **Factor**                      | **Dominant Inheritance**                                      | **Recessive Inheritance**                                      |
    |----------------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
    | **Expression of Mutation**       | One copy of the mutated gene expresses the disease.           | Two copies of the mutated gene are needed for expression.      |
    | **Impact of Fitness**            | More prone to selection if harmful, as it expresses in both heterozygotes and homozygotes. | More stable since carriers don't express the disease, allowing persistence at low frequencies. |
    | **Prevalence Change**            | Can increase or decrease rapidly based on the mutation’s fitness effect. | Mutations can remain in the population longer, even at low frequencies, due to the stability of carriers. |
    | **Effect on Population**         | Changes in gene frequency are visible quickly as the mutation expresses. | Effects are slower to manifest as carriers don't express the disease and aren’t impacted by fitness costs. |
    | **Persistence in Population**    | Dominant mutations don’t persist as long at low frequencies due to their immediate expression. | Recessive mutations can persist longer in carriers and may remain even at low frequencies if not strongly selected against. |
    """)

# Selection Types and Impact on SCA
st.subheader("How Selection Affects SCA")
st.markdown("""
The effect of selection on **SCA** depends on whether the disease allele is **dominant** or **recessive**:

### 1. **Dominant Inheritance** (e.g., **SCA1, SCA2, etc.**)
   - Both **homozygous (AA)** and **heterozygous (Aa)** individuals experience a fitness reduction, leading to a **decrease in allele frequency**.
   - **Selection pressure** is strong because both affected individuals contribute to disease transmission.
   - Over time, the **frequency of the disease allele** can **decrease** significantly if selection is strong enough.

### 2. **Recessive Inheritance** (e.g., **SCA3, SCA7, etc.**)
   - Only **homozygous (aa)** individuals experience a fitness disadvantage, allowing the allele to persist in **heterozygous carriers (Aa)** without reducing fitness.
   - Recessive alleles can be maintained at a **constant frequency** over generations, even with selection, since carriers do not suffer from the disease.
   - While selection against **homozygous affected individuals** reduces allele frequency, the rate of decline is slower than in dominant diseases.
""")
st.subheader("Reference List")
with st.expander("References"):
    st.markdown("""
    1. Griffiths, A. J. F., Wessler, S. R., Carroll, S. B., & Doebley, J. (2019). *Introduction to genetic analysis* (12th ed.). W.H. Freeman and Company.
    2. Hartl, D. L., & Clark, A. G. (2007). *Principles of population genetics* (4th ed.). Sinauer Associates.
    """)