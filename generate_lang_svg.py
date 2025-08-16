import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Linguagens e cores (cores corrigidas)
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

# Carrega dados do JSON
with open("languages.json") as f:
    data = json.load(f)

# Calcula total
total = sum(data.get(lang, 0) for lang in langs)

# Calcula porcentagens
percentages = [data.get(lang, 0)/total*100 if total > 0 else 0 for lang in langs]

# --- Barra de cores ---
fig, ax = plt.subplots(figsize=(6, 0.5), facecolor='none')  # fundo transparente

start = 0
for i, lang in enumerate(langs):
    ax.barh(0, percentages[i], left=start, color=colors[lang], height=1.0)
    start += percentages[i]

ax.axis('off')
ax.set_xlim(0, 100)
ax.set_ylim(-0.5, 1.5)
plt.tight_layout()
plt.savefig("lang-bar.svg", format="svg", transparent=True)
plt.close()

# --- Legenda ---
fig2, ax2 = plt.subplots(figsize=(6, 2), facecolor='none')  # fundo transparente
ax2.axis('off')

y_start = 1.5  # aumenta o espaçamento
y_step = 0.3
for i, lang in enumerate(langs):
    # círculo colorido
    circle = Circle((0, y_start - i*y_step), 0.08, color=colors[lang])
    ax2.add_patch(circle)
    # texto com nome e porcentagem
    ax2.text(0.2, y_start - i*y_step, f"{lang} {percentages[i]:.1f}%", va='center', fontsize=10)

ax2.set_xlim(0, 6)
ax2.set_ylim(0, 2)
plt.tight_layout()
plt.savefig("lang-legend.svg", format="svg", transparent=True)
plt.close()
