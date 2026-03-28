# 🎬 Projeto Netflix - Seletor de Perfis

## 📋 Descrição Geral

Este é um projeto front-end que reproduz a interface de seleção de perfis do Netflix. Inclui responsividade completa, modo escuro/claro, animações interativas e acessibilidade.

---

## 📁 Estrutura do Projeto

```
Projeto Netflix/
├── index.html       # Arquivo HTML principal
├── style.css        # Estilos CSS (responsividade + temas)
├── script.js        # JavaScript (gerenciador de tema)
├── assets/          # Pasta com imagens dos perfis
│   ├── foto maneu.jfif
│   ├── foto junio].jfif
│   ├── foto eduarda.jfif
│   ├── foto carol.jfif
│   └── foto josi.jfif
└── README.md        # Este arquivo
```

---

## 🎨 Funcionalidades

### 1. **Responsividade Completa**
- 📱 **Mobile** (até 480px): Imagens pequenas, layout flexível
- 📱 **Tablet** (481-768px): Tamanho intermediário
- 💻 **Desktop** (769px+): Layout completo
- 🖥️ **Extra Grande** (1920px+): Imagens ampliadas

### 2. **Dark Mode / Light Mode**
- 🌙 Alterna entre modo escuro (padrão) e claro
- 💾 Salva preferência no `localStorage`
- ✨ Transições suaves de cores

### 3. **Animações Interativas**
- ✨ Hover effects nos perfis
- 🎨 Cores únicas para cada perfil
- 📤 Movimento flutuante ao passar o mouse

### 4. **Acessibilidade**
- ♿ Suporte a navegação por teclado
- 🔊 Labels descritivas para leitores de tela
- 🚫 Respeita preferência de movimento reduzido
- 🌗 Suporta preferência de tema do sistema

---

## 🚀 Como Usar

### Abrir o Projeto
1. Abra `index.html` em um navegador moderno
2. Use o botão 🌙/☀️ no canto superior direito para alternar tema
3. Passe o mouse sobre um perfil para ver a animação

### Compatibilidade
- ✅ Chrome/Edge (versão 90+)
- ✅ Firefox (versão 88+)
- ✅ Safari (versão 14+)
- ✅ Qualquer navegador moderno com ES6

---

## 📝 Explicação dos Arquivos

### **index.html** - Estrutura Semântica
```html
<!-- Botão para alternar tema -->
<button id="theme-toggle" aria-label="...">
    <span id="theme-icon">🌙</span>
</button>

<!-- Lista de perfis -->
<section aria-label="Perfis disponíveis">
    <ul class="profiles">
        <li class="profile">
            <ol>
                <li>
                    <figure>
                        <img src="..." alt="...">
                        <figcaption>Nome do Perfil</figcaption>
                    </figure>
                </li>
            </ol>
        </li>
    </ul>
</section>
```

**Elementos Principais:**
- `button#theme-toggle`: Botão circular com ícone de lua/sol
- `ul.profiles`: Lista não-ordenada de perfis
- `li.profile`: Cada perfil é um item da lista
- `ol`: Lista ordenada interna (estrutura semântica)
- `figure`: Agrupa imagem + legenda
- `figcaption`: Nome do perfil

---

### **style.css** - Estilos e Layout

#### **Estrutura de Cores**
```css
/* Dark Mode (padrão) */
body { background: #141414; color: #fff; }

/* Light Mode (data-theme="light") */
[data-theme="light"] body { background: #f5f5f5; color: #141414; }
```

#### **Cores por Perfil**
Cada perfil tem uma cor única:
- 1º Maneu: Vermelho Netflix (#e50914)
- 2º Junio: Azul (#0071eb)
- 3º Eduarda: Rosa (#ff07b5)
- 4º Carol: Púrpura (#8700f5)
- 5º Josiani: Púrpura Escuro (#9b59b6)

#### **Breakpoints Responsivos**
| Dispositivo | Largura | Tamanho Imagem |
|-------------|---------|----------------|
| Mobile | até 480px | 120×130px |
| Tablet | 481-768px | 180×200px |
| Desktop | 769px+ | 270×290px |
| Extra Grande | 1920px+ | 300×320px |

#### **Media Queries Especiais**
```css
/* Modo paisagem com altura limitada */
@media (orientation: landscape) and (max-height: 500px)

/* Preferência de tema do sistema */
@media (prefers-color-scheme: dark)

/* Reduce motion para acessibilidade */
@media (prefers-reduced-motion: reduce)
```

---

### **script.js** - Gerenciador de Tema

#### **Classe: ThemeManager**

```javascript
class ThemeManager {
    // Propriedades
    this.themeToggle    // Botão de alternância
    this.themeIcon      // Ícone (lua/sol)
    this.currentTheme   // Tema atual ('dark' ou 'light')

    // Métodos
    init()              // Inicializa listeners
    toggleTheme()       // Alterna tema
    applyTheme(theme)   // Aplica tema visual
    saveTheme()         // Salva no localStorage
}
```

#### **Fluxo de Funcionamento**

1. **Ao carregar a página:**
   ```
   Construtor → Recupera tema salvo (ou 'dark')
             → Chamado init()
             → Aplica tema visual
             → Adiciona event listener ao botão
   ```

2. **Ao clicar o botão:**
   ```
   Click → toggleTheme()
        → Alterna tema (dark ↔ light)
        → applyTheme()
        → Muda atributo data-theme no HTML
        → Muda ícone (🌙 ↔ ☀️)
        → saveTheme() → localStorage
   ```

#### **localStorage**
```javascript
// Armazena a preferência do usuário
localStorage.setItem('theme', 'light');
localStorage.getItem('theme'); // Recupera

// Persiste entre visitas ao site
```

---

## 🎨 Customização

### Mudar Cores dos Perfis
No arquivo **style.css**, procure por:
```css
li.profile:nth-of-type(1):hover img {
    border-color: #e50914; /* Mude esta cor */
}
```

### Mudar Tamanho das Imagens
```css
/* Desktop */
img {
    width: 270px;
    height: 290px;
}

/* Mobile - altere em @media (max-width: 480px) */
```

### Mudar Velocidade de Animações
```css
transition: transform 0.2s; /* Aumente para mais lento */
```

---

## ♿ Acessibilidade

### Atributos ARIA
```html
<!-- aria-label no botão informatico ao leitor de tela -->
<button id="theme-toggle" aria-label="Alternar para modo claro">

<!-- aria-label na seção -->
<section aria-label="Perfis disponíveis">
```

### Suporte a Taeclado
- ✅ Tab: Navega até o botão
- ✅ Enter/Espaço: Clica o botão
- ✅ Contorno visível no focus

### Reducedmotion
```css
@media (prefers-reduced-motion: reduce) {
    /* Remove animações para usuários sensíveis */
}
```

---

## 🔍 Estrutura Semântica HTML

```
main (container principal, flexbox)
├── button#theme-toggle (botão de tema)
├── h1 (título "Quem está assistindo?")
└── section[aria-label="Perfis disponíveis"]
    └── ul.profiles (lista de perfis)
        └── li.profile (cada perfil)
            └── ol (lista ordenada semântica)
                └── li
                    └── figure (imagem + legenda)
                        ├── img
                        └── figcaption
```

**Por que essa estrutura?**
- `<ul>` + `<li>`: Indica uma lista de perfis
- `<ol>` interno: Estrutura semântica adicional
- `<figure>` + `<figcaption>`: Agrupa imagem com descrição
- `<section>` com `aria-label`: Identifica seção semanticamente

---

## 📊 CSS - Ordem de Especificidade

1. **Estilos Base** (body, main, h1, etc.)
2. **Layout dos Perfis** (ul, li, figure)
3. **Imagens** (img: tamanho, borda, transições)
4. **Efeitos de Hover** (mudança de cor por perfil)
5. **Responsividade** (media queries mobile → desktop)
6. **Dark/Light Mode** ([data-theme="light"])
7. **Acessibilidade** (prefers-reduced-motion, etc.)

---

## 🐛 Troubleshooting

### Tema não salva
- Verificar se localStorage está ativado no navegador
- Limpar cookies/cache do site

### Imagens não carregar
- Verificar se o caminho em `src="/assets/..."` está correto
- Verificar se os nomes dos arquivos têm a extensão correta

### Animações não funcionam
- Verificar se JavaScript está ativado
- Abrir console (F12) para erros

---

## 📚 Recursos Utilizados

- **HTML5 semântico** para acessibilidade
- **CSS3 Flexbox** para layout responsivo
- **JavaScript ES6** para interatividade
- **localStorage** para persistência de dados
- **Media Queries** para responsividade
- **ARIA Labels** para acessibilidade

---

## 📝 Notas Importantes

1. **Responsividade**: Testada em dispositivos reais e emuladores
2. **Acessibilidade**: Segue recomendações WCAG 2.1
3. **Performance**: Sem dependências externas (HTML/CSS/JS puro)
4. **Compatibilidade**: Funciona em navegadores modernos

---

## 🎓 Conceitos Implementados

- ✅ Flexbox Layout
- ✅ Media Queries Responsivas
- ✅ DOM Manipulation (JavaScript)
- ✅ localStorage API
- ✅ CSS Custom Properties (valores relativo)
- ✅ Efeitos CSS (transform, filter, box-shadow)
- ✅ Pseudo-classes (:hover, :nth-of-type)
- ✅ Estrutura Semântica HTML
- ✅ Acessibilidade Web
- ✅ UX/UI (User Experience)

---

## 👤 Autor
Projeto desenvolvido como prática de HTML, CSS e JavaScript.

---

## 📄 Licença
Código livre para uso educacional e pessoal.