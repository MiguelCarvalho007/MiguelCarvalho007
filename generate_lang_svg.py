import json
import matplotlib.pyplot as plt

# Linguagens que você quer mostrar e suas cores
langs = ["Python", "CSS", "HTML", "JavaScript", "SQLite", "Arduino", "MySQL"]
colors = {
    "Python": "#306998",
    "CSS": "#264de4",
    "HTML": "#e34c26",
    "JavaScript": "#f7df1e",
    "SQLite": "#003b57",
    "Arduino": "#00979D",
    "MySQL": "#00758f"
}

# Abre o JSON gerado pelo workflow
with open("languages.json") as f:
    data = json.load(f)

# Calcula o total
total = sum(data.get(lang, 0) for lang in langs)

# Calcula porcentagens
percentages = [data.get(lang, 0)/total*100 if total > 0 else 0 for lang in langs]

# Cria barra empilhada (stacked bar)
fig, ax = plt.subplots(figsize=(6, 1.5))

start = 0
for i, lang in enumerate(langs):
    ax.barh(0, percentages[i], left=start, color=colors[lang])
    start += percentages[i]

# Remove eixos desnecessários
ax.axis('off')

# Adiciona os nomes e porcentagens acima da barra
start = 0
for i, lang in enumerate(langs):
    if percentages[i] > 0:
        ax.text(start + percentages[i]/2, 0, f"{lang} {percentages[i]:.1f}%", 
                ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    start += percentages[i]

plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg")
