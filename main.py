import streamlit as st
import time
import pickle
import nltk
import re
nltk.download('wordnet')
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer

def predict_mail(mail):
    
    model = pickle.load(open("model.pckl",mode="rb"))
    vectorizer = pickle.load(open("vectorizer.pckl",mode="rb"))
    
    lemma = WordNetLemmatizer()
    
    stopwords = nltk.corpus.stopwords.words('english')
    
    mail = re.sub(r"http\S+", "", mail)
    mail = re.sub("[^a-zA-Z0-9]"," ",mail)
    mail = mail.lower()
    mail = nltk.word_tokenize(mail)
    mail = [lemma.lemmatize(word) for word in mail]
    mail = [word for word in mail if word not in stopwords]
    mail = " ".join(mail)
    
    vector = vectorizer.transform([mail])
    decision = model.predict(vector.toarray())
    
    return decision[0]

st.title("Welcome to Spam Filtering")

nav = st.sidebar.radio("Navigation", ["Home", "About", "Filter"])

if nav == "Home":
    st.markdown("""<br>""", True)
    st.markdown(""" Welcome
              <br />
             """, True)
    st.markdown("### New Visitor?")
    if st.button("Register"):
        first, last = st.beta_columns(2)
        first.text_input("First Name")
        last.text_input("Last Name")
        email, mobile = st.beta_columns([3, 1])
        email.text_input("Email Id")
        mobile.text_input("Mobile No")
        username, pw, rpw = st.beta_columns(3)
        username.text_input("Username")
        pw.text_input("Password", type="password")
        rpw.text_input("Re-enter Password", type="password")
        check, space, submit = st.beta_columns(3)
        check.checkbox("I agree to all T&C", value=False)
        submit.button("Submit")

    st.markdown("### Already a visitor?")
    if st.button("Login", key="login"):
        email = st.text_input("Enter Email Id")
        password = st.text_input("Enter password", type="password")
        st.button("Login Here", key="entry")
    


if nav == "About":
    st.markdown("## Email Spam Filtering")
    st.markdown("""Test""")
    


if nav == "Filter":
    st.markdown("# Hi, I am your _buddy Email Spam Filtering_")
#     st.markdown("## Click here to activate me")
#     if(st.button("Activate")):
#         progress = st.progress(0)
#         for i in range(100):
#             time.sleep(0.1)
#             progress.progress(i+1)
#         st.balloons()
    sentence = st.text_area("Input your sentence here:") 

    if st.button("Predict"):
        output = predict_mail(sentence)
        if output == 1:
            st.markdown('Its a Spam Email')
        else:
            st.markdown('Its Not a Spam Email')
        
     
                                                               
