def login_page():
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1.2, 1.2, 1.2])

    with col2:
        st.markdown('<div class="custom-card">', unsafe_allow_html=True)
        st.markdown('<div class="login-title">🤖 AI Bot Login</div>', unsafe_allow_html=True)
        st.markdown('<div class="login-subtitle">Secure access to your intelligent assistant</div>', unsafe_allow_html=True)

        # Pre-filled demo credentials
        username = st.text_input("Username", value="admin", placeholder="Enter username")
        password = st.text_input("Password", value="password123", type="password", placeholder="Enter password")

        st.markdown("<br>", unsafe_allow_html=True)

        # Normal login button
        if st.button("Login", use_container_width=True):
            if username == VALID_USERNAME and password == VALID_PASSWORD:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("❌ Invalid username or password")

        st.markdown("<br>", unsafe_allow_html=True)

        # Demo Login button
        if st.button("🚀 Demo Login", use_container_width=True):
            st.session_state.logged_in = True
            st.session_state.username = VALID_USERNAME
            st.rerun()

        # Demo info box
        st.markdown("""
        <div class="demo-box">
            <h4 style="color:#ddd6fe; margin-bottom:10px;">🔐 Demo Mode Ready</h4>
            <p style="color:#c4b5fd; margin:0;">Username and password are already filled in.</p>
            <p style="color:#c4b5fd; margin:0;">You can click <b>Login</b> or simply use <b>Demo Login</b>.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
