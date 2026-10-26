**Polski** | [English](README.en.md)

# Python Bootcamp — 100 Days of Code (dzień 16+)

Kontynuacja mojej pracy nad kursem **100 Days of Code: The Complete Python Pro Bootcamp**, od 16. dnia — części kursu, w której każdy projekt to samodzielny skrypt zamiast szablonu JetBrains Academy. Dni 1–15 są w repozytorium [Python_Basics](https://github.com/francesspot/Python_Basics).

Główny nacisk to **programowanie obiektowe** i proste gry napisane z użyciem modułu `turtle`.

## Projekty

| Folder | Dzień | Co to jest |
|--------|-------|------------|
| `day-16-start` | 16 | Wprowadzenie do OOP; **Coffee Machine** przepisany na klasy (`CoffeeMaker`, `Menu`, `MoneyMachine`) |
| `day-17-start` | 17 | Tworzenie własnych klas; **Quiz Game** (`Question`, `QuizBrain`) |
| `day-18-start` | 18 | Grafika żółwia; **Hirst Painting** — obraz z kropek w kolorach pobranych ze zdjęcia |
| `day-19-start` | 19 | Obsługa zdarzeń; Etch-a-Sketch i **wyścig żółwi** z obstawianiem |
| `snake_game` | 20–21, 24 | **Snake** — z tablicą wyników i rekordem zapisywanym w `data.txt` |
| `pong_game` | 22 | **Pong** dla dwóch graczy |
| `turtle-crossing-start` | 23 | **Turtle Crossing** — gra w stylu Froggera z coraz szybszymi poziomami |
| `day-24-start` | 24 | Odczyt i zapis plików |
| `Mail Merge Project Start` | 24 | **Mail Merge** — generuje spersonalizowane zaproszenie dla każdego nazwiska z listy |

## Wymagania

Python 3 z `tkinter` (potrzebny modułowi `turtle`; jest w standardowych instalatorach dla Windows/macOS). Dwa projekty wymagają dodatkowych pakietów:

```bash
pip install prettytable colorgram.py
```

## Uruchamianie

Każda gra importuje własne moduły, więc uruchamiaj ją z jej folderu:

```bash
cd snake_game
python main.py
```

Wyjątkiem jest Mail Merge — używa ścieżek względem katalogu głównego repozytorium:

```bash
python "Mail Merge Project Start/main.py"
```
