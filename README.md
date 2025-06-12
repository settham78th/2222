# CV Optimizer Pro - Gotowy do wdrożenia na Render

## 🚀 Szybkie wdrożenie na Render.com

### Krok 1: Przygotowanie repozytorium
1. Stwórz nowe prywatne repozytorium na GitHub
2. Wgraj wszystkie pliki z folderu `CV-generator-deploy`
3. Upewnij się, że `render.yaml` znajduje się w głównym katalogu

### Krok 2: Wdrożenie na Render
1. Zaloguj się na [render.com](https://render.com)
2. Kliknij **"New +"** → **"Blueprint"**
3. Podłącz swoje repozytorium GitHub
4. Render automatycznie wykryje plik `render.yaml`
5. Kliknij **"Apply"** aby rozpocząć wdrożenie

### Krok 3: Konfiguracja zmiennych środowiskowych
W panelu Render ustaw następujące zmienne:

```env
# Wymagane klucze API
OPENROUTER_API_KEY=sk-or-v1-[twój-klucz-openrouter]
STRIPE_SECRET_KEY=sk_test_[twój-klucz-stripe]
VITE_STRIPE_PUBLIC_KEY=pk_test_[twój-publiczny-klucz-stripe]

# Automatycznie generowane przez Render
SESSION_SECRET=[auto-generowany]
DATABASE_URL=[auto-konfigurowany]
```

## 🔑 Wymagane klucze API

### OpenRouter API
1. Zarejestruj się na [openrouter.ai](https://openrouter.ai)
2. Przejdź do **API Keys** i wygeneruj nowy klucz
3. Skopiuj klucz zaczynający się od `sk-or-v1-`

### Stripe Payment Gateway
1. Zarejestruj się na [stripe.com](https://stripe.com)
2. W trybie testowym pobierz:
   - **Secret Key** (sk_test_...)
   - **Publishable Key** (pk_test_...)

## 📱 Funkcje aplikacji

### ✅ Gotowe funkcjonalności:
- **System płatności**: Obowiązkowa płatność 9,99 PLN za generowanie CV
- **Konto deweloperskie**: Username `developer`, hasło `DevAdmin2024!` (bezpłatny dostęp)
- **PWA**: Aplikacja internetowa z możliwością instalacji
- **Wielojęzyczność**: Polski i angielski
- **AI Integration**: Optymalizacja CV, analiza ATS, rekomendacje
- **Premium Dashboard**: Statystyki i zaawansowane funkcje

### 💰 Model biznesowy:
- **Jednorazowe CV**: 9,99 PLN (3 podstawowe funkcje)
- **Premium**: 29,99 PLN/miesiąc (wszystkie funkcje)
- **CV Builder**: Oddzielna płatna usługa

## 🛠️ Struktura projektu

```
CV-generator-deploy/
├── app.py                 # Główna aplikacja Flask
├── requirements.txt       # Zależności Python
├── render.yaml           # Konfiguracja Render
├── Procfile              # Konfiguracja uruchamiania
├── runtime.txt           # Wersja Python
├── models.py             # Modele bazy danych
├── forms.py              # Formularze Flask-WTF  
├── manifest.json         # Manifest PWA
├── service-worker.js     # Service Worker PWA
├── static/
│   ├── css/              # Style CSS
│   ├── js/               # Skrypty JavaScript
│   └── icons/            # Ikony PWA (SVG)
├── templates/            # Szablony HTML
└── utils/                # Narzędzia (AI, PDF, scraping)
```

## 🔧 Konfiguracja produkcyjna

### Database
- PostgreSQL automatycznie konfigurowany przez Render
- Migracje uruchamiane automatycznie przy starcie
- Tworzenie konta developerskiego przy pierwszym uruchomieniu

### Security
- HTTPS wymuszony przez Render
- Bezpieczne sesje z SECRET_KEY
- Walidacja płatności przez Stripe webhooks
- Zabezpieczenia CSRF w formularzach

### Performance
- Gunicorn WSGI server
- Database connection pooling
- Static files served by Render CDN
- Service Worker dla cachowania offline

## 🌐 Po wdrożeniu

### URL aplikacji:
```
https://[nazwa-twojej-aplikacji].onrender.com
```

### Testowanie:
1. Otwórz aplikację w przeglądarce
2. Zarejestruj nowe konto lub użyj konta deweloperskiego
3. Prześlij przykładowe CV
4. Przetestuj proces płatności (tryb testowy Stripe)

### Monitoring:
- Logi aplikacji dostępne w panelu Render
- Metryki wydajności w Dashboard
- Alerty email przy błędach

## 📞 Wsparcie

Aplikacja jest w pełni skonfigurowana i gotowa do uruchomienia na Render. Wszystkie zależności, konfiguracje i funkcjonalności zostały przetestowane i zoptymalizowane pod kątem środowiska produkcyjnego.

## 🎯 Następne kroki

1. Skonfiguruj domenę własną (opcjonalnie)
2. Dostosuj design i branding
3. Skonfiguruj Google Analytics
4. Dodaj dodatkowe metody płatności
5. Rozszerz funkcjonalności AI