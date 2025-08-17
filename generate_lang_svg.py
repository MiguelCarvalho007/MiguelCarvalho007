import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Linguagens na ordem especificada
langs = ["Python", "HTML", "CSS", "JavaScript", "Arduino", "SQLite", "MySQL"]
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
fig, ax = plt.subplots(figsize=(10, 4), facecolor='none')
ax.axis('off')

# --- Barra no topo ---
start = 0
for i, lang in enumerate(langs):
    ax.barh(3.0, percentages[i], left=start, color=colors[lang], height=0.4)
    start += percentages[i]

# --- Legenda abaixo da barra ---
y_start = 2.0
y_step = 0.5
circle_radius = 0.18
text_margin = 0.15
fontsize = 12  # Aumentei o tamanho da fonte

for i, lang in enumerate(langs):
    # Círculo colorido
    circle = Circle((0.1, y_start - i*y_step), circle_radius, color=colors[lang])
    ax.add_patch(circle)
    
    # Texto com porcentagem (formato com 2 casas decimais)
    ax.text(0.1 + circle_radius + text_margin, y_start - i*y_step, 
            f"{lang} {percentages[i]:.2f}%", 
            va='center', fontsize=fontsize, weight='bold', color='white')

# Ajustes finais
ax.set_xlim(0, 100)
ax.set_ylim(0, 3.5)
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg", transparent=True)
plt.close()
