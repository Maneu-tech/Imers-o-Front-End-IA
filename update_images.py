import base64
import os
import re

# Caminhos das imagens
images = [
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289655-g62c3521.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-b5btgucp.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-e20dj41c.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-00hg4dtv.png',
    r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-vaekesou.png',
]

# Converter cada imagem para base64
base64_strings = []
for i, img_path in enumerate(images, 1):
    if os.path.exists(img_path):
        with open(img_path, 'rb') as f:
            img_data = base64.b64encode(f.read()).decode('utf-8')
        base64_strings.append(f'window.IMG_{i}="data:image/jpeg;base64,{img_data}"')
        print(f'✓ Imagem {i} convertida')
    else:
        print(f'✗ Não encontrado: {img_path}')

# Ler o arquivo HTML
html_path = r'c:\Users\mateu\Downloads\fotos maezinha\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Substituir cada window.IMG_X
for i, base64_line in enumerate(base64_strings, 1):
    # Encontrar a linha window.IMG_i com qualquer base64 e substituir
    pattern = f'window\\.IMG_{i}="data:image/[^"]*"'
    content = re.sub(pattern, base64_line, content)

# Salvar o arquivo atualizado
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'\n✓ Arquivo {html_path} atualizado com sucesso!')
