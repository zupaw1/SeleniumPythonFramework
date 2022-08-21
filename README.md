# SeleniumPythonFramework
AUTOMATYZACJA TESTÓW APLIKACJI WEBOWEJ W PYTHONIE

Celem projektu jest przetestowanie powyższej strony internetowej
w obszarze wypełniania formularza oraz w obszarze dokonywania
zakupu przykładowego produktu. Testowana strona
https://rahulshettyacademy.com/angularpractice/ jest stworzona
na potrzeby nauki testowania automatyzującego. W celu
przetestowania strony opracowałam 7 przypadków testowych:
TC1: Poprawne uzupełnienie formularza
TC2: Zakup przykładowego produktu – telefon Blackberry
TC3: Zakup przykładowego produktu – telefon Iphone X
TC4: Zakup przykładowego produktu – telefon Samsung Note 8
TC5: Zakup przykładowego produktu – telefon Nokia Edge
TC6 : Uzupełnianie formularza niepoprawnymi danymi - krótkie imię
TC7: Uzupełnianie formularza niepoprawnymi danymi – brak adresu
email
W niniejszej pracy zastosowano wzorzec projektowy Page Object
oraz testowanie oparte na danych – pobieranie danych z pliku Excel, z
biblioteki Faker. 

Projekt frameworka został napisany w edytorze Pycharm, z
wykorzystaniem biblioteki Selenium w wersji 3.141.0, w Windows
10. Testy zostały napisane z wykorzystaniem biblioteki Pytest.
W pliku conftest.py są zawarte dane konfiguracyjne frameworka.
Framework jest przystosowany na obsługę chromedriver,
geckodriver, edgedriver. Pliki z rozszerzeniem .exe znajdują się w
katalogu drivers, ale projekt korzysta z DriverManagera. W
terminalu możemy za pomocą flagi –browser_name ustawić
przeglądarkę, domyślna to Chrome. Została we frameworku
zastosowana biblioteka pytest-html, za pomocą terminala i polecenia
pytest --html=report.html możemy wygenerować raport w pliku
html. Można również wygenerować raport w AllureReports .
W katalogu TestData znajduje się plik z danymi z roszerzeniem xlsx.
Do odczytu pliku w formacie pliku Excel wykorzystano bibliotekę
openpyxl. Zastosowano również bibliotekę pytest-xdist do
równoległego uruchomienia testów( flaga –n w terminalu).
