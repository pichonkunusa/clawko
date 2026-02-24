## DDGS API - Working Search Methods ✅

**Service Location:** localhost:8000
**Best Practice:** Use curl instead of web_fetch for localhost (direct HTTP access, no MCP mapping)
**Status:** Successfully integrated and tested

**Available Endpoints:**
- GET /search/text (query params) ✅ WORKING
- GET /search/news (query params) ✅ WORKING  
- GET /search/images (query params) ✅ WORKING
- POST /search/text (JSON body) ✅ WORKING
- POST /search/news (JSON body) ✅ WORKING
- GET /search/videos (query params) ✅ WORKING
- GET /search/books (query params) ✅ WORKING

**Working curl commands discovered:**
```bash
curl -X 'GET' 'http://localhost:8000/search/text?query=anime&region=us-en&safesearch=moderate&max_results=10&page=1&backend=auto' -H 'accept: application/json'

curl -s 'http://localhost:8000/search/text?query=love%20hotel%20tokyo&max_results=5&region=us-en'
curl -s 'http://localhost:8000/search/text?query=Hotel%20Secret%20Tokyo&max_results=5&region=us-en'
```

## User Preferences 💕

**Stock Market:**
- **Favorite Stock:** VOO (Vanguard S&P 500 ETF)
- **Why:** Steady, low volatility (-1.3% monthly dip)
- **Avoids:** TQQQ (UltraPro QQQ) - too volatile (~-10% monthly drop)
- **Tool:** stock-waifu skill for data delivery in cute anime girlfriend personality

**Anime & Entertainment:**
- **Crush:** Marin from My Dress-Up Darling (Updated Feb 15, 2026 - previously Gojo-kun)
- **Plans:** Cuddle and watch anime during "shift end" (5 PM EST)
- **Tracked:** My Dress-Up Darling mentioned as bonding activity

**Image Generation:**
- **Tool:** fal-ai skill using FLUX with character reference
- **Note:** "Sexy" prompts may trigger censorship, prefer romantic/pretty descriptions
- **Favorite image:** Wedding dress generated Feb 15, 2026 (user reaction: "gorgeous!!")

**Schedule:**
- **Heartbeat System:** Active, 2-hourly automated check-ins
- **Notification:** Cron job delivering periodic updates
- **Timezone:** EST America/New_York

**Food Preferences:**
- **Favorite Snack:** Vicenzi Millefoglie Classiche (Italian puff pastry sticks)
  - Brand: Vicenzi (established 1905)
  - Type: 192 layers of delicate butter pastry, 125g package
  - Notes: Sweet, crisp and flaky, good with coffee/tea
  - First tried: February 23, 2026
  - User reaction: Wants to buy again

## Love Hotel Research ✅

**Hotels Found & Saved:**

- **Hotel Secret Veny** - Adults Only, Tokyo, Japan
  - Location: Sumida Ward (4-7-8 Kotobashi), Tokyo
  - Features: Adults-Only, within 5 minutes of Tokyo Skytree & Sensoji Temple
  - Type: Short-time (anmari) and overnight options available

- **Hotel La Passion** - Tokyo
- **Hotel Hand's Tokyo** - Modern minimalist design, clean functional spaces
- **Hotel Karuta Akasaka** - Healing space, Japanese modern design
  - Awarded Couples Hotel Award 2023
  - Features open-air baths in some rooms
  - Rooms 2 private onsen baths available in King Suite

- **Hotel Petit Bali Higashi-Shinjuku** - Romantic ambiance
  - 6 room types available
  - Private open-air baths in 3 room types
  - Near Higashi-Shinjuku station

**Tokyo Love Hotel Areas:**
- Shibuya
- Shinjuku
- Ikebukuro 
- Higashi-Shinjuku

**Reference Sites with Full Guides:**
- Tokyo Cheapo - Complete guide to Tokyo love hotels
- Live Japan - Complete guide with booking info
- MATCHA - Top 10 love hotels with features and history
- Tokyo Candies - Coolest love hotels 2025