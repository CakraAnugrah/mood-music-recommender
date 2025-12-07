import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import random

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Mood Music Recommender",
    page_icon="🎵",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== INITIALIZE SESSION STATE ==========
if 'predicted_emotion' not in st.session_state:
    st.session_state.predicted_emotion = None
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'emotion_history' not in st.session_state:
    st.session_state.emotion_history = []

# ========== EMOTION THEMES ==========
emotion_themes = {
    "joy": {
        "primary": "#FFD700",
        "secondary": "#FFA500",
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "bg": "linear-gradient(135deg, #FFF5E6 0%, #FFE5B4 50%, #FFD98E 100%)",
        "particle": "#FFD700",
        "emoji": "😊"
    },
    "sadness": {
        "primary": "#4A90E2",
        "secondary": "#5E7CE2",
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "bg": "linear-gradient(135deg, #E8EAF6 0%, #C5CAE9 50%, #9FA8DA 100%)",
        "particle": "#4A90E2",
        "emoji": "😢"
    },
    "anger": {
        "primary": "#E74C3C",
        "secondary": "#C0392B",
        "gradient": "linear-gradient(135deg, #f5576c 0%, #c0392b 100%)",
        "bg": "linear-gradient(135deg, #FFEBEE 0%, #FFCDD2 50%, #EF9A9A 100%)",
        "particle": "#E74C3C",
        "emoji": "😡"
    },
    "fear": {
        "primary": "#9B59B6",
        "secondary": "#8E44AD",
        "gradient": "linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)",
        "bg": "linear-gradient(135deg, #F3E5F5 0%, #E1BEE7 50%, #CE93D8 100%)",
        "particle": "#9B59B6",
        "emoji": "😨"
    },
    "love": {
        "primary": "#E91E63",
        "secondary": "#F06292",
        "gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)",
        "bg": "linear-gradient(135deg, #FCE4EC 0%, #F8BBD0 50%, #F48FB1 100%)",
        "particle": "#E91E63",
        "emoji": "❤️"
    },
    "default": {
        "primary": "#667eea",
        "secondary": "#764ba2",
        "gradient": "linear-gradient(135deg, #667eea 0%, #764ba2 100%)",
        "bg": "linear-gradient(135deg, #E8EAF6 0%, #D1C4E9 50%, #B39DDB 100%)",
        "particle": "#667eea",
        "emoji": "🎵"
    }
}

# ========== DATA DICTIONARIES ==========
youtube_videos = {
    "joy": [
        ("The Man in the Photo | Comedy Short Film", "https://www.youtube.com/watch?v=u6WpwmPe9Ks", "u6WpwmPe9Ks"),
        ("Michael Cera - Gregory Go Boom", "https://www.youtube.com/watch?v=LE8kTPtLftI", "LE8kTPtLftI"),
        ("Coffee Is Important", "https://www.youtube.com/watch?v=8_CPZgGw5-Y", "8_CPZgGw5-Y")
    ],
    "sadness": [
        ("MANA JANJI AYAH?", "https://www.youtube.com/watch?v=sy_Z4uspslA", "sy_Z4uspslA"),
        ("KESEPIAN", "https://www.youtube.com/watch?v=wX3QNXmYfXg", "wX3QNXmYfXg"),
        ("Love Is Not Enough", "https://www.youtube.com/watch?v=uW7LiR1H3wA", "uW7LiR1H3wA")
    ],
    "anger": [
        ("The Honest Critic", "https://www.youtube.com/watch?v=3QMRfStEctk", "3QMRfStEctk"),
        ("GARA-GARA BURUNG", "https://www.youtube.com/watch?v=-LcMSZ44ees", "-LcMSZ44ees"),
        ("Anger Management", "https://www.youtube.com/watch?v=zJg77RPKzJw", "zJg77RPKzJw")
    ],
    "fear": [
        ("The Present", "https://www.youtube.com/watch?v=3XA0bB79oGc", "3XA0bB79oGc"),
        ("Alike", "https://www.youtube.com/watch?v=FE5F5FJg-5M", "FE5F5FJg-5M"),
        ("Joy Story", "https://www.youtube.com/watch?v=ZQGuVKHtrxc", "ZQGuVKHtrxc")
    ],
    "love": [
        ("ROMANTIC CRUSH", "https://www.youtube.com/watch?v=SH7_RFn7Mqo", "SH7_RFn7Mqo"),
        ("RAHASIA CINTAKU", "https://www.youtube.com/watch?v=Kjj0M9AOTKw", "Kjj0M9AOTKw"),
        ("CINTA DI PENGHUJUNG MALAM", "https://www.youtube.com/watch?v=zFaaVwN5J0c", "zFaaVwN5J0c")
    ]
}

indo_emotions = {
    "kesel": "anger", "marah": "anger", "bete": "anger", "emosi": "anger",
    "takut": "fear", "cemas": "fear", "khawatir": "fear", "deg-degan": "fear",
    "senang": "joy", "bahagia": "joy", "gembira": "joy", "ceria": "joy",
    "sedih": "sadness", "kecewa": "sadness", "galau": "sadness",
    "sayang": "love", "cinta": "love", "rindu": "love", "kangen": "love",
}

mood_boosters = {
    "joy": [
        "Keep smiling! Your happiness is contagious 😊",
        "You're glowing today — keep that positive energy!",
        "Enjoy this moment, you deserve all the joy ✨"
    ],
    "sadness": [
        "It's okay to feel sad. Take your time 💛",
        "Bad days happen, but they don't define you.",
        "You're not alone — brighter days are coming 🤍"
    ],
    "anger": [
        "Take a deep breath… you're doing great 😮‍💨",
        "It's okay to be upset, just don't let it stay too long.",
        "Your peace matters 🕊️"
    ],
    "fear": [
        "You're braver than you think 💪",
        "Whatever you're facing, you can get through it.",
        "Every storm eventually passes 🌤️"
    ],
    "love": [
        "Your heart is warm — keep spreading love 💖",
        "Someone appreciates you more than you know.",
        "Love looks beautiful on you ✨"
    ]
}

daily_challenges = {
    "joy": ["Share happiness: kirim pesan positif 🎉", "Foto hal yang bikin senang 📸", "Dengerin lagu happy 🎶"],
    "sadness": ["Tulis 3 hal yang disyukuri 📝", "Minum teh hangat ☕", "Jalan 5 menit 🚶‍♂️"],
    "anger": ["10 deep breaths 😮‍💨", "Tulis rasa marah ✍️", "Stretching 1 menit 🧘"],
    "fear": ["Tulis ketakutan & cara hadapi 📝", "Grounding: 5 barang sekitar 👀", "Minum air pelan 💧"],
    "love": ["Kirim pesan manis 💌", "Tulis hal yang dicintai diri ❤️", "Lagu mellow 🎧"]
}

gauge_emoji = {"joy": "😊", "sadness": "😢", "anger": "😡", "fear": "😨", "love": "❤️"}

spotify_recommendations = {
    "joy": [
        {"title": "Happy", "artist": "Pharrell Williams", "uri": "60nZcImufyMA1MKQY3dcCH"},
        {"title": "Good Life", "artist": "OneRepublic", "uri": "5kIXKt7FtKM5rgP39YmTLN"},
        {"title": "Don't Stop Me Now", "artist": "Queen", "uri": "7hQJA50XrCWABAu5v6QZ4i"},
        {"title": "Shake It Off", "artist": "Taylor Swift", "uri": "0cqRj7pUJDkTCEsJkx8snD"},
    ],
    "sadness": [
        {"title": "Someone Like You", "artist": "Adele", "uri": "1zwMYTA5nlNjZxYrvBB2pV"},
        {"title": "The Night We Met", "artist": "Lord Huron", "uri": "7I7JbDv63ZJJsSi24DyJrz"},
        {"title": "Fix You", "artist": "Coldplay", "uri": "7LVHVU3tWfcxj5aiPFEW4Q"},
        {"title": "Let Her Go", "artist": "Passenger", "uri": "4i6cwNY0JVeJJXmVLZXq9R"}
    ],
    "anger": [
        {"title": "In the End", "artist": "Linkin Park", "uri": "60a0Rd05X7vU1a55vU4dqE"},
        {"title": "Numb", "artist": "Linkin Park", "uri": "2nLtzopw4rPReszdYBJU6h"},
        {"title": "Break Stuff", "artist": "Limp Bizkit", "uri": "3MrRksHupTVEQ7YbA0FsZK"},
        {"title": "Last Resort", "artist": "Papa Roach", "uri": "3VzvGb4QSWolNE2NvfjWz9"}
    ],
    "fear": [
        {"title": "Breathe Me", "artist": "Sia", "uri": "3vB2JZVLKcCPFfwhBu9e2m"},
        {"title": "Brave", "artist": "Sara Bareilles", "uri": "2g0lL5x1hs5dLSr8T2gU22"},
        {"title": "Not Afraid", "artist": "Eminem", "uri": "5Z01UMMf7V1o0MzF86s6WJ"},
        {"title": "Stronger", "artist": "Kanye West", "uri": "4fzsfWzRhPawzqhX8Qt9F3"}
    ],
    "love": [
        {"title": "Perfect", "artist": "Ed Sheeran", "uri": "0tgVpDi06FyKpA1z0VMD4v"},
        {"title": "All of Me", "artist": "John Legend", "uri": "3U4isOIWM3VvDubwSI3y7a"},
        {"title": "A Thousand Years", "artist": "Christina Perri", "uri": "6jyLfYQnPQaFmqCFPQsJe7"},
        {"title": "Lover", "artist": "Taylor Swift", "uri": "1dGr1c8CrMLDpV6mPbImSI"}
    ]
}

# ========== TRAIN MODEL ==========
@st.cache_resource
def train_model():
    try:
        data = pd.read_csv("emotion_dataset.csv", sep=";", header=None, names=["text", "emotion"])
        valid_emotions = ["fear", "joy", "sadness", "anger", "love"]
        data = data[data["emotion"].isin(valid_emotions)]
        X, y = data["text"], data["emotion"]
        vectorizer = CountVectorizer(stop_words="english")
        X_vec = vectorizer.fit_transform(X)
        model = MultinomialNB()
        model.fit(X_vec, y)
        return model, vectorizer, True
    except:
        return None, None, False

# Load model
model, vectorizer, success = train_model()

if not success:
    st.error("❌ Error: emotion_dataset.csv not found!")
    st.stop()

# ========== IMPORT CSS & CHAT ==========
from styles import get_premium_css
from chat_companion import render_chat_companion

# Apply CSS
current_emotion = st.session_state.predicted_emotion or "default"
st.markdown(get_premium_css(current_emotion, emotion_themes), unsafe_allow_html=True)

# ========== HEADER WITH ANIMATION ==========
st.markdown("""
<div class="hero-section">
    <div class="particles" id="particles"></div>
    <div class="hero-content">
        <h1 class="hero-title animate-fade-in">
            <span class="gradient-text">Mood Music</span> Recommender
        </h1>
        <p class="hero-subtitle animate-fade-in-delay">
            Discover the perfect soundtrack for your emotions
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

# ========== SIDEBAR ==========
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    
    st.markdown("## 📊 Dashboard")
    
    if st.session_state.emotion_history:
        st.markdown("### Recent Emotions")
        for i, (emo, timestamp) in enumerate(st.session_state.emotion_history[-3:]):
            st.markdown(f"""
            <div class="history-item">
                <span class="history-emoji">{gauge_emoji[emo]}</span>
                <span class="history-text">{emo.capitalize()}</span>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎯 Quick Guide")
    st.markdown("""
    <div class="guide-step">
        <div class="step-number">1</div>
        <div class="step-text">Express your feelings</div>
    </div>
    <div class="guide-step">
        <div class="step-number">2</div>
        <div class="step-text">Get AI analysis</div>
    </div>
    <div class="guide-step">
        <div class="step-number">3</div>
        <div class="step-text">Enjoy recommendations</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🎨 Emotions")
    for emo, emoji in gauge_emoji.items():
        st.markdown(f"""
        <div class="emotion-badge">
            <span>{emoji}</span>
            <span>{emo.capitalize()}</span>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ========== MAIN INPUT ==========
st.markdown('<div class="input-container glass-card">', unsafe_allow_html=True)

user_input = st.text_input(
    "💭 How are you feeling today?",
    placeholder="Tell me how you're feeling today...",
    label_visibility="collapsed",
    key="mood_input"
)

analyze_button = st.button("✨ Analyze My Mood", use_container_width=True, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# ========== ANALYSIS & RESULTS ==========
if analyze_button and user_input:
    with st.spinner("🔮 Reading your emotions..."):
        # Predict
        user_vec = vectorizer.transform([user_input])
        predicted_proba = model.predict_proba(user_vec)[0]
        predicted_emotion = model.classes_[np.argmax(predicted_proba)]
        
        # Check Indonesian
        for ind, emo in indo_emotions.items():
            if ind in user_input.lower():
                predicted_emotion = emo
                break
        
        # Save to history
        import datetime
        st.session_state.emotion_history.append((predicted_emotion, datetime.datetime.now()))
        st.session_state.predicted_emotion = predicted_emotion
        st.session_state.show_results = True
        
        # Rerun to apply new theme
        st.rerun()

if st.session_state.show_results and st.session_state.predicted_emotion:
    emotion = st.session_state.predicted_emotion
    user_vec = vectorizer.transform([user_input]) if user_input else None
    
    if user_vec is not None:
        predicted_proba = model.predict_proba(user_vec)[0]
        emotion_probs = list(zip(model.classes_, predicted_proba))
        sorted_probs = sorted(emotion_probs, key=lambda x: x[1], reverse=True)[:3]
        
        st.markdown('<div class="results-appear">', unsafe_allow_html=True)
        
        # Emotion Cards
        st.markdown("## 🧠 Emotion Analysis")
        cols = st.columns(3)
        for idx, (emo, prob) in enumerate(sorted_probs):
            with cols[idx]:
                st.markdown(f"""
                <div class="metric-card glass-card">
                    <div class="metric-emoji">{gauge_emoji[emo]}</div>
                    <div class="metric-value">{prob*100:.1f}%</div>
                    <div class="metric-label">{emo.capitalize()}</div>
                    <div class="metric-bar">
                        <div class="metric-fill" style="width: {prob*100}%"></div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        # Dominant Emotion
        st.markdown(f"""
        <div class="dominant-card glass-card">
            <div class="dominant-emoji pulse-animation">{gauge_emoji[emotion]}</div>
            <h2 class="dominant-text">Your dominant emotion: <span class="gradient-text">{emotion.upper()}</span></h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Messages
        col1, col2 = st.columns(2)
        
        with col1:
            booster = random.choice(mood_boosters.get(emotion, ["Stay strong! ❤️"]))
            st.markdown(f"""
            <div class="message-card glass-card">
                <div class="message-icon">💬</div>
                <h3>Mood Booster</h3>
                <p>{booster}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            challenge = random.choice(daily_challenges.get(emotion, ["Do good today ❤️"]))
            st.markdown(f"""
            <div class="message-card glass-card">
                <div class="message-icon">🎯</div>
                <h3>Daily Challenge</h3>
                <p>{challenge}</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("## 🎁 Your Personalized Playlist")
        
        tab1, tab2, tab3 = st.tabs(["🎧 Music", "▶️ Videos", "💬 AI Chat"])
        
        with tab1:
            tracks = spotify_recommendations.get(emotion, [])
            cols = st.columns(2)
            for idx, track in enumerate(tracks):
                with cols[idx % 2]:
                    st.markdown(f"""
                    <div class="spotify-card glass-card">
                        <iframe 
                            src="https://open.spotify.com/embed/track/{track['uri']}?utm_source=generator&theme=0" 
                            width="100%" 
                            height="152" 
                            frameBorder="0" 
                            allowfullscreen="" 
                            allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
                            loading="lazy">
                        </iframe>
                    </div>
                    """, unsafe_allow_html=True)
        
        with tab2:
            videos = youtube_videos.get(emotion, [])
            cols = st.columns(3)
            for idx, (title, link, video_id) in enumerate(videos):
                with cols[idx % 3]:
                    thumbnail = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
                    st.markdown(f"""
                    <div class="video-card glass-card">
                        <div class="video-thumbnail">
                            <img src="{thumbnail}" alt="{title}">
                            <div class="play-overlay">
                                <div class="play-button">▶</div>
                            </div>
                        </div>
                        <div class="video-info">
                            <h4>{title}</h4>
                            <a href="{link}" target="_blank" class="watch-btn">Watch Now</a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        
        with tab3:
            render_chat_companion(emotion)
        
        st.markdown('</div>', unsafe_allow_html=True)

elif analyze_button and not user_input:
    st.warning("💭 Please share your feelings first!")

# Footer
st.markdown("""
<div class="footer">
    <p>Made with ❤️ using AI & Machine Learning</p>
    <p class="footer-small">Your emotions matter. Take care of yourself.</p>
</div>
""", unsafe_allow_html=True)