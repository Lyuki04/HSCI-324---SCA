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
ax.legend([f"Simulation {i+1}" for i in range(num_simulations)], loc="upper right")

st.pyplot(fig)

# Explain Genetic Drift
st.markdown("""
### How Genetic Drift Affects the Disease Allele Frequency

Genetic drift is the random fluctuation of allele frequencies over time, especially in small populations. In the Wright-Fisher model, this effect is due to the random sampling of alleles each generation, where alleles can be lost or fixed due to chance alone.

For **dominant inheritance**, individuals with a **dominant allele (A)** exhibit the disease even if they are heterozygous (Aa). Genetic drift can significantly impact the frequency of this allele, especially when the initial frequency is low or the population is small. This is because chance events may cause the dominant allele to be lost or fixed, even if there is a selective advantage to having it.
""")
