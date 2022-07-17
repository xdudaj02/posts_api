#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drf_api.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


'''
Vytvor microservice v Pythone, ktorý bude sprostredkovať RESTful API na manažovanie príspevkov používateľov. 
Formát príspevku je nasledovný:
- id: integer
- userId: integer
- title: string
- body: string

Funkčné požiadavky:
- Pridanie príspevku - potrebné validovať userID pomocou externej API
- Zobrazenie príspevku
   - na základe id alebo userId
   - ak sa príspevok nenájde v systéme, je potrebné ho dohľadať pomocou externej API a uložiť (platné iba pre vyhľadávanie pomocou id príspevku)
- Odstránenie príspevku
- Upravenie príspevku - možnosť meniť title a body

Externú API nájdeš na linku https://jsonplaceholder.typicode.com/ - používaj endpointy users a posts.

Všeobecné požiadavky:
- ReadMe s popisom inštalácie a prvého spustenia
- Dokumentácia API (napr. Swagger)
- Validácia vstupných dát
- Použitie ORM

Riešenie by malo demonštrovať schopnosti pracovať s (čím viac tým lepšie):
- ORM
- REST
- Práca s API tretích strán
- Validácia vstupov
- Error handling
- Rozumným štrukturovaním zdrojových kódov aplikácie

Voliteľné úlohy:
- neposkytovať iba API, ale poskytovať aj jednoduchý frontend podporujúci tieto funkcie
- kontajnerizácia (napr. cez Docker)
'''