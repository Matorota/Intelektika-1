#!/bin/bash

echo "═══════════════════════════════════════════════════════════════════════"
echo "   🚀 GitHub Repository Setup Script"
echo "═══════════════════════════════════════════════════════════════════════"
echo ""

# Spalvos
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Patikrinti ar esame git repozitorijoje
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}❌ Klaida: Nesate git repozitorijoje!${NC}"
    echo "Inicializuojame git..."
    git init
fi

echo -e "${YELLOW}📝 Įveskite savo GitHub username:${NC}"
read -p "Username: " USERNAME

if [ -z "$USERNAME" ]; then
    echo -e "${RED}❌ Username negali būti tuščias!${NC}"
    exit 1
fi

echo ""
echo -e "${YELLOW}📝 Įveskite repository pavadinimą (default: intelektika-1):${NC}"
read -p "Repository: " REPO
REPO=${REPO:-intelektika-1}

echo ""
echo -e "${YELLOW}🔗 Pasirinkite URL tipą:${NC}"
echo "  1) HTTPS (lengviau pradedantiesiems)"
echo "  2) SSH (reikia SSH key)"
read -p "Pasirinkimas (1/2): " URL_TYPE

if [ "$URL_TYPE" == "2" ]; then
    REMOTE_URL="git@github.com:$USERNAME/$REPO.git"
else
    REMOTE_URL="https://github.com/$USERNAME/$REPO.git"
fi

echo ""
echo "═══════════════════════════════════════════════════════════════════════"
echo "  Veiksmai:"
echo "═══════════════════════════════════════════════════════════════════════"
echo "  1. Pridėti remote: $REMOTE_URL"
echo "  2. Commit visi failai"
echo "  3. Push į GitHub"
echo "═══════════════════════════════════════════════════════════════════════"
echo ""

read -p "Tęsti? (y/n): " CONFIRM
if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
    echo "Atšaukta."
    exit 0
fi

echo ""
echo -e "${GREEN}✓ Pridedamas remote...${NC}"
git remote add origin $REMOTE_URL 2>/dev/null || {
    echo -e "${YELLOW}⚠ Remote jau egzistuoja, atnaujiname...${NC}"
    git remote set-url origin $REMOTE_URL
}

echo -e "${GREEN}✓ Pridedami failai...${NC}"
git add .

echo -e "${GREEN}✓ Commit...${NC}"
git commit -m "Neinformuotos paieškos algoritmai: DFS vs BFS palyginimas" 2>/dev/null || {
    echo -e "${YELLOW}⚠ Nieko naujo commit'inti${NC}"
}

echo -e "${GREEN}✓ Nustatoma main šaka...${NC}"
git branch -M main

echo ""
echo -e "${GREEN}🚀 Bandomas push į GitHub...${NC}"
echo ""

git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "═══════════════════════════════════════════════════════════════════════"
    echo -e "${GREEN}✅ SĖKMĖ! Projektas įkeltas į GitHub!${NC}"
    echo "═══════════════════════════════════════════════════════════════════════"
    echo ""
    echo "🌐 Peržiūrėkite: https://github.com/$USERNAME/$REPO"
    echo ""
else
    echo ""
    echo "═══════════════════════════════════════════════════════════════════════"
    echo -e "${RED}❌ KLAIDA!${NC}"
    echo "═══════════════════════════════════════════════════════════════════════"
    echo ""
    echo "Galimos priežastys:"
    echo "  1. Repozitorija dar nesukurta GitHub'e"
    echo "     → Sukurkite: https://github.com/new"
    echo ""
    echo "  2. Nėra prieigos teisių"
    echo "     → Sukurkite Personal Access Token:"
    echo "       https://github.com/settings/tokens"
    echo ""
    echo "  3. SSH key nesustatytas (jei naudojate SSH)"
    echo "     → Setup: ssh-keygen -t ed25519"
    echo ""
    echo "Bandykite rankiniu būdu:"
    echo "  git remote add origin $REMOTE_URL"
    echo "  git push -u origin main"
    echo ""
fi
