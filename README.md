# Neinformuotos Paieškos Algoritmų Palyginimas

## Aprašymas

Ši programa realizuoja ir lygina du neinformuotos paieškos algoritmus:

- **DFS (Depth First Search)** - gilumo paieška
- **BFS (Breadth First Search)** - platumo paieška

## Funkcionalumas

### Realizuoti algoritmai

1. **DFS (Depth First Search)** - naudoja dėklą (stack), eina į gylį kiek įmanoma
2. **BFS (Breadth First Search)** - naudoja eilę (queue), tikrina visus kaimynus prieš einant į kitą lygį

### Duomenų rinkiniai

Programoje naudojami 3 skirtingi duomenų rinkiniai:

1. **Atsitiktinis grafas** - 25 viršūnės su atsitiktinėmis briaunomis
2. **Tinklelio grafas** - 5x5 tinklelis (25 viršūnės)
3. **Medžio struktūra** - 30 viršūnių medis su šakojimosi faktoriumi 3

Visi duomenų rinkiniai turi **20 ar daugiau viršūnių**.

### Palyginamasis įvertinimas

Programa vertina:

- **Kelio ilgis** - kiek viršūnių nuo pradžios iki tikslo
- **Aplankytų viršūnių skaičius** - kiek viršūnių algoritmas aplankė ieškodamas
- **Vykdymo laikas** - algoritmo greitaveika milisekundėmis
- **Vizualizacija** - grafų atvaizdavimas su pažymėtu keliu

## Diegimas

### 1. Bibliotekų įdiegimas

```bash
pip install -r requirements.txt
```

arba rankiniu būdu:

```bash
pip install networkx matplotlib
```

### 2. Programos paleidimas

```bash
python search_algorithms.py
```

## Rezultatai

Programa:

1. Generuoja 3 skirtingus grafus
2. Kiekvienam grafui:
   - Atlieka DFS paiešką
   - Atlieka BFS paiešką
   - Palygina rezultatus
   - Išsaugo vizualizacijas PNG formatu
3. Pateikia bendrą išvadą apie abu algoritmus

## Vizualizacija

Kiekviename vizualizacijos faile:

- **Žalia viršūnė** - pradžios taškas
- **Raudona viršūnė** - tikslo taškas
- **Geltona spalva** - aplankytos viršūnės
- **Raudona linija** - rastas kelias

## Išvados

### BFS (Breadth First Search)

**Privalumai:**

- Visada randa trumpiausią kelią nesvertiniuose grafuose
- Gerai tinka, kai sprendimas yra arti pradžios

**Trūkumai:**

- Naudoja daugiau atminties
- Gali aplankyti daugiau viršūnių nei reikia

### DFS (Depth First Search)

**Privalumai:**

- Naudoja mažiau atminties
- Greičiau randa sprendimą giliuose grafuose

**Trūkumai:**

- Negarantuoja trumpiausio kelio
- Gali įstrigti giliose šakose

## Sudėtingumas

| Algoritmas | Laiko sudėtingumas | Erdvės sudėtingumas |
| ---------- | ------------------ | ------------------- |
| BFS        | O(V + E)           | O(V)                |
| DFS        | O(V + E)           | O(h)                |

kur:

- V - viršūnių skaičius
- E - briaunų skaičius
- h - maksimalus medžio gylis

## Autorius

Programa sukurta kaip neinformuotos paieškos algoritmų tyrimo projektas.
