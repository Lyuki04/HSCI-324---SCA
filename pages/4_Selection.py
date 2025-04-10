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
st.markdown("""### What is Selection <sup>1,2,3</sup>
""",  unsafe_allow_html=True)
st.markdown("""
**Selection** is a fundamental evolutionary process where traits increase in frequency due to their advantage in survival and reproduction. In genetic diseases like **Spinocerebellar Ataxia (SCA)**, selection influences how disease alleles persist or diminish across generations. 
            
Selection can be categorized into **natural selection** and **artificial selection**. In natural selection, advantageous traits become more common, while harmful ones tend to decrease in frequency. For diseases like **SCA**, natural selection typically **reduces the frequency** of harmful alleles, particularly those that affect fitness (e.g., homozygous affected individuals may not survive or reproduce).

Selection is not just about the presence or absence of a disease allele, but how the allele interacts with fitness, influencing whether it persists or diminishes in a population.
""")

# Overview of Fitness
st.markdown("""### Overview of Fitness and Selection <sup>1,2,3</sup>
""",  unsafe_allow_html=True)
st.markdown("""
| **Topic**                           | **Key Point**                                                                 |
|--------------------------------------|-------------------------------------------------------------------------------|
| What is Fitness?                     | The ability of an organism to survive, reproduce, and pass on its genes.      |
| Fitness and Dominant Inheritance     | Dominant mutations impact fitness immediately since they are expressed with one copy. |
| Fitness and Recessive Inheritance    | Recessive mutations often don't affect fitness unless both copies are mutated (homozygous). |
| Fitness and SCA                      | SCA mutations can affect fitness over generations, potentially spreading or declining depending on their impact. |
| Selection and Fitness                | Natural selection increases or decreases the frequency of alleles based on their effect on survival or reproduction. |
""")


st.markdown("""### Influence of Fitness/Selection on Dominant vs. Recessively Inherited Diseases<sup>1,2,3</sup>
   """,  unsafe_allow_html=True)
st.markdown("""
    | **Factor**                      | **Dominant Inheritance**                                      | **Recessive Inheritance**                                      |
    |----------------------------------|---------------------------------------------------------------|----------------------------------------------------------------|
    | **Expression of Mutation**       | One copy of the mutated gene expresses the disease.           | Two copies of the mutated gene are needed for expression.      |
    | **Impact of Selection**            | More prone to selection if harmful, as it expresses in both heterozygotes and homozygotes. | More stable since carriers don't express the disease, allowing persistence at low frequencies. |
    | **Prevalence Change**            | Can increase or decrease rapidly based on the mutation’s fitness effect. | Mutations can remain in the population longer, even at low frequencies, due to the stability of carriers. |
    | **Effect on Population**         | Changes in gene frequency are visible quickly as the mutation expresses. | Effects are slower to manifest as carriers don't express the disease and aren’t impacted by fitness costs. |
    | **Persistence in Population**    | Dominant mutations don’t persist as long at low frequencies due to their immediate expression. | Recessive mutations can persist longer in carriers and may remain even at low frequencies if not strongly selected against. |
    """)

st.subheader("Reference List")
with st.expander("References"):
    st.markdown("""
    1. Furney, S. J., Albà, M. M., & López-Bigas, N. (2006). Differences in the evolutionary history of disease genes affected by dominant or recessive mutations. BMC genomics, 7, 165. https://doi.org/10.1186/1471-2164-7-165
    2. Griffiths, A. J. F., Wessler, S. R., Carroll, S. B., & Doebley, J. (2019). *Introduction to genetic analysis* (12th ed.). W.H. Freeman and Company.
    3. Hartl, D. L., & Clark, A. G. (2007). *Principles of population genetics* (4th ed.). Sinauer Associates.
    """)