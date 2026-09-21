# Praktický test 

Jednoduchá webová aplikace pro vyhledávání, vytvořená jako řešení praktického testu

## Funkce

- Vyhledávací pole s dotazem na klíčové slovo
- Získání organických výsledků z první stránky Google (přes Serper API)
- Export výsledků do CSV
- Pokryto unit testy (pytest)

## Technologie

- **Backend:** Python, FastAPI
- **Frontend:** HTML, CSS, vanilla JavaScript
- **Vyhledávání:** Serper API (Google Search)
- **Testování:** pytest
- **Nasazení:** Docker, Render.com

## Struktura projektu

.
├── main.py # FastAPI backend
├── index.html # Frontend
├── input.css / output.css # Styly
├── test_main.py # Unit testy
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env # API klíč (lokálně, není v gitu)


## Jak spustit lokálně

1. V kořeni projektu vytvořte soubor `.env` s obsahem:

SERPER_API_KEY=váš_klíč_zde

2. Spusťte:
```bash
   docker-compose up --build
```
3. Otevřete v prohlížeči:

http://localhost:8000


## Jak spustit testy

```bash
pytest -v
```

## Živá ukázka

https://inizio-xaej.onrender.com 

## API klíč

Klíč pro Serper API se získá zdarma na [serper.dev](https://serper.dev) (2500 dotazů zdarma). 
