# 🤖 AI Chat Assistant

A modern, responsive AI chat interface built with Flask and vanilla JavaScript. Features a beautiful UI similar to ChatGPT and Perplexity with dark mode support, real-time messaging, and advanced user experience features.

![Chat Assistant Demo](https://img.shields.io/badge/Status-Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-orange)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-yellow)

## ✨ Features

### 🎨 **Modern UI/UX**
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Dark/Light Mode**: Toggle between themes with persistent settings
- **Smooth Animations**: Elegant transitions and micro-interactions
- **Accessibility**: WCAG compliant with keyboard navigation and screen reader support

### 💬 **Chat Features**
- **Real-time Messaging**: Instant message delivery with typing indicators
- **Message History**: Persistent chat sessions with sidebar navigation
- **Message Actions**: Copy messages and like assistant responses
- **Timestamps**: See when each message was sent
- **Character Counter**: Track message length with configurable limits

### ⚙️ **Advanced Settings**
- **Customizable Limits**: Adjust message character limits (100-5000 characters)
- **Auto-scroll**: Toggle automatic scrolling to new messages
- **Sound Notifications**: Enable/disable sound alerts (ready for implementation)
- **Persistent Settings**: All preferences saved to localStorage

### 🎯 **User Experience**
- **Keyboard Shortcuts**: Send messages with `Ctrl+Enter`
- **Auto-resize Input**: Textarea grows with content (max 120px height)
- **Collapsible Sidebar**: Expand/collapse on desktop, slide-in on mobile
- **Error Handling**: Graceful error messages and retry functionality

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd ChatBot/backend
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv chatbot_env
   ```

3. **Activate the virtual environment**
   ```bash
   # On Windows
   chatbot_env\Scripts\activate
   
   # On macOS/Linux
   source chatbot_env/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
backend/
├── app.py                 # Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── static/
│   └── chat.css          # Stylesheet
└── templates/
    └── chat.html         # Main chat interface
```

## 🎮 Usage Guide

### **Basic Chatting**
1. Type your message in the input field
2. Press `Enter` or click the send button (▶️)
3. Use `Ctrl+Enter` for quick sending
4. Messages are sent to your backend API endpoint

### **Sidebar Navigation**
- **Desktop**: Click the arrow (⮜/⮞) to collapse/expand
- **Mobile**: Tap the hamburger menu (☰) to open/close
- **New Chat**: Click "+ New Chat" to start fresh conversations

### **Dark Mode**
- Click the sun/moon toggle in the header
- Your preference is automatically saved
- Works across all browsers and devices

### **Settings**
- Click the gear icon (⚙️) in the sidebar
- Configure message limits, auto-scroll, and notifications
- All settings persist between sessions

### **Message Actions**
- **Copy**: Click the clipboard icon (📋) on any message
- **Like**: Click the thumbs up (👍) on assistant messages
- **Hover**: Actions appear when hovering over messages

## 🔧 Configuration

### **Backend API**
The frontend expects a Flask backend with the following endpoint:

```python
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    
    # Your AI processing logic here
    response = process_message(user_message)
    
    return jsonify({'response': response})
```

### **Environment Variables**
Create a `.env` file in the backend directory:

```env
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-secret-key-here
PORT=5000
```

### **Customization**

#### **Colors and Themes**
Edit `static/chat.css` to customize:
- Primary colors (`--primary`, `--primary-dark`)
- Background colors (`--chat-bg`, `--sidebar-bg`)
- Dark mode colors
- Border radius and shadows

#### **Message Limits**
- Default: 2000 characters
- Range: 100-5000 characters
- Configure in settings modal

#### **Animations**
- Disabled for users with `prefers-reduced-motion`
- Customizable timing in CSS variables
- Smooth transitions for all interactions

## 🛠️ Development

### **Frontend Development**
- **HTML**: Semantic markup with ARIA labels
- **CSS**: Modern CSS with custom properties and flexbox
- **JavaScript**: Vanilla JS with ES6+ features
- **No Frameworks**: Lightweight and fast loading

### **Backend Integration**
- **Flask**: Python web framework
- **RESTful API**: JSON-based communication
- **Error Handling**: Graceful error responses
- **CORS**: Configure for cross-origin requests if needed

### **Testing**
```bash
# Run Flask tests
python -m pytest tests/

# Manual testing checklist:
# ✅ Dark mode toggle
# ✅ Sidebar collapse/expand
# ✅ Mobile responsiveness
# ✅ Message sending/receiving
# ✅ Settings persistence
# ✅ Keyboard shortcuts
# ✅ Accessibility features
```

## 📱 Browser Support

- **Chrome**: 90+ ✅
- **Firefox**: 88+ ✅
- **Safari**: 14+ ✅
- **Edge**: 90+ ✅
- **Mobile Safari**: 14+ ✅
- **Chrome Mobile**: 90+ ✅

## ♿ Accessibility Features

- **Keyboard Navigation**: Full keyboard support
- **Screen Reader**: ARIA labels and semantic HTML
- **High Contrast**: Support for high contrast mode
- **Reduced Motion**: Respects user motion preferences
- **Focus Indicators**: Clear focus states for all interactive elements

## 🔒 Security Considerations

- **Input Validation**: Client and server-side validation
- **XSS Protection**: Proper HTML escaping
- **CSRF Protection**: Implement if needed for your use case
- **Content Security Policy**: Consider adding CSP headers

## 🚀 Deployment

### **Local Development**
```bash
python app.py
```

### **Production Deployment**
1. **Set up a production server** (e.g., Ubuntu with Nginx)
2. **Install Python and dependencies**
3. **Use Gunicorn or uWSGI** for production WSGI server
4. **Configure Nginx** as reverse proxy
5. **Set up SSL certificates** for HTTPS
6. **Configure environment variables**

### **Docker Deployment**
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

### **Render Deployment**
```bash
# Create Procfile
echo "web: python app.py" > Procfile

# Deploy to Render
# 1. Connect your GitHub repository to Render
# 2. Create a new Web Service
# 3. Set the following configuration:
#    - Build Command: pip install -r requirements.txt
#    - Start Command: python app.py
#    - Environment: Python 3.9
#    - Port: 5000
```

**Render Configuration:**
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python app.py`
- **Environment**: Python 3.9
- **Port**: 5000
- **Auto-Deploy**: Enable for automatic deployments from GitHub

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Inter Font**: Beautiful typography by Google Fonts
- **CSS Variables**: Modern theming system
- **Flask**: Lightweight Python web framework
- **Vanilla JavaScript**: No framework dependencies

## 📞 Support

- **Issues**: Report bugs on GitHub Issues
- **Questions**: Ask questions in GitHub Discussions
- **Feature Requests**: Submit via GitHub Issues

---

**Made with ❤️ using Flask and vanilla JavaScript**

*Last updated: December 2024* 