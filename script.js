alert('Bem-vindo ao meu portfólio! Explore meus projetos e habilidades.');





/**
 * GERENCIADOR DE TEMA (Dark/Light Mode)
 * 
 * Esta classe é responsável por:
 * - Alternar entre modo escuro e claro
 * - Salvar a preferência do usuário no localStorage
 * - Atualizar a interface visual (ícone e cores)
 * - Gerenciar o atributo data-theme no HTML
 */

/**
 * GERENCIADOR DE PERFIS
 * 
 * Esta classe é responsável por:
 * - Capturar o clique nos perfis
 * - Armazenar o nome e imagem do perfil ativo no localStorage
 */
class ProfileManager {
    constructor() {
        this.profileLinks = document.querySelectorAll('li.profile a');
        this.init();
    }

    init() {
        this.profileLinks.forEach(link => {
            link.addEventListener('click', () => this.handleProfileClick(link));
        });
    }

    handleProfileClick(link) {
        const figcaption = link.querySelector('figcaption');
        const name = figcaption ? figcaption.textContent.trim() : '';
        const img = link.querySelector('img');
        const imageSrc = img ? img.src : '';

        localStorage.setItem('perfilAtivoNome', name);
        localStorage.setItem('perfilAtivoImagem', imageSrc);
    }
}

class ThemeManager {
    /**
     * Construtor da classe ThemeManager
     * Inicializa os elementos DOM e recupera o tema salvo
     */
    constructor() {
        // Obtém o botão de alternância de tema do DOM
        this.themeToggle = document.getElementById('theme-toggle');
        
        // Obtém o ícone que muda entre lua e sol
        this.themeIcon = document.getElementById('theme-icon');
        
        // Recupera o tema salvo no localStorage ou defaulta para 'dark'
        this.currentTheme = localStorage.getItem('theme') || 'dark';

        // Chama método de inicialização
        this.init();
    }

    /**
     * Método de inicialização
     * - Aplica o tema salvo ao carregar a página
     * - Adiciona event listener ao botão de alternância
     */
    init() {
        // Aplica o tema que estava salvo ou o padrão (dark)
        this.applyTheme(this.currentTheme);

        // Adiciona evento de clique ao botão para alternar tema
        this.themeToggle.addEventListener('click', () => this.toggleTheme());
    }

    /**
     * Método que alterna entre modo escuro e claro
     * - Muda o tema para o oposto do atual
     * - Aplica o novo tema
     * - Salva a preferência
     */
    toggleTheme() {
        // Alterna entre 'dark' e 'light'
        this.currentTheme = this.currentTheme === 'dark' ? 'light' : 'dark';
        
        // Aplica o novo tema à página
        this.applyTheme(this.currentTheme);
        
        // Salva a preferência do usuário
        this.saveTheme();
    }

    /**
     * Método que aplica o tema visual à página
     * 
     * @param {string} theme - O tema a ser aplicado ('dark' ou 'light')
     */
    applyTheme(theme) {
        // Define o atributo data-theme no elemento raiz (html)
        // Isso ativa as regras CSS correspondentes ao tema
        document.documentElement.setAttribute('data-theme', theme);

        // Muda o ícone: lua para dark mode, sol para light mode
        this.themeIcon.textContent = theme === 'dark' ? '🌙' : '☀️';

        // Atualiza o aria-label do botão para melhor acessibilidade
        // Informa ao leitor de tela qual será a ação do botão ao clicar
        this.themeToggle.setAttribute('aria-label',
            theme === 'dark' ? 'Alternar para modo claro' : 'Alternar para modo escuro'
        );
    }

    /**
     * Método que salva a preferência de tema no localStorage
     * Permite que a preferência persista entre visitas
     */
    saveTheme() {
        // Armazena o tema atual no localStorage do navegador
        localStorage.setItem('theme', this.currentTheme);
    }
}

/**
 * INICIALIZAÇÃO DO APLICATIVO
 * 
 * Aguarda o carregamento completo do DOM antes de inicializar
 * o gerenciador de tema. Isso garante que todos os elementos
 * HTML estejam disponíveis para manipulação pelo JavaScript.
 */
document.addEventListener('DOMContentLoaded', () => {
    // Cria uma nova instância do ThemeManager
    // Seu construtor automaticamente inicializa toda a funcionalidade
    new ThemeManager();

    // Cria uma nova instância do ProfileManager para gravar perfil ativo no localStorage
    new ProfileManager();
});