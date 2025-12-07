# 🎵 Mood Music Recommender

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A beautiful web application that analyzes your emotions through text and provides personalized music, video, and chat recommendations to match your mood.

## ✨ Features

### 🧠 **Emotion Detection**
- Machine Learning-powered emotion analysis using Naive Bayes classifier
- Supports 5 emotions: **Joy, Sadness, Anger, Fear, Love**
- Indonesian language support
- Real-time emotion probability visualization

### 🎧 **Personalized Recommendations**
- **Spotify Music**: Curated playlists embedded directly in the app
- **YouTube Videos**: Emotion-matched short films and videos
- **AI Chat Companion**: Rule-based empathetic chatbot

### 💬 **AI Chat Companion**
- Emotion-aware responses
- Empathetic conversation
- Quick suggestion buttons
- Chat history tracking
- Export chat functionality

### 🎨 **Beautiful UI/UX**
- Glass morphism design
- Dynamic theme changes based on emotion
- Smooth animations and transitions
- Particle effects
- Mobile responsive

## 🚀 Demo

![App Screenshot](screenshot.png)

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager

## 🔧 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/mood-music-recommender.git
cd mood-music-recommender
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify required files
Make sure you have these files in your project directory:
```
mood_music/
├── app.py
├── styles.py
├── chat_companion.py
└── emotion_dataset.csv
```

## 🎯 Usage

### Run the application
```bash
streamlit run app.py
```

The app will open automatically in your default browser at `http://localhost:8501`

### How to use:
1. **Express your feelings** - Type how you're feeling in the text input
2. **Analyze** - Click "Analyze My Mood" button
3. **Explore recommendations**:
   - 🎧 **Music Tab**: Listen to Spotify playlists
   - ▶️ **Videos Tab**: Watch emotion-matched videos
   - 💬 **AI Chat Tab**: Chat with the AI companion

## 📁 Project Structure

```
mood_music/
│
├── app.py                      # Main Streamlit application
├── styles.py                   # CSS styling and themes
├── chat_companion.py           # AI Chat companion logic
├── emotion_dataset.csv         # Training data for ML model
│
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🛠️ Tech Stack

### Frontend
- **Streamlit** - Web framework
- **HTML/CSS** - Custom styling with glass morphism
- **JavaScript** - Particle animations

### Backend
- **Python 3.8+** - Core programming language
- **scikit-learn** - Machine Learning (Naive Bayes)
- **pandas** - Data manipulation
- **NumPy** - Numerical computing

### APIs & Integrations
- **Spotify Embed** - Music player
- **YouTube** - Video recommendations

## 📊 Machine Learning Model

### Algorithm
- **Naive Bayes (MultinomialNB)** classifier
- **CountVectorizer** for text feature extraction

### Training Data
- `emotion_dataset.csv` with format: `text;emotion`
- 5 emotion classes: fear, joy, sadness, anger, love

### Performance
- Model trains on app startup
- Cached for performance using `@st.cache_resource`
- Supports English and Indonesian input

## 🎨 Emotion Themes

Each emotion has a unique visual theme:

| Emotion | Color Scheme | Gradient |
|---------|-------------|----------|
| 😊 Joy | Gold/Orange | Pink to Red |
| 😢 Sadness | Blue/Purple | Blue to Purple |
| 😡 Anger | Red | Red to Dark Red |
| 😨 Fear | Purple/Pink | Teal to Pink |
| ❤️ Love | Pink | Pink to Red |

## 💬 Chat Companion

### Features
- Emotion-aware personality
- Rule-based responses
- Quick suggestion buttons
- Session-based chat history
- Export chat as text file

### Response System
The chatbot uses a rule-based system with:
- Emotion-specific greetings
- Contextual responses
- Empathetic language
- Quick action suggestions

## 📦 Dependencies

```txt
streamlit>=1.28.0
pandas>=2.0.0
scikit-learn>=1.3.0
numpy>=1.24.0
```

## 🔐 Privacy & Data

- ✅ All processing happens locally
- ✅ No data is sent to external servers
- ✅ Chat history stored in session (cleared on page refresh)
- ✅ No user data collection

## 🐛 Troubleshooting

### "emotion_dataset.csv not found"
**Solution**: Make sure `emotion_dataset.csv` is in the same directory as `app.py`

### Spotify embeds not loading
**Solution**: Check your internet connection. Spotify embeds require an active connection.

### Style not applying
**Solution**: 
1. Clear browser cache (Ctrl+Shift+R)
2. Restart Streamlit server
3. Check that `styles.py` is in the same directory

### Chat not responding
**Solution**: Check that `chat_companion.py` is properly imported and in the same directory

## 🚀 Future Enhancements

- [ ] User authentication & profile
- [ ] Save emotion history to database
- [ ] Advanced ML models (BERT, transformers)
- [ ] Real-time emotion detection from voice
- [ ] Social sharing features
- [ ] Dark mode toggle
- [ ] Multi-language support
- [ ] Emotion analytics dashboard
- [ ] Integration with music streaming APIs
- [ ] PWA (Progressive Web App) support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Your Name** - *Initial work* - [YourGitHub](https://github.com/yourusername)

## 🙏 Acknowledgments

- Emotion dataset from [Kaggle/Source]
- Spotify for music embed API
- YouTube for video content
- Streamlit community for amazing framework

## 📧 Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter) - your.email@example.com

Project Link: [https://github.com/yourusername/mood-music-recommender](https://github.com/yourusername/mood-music-recommender)

---

Made with ❤️ using Python & Streamlit

⭐ Star this repo if you found it helpful!