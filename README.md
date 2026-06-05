# Code-Review-Buddy

> AI-powered code reviewer built with FastAPI and Groq LLM.  
> 🚧 Building toward: LangChain agents + RAG + static analysis tools (see roadmap)

## ✨ Features

- 🤖 AI-powered Python code review using Groq's Llama 3.3 70B model
- 🛡️ Typed request/response validation via Pydantic
- 📚 Auto-generated OpenAPI documentation at `/docs`
- 🔐 Secure credential management via environment variables
- 🏥 Health check endpoint for monitoring

## 🛠️ Tech Stack

- **FastAPI** — modern Python web framework for building APIs
- **Uvicorn** — ASGI server for running FastAPI applications
- **Groq** — LLM inference API (using Llama 3.3 70B model)
- **python-dotenv** — environment variable management
- **Pydantic** — data validation via type hints


## 🚀 Setup

### Prerequisites
- Python 3.11+
- Git
- A Groq API key ([get one free here](https://console.groq.com))

### Installation

```bash
# Clone the repository
git clone https://github.com/Soundarya0512/Code-Review-Buddy.git
cd Code-Review-Buddy

# Create and activate virtual environment
python -m venv venv

# On Windows (Git Bash):
source venv/Scripts/activate

# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Running the app

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the API.


## 📡 API Endpoints

### `GET /health`

Health check endpoint.

**Response:**
```json
{
  "status": "healthy",
  "message": "Code Review Buddy is running"
}
```

### `POST /review_input`

Submit Python code for AI-powered review.

**Request:**
```json
{
  "code": "def add(a, b):\n    return a+b"
}
```

**Response:**
```json
{
  "review": "The function is simple and correct, but could benefit from..."
}
```



## 🗺️ Roadmap

- [x] **Week 1-2:** FastAPI MVP with Groq LLM integration ✅
- [ ] **Week 3-4:** Static analysis tool integration (pylint, bandit, radon)
- [ ] **Week 5-6:** LangChain agent orchestration for tool selection
- [ ] **Week 7:** RAG layer with style guides (PEP 8, OWASP)
- [ ] **Week 8:** Observability with Langfuse, CI/CD, deployment to Hugging Face Spaces

## 👤 Author

Soundarya
GitHub: @Soundarya0512
LinkedIn: linkedin.com/in/soundarya-kishore
