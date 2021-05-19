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

nav = st.sidebar.radio("", ["Home", "About", "Our Team", "SpamIt"])

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

if nav == "Our Team":
    col1, col2, col3 = st.beta_columns(3)
    col1.markdown("### Warren Fernandes")
    col1.markdown("_\"Its Time to Roll\"_")
    col2.markdown("### Liny Mathew")
    col2.markdown("_\"Its Time to Rock\"_")
    col3.markdown("### Yash Deshmukh")
    col3.markdown("_\"Its Time for Shava Shava\"_")
    st.markdown("""<br>""", True)
    st.markdown("_\"~Your incharge of how you feel. Don't let anyone kill your vibe. Lets stop spams\"_", True)
    st.markdown("""<br>""", True)
    st.image("images/team.jpeg")

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

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Developed with ❤ by <a style='display: block; text-align: center;' href="https://www.linkedin.com/in/warren-fernandes-a354281a3/" target="_blank">Warren <a href="https://www.linkedin.com/in/yash-deshmukh-21576b160/">Yash <a href="https://www.linkedin.com/in/linymathew/" >Liny</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

