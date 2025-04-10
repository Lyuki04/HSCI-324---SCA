import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

# Wright-Fisher Simulation with Recessive Inheritance
def wright_fisher_recessive(N=100, p0=0.1, G=50, s=0.1, mu=0.0001):
    p = p0  # Initial frequency of disease allele (a)
    allele_frequencies = [p]
    
    for gen in range(G):
        # Wild-type allele frequency
        q = 1 - p  

        # Fitness of genotypes
        w_AA = 1      # Homozygous normal (AA)
        w_Aa = 1      # Heterozygous carrier (Aa)
        w_aa = 1 - s  # Homozygous affected (aa)

        # Expected genotype frequencies before selection
        p2 = p**2 * w_aa  # aa
        pq = 2 * p * q * w_Aa  # Aa
        q2 = q**2 * w_AA  # AA
        
        # Normalize frequencies based on fitness
        total_w = p2 + pq + q2
        p_next = (p2 + 0.5 * pq) / total_w  # Next allele frequency

        # Apply mutation (back mutation A ↔ a)
        p_next = (1 - mu) * p_next + mu * (1 - p_next)

        # Sample next generation using binomial distribution
        p = np.random.binomial(2 * N, p_next) / (2 * N)
        allele_frequencies.append(p)

    return allele_frequencies

# Streamlit UI
st.title("Wright-Fisher Simulation with Recessive Inheritance of SCA")

# Sidebar inputs
N = st.sidebar.slider("Population Size (N)", 50, 1000, 100)
p0 = st.sidebar.slider("Initial Disease Allele Frequency", 0.01, 1.0, 0.1)
G = st.sidebar.slider("Generations (G)", 10, 200, 50)
s = st.sidebar.slider("Selection Coefficient (s)", 0.0, 1.0, 0.1)

# Define log-scale range (log10 of mutation rates)
min_log_mu = np.log10(1e-7)  # log10 of 0.0000001
max_log_mu = np.log10(1e-4)  # log10 of 0.0001
default_log_mu = np.log10(1e-6)  # log10 of 0.000001

# Create a slider for log-transformed values
log_mu = st.sidebar.slider(
    "Log-Transformed Mutation Rate (log10(μ))",  # Slider title (without subscript)
    min_log_mu, max_log_mu, default_log_mu, step=0.1  # Step size in log scale
)

# Convert back to linear scale
mu = 10**log_mu  

# Run multiple simulations to visualize genetic drift
num_simulations = 7  # Run 7 simulations to see drift variability
all_allele_frequencies = []

for _ in range(num_simulations):
    allele_frequencies = wright_fisher_recessive(N, p0, G, s, mu)
    all_allele_frequencies.append(allele_frequencies)

# Plot results for multiple simulations
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each simulation
for frequencies in all_allele_frequencies:
    ax.plot(range(G+1), frequencies, marker="o", linestyle="-", alpha=0.7)

ax.set_xlabel("Generations")
ax.set_ylabel("Disease Allele Frequency (a)")
ax.set_title("Wright-Fisher Model: SCA Recessive Inheritance with Genetic Drift")

st.pyplot(fig)

# Explain Parameters

st.subheader("🔍 Explanation of the Simulation Design and Parameters (Recessive Model)")
st.markdown("""
This simulation models how a **recessively inherited** disease allele (like certain forms of **Spinocerebellar Ataxia**) evolves in a population using the **Wright-Fisher model**.
""")

with st.expander("🧬 Population Size (N)"):
    st.markdown("""
- Controls the strength of **genetic drift**.
- **Range**: 50 to 1000.
- Smaller N = more randomness, stronger drift.
- Larger N = drift has less influence; selection/mutation become more dominant.
""")

with st.expander("🌱 Initial Disease Allele Frequency (p₀)"):
    st.markdown("""
- Sets the starting frequency of the disease allele (**a**).
- **Range**: 0.01 to 1.0.
- Low values simulate rare disease scenarios.
""")

with st.expander("🧬 Generations (G)"):
    st.markdown("""
- Number of generations over which the simulation runs.
- **Range**: 10 to 200.
- More generations show long-term effects and trends.
""")

with st.expander("⚖️ Selection Coefficient (s)"):
    st.markdown("""
- Represents the **fitness disadvantage** for affected individuals (aa).
- **Range**: 0.0 (no disadvantage) to 1.0 (lethal).
- Carriers (Aa) are assumed unaffected: `w_Aa = 1`.
""")

with st.expander("🔁 Mutation Rate (μ)"):
    st.markdown("""
- Models **mutation between alleles** (A ↔ a).
- **Range**: 10⁻⁷ to 10⁻⁴ (log scale).
- Realistic human mutation rates are typically around 10⁻⁶.
""")

with st.expander("👥 Recessive Inheritance Model"):
    st.markdown("""
- In this simulation, the disease allele (**a**) is **recessive**, meaning that **two copies** of the allele are required to express the disease phenotype.
- Therefore, **only homozygous (aa)** individuals are considered affected, while **heterozygous carriers (Aa)** do **not** experience symptoms.
- The fitness of these individuals is defined using the selection coefficient `s`:
  - `w_aa = 1 - s`  (two disease alleles; affected)
  - `w_Aa = 1`      (one disease allele; unaffected carrier)
  - `w_AA = 1`      (no disease alleles; unaffected)

This setup represents **recessively inherited disorders** like certain types of **Spinocerebellar Ataxia (SCA)**, where individuals can unknowingly carry and pass on the allele without being affected themselves.

Although selection can act against individuals who are homozygous for the disease allele, the allele may still persist in the population — **hidden in carriers**. Combined with **genetic drift**, especially in small populations, this can lead to unpredictable outcomes: the allele might **disappear**, **persist**, or even **increase in frequency** over time.

This component of the model helps us explore how **"silent" inheritance patterns** interact with evolutionary forces like drift and selection.
""")


with st.expander("🎲 Genetic Drift via Binomial Sampling"):
    st.markdown("""
- In each generation, alleles are sampled randomly based on expected frequency using a binomial distribution.
- Genetic drift or randomness, can lead to allele **loss** or **fixation**.
- Reflects how chance can influence inhertiance in a population
""")

with st.expander("🔁 Multiple Simulation Runs"):
    st.markdown("""
- Seven independent simulations are shown to demonstrate how outcomes vary even under the same conditions.
- Highlights the stochastic nature of evolution and disease allele persistence.
""")
