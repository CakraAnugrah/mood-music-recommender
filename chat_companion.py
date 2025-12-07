import streamlit as st
import json
from datetime import datetime

# ========== EMOTION-SPECIFIC AI PROMPTS ==========
EMOTION_CONTEXTS = {
    "joy": {
        "system_prompt": """You are a warm, enthusiastic AI companion talking to someone feeling joyful. 
        Celebrate their happiness, encourage them to savor the moment, and help them spread positivity. 
        Be upbeat but genuine. Keep responses concise (2-3 paragraphs max).""",
        "greeting": "Hey there! 😊 I can feel your positive energy! What's making you so happy today?",
        "suggestions": [
            "What made you smile today?",
            "Tell me about your happy moment!",
            "How can you share this joy with others?"
        ]
    },
    "sadness": {
        "system_prompt": """You are a gentle, empathetic AI companion talking to someone feeling sad. 
        Listen without judgment, validate their feelings, offer comfort and hope. 
        Be supportive but not overly cheerful. Keep responses warm and understanding (2-3 paragraphs max).""",
        "greeting": "I'm here for you. 💙 It's okay to feel sad. Want to talk about what's on your mind?",
        "suggestions": [
            "What's weighing on your heart?",
            "Tell me what happened...",
            "What do you need right now?"
        ]
    },
    "anger": {
        "system_prompt": """You are a calm, understanding AI companion talking to someone feeling angry. 
        Help them process their anger healthily, validate their feelings, and guide them toward resolution. 
        Be patient and non-judgmental. Keep responses measured and supportive (2-3 paragraphs max).""",
        "greeting": "I hear you. 😮‍💨 It's okay to feel angry. Let's talk through this together.",
        "suggestions": [
            "What triggered this feeling?",
            "How can I help you right now?",
            "What would make this better?"
        ]
    },
    "fear": {
        "system_prompt": """You are a reassuring, grounded AI companion talking to someone feeling fearful. 
        Help them feel safe, break down their fears rationally, and build their courage. 
        Be steady and calming. Keep responses reassuring (2-3 paragraphs max).""",
        "greeting": "You're safe here. 🤍 I'm here to help you through this. What's worrying you?",
        "suggestions": [
            "What are you afraid of?",
            "Let's break this down together",
            "What's the worst that could happen?"
        ]
    },
    "love": {
        "system_prompt": """You are a warm, caring AI companion talking to someone feeling love. 
        Celebrate their feelings, help them express their emotions, and encourage healthy relationships. 
        Be supportive and romantic but balanced. Keep responses heartfelt (2-3 paragraphs max).""",
        "greeting": "Love is beautiful! ❤️ Tell me about what's filling your heart right now.",
        "suggestions": [
            "Who or what do you love?",
            "How does love feel for you?",
            "How can you express this love?"
        ]
    }
}

# ========== INITIALIZE CHAT STATE ==========
def initialize_chat():
    """Initialize chat session state"""
    if 'chat_messages' not in st.session_state:
        st.session_state.chat_messages = []
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

# ========== API CALL FUNCTION ==========
async def get_ai_response(user_message, emotion, conversation_history):
    """Call Anthropic API for AI response"""
    try:
        import anthropic
        
        # Get emotion-specific context
        context = EMOTION_CONTEXTS.get(emotion, EMOTION_CONTEXTS["joy"])
        
        # Build messages with history
        messages = []
        for msg in conversation_history[-6:]:  # Last 3 exchanges
            messages.append({"role": msg["role"], "content": msg["content"]})
        messages.append({"role": "user", "content": user_message})
        
        # Call API
        client = anthropic.Anthropic()
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            system=context["system_prompt"],
            messages=messages
        )
        
        return response.content[0].text
    
    except Exception as e:
        return f"I'm having trouble connecting right now. Error: {str(e)}\n\nBut I'm here for you. Try telling me more about how you're feeling?"

# ========== RENDER CHAT UI ==========
def render_chat_companion(emotion):
    """Render the AI chat companion interface"""
    initialize_chat()
    
    # Get emotion context
    context = EMOTION_CONTEXTS.get(emotion, EMOTION_CONTEXTS["joy"])
    
    # Chat Header
    st.markdown(f"""
    <div class="chat-header glass-card">
        <div class="chat-header-content">
            <div class="chat-avatar">🤖</div>
            <div class="chat-header-text">
                <h3>AI Companion</h3>
                <p class="chat-status">
                    <span class="status-dot"></span> 
                    Ready to listen · Emotion: {emotion.capitalize()}
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Greeting message (show once)
    if len(st.session_state.chat_messages) == 0:
        st.session_state.chat_messages.append({
            "role": "assistant",
            "content": context["greeting"],
            "timestamp": datetime.now().strftime("%H:%M")
        })
    
    # Chat Container
    st.markdown('<div class="chat-container glass-card">', unsafe_allow_html=True)
    
    # Display messages
    for msg in st.session_state.chat_messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="message-wrapper user-message-wrapper">
                <div class="chat-message user-message">
                    <div class="message-content">{msg["content"]}</div>
                    <div class="message-time">{msg["timestamp"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="message-wrapper ai-message-wrapper">
                <div class="chat-avatar-small">🤖</div>
                <div class="chat-message ai-message">
                    <div class="message-content">{msg["content"]}</div>
                    <div class="message-time">{msg["timestamp"]}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Quick suggestions
    st.markdown("### 💭 Quick Questions")
    cols = st.columns(3)
    for idx, suggestion in enumerate(context["suggestions"]):
        with cols[idx]:
            if st.button(suggestion, key=f"suggestion_{idx}", use_container_width=True):
                # Add user message
                st.session_state.chat_messages.append({
                    "role": "user",
                    "content": suggestion,
                    "timestamp": datetime.now().strftime("%H:%M")
                })
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": suggestion
                })
                
                # Get AI response (placeholder for now)
                with st.spinner("🤖 Thinking..."):
                    # Simplified response for now (tanpa API)
                    ai_response = get_simple_response(suggestion, emotion)
                    
                    st.session_state.chat_messages.append({
                        "role": "assistant",
                        "content": ai_response,
                        "timestamp": datetime.now().strftime("%H:%M")
                    })
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": ai_response
                    })
                
                st.rerun()
    
    # Chat Input
    st.markdown("---")
    
    col1, col2 = st.columns([5, 1])
    with col1:
        user_input = st.text_input(
            "Type your message...",
            key="chat_input",
            placeholder="Share what's on your mind...",
            label_visibility="collapsed"
        )
    with col2:
        send_button = st.button("Send 📤", use_container_width=True)
    
    # Handle send
    if send_button and user_input:
        # Add user message
        st.session_state.chat_messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now().strftime("%H:%M")
        })
        st.session_state.chat_history.append({
            "role": "user",
            "content": user_input
        })
        
        # Get AI response
        with st.spinner("🤖 Thinking..."):
            ai_response = get_simple_response(user_input, emotion)
            
            st.session_state.chat_messages.append({
                "role": "assistant",
                "content": ai_response,
                "timestamp": datetime.now().strftime("%H:%M")
            })
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": ai_response
            })
        
        st.rerun()
    
    # Clear chat button
    st.markdown("---")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_messages = []
        st.session_state.chat_history = []
        st.rerun()
    
    # Tips box
    st.markdown("""
    <div class="chat-tips glass-card">
        <h4>💡 Chat Tips</h4>
        <ul>
            <li>Be honest about your feelings</li>
            <li>Take your time to express yourself</li>
            <li>The AI is here to listen, not judge</li>
            <li>Use this space to process your emotions</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# ========== SIMPLE RESPONSE FUNCTION (FALLBACK) ==========
def get_simple_response(user_message, emotion):
    """Generate simple empathetic responses (fallback without API)"""
    
    responses = {
        "joy": [
            "That's wonderful! 😊 Your happiness is contagious. What specifically made this moment special for you?",
            "I love hearing about what brings you joy! It sounds like you're in a really good place right now. How can you keep this positive energy going?",
            "Your excitement is beautiful! These happy moments are so precious. Have you thought about sharing this joy with someone close to you?"
        ],
        "sadness": [
            "I hear you, and I want you to know that what you're feeling is completely valid. 💙 It's okay to feel sad. Would you like to talk more about what's happening?",
            "Thank you for sharing this with me. Sadness can feel heavy, but you don't have to carry it alone. What would help you feel a bit lighter right now?",
            "I'm here with you through this difficult time. Sometimes we need to sit with sadness before we can move through it. What do you need most right now - comfort, advice, or just someone to listen?"
        ],
        "anger": [
            "I can sense your frustration, and that's completely understandable. 😮‍💨 Take a deep breath with me. What's at the core of what's making you angry?",
            "Your feelings are valid. Anger often comes from something important being threatened or hurt. Let's work through this together - what would resolution look like for you?",
            "It's okay to feel angry. This emotion is telling you something important. Once you've had a moment to breathe, what do you think triggered this response?"
        ],
        "fear": [
            "I want you to know that you're safe here. 🤍 Fear can feel overwhelming, but we can work through this together. What specifically is worrying you most?",
            "Thank you for trusting me with your fears. It takes courage to acknowledge what scares us. Let's break this down - what's one small thing we can address first?",
            "Your concerns are valid. Sometimes fear protects us, and sometimes it holds us back. What would help you feel more grounded right now?"
        ],
        "love": [
            "Love is such a beautiful emotion! ❤️ It sounds like your heart is full right now. Tell me more about what's inspiring these feelings.",
            "There's something special about the way you express love. How does this feeling shape your world right now?",
            "Your capacity to love is beautiful. Whether it's love for someone, something, or even yourself - it's worth celebrating. How do you want to honor this feeling?"
        ]
    }
    
    import random
    emotion_responses = responses.get(emotion, responses["joy"])
    return random.choice(emotion_responses)

# ========== EXPORT CHAT FUNCTION ==========
def export_chat_history():
    """Export chat history as text"""
    if st.session_state.chat_messages:
        chat_text = "💬 AI Chat Companion - Conversation History\n"
        chat_text += "=" * 50 + "\n\n"
        
        for msg in st.session_state.chat_messages:
            role = "You" if msg["role"] == "user" else "AI Companion"
            chat_text += f"[{msg['timestamp']}] {role}:\n{msg['content']}\n\n"
        
        return chat_text
    return None