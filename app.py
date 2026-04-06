import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Bot",
    page_icon="💜",
    layout="wide"
)

# -----------------------------
# Custom Professional Styling
# -----------------------------
st.markdown("""
<style>
    /* Main App Background */
    .stApp {
        background: linear-gradient(135deg, #0a0a14 0%, #111827 40%, #1a103d 100%);
        color: #f3e8ff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827 0%, #1a1a2e 100%);
        border-right: 1px solid rgba(167, 139, 250, 0.15);
    }

    /* General Card Style */
    .custom-card {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(167, 139, 250, 0.15);
        border-radius: 20px;
        padding: 28px;
        box-shadow: 0 8px 32px rgba(124, 58, 237, 0.15);
        backdrop-filter: blur(10px);
    }

    /* Login Title */
    .login-title {
        text-align: center;
        color: #ddd6fe;
        font-size: 2.2rem;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .login-subtitle {
        text-align: center;
        color: #a78bfa;
        font-size: 1rem;
        margin-bottom: 25px;
    }

    /* Inputs */
    .stTextInput > div > div > input,
    .stChatInput > div > div > textarea,
    .stChatInput input {
        background-color: rgba(42, 42, 78, 0.95) !important;
        color: #f3e8ff !important;
        border: 1px solid #7c3aed !important;
        border-radius: 12px !important;
        padding: 12px !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(90deg, #7c3aed, #9333ea);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 18px;
        font-weight: 600;
        transition: 0.3s ease;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.25);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        background: linear-gradient(90deg, #6d28d9, #7e22ce);
        box-shadow: 0 6px 18px rgba(124, 58, 237, 0.35);
    }

    /* Chat Messages */
    .stChatMessage {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(167, 139, 250, 0.15);
        border-radius: 18px;
        padding: 16px;
        margin-bottom: 10px;
        box-shadow: 0 4px 12px rgba(124, 58, 237, 0.08);
    }

    /* Titles */
    h1, h2, h3, h4 {
        color: #ddd6fe !important;
    }

    /* Divider */
    hr {
        border-color: rgba(167, 139, 250, 0.2);
    }

    /* Status Badge */
    .status-badge {
        background: rgba(34, 197, 94, 0.15);
        color: #86efac;
        padding: 8px 14px;
        border-radius: 999px;
        display: inline-block;
        font-weight: 600;
        font-size: 0.9rem;
        border: 1px solid rgba(34, 197, 94, 0.2);
    }

    /* History Box */
    .history-box {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(167, 139, 250, 0.12);
        border-radius: 14px;
        padding: 12px;
        margin-bottom: 10px;
    }

    /* Small text */
    .muted-text {
        color: #c4b5fd;
        font-size: 0.92rem;
    }

    /* Demo box */
    .demo-box {
        background: rgba(124, 58, 237, 0.12);
        border: 1px solid rgba(167, 139, 250, 0.18);
        border-radius: 14px;
        padding: 15px;
        margin-top: 18px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# Demo Credentials
# -----------------------------
VALID_USERNAME = "admin"
VALID_PASSWORD = "password123"

# -----------------------------
# Login Page
# -----------------------------
def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 1.2, 1.2])

    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">💜 AI Bot</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Your intelligent assistant is waiting ✨</div>', unsafe_allow_html=True)

        # Pre-filled demo credentials
        username = st.text_input(
            "Username",
            value="admin",
            placeholder="Enter username"
        )

        password = st.text_input(
            "Password",
            value="password123",
            type="password",
            placeholder="Enter password"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        # Normal Login Button
        if st.button("Login", use_container_width=True):
            if username == VALID_USERNAME and password == VALID_PASSWORD:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

        st.markdown("<br>", unsafe_allow_html=True)

        # Demo Login Button
        if st.button("🚀 Demo Login", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.username = VALID_USERNAME
            st.rerun()

        # Demo Info Box
        st.markdown("""
        <div class="demo-box">
            <h4 style="color:#ddd6fe; margin-bottom:10px;">🔐 Demo Login Ready</h4>
            <p style="color:#c4b5fd; margin:0;"><b>Username:</b> admin</p>
            <p style="color:#c4b5fd; margin:0;"><b>Password:</b> password123</p>
            <p style="color:#c4b5fd; margin-top:10px;">You can press <b>Login</b> or simply click <b>Demo Login</b>.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Chatbot Page
# -----------------------------
def chatbot_page():
    # Top Bar
    col1, col2 = st.columns([10, 1])

    with col1:
        st.markdown(f"<h1>💜 AI Bot</h1>", unsafe_allow_html=True)
        st.markdown(f"<p class='muted-text'>Welcome back, <b>{st.session_state.username}</b> 👋</p>", unsafe_allow_html=True)

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.messages = []
            st.rerun()

    # Sidebar
    st.sidebar.markdown("## ⚙️ Controls")

    if st.sidebar.button("🗑️ Reset Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.sidebar.markdown("---")

    model = st.sidebar.selectbox(
        "Choose Model",
        ["GPT-2", "Custom Model", "Offline LLM"]
    )

    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**Current Model:** `{model}`")
    st.sidebar.markdown(f"**Creativity Level:** `{temperature:.1f}`")

    # Main Layout
    col1, col2 = st.columns([2.2, 1])

    # Chat Area
    with col1:
        st.markdown("### 💬 Chat Window")

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        user_input = st.chat_input("Type your message here...")

        if user_input:
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            with st.chat_message("user"):
                st.markdown(user_input)

            # Dummy response (replace later with Ollama / LLM)
            bot_reply = f"✨ You said: **{user_input}**"

            with st.chat_message("assistant"):
                st.markdown(bot_reply)

            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_reply
            })

    # History Panel
    with col2:
        st.markdown("### 🕘 Conversation History")

        if not st.session_state.messages:
            st.markdown(
                '<div class="history-box"><p class="muted-text">No conversation yet.</p></div>',
                unsafe_allow_html=True
            )
        else:
            for i, msg in enumerate(st.session_state.messages):
                role_icon = "🧑" if msg["role"] == "user" else "🤖"
                preview = msg["content"][:60].replace("\n", " ")
                st.markdown(f"""
                <div class="history-box">
                    <p style="color:#ddd6fe; margin-bottom:5px;"><b>{role_icon} {msg['role'].capitalize()} {i+1}</b></p>
                    <p style="color:#a78bfa; font-size:0.88rem; margin:0;">{preview}{'...' if len(msg['content']) > 60 else ''}</p>
                </div>
                """, unsafe_allow_html=True)

        st.divider()
        st.markdown("### ℹ️ Status")
        st.markdown('<div class="status-badge">✅ UI Active</div>', unsafe_allow_html=True)
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"**Messages:** `{len(st.session_state.messages)}`")
        st.markdown(f"**Logged in as:** `{st.session_state.username}`")

# -----------------------------
# Main App Logic
# -----------------------------
if st.session_state.logged_in:
    chatbot_page()
else:
    login_page() now tell me how to connect this code with ollama
