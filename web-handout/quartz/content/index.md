---
title: PDS 2024 - Python Web Handout
---

Vítejte na úvodní stránce handoutu, který vám poskytne základy a praktické ukázky pro pochopení paralelního programování a distribuovaných systémů s využitím jazyka Python. Tento materiál je rozdělen do několika tématických částí, které vás postupně provedou od teoretického úvodu až po pokročilejší použití externích nástrojů a technologií.

---

## Obsah

1. [Úvod do paralelizace v Pythonu](uvod_do_paralelizace.md)
   Ořibližuje vývoj paralelizace v Pythonu od zavedení GIL, jeho omezení na vícejádrových procesorech, až po moderní přístupy jako multiprocessing, concurrent.futures a asyncio. Nabízí také pohled na budoucnost Pythonu bez GIL díky PEP 703.

2. [Synchronizační nástroje standardní knihovny Pythonu](synchronizacni_nastroje_std_knihovny.md)
   Podrobný přehled o modulech `threading`, `multiprocessing`, a `asyncio`, které Python nabízí pro paralelní a asynchronní programování.

3. [Problémy Pythonu a externí nástroje](problemy_jazyka_python_a_externi_nastroje.md)
   Přehled omezení jazyka Python, jako je GIL, a o možnostech jejich překonání pomocí technologií jako je multiprocessing, JIT kompilace, či statická kompilace. Také se seznámíte s nástroji pro paralelizaci a distribuované výpočty, například Dask nebo Ray.

4. [Práce s RabbitMQ](rabbitmq.md)  
   Základy RabbitMQ, jeho hlavními pojmy, typy výměníků a praktickými ukázkami kódu pro posílání a příjem zpráv včetně možností škálování a zajištění spolehlivosti.

5. [Komunikace pomocí soketů a HTTP](socket_http.md)  
   Přehled práce s nízkoúrovňovým modulem socket pro síťovou komunikaci a vysokoúrovňovým modulem http pro práci s protokolem HTTP, včetně praktických příkladů na odesílání, přijímání dat a implementaci vlastních serverů. Obsahuje také informace o výhodách, nevýhodách a souvisejících modulech pro rozšířenou funkcionalitu.

---

## Ukázkové kódy

Všechny ukázky uvedené v handoutu si můžete prohlédnout a spustit. Kódy jsou uspořádány ve složce `codes`, která je rozdělena podle kapitol:  

- **Kapitola 2:** [Synchronizační nástroje (`threading`, `multiprocessing` a `asyncio`)](codes/synchronization_tools/)
- **Kapitola 3:** [Nastínění problémů řešitelných pomoc Dask](codes/dask/)
- **Kapitola 4:** [Ukázka funkcí RabbitMQ](codes/rabbitmq_examples/)
- **Kapitola 5:** [Práce se sokety a HTTP](codes/socket_http/)

Úryvky kódu jsou doplněny o komentáře, které vysvětlují jednotlivé kroky a funkce. Čtenáři se doporučuje kód spustit a vyzkoušet si jeho funkčnost na vlastním počítači.

---

## Související prezentace

Kromě textového handoutu je k dispozici také prezentace, která shrnuje klíčové body jednotlivých kapitol. Prezentace je k dispozici ve formátu PDF a je možné ji stáhnout zde: [PDS 2024 - Python Prezentace](https://github.com/Tarasa24/PDS-2024-Python/releases/latest/download/prezentace.pdf)

---

## Další kroky

Začněte prvním tématem: [Úvod do paralelního programování a distribuovaných systémů](uvod_do_paralelizace.md). Pokud máte nějaké dotazy nebo problémy, neváhejte se obrátit na contributory [tohoto repozitáře](https://github.com/Tarasa24/PDS-2024-Python).
