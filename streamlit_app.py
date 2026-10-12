"""
FinStart – FinTech Financial Super-App
Streamlit Deployment Entry Point
"""

import os
import subprocess
import streamlit as st
import streamlit.components.v1 as components

# Configure Streamlit page settings
st.set_page_config(
    page_title="FinStart – FinTech Financial Super-App",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom CSS for seamless fullscreen integration
st.markdown(
    """
    <style>
        /* Hide Streamlit default header decorations */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Maximize workspace viewport */
        .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }

        /* Seamless iframe container */
        iframe {
            width: 100% !important;
            border: none !important;
            border-radius: 0px;
        }

        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #FFFFFF;
            border-right: 1px solid #E2E8F0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_INDEX_PATH = os.path.join(BASE_DIR, "dist", "index.html")

# Sidebar Information & Controls
with st.sidebar:
    st.markdown("### 🛡️ FinStart Project")
    st.caption("FinTech Financial Super-App • College Project")
    
    st.markdown(
        """
        **Educational Sandbox**:
        - 💳 ₹10,000 Virtual Wallet
        - 🎯 Targeted Savings Goals
        - 🧮 Loan & EMI Simulator
        - 📈 SIP Compounding Modeler
        - 🩺 100-Point Financial Health Score
        """
    )
    st.divider()

    app_height = st.slider(
        "Viewport Height (px)",
        min_value=750,
        max_value=1600,
        value=980,
        step=50,
        help="Adjust the display height for different screen sizes",
    )

    st.divider()
    st.markdown("##### 🚀 Deployment Info")
    st.caption(
        "Self-contained single-page bundle running inside Streamlit Components. "
        "Compatible with Streamlit Community Cloud, Docker, and local servers."
    )

    # Optional Rebuild button if Node is installed locally
    if st.button("🔨 Rebuild Frontend", help="Recompile React frontend with Vite"):
        with st.spinner("Building frontend..."):
            try:
                import shutil
                npm_bin = shutil.which("npm") or ("npm.cmd" if os.name == "nt" else "npm")
                env = os.environ.copy()
                local_node_bin = os.path.expanduser("~/.local/node/bin")
                if os.path.exists(local_node_bin):
                    env["PATH"] = f"{local_node_bin}:{env.get('PATH', '')}"
                
                result = subprocess.run(
                    [npm_bin, "run", "build"],
                    cwd=BASE_DIR,
                    env=env,
                    shell=(os.name == "nt"),
                    capture_output=True,
                    text=True,
                    check=True,
                )
                st.success("Frontend built successfully!")
                st.rerun()
            except Exception as e:
                st.error(f"Build failed: {e}")

# Check if production build exists
if not os.path.exists(DIST_INDEX_PATH):
    st.error("⚠️ Frontend build not found! Please build the React application first.")
    st.info("Run `npm run build` in your project directory to create `dist/index.html`.")
else:
    # Read self-contained bundled HTML
    with open(DIST_INDEX_PATH, "r", encoding="utf-8") as f:
        html_content = f.read()

    # Render seamless interactive component
    components.html(html_content, height=app_height, scrolling=True)
