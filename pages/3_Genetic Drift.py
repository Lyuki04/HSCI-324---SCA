import streamlit as st

st.title("Genetic Drift and Fitness")

st.markdown("### Overview of Genetic Drift<sup>1,2,3</sup>", unsafe_allow_html=True)

# Interactive Table for Key Points (Optional)
st.markdown("""
| **Topic**                        | **Key Point**                                                                 |
|-----------------------------------|-------------------------------------------------------------------------------|
| What is Genetic Drift?            | Random changes in gene frequencies over time.                                 |
| Why Does it Matter for SCA?       | Increases the prevalence of disease-causing mutations, especially in small populations. |
| Impact on Small Populations       | Random events have a larger impact on gene frequency in small groups.         |
| SCA and Genetic Drift             | SCA mutations can become more common in small, isolated populations by chance. |
""")

st.subheader("Learn More About Genetic Drift")

with st.expander("What is Genetic Drift?"):
    st.markdown("""
        - **Genetic drift** is a random process where gene frequencies change in a population due to chance.<sup>1,2</sup>
        - Genetic drift doesn't depend on whether a gene provides a survival advantage.<sup>1,2</sup>
        - More pronounced in **small populations**.<sup>1,2</sup>
        - Over time, some genes may become **more or less common**, or even disappear entirely.<sup>1,2</sup>
    """, unsafe_allow_html=True)

with st.expander("Common Types of Genetic Drift"):
    st.markdown("""
        - **Founder effect**: When a small group of individuals from a larger population start a new population, their genetic traits can become more common in future generations due to genetic drift.<sup>1,2,6</sup>
        - **Bottleneck effect**: After a major population reduction, the gene pool is limited, and certain genes may become overrepresented due to genetic drift.<sup>1,2,6</sup>
    """, unsafe_allow_html=True)

with st.expander("How Does Genetic Drift Affect Spinocerebellar Ataxia (SCA)?"):
    st.markdown("""
        - SCA mutations are passed down through generations, but **genetic drift** can cause the frequency of the disease-causing mutation to rise or fall, especially in **small or isolated communities**.
        - By chance, these mutations can spread in the population, or conversely, they can diminish or disappear completely over time.
        - Over generations, this can make the disease more prevalent or even lessen its impact depending on random fluctuations.
    """)

with st.expander("Why is Genetic Drift More Pronounced in Small Populations?"):
    st.markdown("""
        - In **small populations**, random events (like who mates with whom) can drastically change gene frequencies.<sup>3,4,5</sup>
        - In large populations, the effects of genetic drift are less noticeable because of the **larger gene pool**.<sup>3,4,5</sup>
        - In small populations, genetic drift can rapidly increase or decrease the frequency of the SCA gene, depending on the random events at play.<sup>3,4,5</sup>
    """, unsafe_allow_html=True)

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
