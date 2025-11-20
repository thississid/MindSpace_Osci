# Osci's Intelligence 🤖

A modern, ChatGPT-inspired local AI chat application powered by Ollama, featuring a clean interface with retro terminal aesthetics.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Next.js](https://img.shields.io/badge/Next.js-14-black)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![Ollama](https://img.shields.io/badge/Ollama-Local-orange)

## ✨ Features

- 🚀 **Local AI Processing** - Run powerful language models locally using Ollama
- 🎨 **Modern UI** - ChatGPT-inspired interface with clean, responsive design
- 🖥️ **Retro Sidebar** - Terminal-style session history with vintage aesthetics
- 🔄 **Model Switching** - Dynamically switch between different Ollama models
- ⚡ **Real-time Streaming** - See AI responses as they're generated
- 💬 **Markdown Support** - Full markdown rendering with code syntax highlighting
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile

## 🛠️ Tech Stack

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe development
- **Tailwind CSS** - Utility-first styling
- **React Markdown** - Markdown rendering
- **Lucide React** - Beautiful icons

### Backend
- **FastAPI** - Modern Python web framework
- **Ollama** - Local LLM inference
- **HTTPX** - Async HTTP client
- **Pydantic** - Data validation

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v18 or higher)
- **Python** (v3.8 or higher)
- **Ollama** - [Download here](https://ollama.ai)

## 🚀 Quick Start

### 1. Install Ollama

```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Or download from https://ollama.ai
```

### 2. Pull a Model

```bash
ollama pull llama3
# Or try other models: mistral, codellama, phi, etc.
```

### 3. Clone the Repository

```bash
git clone https://github.com/thississid/MindSpace_Osci
cd CHat
```

### 4. Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn main:app --reload
```

The backend will be running at `http://localhost:8000`

### 5. Setup Frontend

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

The frontend will be running at `http://localhost:3000`

### 6. Start Chatting! 🎉

Open your browser and navigate to `http://localhost:3000`

## 📁 Project Structure

```
CHat/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   └── venv/               # Virtual environment
│
├── frontend/
│   ├── app/
│   │   ├── globals.css     # Global styles
│   │   ├── layout.tsx      # Root layout
│   │   └── page.tsx        # Home page
│   ├── components/
│   │   ├── ChatInterface.tsx  # Main chat component
│   │   └── Message.tsx        # Message display component
│   ├── package.json
│   └── next.config.js
│
└── README.md
```

## 🎨 Features in Detail

### Model Selection
Switch between different Ollama models on the fly. The dropdown in the footer allows you to select from all locally available models.

### Session History
The retro-styled sidebar keeps track of your conversation sessions with timestamps and quick access.

### Markdown Support
Full markdown rendering including:
- Code blocks with syntax highlighting
- Lists (ordered and unordered)
- Headers
- Inline code
- And more!

### Streaming Responses
Watch as the AI generates responses in real-time, just like ChatGPT.

## 🔧 Configuration

### Backend Configuration

Edit `backend/main.py` to customize:
- CORS settings
- Ollama server URL (default: `http://localhost:11434`)
- API endpoints

### Frontend Configuration

Edit `frontend/components/ChatInterface.tsx` to customize:
- Default model
- UI colors and styling
- Message formatting

## 🎯 Available Models

You can use any model available in Ollama:

```bash
# List installed models
ollama list

# Pull new models
ollama pull mistral
ollama pull codellama
ollama pull phi
```

Popular models:
- **llama3** - Meta's latest Llama model
- **mistral** - Fast and efficient
- **codellama** - Specialized for coding
- **phi** - Lightweight and fast

## 🐛 Troubleshooting

### Backend won't start
- Ensure Ollama is running: `ollama serve`
- Check if port 8000 is available
- Verify Python dependencies are installed

### Frontend won't connect
- Ensure backend is running on port 8000
- Check CORS settings in `backend/main.py`
- Verify Node.js dependencies are installed

### No models available
- Pull at least one model: `ollama pull llama3`
- Restart the backend after pulling models

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is licensed under the MIT License.

## 🙏 Acknowledgments

- [Ollama](https://ollama.ai) - For making local LLMs accessible
- [Next.js](https://nextjs.org) - For the amazing React framework
- [FastAPI](https://fastapi.tiangolo.com) - For the modern Python web framework
- [ChatGPT](https://chat.openai.com) - For UI/UX inspiration

## 📧 Contact

Created by Siddartha Yadav

---

**Note**: This application runs entirely locally. Your conversations are private and never leave your machine.
