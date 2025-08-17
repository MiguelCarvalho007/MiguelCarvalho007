import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Linguagens e cores
langs = ["Python", "CSS", "HTML", "JavaScript", "SQLite", "Arduino", "MySQL"]
colors = {
    "Python": "#306998",
    "CSS": "#264de4",
    "HTML": "#e34c26",
    "JavaScript": "#f7df1e",
    "SQLite": "#003B57",
    "Arduino": "#00979D",
    "MySQL": "#00758F"
}

# Carrega dados
with open("languages.json") as f:
    data = json.load(f)

# Calcula total e porcentagens
total = sum(data.get(lang, 0) for lang in langs)
percentages = [data.get(lang, 0)/total*100 if total > 0 else 0 for lang in langs]

# --- Cria figura única ---
fig, ax = plt.subplots(figsize=(8, 2), facecolor='none')
ax.axis('off')

# Barra empilhada
start = 0
for i, lang in enumerate(langs):
    ax.barh(1.5, percentages[i], left=start, color=colors[lang], height=0.3)
    start += percentages[i]

# Legenda abaixo
y_pos = 1.0
y_step = 0.3
for i, lang in enumerate(langs):
    circle = Circle((0.2, y_pos - i*y_step), 0.05, color=colors[lang])
    ax.add_patch(circle)
    ax.text(0.3, y_pos - i*y_step, f"{lang} {percentages[i]:.1f}%", va='center', fontsize=10)

# Ajustes da figura
ax.set_xlim(0, 100)
ax.set_ylim(0, 2)
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg", transparent=True)
plt.close()
