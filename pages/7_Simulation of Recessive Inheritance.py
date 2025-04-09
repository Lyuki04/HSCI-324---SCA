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
ax.legend([f"Simulation {i+1}" for i in range(num_simulations)], loc="upper right")

st.pyplot(fig)

# Explain Genetic Drift
st.markdown("""
### How Genetic Drift Affects the Disease Allele Frequency

Genetic drift is the random fluctuation of allele frequencies over time, especially in small populations. In the Wright-Fisher model, this effect is due to the random sampling of alleles each generation, where alleles can be lost or fixed due to chance alone.

For **recessive inheritance**, individuals must inherit two copies of the disease allele (aa) to show the disease phenotype. This makes the recessive allele less likely to be selected against if it's present in a heterozygous state (Aa), as it doesn't display the disease. However, **genetic drift** can still significantly impact the frequency of this allele, especially when the initial frequency is low or the population is small. In small populations, the recessive allele can randomly disappear (become fixed) or increase due to chance events, even though it may be "hidden" in carriers.
""")
