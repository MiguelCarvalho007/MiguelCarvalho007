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

# Garantir que todas as linguagens estão presentes
data_complete = {lang: data.get(lang, 0) for lang in langs}

# Calcula total e porcentagens
total = sum(data_complete.values())
percentages = [data_complete[lang]/total*100 if total > 0 else 0 for lang in langs]

# --- Cria figura única ---
fig, ax = plt.subplots(figsize=(8, 2.5), facecolor='none')
ax.axis('off')

# Barra empilhada (mais fina)
start = 0
for i, lang in enumerate(langs):
    ax.barh(1.8, percentages[i], left=start, color=colors[lang], height=0.2)
    start += percentages[i]

# Legenda abaixo
y_start = 1.0
y_step = 0.35
circle_radius = 0.20  # aumenta o tamanho das bolinhas
fontsize = 12
text_margin = 0.20

for i, lang in enumerate(langs):
    # círculo colorido
    circle = Circle((0.1, y_start - i*y_step), circle_radius, color=colors[lang])
    ax.add_patch(circle)
    # texto com margem à esquerda do círculo
    ax.text(0.1 + circle_radius + text_margin, y_start - i*y_step, 
            f"{lang} {percentages[i]:.1f}%", 
            va='center', fontsize=fontsize, weight='bold', color='white')

# Ajustes da figura
ax.set_xlim(0, 100)
ax.set_ylim(0, 2.5)
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg", transparent=True)
plt.close()
