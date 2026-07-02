import streamlit as st

# -----------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------
st.set_page_config(
    page_title="EGSA Budget Closing Ceremony",
    page_icon="🎊",
    layout="wide"
)

# -----------------------------------------------------
# CUSTOM CSS
# -----------------------------------------------------
st.markdown("""
<style>

.main{
    background-color:#f7f9fc;
}

.title{
    text-align:center;
    color:#0B5ED7;
    font-size:48px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#444;
    font-size:22px;
}

.step{
    font-size:20px;
    color:#666;
    font-weight:bold;
}

.box{
    background:white;
    border-radius:20px;
    padding:35px;
    box-shadow:0px 0px 15px rgba(0,0,0,0.15);
}

.bigicon{
    font-size:90px;
    text-align:center;
}

.heading{
    text-align:center;
    color:#0B5ED7;
    font-size:36px;
    font-weight:bold;
}

.text{
    font-size:24px;
    text-align:center;
    line-height:1.8;
}

.footer{
    text-align:center;
    color:gray;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------
# DATA
# -----------------------------------------------------

agenda = [
    {
        "title": "Simannaa Keessummootaa",
        "icon": "🤝",
        "text": "Keessummoonni kabajamoon, miseensonni fi affeeramtoonni gara galma sagantichaatti dhufanii bakka isaanii qabatu."
    },
    {
        "title": "Baniinsa Sagantaa",
        "icon": "🙏",
        "text": "Sagantaan eebba mootummaa Waaqayyootiin ni saaqama."
    },
    {
        "title": "Ibsa Sochii Bara Baajeta 2018 fi Karoora Bara 2019",
        "icon": "📊",
        "text": """Dura Taa'aan EGSA hojiiwwan bara baajeta 2018 keessatti
raawwataman irratti ibsa bal'aa ni kenna.

Milkaa'inoota,
qormaata,
barnoota irraa argaman ni ibsama.

Karoora bara baajeta 2019 ni ifoomsa."""
    },
    {
        "title": "Yaada Marii fi Duubdeebii",
        "icon": "💬",
        "text": """Miseensota muraasa irraa yaadni marii ni fudhatama.

Keessummoota kabajamoo irraa yaadni ijaaraa ni kennama."""
    },
    {
        "title": "Waraqaa Beekamtii",
        "icon": "📜",
        "text": "Miseensota hojii boonsaa hojjetaniif Waraqaan Beekamtii ni kennama."
    },
    {
        "title": "Sirna Badhaasaa",
        "icon": "🏆",
        "text": """Miseensota hojii isaanii irratti hundaa'uun

🥇 1ffaa

🥈 2ffaa

🥉 3ffaa

badhaasni addaa ni kennama."""
    },
    {
        "title": "Qoodinsa Bu'aa Share",
        "icon": "💰",
        "text": "Bu'aan waggaa keessatti argame akka Share miseensotaa irratti hundaa'ee ni qoodama."
    },
    {
        "title": "Lottery",
        "icon": "🎁",
        "text": "Carraan mootummaa sagantichaaf qophaa'e ni buufama."
    },
    {
        "title": "Galateeffannaa",
        "icon": "👏",
        "text": "Miseensotaa, Keessummootaa fi Deeggartoota hundaaf galateeffannaan ni dhiyaata."
    },
    {
        "title": "Cufiinsa Sagantaa",
        "icon": "🎉",
        "text": "Sagantaan akkuma eebbaan itti baname eebbaan ni xumurama."
    }
]

# -----------------------------------------------------
# SESSION STATE
# -----------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = 0

total = len(agenda)

current = agenda[st.session_state.page]

# -----------------------------------------------------
# HEADER
# -----------------------------------------------------

st.markdown('<div class="title">🎊 EGSA 🎊</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">'
    'Sirna Gamaaggamaa fi Cufiinsa Bara Baajeta 2018'
    '<br>'
    'Akkasumas Eegala Karoora Bara 2019'
    '</div>',
    unsafe_allow_html=True
)

st.divider()

# -----------------------------------------------------
# PROGRESS
# -----------------------------------------------------

progress = (st.session_state.page + 1) / total

st.progress(progress)

st.markdown(
    f"<div class='step'>STEP {st.session_state.page+1} OF {total}</div>",
    unsafe_allow_html=True
)

# -----------------------------------------------------
# MAIN CARD
# -----------------------------------------------------

st.markdown('<div class="box">', unsafe_allow_html=True)

st.markdown(
    f"<div class='bigicon'>{current['icon']}</div>",
    unsafe_allow_html=True
)

st.markdown(
    f"<div class='heading'>{current['title']}</div>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    f"<div class='text'>{current['text']}</div>",
    unsafe_allow_html=True
)

st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------------------------------
# SPECIAL EFFECTS
# -----------------------------------------------------

if current["title"] == "Sirna Badhaasaa":
    st.balloons()

if current["title"] == "Lottery":
    st.snow()

# -----------------------------------------------------
# BUTTONS
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

    st.header("Agenda")

    for i, item in enumerate(agenda):

        if st.button(
            f"{i+1}. {item['title']}",
            key=i,
            use_container_width=True
        ):
            st.session_state.page = i
            st.rerun()

    st.divider()

    st.success(f"Current Step : {st.session_state.page+1}/{total}")

# -----------------------------------------------------
# FOOTER
# -----------------------------------------------------

st.divider()

st.markdown(
"""
<div class='footer'>

<h3>🌟 Dhaadannoo Guyyichaa 🌟</h3>

<h2>
"Tokkummaan ni guddanna,
Qusannaan ni badhaanna,
Hojii fi Kutannoon immoo
Milkaa'ina ni Gonfanna."
</h2>

</div>
""",
unsafe_allow_html=True
)