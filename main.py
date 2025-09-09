import streamlit as st
import requests
import textwrap

st.set_page_config(
    page_title="SmartTestFramework Installer",
    page_icon="🛠️",
    layout="centered"
)

# ----- Versions -----
versions = [
    {"id": "v0", "title": "SmartTestFramework v0", "status": "available",
     "link": "https://github.com/thenameis-varun/SmartTestFramework/archive/refs/heads/main.zip"},
    {"id": "v1", "title": "Version 1", "status": "coming"},
    {"id": "v2", "title": "Version 2", "status": "coming"},
    {"id": "v3", "title": "Version 3", "status": "coming"},
]

if "selected_version" not in st.session_state:
    st.session_state.selected_version = "v0"

# ----- CSS -----
st.markdown("""
<style>
.scroll-box {
    display:flex;
    gap:16px;
    overflow-x:auto;
    padding:10px;
    max-width:700px;
    margin:auto;
}
.version-card {
    flex:0 0 260px;
    background:linear-gradient(180deg, rgba(24,40,68,0.95), rgba(18,30,56,0.95));
    border-radius:12px;
    padding:20px;
    text-align:center;
    color:#E8F4FF;
    font-weight:600;
    transition:all 0.2s ease;
    cursor:pointer;
}
.version-card:hover {
    transform:translateY(-5px);
    box-shadow:0 8px 24px rgba(10,20,40,0.5);
}
.selected { outline: 3px solid rgba(120,170,255,0.55); }
.coming {
    border:1px dashed rgba(160,170,190,0.25);
    opacity:0.35;
    cursor:not-allowed;
}
.folder-emoji { font-size:42px; margin-bottom:10px; }
.ver-title { font-size:16px; font-weight:600; }
.step-header { font-size:20px; font-weight:700; margin-top:24px; margin-bottom:12px; text-align:center; }

/* Page Heading */
.page-header {
    font-size:40px;
    font-weight:900;
    text-align:center;
    margin-top:10px;
    margin-bottom:30px;
    color:#ffffff;
}

/* Download button */
.dl-btn button {
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
    color: white !important;
    border: none !important;
    padding: 14px 28px !important;
    border-radius: 14px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    transition: all 0.3s ease-in-out !important;
}
.dl-btn button:hover {
    transform: scale(1.05) translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,0.45) !important;
    background: linear-gradient(90deg, #43e97b, #38f9d7) !important;
}
.dl-btn button:active {
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important; /* stays blue */
    color: white !important;
}

/* Quick usage wrapper */
.quick-usage-wrapper {
    width: 100%;
    margin: 20px 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
    padding: 10px;
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px;
    background: linear-gradient(180deg, rgba(18,28,44,0.85), rgba(10,18,36,0.85));
}

/* Usage card styles */
.usage-card {
    width: 260px;  
    background: linear-gradient(180deg, rgba(18,28,44,0.65), rgba(10,18,36,0.65));
    border-radius: 12px;
    padding: 10px;
    color: #E8F4FF;
    box-shadow: 0 6px 18px rgba(0,0,0,0.35);
    border: 1px solid rgba(255,255,255,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    overflow: hidden;
}
.usage-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 30px rgba(0,0,0,0.55);
}

/* Heights by level */
.usage-card.top { height: 66px; }     /* +10% */
.usage-card.mid { height: 85px; }    
.usage-card.leaf { height: 110px; }  

/* Only increase height of element 3 (Dashboard Tab) */
.usage-card.top.dashboard { height: 66px; }

/* Tree text */
.tree-title { 
    font-family: Arial, sans-serif;
    font-weight: 900; 
    font-size: 15px; 
    margin-bottom: 4px; 
    color: #ffffff; 
    text-transform: uppercase;
}
.tree-content { 
    font-size: 13px; 
    color: #a5c7e5; 
    line-height: 1.3; 
    flex-grow: 1; 
    overflow-wrap: break-word; 
    transition: color 0.25s ease;
}
.usage-card:hover .tree-content {
    color: #ffffff;
}

/* Indentation */
.subcard.mid { margin-left: calc(50% - 130px); }      
.subsubcard.leaf { margin-left: calc(100% - 260px); } 

/* Inline code look */
.quick-usage-wrapper code {
    background: rgba(255,255,255,0.07);
    padding: 2px 6px;
    border-radius: 6px;
    font-family: monospace;
    font-size: 13px;
    color: #E8F4FF;
}
</style>
""", unsafe_allow_html=True)

# ----- Page Heading -----
st.markdown('<div class="page-header">SmartTestFramework — Archive</div>', unsafe_allow_html=True)

# ----- Step 1: Framework Versions -----
st.markdown('<div class="step-header">Select Framework Version</div>', unsafe_allow_html=True)

cols_html = '<div class="scroll-box">'
for v in versions:
    sel_cls = "selected" if st.session_state.selected_version == v["id"] else ""
    if v["status"] == "available":
        cols_html += f"""
        <div class="version-card {sel_cls}">
            <div class="folder-emoji">📂</div>
            <div class="ver-title">{v['title']}</div>
        </div>"""
    else:
        cols_html += f"""
        <div class="version-card coming">
            <div class="folder-emoji">🗂️</div>
            <div class="ver-title">Coming Soon</div>
        </div>"""
cols_html += "</div>"
st.markdown(cols_html, unsafe_allow_html=True)

# ----- Step 2: Download Package -----
st.markdown('<div class="step-header">Download Package</div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="dl-btn">', unsafe_allow_html=True)
    download_url = "https://github.com/thenameis-varun/SmartTestFramework/archive/refs/heads/main.zip"
    response = requests.get(download_url)
    zip_data = response.content
    st.download_button(
        label="⬇️ Download ",
        data=zip_data,
        file_name="SmartTestFramework_V0.zip",
        mime="application/zip",
        use_container_width=True,
    )
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Step 3: Quick Usage -----
st.markdown('<div class="step-header">Quick User Manual</div>', unsafe_allow_html=True)

quick_usage_html = textwrap.dedent("""
<div class="quick-usage-wrapper">

  <div class="usage-card top">
    <div class="tree-title">1.launch Framework</div>
    <div class="tree-content">Unzip package & use launch.bat/launch.sh</div>
  </div>

  <div class="usage-card top">
    <div class="tree-title">2. Main Tab</div>
    <div class="tree-content">Job Triggering</div>
  </div>

  <div class="usage-card mid subcard mid">
    <div class="tree-title">a. Select the DUT</div>
    <div class="tree-content">Choose a device to test</div>
  </div>

  <div class="usage-card leaf subsubcard leaf">
    <div class="tree-title">i. Serial connection</div>
    <div class="tree-content">Choose amongst pre-registered DUT's,     Note: Update the relevant DUT info at hardware.py and relevant serial commands at src/plugins/tests/.</div>
  </div>

  <div class="usage-card leaf subsubcard leaf">
    <div class="tree-title">ii. Auto Detect Device</div>
    <div class="tree-content">Choose amongst reachable devices, Note: Make sure the desired device is in LAN and has Openssh running</div>
  </div>

  <div class="usage-card mid subcard mid">
    <div class="tree-title">c. AI suggestion</div>
    <div class="tree-content">QLearning Agent will train dynamically on job catalog & suggest optimal parameters</div>
  </div>

  <div class="usage-card mid subcard mid">
    <div class="tree-title">d. Run Test</div>
    <div class="tree-content">Submit the job.</div>
  </div>

  <div class="usage-card mid subcard mid">
    <div class="tree-title">e. Job Status</div>
    <div class="tree-content">Track the lifecycle of jobs triggered.</div>
  </div>

  <div class="usage-card top">
    <div class="tree-title">3. Dashboard Tab</div>
    <div class="tree-content">Job History</div>
  </div>

  <div class="usage-card mid subcard mid">
    <div class="tree-title">a. Default mode</div>
    <div class="tree-content">Select the Hardware class or Test name, View dynamically rendered visuals</div>
  </div>

  <div class="usage-card mid subcard mid">
    <div class="tree-title">b. Remote device mode</div>
    <div class="tree-content">Select any combination of registered usernames and corresponding tests.</div>
  </div>

</div>
""").strip()

st.markdown(quick_usage_html, unsafe_allow_html=True)


# ----- CSS for consistent button styling -----
st.markdown("""
<style>
/* Demo & More Info buttons */
.custom-btn {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    color: white;
    font-weight: 600;
    font-size: 15px;
    padding: 10px 20px;
    border-radius: 10px;
    border: none;
    cursor: pointer;
    transition: all 0.3s ease;
}
.custom-btn:hover {
    transform: scale(1.05) translateY(-2px);
    box-shadow: 0 6px 16px rgba(0, 114, 255, 0.5);
}

/* Keep download button always blue */
.dl-btn button {
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important;
    color: white !important;
    border: none !important;
    padding: 14px 28px !important;
    border-radius: 14px !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    box-shadow: 0 4px 12px rgba(0,0,0,0.25) !important;
    transition: all 0.3s ease-in-out !important;
}
.dl-btn button:hover {
    transform: scale(1.05) translateY(-2px) !important;
    box-shadow: 0 8px 18px rgba(0,0,0,0.45) !important;
    background: linear-gradient(90deg, #43e97b, #38f9d7) !important;
}
.dl-btn button:active {
    background: linear-gradient(90deg, #00c6ff, #0072ff) !important; /* prevent turning red */
}
</style>
""", unsafe_allow_html=True)

# ----- Demo -----
st.markdown("""
<div style="display:flex; justify-content:center; align-items:center; gap:12px; margin-top:20px;">
    <span style="font-size:16px; font-weight:600; color:white;">SmartTestFramework Demo →</span>
    <a href="https://smart-test-framework-it-probably-works.streamlit.app/" target="_blank">
        <button class="custom-btn">Open</button>
    </a>
</div>
""", unsafe_allow_html=True)
st.markdown(
    "<p style='font-size:14px; color:#cccccc; margin-top:8px; margin-bottom:0; text-align:center;'>"
    "⚠️ Notice: Please download from current page and run the framework locally to enable auto-detection of devices in the LAN and to use a dedicated (unshared) database."
    "</p>",
    unsafe_allow_html=True,
)

# ----- More Info -----
st.markdown("""
<div style="display:flex; justify-content:center; align-items:center; gap:12px; margin-top:20px;">
    <span style="font-size:16px; font-weight:600; color:white;">SmartTestFramework More Info →</span>
    <a href="https://github.com/thenameis-varun/SmartTestFramework/blob/main/README.md" target="_blank">
        <button class="custom-btn">Open</button>
    </a>
</div>
""", unsafe_allow_html=True)
