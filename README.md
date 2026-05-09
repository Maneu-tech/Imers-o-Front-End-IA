# Como atualizar as fotos da apresentação

Criei dois scripts para você atualizar as fotos automaticamente. Escolha o que preferir:

## Opção 1: Usando Python (recomendado)

1. Abra o **Prompt de Comando** ou **PowerShell**
2. Navegue até a pasta com a apresentação:
   ```
   cd "c:\Users\mateu\Downloads\fotos maezinha"
   ```
3. Execute o script:
   ```
   python update_fotos.py
   ```
   ou (se Python não estiver no PATH):
   ```
   py update_fotos.py
   ```

## Opção 2: Usando Node.js

1. Abra o **Prompt de Comando** ou **PowerShell**
2. Navegue até a pasta:
   ```
   cd "c:\Users\mateu\Downloads\fotos maezinha"
   ```
3. Execute:
   ```
   node update.js
   ```

## Como usar a apresentação

Depois que as fotos forem atualizadas:

1. Abra o arquivo `index.html` no navegador (Chrome, Edge, Firefox, etc.)
2. A apresentação vai funcionar automaticamente com um slideshow das suas fotos
3. Use os botões para navegar:
   - ⏸ Play/Pause
   - ◀ Anterior
   - ▶ Próximo
4. Você também pode clicar nos pontos para ir para uma foto específica

## O que cada arquivo faz

- **index.html** - A apresentação (main file)
- **update_fotos.py** - Script Python para atualizar as imagens
- **update.js** - Script Node.js para atualizar as imagens (alternativa)
- **assets/** - Pasta com assets (você pode adicionar outros itens aqui)

## Problemas?

Se o script não funcionar, tente:
1. Certifique-se de que Python ou Node.js estão instalados
2. Verifique se os caminhos das imagens estão corretos
3. Tente abrir os scripts manualmente

## Localização dos arquivos que serão atualizados

- **Arquivo HTML**: `c:\Users\mateu\Downloads\fotos maezinha\index.html`
- **Imagens originais**: `c:\Users\mateu\AppData\Roaming\Code\User\globalStorage\github.copilot-chat\copilot-cli-images\`

Aproveite a apresentação! 📸💕
