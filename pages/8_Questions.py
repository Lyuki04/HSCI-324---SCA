import streamlit as st

st.title("Questions")

st.header("Fill In The Blank")

st.subheader("This part of the brain, primarily affected by Spinocerebellar Ataxia, is responsible for motor coordination.")
with st.expander("Answer"):
    st.markdown("""
    Cerebellum 
    """)

st.subheader("The genetic condition causing most dominant forms of SCA involves toxic expansion of this repeating sequence.")
with st.expander("Answer"):
    st.markdown("""
    CAG 
    """)

st.subheader("The type of inheritance pattern where only one mutated gene copy is needed to inherit SCA.")
with st.expander("Answer"):
    st.markdown("""
    Dominant 
    """)

st.subheader("Spinocerebellar Ataxia caused by CAG repeat expansions often displays this phenomenon, where the disease onset becomes earlier in successive generations.")
with st.expander("Answer"):
    st.markdown("""
    Anticipation
    """)

st.subheader("This term refers to the random fluctuation in gene frequencies over time, especially noticeable in smaller populations.")
with st.expander("Answer"):
    st.markdown("""
    Genetic Drift
    """)

st.subheader("This phenomenon occurs when a small group from a larger population starts a new population, influencing genetic traits through drift.")
with st.expander("Answer"):
    st.markdown("""
    Founder Effect
    """)

st.subheader("The ability of an organism to survive, reproduce, and pass on its genes.")
with st.expander("Answer"):
    st.markdown("""
    Fitness
    """)

st.subheader("The Wright-Fisher model assumes this kind of population structure.")
with st.expander("Answer"):
    st.markdown("""
    Discrete, non-overlapping
    """)

st.subheader("This factor is assumed to be constant across generations in the Wright-Fisher model, meaning there is no change")
with st.expander("Answer"):
    st.markdown("""
    Population size
    """)

st.header("Short Answer")

st.subheader("Explain the key assumptions of the Wright-Fisher model.")
with st.expander("Answer"):
    st.markdown("""
    The Wright-Fisher model assumes discrete, non-overlapping generations, random mating, a fixed population size (N), no migration, and that allele frequency changes occur due to genetic drift. It simulates the random sampling of alleles during reproduction, affecting the allele frequencies in the next generation.
    """)

st.subheader("How does genetic drift influence allele frequencies in small populations?")
with st.expander("Answer")
    st.markdown("""
     In small populations, genetic drift has a stronger effect because random fluctuations in allele frequencies can lead to the loss of genetic diversity or the random fixation of alleles. These fluctuations are more pronounced due to the smaller gene pool and fewer alleles to choose from.
    """)

st.subheader("How might both selection and genetic drift influence the frequency of the disease allele in the context of SCA1 (a dominant inheritance form of Spinocerebellar Ataxia) over generations?")
with st.expander("Answer")
    st.markdown("""
     In SCA1 (dominant inheritance), selection acts to reduce the frequency of the disease allele because affected individuals may have lower fitness (e.g., reduced survival or reproduction). However, genetic drift causes random fluctuations in allele frequencies, especially in small populations, and can either increase or decrease the frequency of the disease allele by chance, independent of its fitness effect. Over time, selection will typically reduce the allele frequency, while genetic drift can cause random changes, particularly in small populations.
    """)

st.subheader("In what ways can the Wright-Fisher model help researchers understand the dynamics of disease allele frequencies in a population?")
with st.expander("Answer")
    st.markdown("""
     The Wright-Fisher model helps researchers simulate how disease allele frequencies evolve over time under the influence of genetic drift, selection, and mutation. It provides insight into how alleles fluctuate due to random sampling, how selection pressures reduce or increase the frequency of harmful alleles, and how genetic diversity is lost or maintained, all of which are crucial for understanding genetic diseases like SCA.
    """)