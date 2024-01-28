import random

class MovieBase:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        self._liczba_odtworzeń = liczba_odtworzeń 

    @property
    def play(self):
        self._liczba_odtworzeń += 1
        return f"{self.tytuł} został obejrzany {self._liczba_odtworzeń} razy"
    
    def __str__(self):
        return f"Tytuł: {self.tytuł}, Rok wydania: {self.rok_wydania}, Gatunek: {self.gatunek}, Odtworzenia: {self._liczba_odtworzeń}\n"

class Series(MovieBase):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu
   
    @property
    def play(self):
        super().play
        return f"{self.tytuł} o numerze {self.numer_odcinka}{self.numer_sezonu} został obejrzany {self._liczba_odtworzeń} razy"

    def __str__(self):
        return  f"Tytuł: {self.tytuł}, Rok wydania: {self.rok_wydania}, Gatunek: {self.gatunek}, " \
               f"Numer odcinka: {self.numer_odcinka}, Numer sezonu: {self.numer_sezonu}, " \
               f"Odtworzenia: {self._liczba_odtworzeń}\n" 

    
series1 = Series(tytuł="Gra o tron", rok_wydania="2015", gatunek="Fantasy", numer_odcinka="E01", numer_sezonu="S01", liczba_odtworzeń=10)
series2 = Series(tytuł="Pacyfik", rok_wydania="2010", gatunek="Historyczny", numer_odcinka="E01", numer_sezonu="S01", liczba_odtworzeń=8)
series3 = Series(tytuł="Entourage", rok_wydania="2007", gatunek="Fabularny", numer_odcinka="E01", numer_sezonu="S01", liczba_odtworzeń=15)
series4 = Series(tytuł="Egzorcysta", rok_wydania="2016", gatunek="Realistyczny", numer_odcinka="E01", numer_sezonu="S01", liczba_odtworzeń=12)
series5 = Series(tytuł="Kapitan Bomba", rok_wydania="2010", gatunek="Realistyczny", numer_odcinka="E01", numer_sezonu="S01", liczba_odtworzeń=20)

movie1 = MovieBase(tytuł="Arnold Schwarzenegger", rok_wydania="1945", gatunek="dokument", liczba_odtworzeń=5)
movie2 = MovieBase(tytuł="Herkules w Nowym Yorku", rok_wydania="1970", gatunek="Historyczny", liczba_odtworzeń=8)
movie3 = MovieBase(tytuł="Terminator", rok_wydania="1982", gatunek="Sci-fi", liczba_odtworzeń=15)
movie4 = MovieBase(tytuł="Conan Barbarzyńca", rok_wydania="1989", gatunek="Fantasy", liczba_odtworzeń=12)
movie5 = MovieBase(tytuł="Conan Niszczyciel", rok_wydania="1991", gatunek="Fantasy", liczba_odtworzeń=20)

biblioteka = [series1, series2, series3, series4, series5, movie1, movie2, movie3, movie4, movie5]

def baza_view():
    asking = input("Jaką bazę chcesz otworzyć? Filmy czy Seriale?:  ")
    if asking.lower() == "seriale":
        sorted_series = sorted([item for item in biblioteka if isinstance(item, Series)], key=lambda x: x.tytuł)
        for item in sorted_series:
            print(item)
    elif asking.lower() == "filmy":
        sorted_movies = sorted([item for item in biblioteka if isinstance(item, MovieBase)], key=lambda x: x.tytuł)
        for item in sorted_movies:
            print(item)
    else:
        print("Wybrano niepoprawną opcję")

print(series1.play)
print(movie2.play)
baza_view()

def szukaj(biblioteka, title):
    for item in biblioteka:
        if item.tytuł.lower() == title.lower():
            return item
    return None

def szukanie():
    ask = input("Jakiego tytułu szukasz?: ")
    found_item = szukaj(biblioteka, ask)
    if found_item:
        print("Znaleziono", found_item)
    else:
        print("Nie znaleziono elementu o podanym tytule.")

szukanie()

def generate_views(item):
    views = random.randint(1, 100)
    item._liczba_odtworzeń += views

for item in biblioteka:
    for _ in range(10):
        generate_views(item)
        print(f"{item.tytuł} wyświetlono {item._liczba_odtworzeń} razy")
        break

def top_titles(biblioteka, n):
    return sorted(biblioteka, key=lambda x: x._liczba_odtworzeń, reverse=True)[:n]

najpopularniejsze_tytuly = top_titles(biblioteka, 3)

print("\nNajpopularniejsze tytuły:")
for pozycja in najpopularniejsze_tytuly:
    print(f"{pozycja.tytuł} - Odtworzenia: {pozycja._liczba_odtworzeń}")