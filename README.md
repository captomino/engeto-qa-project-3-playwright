# Automatizované testování e-shop aplikace (Playwright)

![Project Status](https://img.shields.io/badge/status-⏳_Awaiting%20Review-yellow)


## O projektu

Projekt je zaměřen na **automatizované end-to-end testování e-shopové webové aplikace SauceDemo**:  
https://www.saucedemo.com

Testy simulují reálné uživatelské scénáře od přihlášení až po odhlášení a pokrývají základní funkcionality aplikace, jako je práce s produkty a košíkem.

Projekt byl realizován v rámci **ENGETO Testing Akademie** a slouží jako ukázka implementace UI automatizovaných testů v Pythonu pomocí Playwright a pytest.

> Projekt splňuje zadání (minimálně 3 testy) a obsahuje rozšířenou sadu 10 testů (včetně parametrizovaných variant) pokrývajících klíčové uživatelské scénáře.


## Rozsah testování

Testovací sada pokrývá následující oblasti:

### Přihlášení uživatele
  - validní přihlášení
  - nevalidní přihlašovací údaje  

### Produkty
  - načtení seznamu produktů po přihlášení
  - přidání více různých produktů (parametrizovaný test)

### Košík
  - přidání produktu do košíku
  - odebrání produktu z košíku
  - kontrola obsahu košíku  

### Odhlášení
- odhlášení uživatele přes menu

Testy využívají Playwright fixtures a assertion knihovnu `expect` pro zajištění stability a čitelnosti.


## Struktura projektu

```plaintext
engeto-qa-project-3-playwright/
├─ tests/
│  └─ test_saucedemo.py
├─ conftest.py
├─ pytest.ini
├─ requirements.txt
├─ .gitignore
└─ README.md
```


## Spuštění projektu

### Instalace

Stažení projektu:

```bash
git clone https://github.com/captomino/engeto-qa-project-3-playwright
cd engeto-qa-project-3-playwright
```

Vytvoření virtuálního prostředí:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

Instalace závislostí:

```bash
pip install -r requirements.txt
```

Instalace Playwright prohlížečů:

```bash
playwright install
```

### Spuštění testů

Spuštění všech testů:

```bash
pytest
```

Spuštění konkrétního testu:

```bash
pytest -k test_login_success
```

Spuštění v UI režimu:
```bash
pytest --headed --slowmo 500
```


## Výsledky testů

- **Celkem testů:** 10 (včetně parametrizovaných variant) 
- **Úspěšné:** 10 
- **Neúspěšné:** 0  

Testy jsou navrženy jako **nezávislé a opakovatelné**, s důrazem na stabilitu a čitelnost. 

Testy byly úspěšně spuštěny v prostředí Chromium pomocí Playwright.

## Omezení projektu

- testováno na veřejné demo aplikaci
- omezený rozsah scénářů (modelový projekt)
- neřeší pokročilé scénáře (např. paralelní běhy, CI/CD integrace)


## Možná rozšíření
- implementace Page Object Model (POM)
- integrace do CI/CD (např. GitHub Actions)
- vizuální testing (screenshot comparison)
- rozšíření parametrizovaných testů
- generování reportů (Allure / HTML report)


## Autor

**Tomáš Čáp**  
Projekt vytvořen v rámci ENGETO Testing Akademie (2026)  
GitHub: https://github.com/captomino


## Licence

Projekt je určen pro vzdělávací účely.