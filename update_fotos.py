#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para atualizar as fotos no arquivo index.html
Execute este script no terminal com:  python update_fotos.py
"""

import base64
import os
import re

def converter_imagens():
    """Converte as imagens para base64 e atualiza o HTML"""
    
    # Caminhos das imagens que você enviou
    images = [
        r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289655-g62c3521.png',
        r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-b5btgucp.png',
        r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-e20dj41c.png',
        r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-00hg4dtv.png',
        r'c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\1778278289656-vaekesou.png',
    ]
    
    html_path = r'c:\Users\mateu\Downloads\fotos maezinha\index.html'
    
    print("=" * 60)
    print("🎞️  Atualizando fotos da apresentação...")
    print("=" * 60)
    
    # Converter cada imagem para base64
    base64_strings = {}
    for i, img_path in enumerate(images, 1):
        if os.path.exists(img_path):
            try:
                with open(img_path, 'rb') as f:
                    img_data = base64.b64encode(f.read()).decode('utf-8')
                base64_strings[i] = img_data
                print(f"✓ Imagem {i} convertida ({len(img_data)} caracteres)")
            except Exception as e:
                print(f"✗ Erro ao processar imagem {i}: {e}")
        else:
            print(f"✗ Imagem {i} não encontrada: {img_path}")
    
    if not base64_strings:
        print("\n❌ Nenhuma imagem foi processada com sucesso!")
        return False
    
    # Ler o arquivo HTML
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"\n✓ Arquivo HTML lido ({len(content)} caracteres)")
    except Exception as e:
        print(f"\n✗ Erro ao ler HTML: {e}")
        return False
    
    # Substituir cada window.IMG_X
    for i, base64_data in base64_strings.items():
        new_line = f'window.IMG_{i}="data:image/jpeg;base64,{base64_data}"'
        # Encontrar a linha window.IMG_i com qualquer base64 e substituir
        pattern = f'window\\.IMG_{i}="data:image/[^"]*"'
        old_content = content
        content = re.sub(pattern, new_line, content)
        if content != old_content:
            print(f"✓ window.IMG_{i} atualizado")
        else:
            print(f"⚠️  window.IMG_{i} não encontrado (pode ser primeira execução)")
    
    # Salvar o arquivo atualizado
    try:
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"\n✓ Arquivo HTML atualizado com sucesso!")
        print(f"  Caminho: {html_path}")
        print("\n🎉 Suas fotos foram adicionadas à apresentação!")
        print("   Abra o arquivo index.html no navegador para ver o resultado.")
        return True
    except Exception as e:
        print(f"\n✗ Erro ao salvar HTML: {e}")
        return False

if __name__ == '__main__':
    sucesso = converter_imagens()
    exit(0 if sucesso else 1)
