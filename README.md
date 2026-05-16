# KetanWeather

An AI-powered weather assistant built with Streamlit. It uses an OpenAI-compatible API to generate weather information for any city.

## Features

- Enter any city name to get weather details
- Returns temperature (°C and °F), conditions, humidity, wind speed, and a short forecast
- API key and base URL are loaded from a `.env` file and can be overridden in the sidebar at runtime
- Supports any OpenAI-compatible API endpoint (e.g. Hack Club AI proxy)

## Setup

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment variables**

   Create a `.env` file in the project root (already set up):

   ```env
   API_KEY=your-api-key-here
   BASE_URL=https://ai.hackclub.com/proxy/v1
   ```

3. **Run the app**

   ```bash
   streamlit run ketanweather.py
   ```

## Project Structure

```
claudecode/
├── ketanweather.py   # Main Streamlit app
├── requirements.txt  # Python dependencies
├── .env              # API key and base URL (not committed)
├── .gitignore        # Ignores .env and build artifacts
├── README.md         # This file
└── CLAUDE.md         # Context for Claude Code
```

## Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `openai` | OpenAI-compatible API client |
| `python-dotenv` | Loads `.env` into environment variables |

## Notes

- The app does not call a live weather API — it uses an LLM to generate weather estimates. Real-time accuracy is not guaranteed.
- The sidebar lets you change the API key, base URL, and model without editing any files.
