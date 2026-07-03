import streamlit as st
from PIL import Image

# -----------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------
st.set_page_config(
    page_title="EGSA Budget Closing Ceremony",
    page_icon="🎊",
    layout="wide"
)

# -----------------------------------------------------
# CUSTOM CSS (ANIMATION + DESIGN)
# -----------------------------------------------------
st.markdown("""
<style>

.stApp {
    background: linear-gradient(to bottom, #eef5ff, #ffffff);
}

.title {
    text-align:center;
    color:#0B5ED7;
    font-size:52px;
    font-weight:bold;
    animation: fadeIn 1s ease-in;
}

.subtitle {
    text-align:center;
    color:#444;
    font-size:22px;
    animation: fadeIn 1.5s ease-in;
}

.step {
    font-size:20px;
    color:#0B5ED7;
    font-weight:bold;
    text-align:center;
}

.box {
    background:white;
    border-radius:20px;
    padding:40px;
    box-shadow:0px 8px 25px rgba(0,0,0,0.15);
    animation: fadeIn 0.8s ease-in;
    transition:0.3s;
}

.box:hover {
    transform: scale(1.01);
}

.bigicon {
    font-size:100px;
    text-align:center;
}

.heading {
    text-align:center;
    color:#0B5ED7;
    font-size:38px;
    font-weight:bold;
}

.text {
    font-size:24px;
    text-align:center;
    line-height:1.8;
}

.footer {
    text-align:center;
    color:gray;
    margin-top:30px;
}

@keyframes fadeIn {
    from {opacity:0; transform:translateY(20px);}
    to {opacity:1; transform:translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# DATA
# -----------------------------------------------------
agenda = [
    {"title":"Simannaa Keessummootaa","icon":"🤝",
     "text":"Keessommoonnii fi kabajamtoot sirna sagantaa keenya irratti argaman bakka ni qabatu."},

    {"title":"Baniinsa Sagantaa","icon":"🙏",
     "text":"Sagantaan eebba Mangoddootaatiin ni saaqama."},

    {"title":"Ibsa Sochii Bara Baajeta 2018 fi Karoora 2019","icon":"📊",
     "text":"Hojiiwwan bara 2018, milkaa'ina fi karoora 2019 ni ibsama."},

    {"title":"Yaada Marii fi Duubdeebii","icon":"💬",
     "text":"Yaadonni ijaarsaa fi qeeqaa Miseensota fi Keessummoota irraa ni eegama."},

    {"title":"Waraqaa Beekamtii","icon":"📜",
     "text":"Miseensota hojii boonsaa hojjetaniif ni kennama."},

    {"title":"Sirna Badhaasaa","icon":"🏆",
     "text":"Sadarkaa 1ffaa hanga 3ffaa Miseensota hojii isaaniitiin ga`uumsaan qabxii olaanaa argataniif badhaasni ni kennama."},

    {"title":"Qoodinsa Bu'aa Share","icon":"💰",
     "text":"Bu'aan qabeenya miseensotaa irratti hundaa'ee haaluma qaneenya isaanitiin ni qoodamaaf."},

    {"title":"Lottery","icon":"🎁",
     "text":"Carraan ni buufama."},

    {"title":"Galateeffannaa","icon":"👏",
     "text":"Hirmaattota hundaaf galateeffannaan ni dhiyaata."},

    {"title":"Cufiinsa Sagantaa","icon":"🎉",
     "text":"Sagantaan eebbaan eegale eebbaan ni xumurama."}
]

# -----------------------------------------------------
# SESSION STATE
# -----------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = 0

page = st.session_state.page
current = agenda[page]
total = len(agenda)

# -----------------------------------------------------
# LOGO
# -----------------------------------------------------
try:
    logo = Image.open("EGSA _.png")
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.image(logo, width=170)
except:
    st.warning("Logo file not found (EGSA _.png)")

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------
st.markdown("""
<div class="title">
ECONOMIC GROWTH SOLUTION ASSOCIATION (EGSA)
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="subtitle">
Sirna Gamaaggamaa fi Cufiinsa Bara Baajeta 2018<br>
Akkasumas Wixinee Karoora Bara 2019 ni dhihaata.
</div>
""", unsafe_allow_html=True)

st.divider()

# -----------------------------------------------------
# PROGRESS
# -----------------------------------------------------
st.progress((page+1)/total)
st.markdown(f"<div class='step'>STEP {page+1} / {total}</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# MAIN CARD
# -----------------------------------------------------
st.markdown("<div class='box'>", unsafe_allow_html=True)

st.markdown(f"<div class='bigicon'>{current['icon']}</div>", unsafe_allow_html=True)

st.markdown(f"<div class='heading'>{current['title']}</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"<div class='text'>{current['text']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# EFFECTS
# -----------------------------------------------------
if current["title"] == "Sirna Badhaasaa":
    st.balloons()

if current["title"] == "Lottery":
    st.snow()

if current["title"] == "Qoodinsa Bu'aa Share":
    st.success("💰 Bu'aan Share ni qoodama.")

# -----------------------------------------------------
# NAVIGATION
# -----------------------------------------------------
col1, col2, col3 = st.columns([1,2,1])

with col1:
    if st.button("⬅ Previous", use_container_width=True):
        if st.session_state.page > 0:
            st.session_state.page -= 1
            st.rerun()

with col3:
    if st.button("Next ➡", use_container_width=True):
        if st.session_state.page < total-1:
            st.session_state.page += 1
            st.rerun()

# -----------------------------------------------------
# SIDEBAR
# -----------------------------------------------------
with st.sidebar:
    st.header(" Akkaataa adeemsa sagantaa")

    for i, item in enumerate(agenda):
        if st.button(f"{i+1}. {item['title']}", key=i):
            st.session_state.page = i
            st.rerun()

    st.divider()
    st.success(f"Step {page+1} of {total}")

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------
st.divider()

st.markdown("""
<div class="footer">

<h2>🌟 Dhaadannoo Guyyichaa 🌟</h2>

<h3 style="color:#0B5ED7;">
Tokkummaan ni guddanna<br>
Qusannaa aadaa hojii godhanna<br>
Hojii fi Kutannoon immoo<br>
Milkaa'ina ni gonfanna
</h3>

</div>
""", unsafe_allow_html=True)
