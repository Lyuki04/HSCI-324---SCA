import streamlit as st
import matplotlib.pyplot as plt

# Page Configuration
st.set_page_config(page_title="Wright-Fisher Model", page_icon="🧬", layout="wide")

# Title
st.title("The Wright-Fisher Model and Its Application to Genetics")

# Introduction to the Wright-Fisher Model
st.markdown("""### What is the Wright-Fisher Model? <sup>1,2,3,4,5</sup>
""",  unsafe_allow_html=True)

st.markdown("""
The **Wright-Fisher model** is a fundamental model in population genetics that describes the genetic variation of alleles in a population over time. It is primarily used to simulate how allele frequencies evolve through generations under the influence of genetic drift, selection, mutation, and migration.

The model assumes:
- **Discrete, non-overlapping generations**: Individuals in one generation do not overlap with the next.
- **Random mating**: Individuals mate randomly without any biases.
- **Fixed population size (N)**: The population size remains constant across generations.
- **No migration**: There is no gene flow into or out of the population.
- **Allele frequency changes due to genetic drift**: Random sampling of alleles affects the next generation's allele frequencies.

### Why is the Wright-Fisher Model Useful? <sup>1,2,3,4,5</sup>

The Wright-Fisher model is useful because it provides a simple, yet powerful framework for understanding the dynamics of genetic variation in populations. It helps to:
- **Model genetic drift**: It shows how random fluctuations in allele frequencies can lead to the loss of genetic diversity, especially in small populations.
- **Understand evolutionary processes**: The model helps researchers understand how evolutionary forces like natural selection, genetic drift, and mutation interact over time to shape populations.
- **Simulate genetic diseases**: It is particularly valuable in studying the inheritance of genetic disorders, such as **Spinocerebellar Ataxia (SCA)**, to understand how genetic variation of disease alleles may change over generations.
- **Evaluate the impact of different factors**: Researchers can adjust parameters like population size, mutation rate, and selection coefficients to explore their effects on allele frequency dynamics.

### Key Features of the Wright-Fisher Model <sup>1,2,3,4,5</sup>:
- **Genetic Drift**: This model simulates random fluctuations in allele frequencies due to the random sampling of alleles during reproduction.
- **Mutation**: The model can incorporate mutation (back mutations), where alleles may change over generations.
- **Selection**: The Wright-Fisher model can account for natural selection by assigning fitness values to different genotypes (e.g., a diseased allele might be selected against).

---

## Application to Spinocerebellar Ataxia (SCA) <sup>1,2,3,4,5</sup>

In the case of **Spinocerebellar Ataxia (SCA)**, a genetic disorder caused by mutations in specific genes, the Wright-Fisher model can be used to simulate the inheritance patterns and how genetic drift and selection influence the disease allele over multiple generations. 

### For example:
- In **dominant inheritance** (e.g., **SCA1**), the presence of just one copy of the disease allele is sufficient to cause the disease. Over generations, the allele may decrease in frequency due to selection, but genetic drift could cause fluctuations in its frequency.
- In **recessive inheritance** (e.g., **SCA3**), two copies of the disease allele are required for an individual to be affected. The disease allele may persist at low frequencies in the population due to carriers (heterozygotes) not showing symptoms, which could cause genetic drift to play a significant role in allele frequency fluctuations.

By using the Wright-Fisher model, you can simulate how the disease allele behaves over time in a population, accounting for random fluctuations (drift) and the influence of selective pressures. This can help researchers understand how **SCA alleles** might be passed on and how their frequency may change over multiple generations.

---
""",  unsafe_allow_html=True)

st.subheader("Reference List")
with st.expander("References"):
    st.markdown("""
    1. Griffiths, A. J. F., Wessler, S. R., Carroll, S. B., & Doebley, J. (2019). *Introduction to genetic analysis* (12th ed.). W.H. Freeman and Company.
    2. Hartl, D. L., & Clark, A. G. (2007). *Principles of population genetics* (4th ed.). Sinauer Associates.
    3. Kaj, I., Mugal, C. F., & Müller-Widmann, R. (2024). A Wright–Fisher graph model and the impact of directional selection on genetic variation. Theoretical Population Biology, 159, 13–24. https://doi.org/10.1016/j.tpb.2024.07.004
    4. Messer, P. W. (2016). Neutral models of genetic drift and mutation. In R. M. Kliman (Ed.), Encyclopedia of evolutionary biology (pp. 119–123). Academic Press. https://doi.org/10.1016/B978-0-12-800049-6.00031-7
    5. O'Brien, P. (1982). Allele frequencies in a multidimensional Wright-Fisher model with general mutation. Journal of Mathematical Biology, 15(3), 227–237. https://doi.org/10.1007/BF00275075
    """)

