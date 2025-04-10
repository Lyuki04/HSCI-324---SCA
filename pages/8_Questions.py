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
with st.expander("Answer")
    st.markdown("""
    Anticipation
    """)
