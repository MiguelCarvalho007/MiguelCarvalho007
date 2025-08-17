import json
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Linguagens e cores (mantendo suas linguagens originais)
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

# Carrega dados do JSON
with open("languages.json") as f:
    data = json.load(f)

# Garantir que todas as linguagens estão presentes
data_complete = {lang: data.get(lang, 0) for lang in langs}

# Calcula total e porcentagens (com 2 casas decimais como na imagem)
total = sum(data_complete.values())
percentages = {lang: round(data_complete[lang]/total*100, 2) if total > 0 else 0 for lang in langs}

# --- Cria figura ---
fig, ax = plt.subplots(figsize=(10, 3), facecolor='none')
ax.axis('off')

# --- Barra superior (mais grossa como na imagem) ---
start = 0
for lang in langs:
    ax.barh(2.0, percentages[lang], left=start, color=colors[lang], height=0.4)
    start += percentages[lang]

# --- Legenda com círculos ---
y_start = 1.0  # Posição inicial mais baixa
y_step = 0.45  # Espaçamento entre linhas
circle_radius = 0.15
text_margin = 0.2  # Espaçamento entre círculo e texto
fontsize = 11

# Ordena pelas porcentagens (como na imagem)
sorted_langs = sorted(langs, key=lambda x: -percentages[x])

for i, lang in enumerate(sorted_langs):
    if percentages[lang] == 0:  # Pula linguagens com 0%
        continue
    
    # Círculo colorido com borda branca
    circle = Circle((0.1, y_start - i*y_step), 
                   circle_radius, 
                   color=colors[lang],
                   ec='white',
                   lw=1)
    ax.add_patch(circle)
    
    # Texto formatado exatamente como na imagem (sem espaço após nome)
    ax.text(0.1 + circle_radius + text_margin, 
            y_start - i*y_step, 
            f"{lang}{percentages[lang]:.2f}%", 
            va='center', 
            fontsize=fontsize, 
            weight='bold', 
            color='white')

# Ajustes finais
ax.set_xlim(0, 100)
ax.set_ylim(0, 2.5)
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg", transparent=True)
plt.close()
