import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/d921db5e-1ee5-41b7-a07d-9c50be5406f7/aMx9k09kLK.json"

img_gene = Image.open("Images/Genetic_Drift.png")


left_column, right_column = st.columns((2,3))
with left_column:
    st.title("Genetic Drift")
with right_column:
    st_lottie(lottie_coding, height=300, key="GENE")

st.write("---")

st.markdown("### Overview of Genetic Drift<sup>1,2,3,4,5</sup>", unsafe_allow_html=True)



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
    st.image(img_gene)
    st.markdown("_Source: https://www.khanacademy.org/science/ap-biology/natural-selection/population-genetics/a/genetic-drift-founder-bottleneck)_")


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
