# CLAUDE.md

Context for Claude Code when working in this repository.

## Project

**KetanWeather** — a single-file Streamlit app that uses an OpenAI-compatible LLM to generate weather info for a given city.

## Key Files

- `ketanweather.py` — the entire app (UI + API call), single file, keep it that way
- `requirements.txt` — pip dependencies: streamlit, openai, python-dotenv
- `.env` — holds `API_KEY` and `BASE_URL`; never commit this file
- `.gitignore` — already excludes `.env` and Python build artifacts

## API Details

- **Provider**: Hack Club AI proxy (OpenAI-compatible)
- **Base URL**: `https://ai.hackclub.com/proxy/v1`
- **Client**: `openai.OpenAI` with custom `base_url` — not the official OpenAI endpoint
- **Default model**: `gpt-4o-mini` (user can override in sidebar)

## Environment Variables

| Variable | Description |
|---|---|
| `API_KEY` | API key for the LLM provider |
| `BASE_URL` | Base URL for the OpenAI-compatible endpoint |

Loaded via `python-dotenv` (`load_dotenv()` at the top of `ketanweather.py`). The sidebar pre-fills from these values but allows runtime overrides.

## Conventions

- Keep the app as a single file (`ketanweather.py`) — no splitting into modules unless explicitly asked
- Do not add a real weather API (e.g. OpenWeatherMap) unless the user asks — the LLM response is intentional
- Do not commit `.env` under any circumstances
- No comments in code unless the logic is non-obvious
- Streamlit reruns the entire script on each interaction — keep state considerations in mind

## Running Locally

```bash
pip install -r requirements.txt
streamlit run ketanweather.py
```
