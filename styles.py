# type: ignore
def get_premium_css(emotion, emotion_themes):
    theme = emotion_themes.get(emotion, emotion_themes["default"])
    
    return f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@400;500;600;700&display=swap');
    
    * {{
        font-family: 'Poppins', sans-serif;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}
    
    /* ========== BACKGROUND & BASE ========== */
    .main {{
        background: {theme['bg']} !important;
        animation: gradientShift 15s ease infinite;
    }}
    
    .stApp {{
        background: {theme['bg']} !important;
    }}
    
    @keyframes gradientShift {{
        0%, 100% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
    }}
    
    /* ========== GLASS MORPHISM ========== */
    .glass-card {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border-radius: 24px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }}
    
    .glass-card:hover {{
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(0, 0, 0, 0.2);
        border: 1px solid {theme['primary']};
    }}
    
    /* ========== HERO SECTION ========== */
    .hero-section {{
        position: relative;
        text-align: center;
        padding: 80px 20px;
        margin-bottom: 60px;
        overflow: hidden;
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        border-radius: 32px;
        backdrop-filter: blur(10px);
    }}
    
    .hero-content {{
        position: relative;
        z-index: 2;
    }}
    
    .hero-title {{
        font-size: 4.5rem;
        font-weight: 800;
        font-family: 'Space Grotesk', sans-serif;
        margin-bottom: 20px;
        letter-spacing: -2px;
        color: #1a1a1a;
    }}
    
    .gradient-text {{
        background: {theme['gradient']};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: gradientFlow 3s ease infinite;
    }}
    
    @keyframes gradientFlow {{
        0%, 100% {{ background-position: 0% 50%; }}
        50% {{ background-position: 100% 50%; }}
    }}
    
    .hero-subtitle {{
        font-size: 1.5rem;
        color: #4a5568;
        font-weight: 400;
    }}
    
    /* ========== PARTICLES ANIMATION ========== */
    .particles {{
        position: absolute;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: 1;
        overflow: hidden;
    }}
    
    .particles::before,
    .particles::after {{
        content: '';
        position: absolute;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: {theme['particle']};
        opacity: 0.1;
        animation: float 20s infinite;
    }}
    
    .particles::before {{
        top: -150px;
        left: -150px;
        animation-delay: 0s;
    }}
    
    .particles::after {{
        bottom: -150px;
        right: -150px;
        animation-delay: 10s;
    }}
    
    @keyframes float {{
        0%, 100% {{ transform: translate(0, 0) scale(1); }}
        33% {{ transform: translate(100px, -100px) scale(1.1); }}
        66% {{ transform: translate(-100px, 100px) scale(0.9); }}
    }}
    
    /* ========== ANIMATIONS ========== */
    @keyframes fadeIn {{
        from {{
            opacity: 0;
            transform: translateY(30px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes slideInRight {{
        from {{
            opacity: 0;
            transform: translateX(50px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    .animate-fade-in {{
        animation: fadeIn 1s ease-out;
    }}
    
    .animate-fade-in-delay {{
        animation: fadeIn 1s ease-out 0.3s both;
    }}
    
    .pulse-animation {{
        animation: pulse 2s ease-in-out infinite;
    }}
    
    .results-appear {{
        animation: fadeIn 0.8s ease-out;
    }}
    
    /* ========== INPUT SECTION ========== */
    .input-container {{
        padding: 50px;
        margin: 40px auto;
        max-width: 900px;
        animation: slideInLeft 0.8s ease-out;
    }}
    
    .stTextInput>div>div>input {{
        border: 3px solid transparent;
        border-radius: 20px;
        padding: 20px 20px 20px 60px !important;
        font-size: 18px !important;
        background: white !important;
        color: #1a202c !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
        transition: all 0.3s ease !important;
    }}
    
    .stTextInput>div>div>input:focus {{
        border-color: {theme['primary']} !important;
        box-shadow: 0 8px 30px rgba(0,0,0,0.15), 0 0 0 4px {theme['particle']}33 !important;
        transform: translateY(-2px);
    }}
    
    /* ========== BUTTON ========== */
    .stButton>button {{
        background: {theme['gradient']} !important;
        color: white !important;
        border: none !important;
        padding: 18px 50px !important;
        border-radius: 16px !important;
        font-weight: 700 !important;
        font-size: 18px !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 10px 30px {theme['particle']}40 !important;
    }}
    
    .stButton>button:hover {{
        transform: translateY(-4px) scale(1.02) !important;
        box-shadow: 0 15px 40px {theme['particle']}60 !important;
    }}
    
    /* ========== METRIC CARDS ========== */
    .metric-card {{
        padding: 30px;
        text-align: center;
        animation: slideInRight 0.8s ease-out;
        margin: 10px;
    }}
    
    .metric-emoji {{
        font-size: 64px;
        margin-bottom: 15px;
        animation: pulse 2s ease-in-out infinite;
    }}
    
    .metric-value {{
        font-size: 48px;
        font-weight: 800;
        background: {theme['gradient']};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 10px 0;
    }}
    
    .metric-label {{
        font-size: 18px;
        color: #4a5568;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }}
    
    .metric-bar {{
        height: 8px;
        background: #e2e8f0;
        border-radius: 10px;
        margin-top: 20px;
        overflow: hidden;
    }}
    
    .metric-fill {{
        height: 100%;
        background: {theme['gradient']};
        border-radius: 10px;
        animation: fillBar 1.5s ease-out;
    }}
    
    @keyframes fillBar {{
        from {{ width: 0%; }}
    }}
    
    /* ========== DOMINANT EMOTION ========== */
    .dominant-card {{
        padding: 50px;
        text-align: center;
        margin: 40px 0;
        animation: fadeIn 1s ease-out 0.5s both;
    }}
    
    .dominant-emoji {{
        font-size: 120px;
        margin-bottom: 20px;
        display: inline-block;
    }}
    
    .dominant-text {{
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d3748;
        font-family: 'Space Grotesk', sans-serif;
    }}
    
    /* ========== MESSAGE CARDS ========== */
    .message-card {{
        padding: 35px;
        margin: 20px 0;
        animation: fadeIn 1s ease-out 0.8s both;
        position: relative;
        overflow: hidden;
    }}
    
    .message-card::before {{
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 5px;
        height: 100%;
        background: {theme['gradient']};
    }}
    
    .message-icon {{
        font-size: 40px;
        margin-bottom: 15px;
    }}
    
    .message-card h3 {{
        color: #2d3748 !important;
        font-size: 22px !important;
        font-weight: 700 !important;
        margin-bottom: 15px !important;
    }}
    
    .message-card p {{
        color: #4a5568;
        font-size: 16px;
        line-height: 1.8;
    }}
    
    /* ========== SPOTIFY CARDS ========== */
    .spotify-card {{
        padding: 15px;
        margin: 15px 0;
        animation: fadeIn 0.6s ease-out;
    }}
    
    .spotify-card:hover {{
        transform: translateY(-5px) scale(1.02);
    }}
    
    .spotify-card iframe {{
        border-radius: 16px;
    }}
    
    /* ========== VIDEO CARDS ========== */
    .video-card {{
        overflow: hidden;
        margin: 20px 0;
        animation: fadeIn 0.8s ease-out;
    }}
    
    .video-thumbnail {{
        position: relative;
        overflow: hidden;
        border-radius: 16px 16px 0 0;
    }}
    
    .video-thumbnail img {{
        width: 100%;
        height: 200px;
        object-fit: cover;
        transition: transform 0.5s ease;
    }}
    
    .video-card:hover .video-thumbnail img {{
        transform: scale(1.1);
    }}
    
    .play-overlay {{
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        opacity: 0;
        transition: opacity 0.3s ease;
    }}
    
    .video-card:hover .play-overlay {{
        opacity: 1;
    }}
    
    .play-button {{
        width: 80px;
        height: 80px;
        background: {theme['gradient']};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 32px;
        color: white;
        transform: scale(0.9);
        transition: transform 0.3s ease;
    }}
    
    .video-card:hover .play-button {{
        transform: scale(1.1);
    }}
    
    .video-info {{
        padding: 25px;
    }}
    
    .video-info h4 {{
        color: #2d3748;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 15px;
        line-height: 1.5;
    }}
    
    .watch-btn {{
        display: inline-block;
        background: {theme['gradient']};
        color: white;
        padding: 12px 30px;
        border-radius: 12px;
        text-decoration: none;
        font-weight: 600;
        font-size: 15px;
        transition: all 0.3s ease;
    }}
    
    .watch-btn:hover {{
        transform: translateX(5px);
        box-shadow: 0 5px 20px {theme['particle']}40;
    }}
    
    /* ========== TABS ========== */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 15px;
        background: rgba(255, 255, 255, 0.5);
        padding: 10px;
        border-radius: 20px;
        backdrop-filter: blur(10px);
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        color: #4a5568;
        border-radius: 14px;
        padding: 15px 35px;
        font-weight: 700;
        font-size: 16px;
        transition: all 0.3s ease;
    }}
    
    .stTabs [data-baseweb="tab"]:hover {{
        background: rgba(255, 255, 255, 0.8);
        transform: translateY(-2px);
    }}
    
    .stTabs [aria-selected="true"] {{
        background: {theme['gradient']} !important;
        color: white !important;
        box-shadow: 0 5px 20px {theme['particle']}40;
    }}
    
    /* ========== SIDEBAR ========== */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #1a202c 0%, #2d3748 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    [data-testid="stSidebar"] h2 {{
        color: white !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        margin-bottom: 20px !important;
    }}
    
    [data-testid="stSidebar"] h3 {{
        color: white !important;
        font-size: 18px !important;
        font-weight: 600 !important;
    }}
    
    .history-item {{
        display: flex;
        align-items: center;
        gap: 15px;
        background: rgba(255, 255, 255, 0.1);
        padding: 15px;
        border-radius: 12px;
        margin: 10px 0;
        transition: all 0.3s ease;
    }}
    
    .history-item:hover {{
        background: rgba(255, 255, 255, 0.15);
        transform: translateX(5px);
    }}
    
    .history-emoji {{
        font-size: 28px;
    }}
    
    .history-text {{
        color: white;
        font-weight: 600;
        font-size: 16px;
    }}
    
    .guide-step {{
        display: flex;
        align-items: center;
        gap: 15px;
        margin: 15px 0;
        animation: slideInLeft 0.6s ease-out;
    }}
    
    .step-number {{
        width: 40px;
        height: 40px;
        background: {theme['gradient']};
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: 700;
        font-size: 18px;
        flex-shrink: 0;
    }}
    
    .step-text {{
        color: rgba(255, 255, 255, 0.9);
        font-size: 15px;
        font-weight: 500;
    }}
    
    .emotion-badge {{
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: rgba(255, 255, 255, 0.1);
        padding: 10px 18px;
        border-radius: 25px;
        margin: 5px;
        transition: all 0.3s ease;
    }}
    
    .emotion-badge:hover {{
        background: {theme['gradient']};
        transform: scale(1.05);
    }}
    
    .emotion-badge span {{
        color: white;
        font-weight: 600;
        font-size: 14px;
    }}
    
    /* ========== AI CHAT COMPANION STYLES ========== */
    
    .chat-header {{
        padding: 25px 30px;
        margin-bottom: 25px;
        animation: slideInLeft 0.8s ease-out;
    }}
    
    .chat-header-content {{
        display: flex;
        align-items: center;
        gap: 20px;
    }}
    
    .chat-avatar {{
        width: 70px;
        height: 70px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 36px;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
        animation: pulse 2s ease-in-out infinite;
    }}
    
    .chat-header-text h3 {{
        margin: 0 !important;
        font-size: 24px !important;
        font-weight: 700 !important;
        color: #2d3748 !important;
    }}
    
    .chat-status {{
        display: flex;
        align-items: center;
        gap: 8px;
        color: #718096;
        font-size: 14px;
        margin: 5px 0 0 0 !important;
    }}
    
    .status-dot {{
        width: 10px;
        height: 10px;
        background: #48bb78;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
    }}
    
    .chat-container {{
        padding: 30px;
        margin: 25px 0;
        max-height: 500px;
        overflow-y: auto;
        animation: fadeIn 0.6s ease-out;
        scroll-behavior: smooth;
    }}
    
    .message-wrapper {{
        display: flex;
        margin-bottom: 20px;
        animation: messageSlideIn 0.4s ease-out;
    }}
    
    @keyframes messageSlideIn {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    .user-message-wrapper {{
        justify-content: flex-end;
    }}
    
    .ai-message-wrapper {{
        justify-content: flex-start;
        gap: 12px;
    }}
    
    .chat-avatar-small {{
        width: 40px;
        height: 40px;
        min-width: 40px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.2);
    }}
    
    .chat-message {{
        max-width: 70%;
        padding: 16px 20px;
        border-radius: 18px;
        position: relative;
        word-wrap: break-word;
        animation: messageAppear 0.3s ease-out;
    }}
    
    @keyframes messageAppear {{
        from {{
            opacity: 0;
            transform: scale(0.95);
        }}
        to {{
            opacity: 1;
            transform: scale(1);
        }}
    }}
    
    .user-message {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-bottom-right-radius: 4px;
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
    }}
    
    .ai-message {{
        background: rgba(255, 255, 255, 0.95);
        color: #2d3748;
        border: 1px solid rgba(102, 126, 234, 0.2);
        border-bottom-left-radius: 4px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }}
    
    .message-content {{
        font-size: 15px;
        line-height: 1.6;
        margin-bottom: 8px;
    }}
    
    .message-time {{
        font-size: 11px;
        opacity: 0.7;
        text-align: right;
    }}
    
    .user-message .message-time {{
        color: rgba(255, 255, 255, 0.8);
    }}
    
    .ai-message .message-time {{
        color: #718096;
    }}
    
    .chat-tips {{
        padding: 25px;
        margin: 25px 0;
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.1) 100%);
        border: 1px solid rgba(102, 126, 234, 0.2);
    }}
    
    .chat-tips h4 {{
        color: #667eea !important;
        font-size: 18px !important;
        font-weight: 700 !important;
        margin-bottom: 15px !important;
    }}
    
    .chat-tips ul {{
        list-style: none;
        padding: 0;
        margin: 0;
    }}
    
    .chat-tips ul li {{
        color: #4a5568;
        font-size: 14px;
        padding: 8px 0;
        padding-left: 25px;
        position: relative;
    }}
    
    .chat-tips ul li::before {{
        content: '✨';
        position: absolute;
        left: 0;
        top: 8px;
    }}
    
    .chat-container::-webkit-scrollbar {{
        width: 8px;
    }}
    
    .chat-container::-webkit-scrollbar-track {{
        background: rgba(0, 0, 0, 0.05);
        border-radius: 10px;
    }}
    
    .chat-container::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 10px;
    }}
    
    .chat-container::-webkit-scrollbar-thumb:hover {{
        background: #667eea;
    }}
    
    /* ========== FOOTER ========== */
    .footer {{
        text-align: center;
        padding: 50px 20px;
        margin-top: 80px;
        background: rgba(255, 255, 255, 0.5);
        border-radius: 24px;
        backdrop-filter: blur(10px);
    }}
    
    .footer p {{
        color: #4a5568;
        font-size: 18px;
        font-weight: 600;
        margin: 10px 0;
    }}
    
    .footer-small {{
        font-size: 14px !important;
        font-weight: 400 !important;
        color: #718096 !important;
    }}
    
    /* ========== RESPONSIVE ========== */
    @media (max-width: 768px) {{
        .hero-title {{
            font-size: 3rem;
        }}
        
        .metric-emoji {{
            font-size: 48px;
        }}
        
        .dominant-emoji {{
            font-size: 80px;
        }}
        
        .input-container {{
            padding: 30px;
        }}
        
        .chat-message {{
            max-width: 85%;
        }}
        
        .chat-avatar {{
            width: 50px;
            height: 50px;
            font-size: 28px;
        }}
        
        .chat-avatar-small {{
            width: 35px;
            height: 35px;
            min-width: 35px;
            font-size: 18px;
        }}
    }}
    
    /* ========== SCROLLBAR ========== */
    ::-webkit-scrollbar {{
        width: 12px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: rgba(0, 0, 0, 0.1);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: {theme['gradient']};
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: {theme['primary']};
    }}
</style>

<script>
// Add particle effect
document.addEventListener('DOMContentLoaded', function() {{
    const particles = document.getElementById('particles');
    if (particles) {{
        for (let i = 0; i < 20; i++) {{
            const particle = document.createElement('div');
            particle.style.position = 'absolute';
            particle.style.width = Math.random() * 10 + 5 + 'px';
            particle.style.height = particle.style.width;
            particle.style.background = '{theme['particle']}';
            particle.style.borderRadius = '50%';
            particle.style.opacity = Math.random() * 0.3;
            particle.style.left = Math.random() * 100 + '%';
            particle.style.top = Math.random() * 100 + '%';
            particle.style.animation = `float ${{Math.random() * 10 + 10}}s infinite`;
            particles.appendChild(particle);
        }}
    }}
}});
</script>
"""