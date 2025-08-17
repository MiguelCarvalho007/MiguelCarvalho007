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

# Carrega dados (substitua pelos valores da imagem se necessário)
data = {
    "Python": 22.60,
    "HTML": 20.18,
    "CSS": 27.82,
    "JavaScript": 29.40,
    "Arduino": 0.00,
    "SQLite": 0.00,
    "MySQL": 0.00
}

# --- Cria figura única ---
fig, ax = plt.subplots(figsize=(10, 4), facecolor='none')
ax.axis('off')

# --- Barra no topo ---
start = 0
for lang in langs:
    ax.barh(3.0, data[lang], left=start, color=colors[lang], height=0.4)
    start += data[lang]

# --- Legenda com círculos ---
y_start = 1.8  # Posição inicial mais baixa
y_step = 0.5   # Espaçamento entre linhas
circle_radius = 0.2
text_margin = 0.3  # Aumentei o espaçamento entre círculo e texto
fontsize = 12

for i, lang in enumerate(langs):
    # Círculo colorido - AUMENTEI O RAIO E ADICIONEI CONTORNO BRANCO
    circle = Circle((0.1 + circle_radius, y_start - i*y_step), 
                  circle_radius, 
                  color=colors[lang],
                  ec='white',  # Borda branca
                  lw=1.5)      # Espessura da borda
    ax.add_patch(circle)
    
    # Texto com porcentagem - AUMENTEI O ESPAÇAMENTO (text_margin)
    ax.text(0.1 + 2*circle_radius + text_margin, 
            y_start - i*y_step, 
            f"{lang} {data[lang]:.2f}%", 
            va='center', 
            fontsize=fontsize, 
            weight='bold', 
            color='white')

# Ajustes finais para garantir visibilidade
ax.set_xlim(0, 100)
ax.set_ylim(0, 3.5)
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg", transparent=True)
plt.close()
