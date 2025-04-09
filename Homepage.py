from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="The Inheritance of Spinocerebellar Ataxia", page_icon="🧬", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/6c7b466d-e903-4a96-8b10-afed4d4d13fb/XO1Er1WTNm.json"
img_autosomal = Image.open("Images/Autosomal.png")
img_book = Image.open("Images/book.jpg")

st.title("Homepage")
st.header("Spinocerebellar Ataxia and the Wright-Fisher Model")
st_lottie(lottie_coding, height=300, key="DNA")

with st.container():
    st.write("---")
    st.header("Topics")
    left_column, middle1_column, middle2_column, middle3_column, right_column = st.columns((4.3,4,3,3.8,4))
    with left_column:
        st.subheader("Spinocerebellar Ataxia")
        st.page_link("pages/1_Spinocerebellar Ataxia.py", label="***Learn More***")
    with middle1_column:
        st.subheader("Inheritance Types")
        st.page_link("pages/2_Inheritance Types.py", label="***Learn More***")
    with middle2_column:
        st.subheader("Genetic Drift")
        st.page_link("pages/3_Genetic Drift.py", label="***Learn More***")
    with middle3_column:
        st.subheader("Wright-Fisher Model")
        st.page_link("pages/5_Wright-Fisher Model.py", label="***Learn More***")
    with right_column:
        st.subheader("Simulations")
        st.write("**Dominant Inheritance**")
        st.page_link("pages/6_Simulation of Dominant Inheritance.py", label="***Learn More***")
        st.write("**Recessive Inheritance**")
        st.page_link("pages/7_Simulation of Recessive Inheritance.py", label="***Learn More***")

with st.container():
    st.write("---")
    st.header("Why This Topic?")
    text_column, image_column = st.columns((2,1))
    with image_column:
        st.image(img_book)
    with text_column:
        st.subheader("1 Litre of Tears")
        st.write(
            """My interest in spinocerebellar ataxia (SCA) was sparked by the story of a young Japanese girl named Aya Kitō. 
            She was diagnosed with SCA at 15 years old and wrote about her experiences with the condition in a diary, which later became a book called ***1 Litre of Tears***. 
            Having read the book, it highlighted much of the complexities, beyond just the physical component, of living with a genetic and chronic diseases that often go unnoticed.
            Through this project, I wanted to further explore the genetic underpinnings of SCA, and create a space where others can learn more about the disease and its impact. 
            """
        )

with st.container():
    st.write("---")
    st.header("Inquiry")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/luka.capstone@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="questions" placeholder="Your Questions" requried></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()