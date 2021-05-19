from nltk.stem import WordNetLemmatizer
import streamlit as st
import time
import pickle
import nltk
import re
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')


def predict_mail(mail):

    model = pickle.load(open("model.pckl", mode="rb"))
    vectorizer = pickle.load(open("vectorizer.pckl", mode="rb"))

    lemma = WordNetLemmatizer()

    stopwords = nltk.corpus.stopwords.words('english')

    mail = re.sub(r"http\S+", "", mail)
    mail = re.sub("[^a-zA-Z0-9]", " ", mail)
    mail = mail.lower()
    mail = nltk.word_tokenize(mail)
    mail = [lemma.lemmatize(word) for word in mail]
    mail = [word for word in mail if word not in stopwords]
    mail = " ".join(mail)

    vector = vectorizer.transform([mail])
    decision = model.predict(vector.toarray())

    return decision[0]


st.title("SPAMIT")

nav = st.sidebar.radio("", ["Home", "About", "SpamIt"])

if nav == "Home":
    st.markdown("""<br/>""", True)
    st.markdown(""" Electronic spamming is the use of electronic messaging systems to send an
    unsolicited message (spam), especially advertising, as well as sending messages
    repeatedly on the same site.
    While the most widely recognized form of spam is email spam. The source and
    identity of the sender is anonymous and there is no option to cease receiving
    future e-mails. Spam e-mail is usually sent by spam bot, which is program that
    continually sends out email. Often spammers will create a virus that install a
    spam bot into unsuspecting users’ computers and will use their internet
    connection and computer to send spam. Also, spam e-mails are message
    randomly sent to multiple addressees by all sorts of groups, but mostly lazy
    advertisers and criminals who wish to lead you to phishing sites. The sites
    attempt to steal your personal, electronic, and financial information.
             """, True)

    st.image("./images/spam-2.jpg")
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
    st.markdown("## Email Spam Filtering ")
    st.markdown("""The objective of classification of Spam e-mails are - <br/>
    To classify the email into spam and non-spam
    <br/>
    <br/>
    With the help of text-classifier algorithms, rejecting mails based on text analysis
    can be serious problem in case of false positives. Normally users and
    organizations would not want any genuine e-mails to be lost. Black list approach
    has been one of the earliest approaches tried for the filtering of spams. The
    strategy is to accept all the mails except the ones from the domain/e-mail ids.
    With newer domains entering the category of spamming domains this strategy
    tends to not work so well. White list approach is the strategy of accepting the
    mails from the domains/addresses explicitly white listed and put others in a less
    priority queue, which is delivered only after sender responds to a confirmation
    request sent by the spam filtering system.
    """, True)
    st.image("./images/spam-1.png")


if nav == "SpamIt":
    st.markdown("# _Let's filter out your emails!_")
    sentence = st.text_area("Input your email/sentence here:")
    if st.button("Predict"):
        if sentence != "":
            output = predict_mail(sentence)
            if output == 1:
                st.markdown('### It\'s a SPAM Email')
            else:
                st.markdown('### It\'s NOT a SPAM Email')
