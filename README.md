### [PL]
Aplikacja wykorzystuje API OpenAI, by przekształcić plik tekstowy (zawierający treść artykułu) w plik HTML, dodając odpowiednie grafiki tam, gdzie warto je dodać. Uzyskany plik powinien być gotowy do wklejenia między tagi `<body>` i `</body>`. Repozytorium zawiera przykładowy tekst artykułu, wygenerowany artykuł, szablon HTML, oraz podgląd całości.

Aby uruchomić aplikację: 
1. Sklonuj repozytorium (lub pobierz jego zawartość).
2. Dodaj zmienną środowiskową OPENAI_API_KEY z poprawnym kluczem, lub dodaj do folderu z projektem plik `.env` o treści `OPENAI_API_KEY = twój_klucz`.
3. Otwórz konsolę w folderze z projektem i uruchom program komendą `python main.py` lub otwórz projekt w wybranym IDE i uruchom plik `main.py` (uruchomienie może wymagać zainstalowania bibliotek openai i python-dotenv, w przypadku czego zainstaluj je poleceniem `pip install openai python-dotenv`).
4. Podmień treść pliku `text_file.txt`, by stworzyć inny artykuł.

### [ENG]
The app uses OpenAI's API to transform a text file (containing an article's content) into an HTML file, and add images in appropriate places. The generated file should be ready to paste in between the `<body>` and `</body>` tags. The repo includes example article content, generated article, HTML template and a complete preview.

To run the app:
1. Clone the repo (or download its contents).
2. Add an environmental variable OPENAI_API_KEY with a valid key, or add a `.env` file with `OPENAI_API_KEY = your_key` to the project's directory.
3. Open the console in the project's directory and run the program with `python main.py` or open the project in an IDE and run `main.py` (running it may require you to install the openai and python-dotenv library, in which case do so with `pip install openai python-dotenv`.)
4. Replace the content of `text_file.txt` to create a different article.
