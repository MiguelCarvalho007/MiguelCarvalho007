import json
import matplotlib.pyplot as plt

with open("languages.json") as f:
    data = json.load(f)

# Ordena por mais usado e pega top 5
data = dict(sorted(data.items(), key=lambda x: x[1], reverse=True)[:5])

plt.figure(figsize=(5,2))
plt.bar(data.keys(), data.values(), color="#6272a4")
plt.title("Most Used Languages")
plt.tight_layout()
plt.savefig("lang-stats.svg", format="svg")
