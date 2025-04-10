import numpy as np
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Wright-Fisher Model Simulations of Spinocerebellar Ataxia", page_icon="🧬", layout="wide")

# Wright-Fisher Simulation with Dominant Inheritance
def wright_fisher_dominant(N=100, p0=0.1, G=50, s=0.1, mu=0.0001):
    p = p0
    allele_frequencies = [p]
    
    for gen in range(G):
        # Calculate fitness (dominant selection)
        q = 1 - p  # Wild-type allele frequency
        w_AA = 1 - s  # Homozygous affected
        w_Aa = 1 - s  # Heterozygous affected
        w_aa = 1      # Homozygous wild-type
        
        # Normalize frequencies based on fitness
        p2 = p**2 * w_AA
        pq = 2 * p * q * w_Aa
        q2 = q**2 * w_aa
        total_w = p2 + pq + q2
        
        p_next = (p2 + 0.5 * pq) / total_w
        
        # Mutation: A → a (back mutation)
        p_next = (1 - mu) * p_next + mu * (1 - p_next)

        # Sample next generation using binomial distribution
        p = np.random.binomial(2 * N, p_next) / (2 * N)
        allele_frequencies.append(p)

    return allele_frequencies

# Streamlit UI
st.title("Wright-Fisher Simulation with Dominant Inheritance of SCA")

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
    allele_frequencies = wright_fisher_dominant(N, p0, G, s, mu)
    all_allele_frequencies.append(allele_frequencies)

# Plot results for multiple simulations
fig, ax = plt.subplots(figsize=(10, 6))

# Plot each simulation
for frequencies in all_allele_frequencies:
    ax.plot(range(G+1), frequencies, marker="o", linestyle="-", alpha=0.7)

ax.set_xlabel("Generations")
ax.set_ylabel("Disease Allele Frequency")
ax.set_title("Wright-Fisher Model: SCA Dominant Inheritance with Genetic Drift")

st.pyplot(fig)

# Explain Simulation

st.subheader("🔍 Explanation of the Simulation Design and Parameters")
st.markdown("""
To create this simulation I expanded upon the basic **Wright-Fisher model** to study the evolution of a dominantly inherited **Spinocerebellar Ataxia (SCA)**. Here's how it works:

---
""")
with st.expander("🧬 Population Size (N)"):
    st.markdown("""
- Controls how strongly **genetic drift** affects allele frequencies.
- **Range**: 50 to 1000.
- Smaller populations = more drift (random effects).
- Larger populations = selection/mutation dominate more.

---
""")

with st.expander("🌱 Initial Disease Allele Frequency (p₀)"):
    st.markdown("""
- Sets how common the disease allele (A) is at the start.
- **Range**: 0.01 to 1.0.
- Lower values simulate rare genetic diseases.

---
""")
    
with st.expander("🧬 Generations (G)"):
    st.markdown("""
- Number of generations to simulate.
- **Range**: 10 to 200.
- Longer simulations show long-term effects of drift and selection.

""")
    
with st.expander("⚖️ Selection Coefficient (s)"):
    st.markdown("""
- Models the **fitness cost** of the disease.
- **Range**: 0.0 (neutral) to 1.0 (lethal).
- Default 0.1 = 10% fitness disadvantage for carriers.

""")

with st.expander("🔁 Mutation Rate (μ)"):
    st.markdown("""
- Simulates **back mutation**: A → a.
- **Range**: 10⁻⁷ to 10⁻⁴ (log scale).
- Default: 10⁻⁶, a realistic point mutation rate in humans.

""")

with st.expander("👥 Dominant Inheritance Model"):
    st.markdown("""
- In this simulation, the disease allele (**A**) is **dominant**, meaning that **just one copy** of the allele is enough to express the disease phenotype.
- Therefore, **both heterozygous (Aa)** and **homozygous (AA)** individuals are considered affected.
- The fitness of these individuals is **reduced** by a selection coefficient `s`:
  - `w_AA = 1 - s`  (two disease alleles)
  - `w_Aa = 1 - s`  (one disease allele)
  - `w_aa = 1`      (no disease alleles; full fitness)

This approach reflects **dominantly inherited disorders** like **Spinocerebellar Ataxia (SCA)**, where symptoms can manifest even if only one parent passes on the mutation.

In a population, natural selection may act **against** carriers of the disease allele, reducing its frequency over time. However, due to **genetic drift**, especially in small populations, the allele can still persist or even become fixed — despite its disadvantage.

This component of the model allows us to explore the **tension between selection and randomness**, helping to visualize how a dominant disease gene behaves across generations.
""")
     
with st.expander ("🎲 Genetic Drift via Binomial Sampling"):
    st.markdown("""
- Each generation’s alleles are sampled randomly using a binomial distribution.
- Reflects how chance affects inheritance in a population.

""")

with st.expander("🔁 Multiple Simulation Runs"):
    st.markdown("""
- Seven runs are shown to visualize **variation due to chance**.
- Even with the same parameters, different outcomes can happen!

""")

