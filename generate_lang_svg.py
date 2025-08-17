import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Linguagens e cores (mantidas as mesmas)
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
fig, ax = plt.subplots(figsize=(10, 3), facecolor='none')
ax.axis('off')

# Barra empilhada (ajustada para ficar mais grossa como na imagem)
start = 0
for i, lang in enumerate(langs):
    ax.barh(1.8, percentages[i], left=start, color=colors[lang], height=0.5)
    start += percentages[i]

# Legenda (ajustada para ficar como na imagem)
y_start = 0.5
y_step = 0.7
circle_radius = 0.15
text_margin = 0.1
fontsize = 10

# Ordena as linguagens por porcentagem (como aparece na imagem)
sorted_indices = sorted(range(len(percentages)), key=lambda i: -percentages[i])
sorted_langs = [langs[i] for i in sorted_indices]
sorted_percentages = [percentages[i] for i in sorted_indices]

for i, (lang, perc) in enumerate(zip(sorted_langs, sorted_percentages)):
    # círculo colorido
    circle = Circle((0.1, y_start + i*y_step), circle_radius, color=colors[lang])
    ax.add_patch(circle)
    # texto com porcentagem
    ax.text(0.1 + circle_radius + text_margin, y_start + i*y_step, 
            f"{lang} {perc:.2f}%", 
            va='center', fontsize=fontsize, weight='bold', color='white')

# Ajustes finais para corresponder à imagem
ax.set_xlim(0, 100)
ax.set_ylim(0, 3.5)
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg", transparent=True)
plt.close()
