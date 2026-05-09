#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Limpar base64 do HTML

html_path = r'c:\Users\mateu\Downloads\fotos maezinha\index.html'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Encontrar onde o loadImages() termina
marker = 'loadImages();'
marker_pos = content.find(marker)

if marker_pos != -1:
    # Pegar tudo até depois de loadImages()
    clean_content = content[:marker_pos + len(marker)]
    
    # Encontrar o </script> após a função loadImages
    script_close = content.find('</script>', marker_pos)
    
    if script_close != -1:
        # Adicionar de volta o </script>
        clean_content += '\n</script>'
        
        # Adicionar o HTML e fecha do arquivo
        rest_of_file = content[script_close + len('</script>'):]
        clean_content += rest_of_file
        
        # Salvar o arquivo limpo
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(clean_content)
        
        print("✅ HTML limpo com sucesso!")
        print(f"Removidos {len(content) - len(clean_content)} caracteres")
    else:
        print("❌ Não encontrado </script>")
else:
    print("❌ Não encontrado loadImages()")
