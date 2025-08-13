import requests
import svgwrite
from datetime import datetime

# Configurações
USERNAME = "MiguelCarvalho007"
OUTPUT_PATH = "dist/github-contribution-grid-snake.svg"
COLORS = ["#9be9a8", "#40c463", "#30a14e", "#216e39"]  # Cores do GitHub

def get_contributions():
    url = f"https://api.github.com/users/{USERNAME}/events"
    response = requests.get(url)
    events = response.json()
    
    # Processa eventos (simplificado - na prática use a API de contribuições)
    contributions = {}
    for event in events:
        date = event["created_at"][:10]
        contributions[date] = contributions.get(date, 0) + 1
    
    return contributions

def generate_svg(contributions):
    dwg = svgwrite.Drawing(OUTPUT_PATH, profile="tiny")
    
    # Lógica para gerar a cobrinha baseada nas contribuições
    # (Implementação completa depende do formato desejado)
    for date, count in contributions.items():
        if count > 0:
            color = COLORS[min(count-1, 3)]
            dwg.add(dwg.rect(insert=(x, y), size=(10, 10), fill=color)
    
    dwg.save()

if __name__ == "__main__":
    contrib_data = get_contributions()
    generate_svg(contrib_data)
