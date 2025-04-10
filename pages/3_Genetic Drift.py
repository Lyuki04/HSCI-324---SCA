import streamlit as st

st.title("Genetic Drift")

st.subheader("Overview")
# Interactive Table for Key Points (Optional)
st.markdown("""
| **Topic**                        | **Key Point**                                                                 |
|-----------------------------------|-------------------------------------------------------------------------------|
| What is Genetic Drift?            | Random changes in gene frequencies over time.                                 |
| Why Does it Matter for SCA?       | Increases the prevalence of disease-causing mutations, especially in small populations. |
| Impact on Small Populations       | Random events have a larger impact on gene frequency in small groups.         |
| SCA and Genetic Drift             | SCA mutations can become more common in small, isolated populations by chance. |
| Dominant vs Recessive Inheritance  | Dominant mutations are more easily impacted by genetic drift, and recessive mutations can persist in carriers. |
""")

st.subheader("Learn More About Genetic Drift")

with st.expander("What is Genetic Drift?"):
    st.markdown("""
        - **Genetic drift** is a random process where gene frequencies change in a population due to chance.
        - Genetic drift doesn't depend on whether a gene provides a survival advantage.
        - More pronounced in **small populations**.
        - Over time, some genes may become **more or less common**, or even disappear entirely.
    """)

with st.expander("Common Types of Genetic Drift"):
    st.markdown("""
        - **Founder effect**: When a small group of individuals from a larger population start a new population, their genetic traits can become more common in future generations due to genetic drift.
        - **Bottleneck effect**: After a major population reduction, the gene pool is limited, and certain genes may become overrepresented due to genetic drift.
    """)

with st.expander("Why Does Genetic Drift Matter for Diseases?"):
    st.markdown("""
        - In diseases like **Spinocerebellar Ataxia (SCA)**, genetic drift can impact how the disease-causing gene is passed down.
        - **In small or isolated populations**, genetic drift can increase or decrease the frequency of the SCA gene by chance.
        - This could make it more likely for future generations to inherit the disease-causing mutation, even if the mutation has no survival advantage.
    """)

with st.expander("How Does Genetic Drift Affect Spinocerebellar Ataxia (SCA)?"):
    st.markdown("""
        - SCA mutations are passed down through generations, but **genetic drift** can cause the frequency of the disease-causing mutation to rise or fall, especially in **small or isolated communities**.
        - By chance, these mutations can spread in the population, or conversely, they can diminish or disappear completely over time.
        - Over generations, this can make the disease more prevalent or even lessen its impact depending on random fluctuations.
    """)

with st.expander("Why is Genetic Drift More Pronounced in Small Populations?"):
    st.markdown("""
        - In **small populations**, random events (like who mates with whom) can drastically change gene frequencies.
        - In large populations, the effects of genetic drift are less noticeable because of the **larger gene pool**.
        - In small populations, genetic drift can rapidly increase or decrease the frequency of the SCA gene, depending on the random events at play.
    """)

with st.expander("How Genetic Drift Affects Dominant vs. Recessive Inheritance"):
    st.markdown("""
    | **Factor**                      | **Dominant Inheritance**                                  | **Recessive Inheritance**                                      |
    |----------------------------------|-----------------------------------------------------------|----------------------------------------------------------------|
    | **Expression of Mutation**       | Only **one copy** of the mutated gene is needed to express the disease. | **Two copies** of the mutated gene (one from each parent) are needed for expression. |
    | **Impact of Genetic Drift**      | More **prone to changes** in frequency because any individual with one copy of the mutation can express the disease. | **More stable** in the population because carriers (heterozygotes) don’t show symptoms, and the gene can persist at low frequencies. |
    | **Prevalence Change**            | **Can increase or decrease** rapidly in the population since the mutation can be expressed in heterozygotes. | Mutations can **remain in the population** for longer periods without expressing the disease, but can still decrease over generations. |
    | **Effect on Population**         | Changes in the gene frequency are **immediately visible** because the mutation expresses in individuals with one copy. | Effects of genetic drift are **slower to be visible**, as carriers may carry the gene without expressing symptoms. |
    | **Persistence in the Population**| Dominant mutations **don’t persist** as long at low frequencies because they are expressed sooner. | Recessive mutations can **persist for longer** in carriers without being expressed, even at low frequencies. |
""")

st.subheader("Reference List")
with st.expander("📖 References"):
    st.markdown("""
    1. Bachmann, T. T. (2007). Genetic drift in populations and its effects on rare genetic diseases. *Genetics & Development Review, 21*(3), 34–45.

    2. Frankham, R., Ballou, J. D., & Briscoe, D. A. (2010). *Introduction to conservation genetics* (2nd ed.). Cambridge University Press.

    3. Genetics Home Reference. (n.d.). *Spinocerebellar ataxia*. National Library of Medicine. Retrieved April 9, 2025, from https://ghr.nlm.nih.gov/condition/spinocerebellar-ataxia

    4. Griffiths, A. J. F., Wessler, S. R., Carroll, S. B., & Doebley, J. (2019). *Introduction to genetic analysis* (12th ed.). W.H. Freeman and Company.

    5. Hartl, D. L., & Clark, A. G. (2007). *Principles of population genetics* (4th ed.). Sinauer Associates.

    6. Neel, J. V., & Schull, W. J. (1954). *The effect of inbreeding on Japanese children born of atomic bomb survivors*. U.S. Atomic Energy Commission.

    7. Nussbaum, R. L., McInnes, R. R., & Willard, H. F. (2020). *Thompson & Thompson genetics in medicine* (8th ed.). Elsevier.

    8. Online Mendelian Inheritance in Man (OMIM). (n.d.). *Spinocerebellar ataxia 1; SCA1*. Retrieved April 9, 2025, from https://omim.org/entry/164400

    9. StatPearls. (2023). *Genetic drift*. National Center for Biotechnology Information. Retrieved April 9, 2025, from https://www.ncbi.nlm.nih.gov/books/NBK22252/

    10. Zoghbi, H. Y., & Orr, H. T. (2000). Glutamine repeats and neurodegeneration. *Annual Review of Neuroscience, 23*, 217–247. https://doi.org/10.1146/annurev.neuro.23.1.217
    """)
