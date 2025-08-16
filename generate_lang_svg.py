import json
import matplotlib.pyplot as plt

# Linguagens e cores
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

# Carrega dados do JSON
with open("languages.json") as f:
    data = json.load(f)

# Calcula total
total = sum(data.get(lang, 0) for lang in langs)

# Calcula porcentagens
percentages = [data.get(lang, 0)/total*100 if total > 0 else 0 for lang in langs]

# Cria figura
fig, ax = plt.subplots(figsize=(6, 0.5))  # barra fina

# Barra empilhada horizontal
start = 0
for i, lang in enumerate(langs):
    ax.barh(0, percentages[i], left=start, color=colors[lang], height=1.0)
    start += percentages[i]

# Remove eixos
ax.axis('off')

# Ajusta limites para não cortar
ax.set_xlim(0, 100)
ax.set_ylim(-0.5, 1.5)

plt.tight_layout()

# Salva o gráfico da barra
plt.savefig("lang-bar.svg", format="svg")
plt.close()

# --- Agora cria a legenda separada ---
from matplotlib.patches import Circle
from matplotlib.lines import Line2D

fig2, ax2 = plt.subplots(figsize=(6, 1.5))
ax2.axis('off')

y_pos = 1.0
for i, lang in enumerate(langs):
    # círculo colorido
    circle = Circle((0, y_pos), 0.1, color=colors[lang])
    ax2.add_patch(circle)
    # texto com nome e porcentagem
    ax2.text(0.2, y_pos, f"{lang} {percentages[i]:.1f}%", va='center', fontsize=10)
    y_pos -= 0.3

ax2.set_xlim(0, 6)
ax2.set_ylim(0, 1.5)
plt.tight_layout()
plt.savefig("lang-legend.svg", format="svg")
plt.close()
