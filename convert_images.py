#!/usr/bin/env python3
import base64
import os

# Caminhos das imagens
images = [
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289655-g62c3521.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-b5btgucp.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-e20dj41c.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-00hg4dtv.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-vaekesou.png',
]

# Converter cada imagem
base64_data = {}
for i, img_path in enumerate(images, 1):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            img_data = base64.b64encode(f.read()).decode('utf-8')
        base64_data[f'IMG_{i}'] = img_data
        print(f'✓ Imagem {i} convertida: {len(img_data)} caracteres')
    else:
        print(f'✗ Não encontrado: {img_path}')

# Gerar linhas de JavaScript para adicionar ao HTML
js_output = []
for key, data in base64_data.items():
    js_output.append(f' window.{key}="data:image/jpeg;base64,{data[:50]}...";  // truncated for display\n')

with open('image_vars.txt', 'w') as f:
    for key in sorted(base64_data.keys()):
        f.write(f'window.{key}="data:image/jpeg;base64,{base64_data[key]}"\n\n')

print("\nSalvo em: image_vars.txt")
