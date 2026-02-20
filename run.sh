#!/bin/bash

echo "==================================================================="
echo "    Neinformuotos Paieškos Algoritmų Palyginimas"
echo "    DFS vs BFS"
echo "==================================================================="
echo ""
echo "Diegiamos reikalingos bibliotekos..."
echo ""

pip install networkx matplotlib

if [ $? -eq 0 ]; then
    echo ""
    echo "Bibliotekos sėkmingai įdiegtos!"
    echo ""
    echo "Paleidžiama programa..."
    echo ""
    python3 search_algorithms.py
else
    echo ""
    echo "Klaida diegiant bibliotekas. Bandykite rankiniu būdu:"
    echo "  pip install networkx matplotlib"
    echo "arba:"
    echo "  pip3 install networkx matplotlib"
    echo ""
    echo "Tada paleiskite programą:"
    echo "  python search_algorithms.py"
    echo "arba:"
    echo "  python3 search_algorithms.py"
fi
