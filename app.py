import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Bot",
    layout="wide"
)

# Add custom styling - Dark theme with purple undertones
st.markdown("""
<style>
    /* Main background - dark with purple undertones */
    .stApp {
        background-color: #0a0a14;
        color: #e0d5ff;
    }
    
    /* Sidebar */
    .stSidebar {
        background-color: #1a1a2e;
    }
    
    /* Input fields */
    .stTextInput > div > div > input,
    .stChatInput > div > div > input {
        background-color: #2a2a4e !important;
        color: #e0d5ff !important;
        border: 1px solid #6d28d9 !important;
    }
    
    /* Chat messages */
    .stChatMessage {
        background-color: #1a1a2e;
        border-radius: 10px;
        padding: 15px;
        border-left: 3px solid #7c3aed;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #7c3aed;
        color: #f0e7ff;
        border: 1px solid #a78bfa;
    }
    
    .stButton > button:hover {
        background-color: #6d28d9;
        border-color: #c4b5fd;
    }
    
    /* Subheadings and text */
    .stSubheader {
        color: #c4b5fd;
    }
    
    /* Divider */
    hr {
        border-color: #6d28d9;
    }
</style>
""", unsafe_allow_html=True)

# Initialize login state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# Hardcoded credentials
VALID_USERNAME = "admin"
VALID_PASSWORD = "password"

def login_page():
    """Display login page"""
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        st.markdown("<h1 style='text-align: center; color: #c4b5fd;'>AI Bot Login</h1>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: #a78bfa;'>Enter your credentials</p>", unsafe_allow_html=True)
        
        st.divider()
        
        username = st.text_input("Username", placeholder="admin")
        password = st.text_input("Password", type="password", placeholder="••••••••")
        
        col_a, col_b, col_c = st.columns(3)
        with col_b:
            if st.button("Login", use_container_width=True):
                if username == VALID_USERNAME and password == VALID_PASSWORD:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")

def chatbot_page():
    """Display main chatbot interface"""
    # Logout button
    col1, col2 = st.columns([10, 1])
    with col2:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.messages = []
            st.rerun()
    
    st.markdown(f"<h1 style='color: #c4b5fd;'>🤖 AI Bot</h1>", unsafe_allow_html=True)
    st.markdown(f"<p style='color: #a78bfa;'>Welcome, {st.session_state.username}!</p>", unsafe_allow_html=True)

    # Sidebar
    st.sidebar.markdown("<h2 style='color: #c4b5fd;'>⚙️ Controls</h2>", unsafe_allow_html=True)

    if st.sidebar.button("🗑️ Reset Conversation"):
        st.session_state.messages = []
        st.rerun()

    # Model selection
    model = st.sidebar.selectbox("Choose Model", ["GPT-2", "Custom Model", "Offline LLM"])
    st.sidebar.markdown(f"<p style='color: #a78bfa;'>Current Model: <span style='color: #c4b5fd;'>{model}</span></p>", unsafe_allow_html=True)

    # Temperature setting
    temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
    st.sidebar.markdown(f"<p style='color: #a78bfa;'>Creativity: <span style='color: #c4b5fd;'>{temperature:.1f}</span></p>", unsafe_allow_html=True)

    # Session State for Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Layout: Chat + History Panel
    col1, col2 = st.columns([2, 1])

    # Main Chat Area
    with col1:
        st.markdown("<h3 style='color: #c4b5fd;'>💬 Chat Window</h3>", unsafe_allow_html=True)

        # Show old messages
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        # Input box
        user_input = st.chat_input("Type your message here...")

        if user_input:
            # Store user message
            st.session_state.messages.append({
                "role": "user",
                "content": user_input
            })

            # Display user message
            with st.chat_message("user"):
                st.markdown(user_input)

            # Temporary dummy bot response (replace with actual LLM call)
            bot_reply = f"You said: {user_input}"

            # Display assistant message
            with st.chat_message("assistant"):
                st.markdown(bot_reply)

            # Store assistant message
            st.session_state.messages.append({
                "role": "assistant",
                "content": bot_reply
            })

    # Conversation History Panel
    with col2:
        st.markdown("<h3 style='color: #c4b5fd;'>🕘 History</h3>", unsafe_allow_html=True)

        if not st.session_state.messages:
            st.markdown("<p style='color: #a78bfa;'>No conversation yet.</p>", unsafe_allow_html=True)
        else:
            for i, msg in enumerate(st.session_state.messages):
                role_icon = "🧑" if msg["role"] == "user" else "🤖"
                preview = msg["content"][:60].replace("\n", " ")
                st.markdown(f"<p style='color: #c4b5fd;'>**{role_icon} {msg['role'].capitalize()} {i+1}:**</p>", unsafe_allow_html=True)
                st.markdown(f"<p style='color: #a78bfa; font-size: 0.85em;'>{preview}{'...' if len(msg['content']) > 60 else ''}</p>", unsafe_allow_html=True)

        st.divider()
        st.markdown("<h4 style='color: #c4b5fd;'>ℹ️ Status</h4>", unsafe_allow_html=True)
        st.markdown("<p style='color: #86efac;'>✅ Connected</p>", unsafe_allow_html=True)
        col_m, col_c = st.columns(2)
        with col_m:
            st.markdown(f"<p style='color: #a78bfa;'>Messages: <span style='color: #c4b5fd;'>{len(st.session_state.messages)}</span></p>", unsafe_allow_html=True)

# Main App Logic
if st.session_state.logged_in:
    chatbot_page()
else:
    login_page()
