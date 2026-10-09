# 🌤️ Weather Agent

A simple AI-powered Weather Agent built using Python. The agent fetches weather information for a given location and demonstrates how to use environment variables for secure API key management.

---

## Project Structure

```text
Agent/
│
├── .env                # Stores API keys and secrets
├── .env.example        # Sample environment variables file
├── .gitignore
├── agent.py            # Main application entry point
├── simple_weather.py   # Weather utility and API functions
├── requirements.txt    # Project dependencies
└── README.md
```

---

## Features

- Get current weather information
- Secure API key handling using `.env`
- Clean and modular Python code
- Easy to extend with new weather-related functionalities
- Beginner-friendly project structure

---

## Prerequisites

Before running the project, make sure you have:

- Python 3.9 or higher
- pip (Python package manager)
- A Weather API Key

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/weather-agent.git
cd weather-agent
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
