const fs = require('fs');
const path = require('path');

const images = [
    'c:\\Users\\mateu\\AppData\\Roaming\\Code\\User\\globalStorage\\github.copilot-chat\\copilot-cli-images\\1778278289655-g62c3521.png',
    'c:\\Users\\mateu\\AppData\\Roaming\\Code\\User\\globalStorage\\github.copilot-chat\\copilot-cli-images\\1778278289656-b5btgucp.png',
    'c:\\Users\\mateu\\AppData\\Roaming\\Code\\User\\globalStorage\\github.copilot-chat\\copilot-cli-images\\1778278289656-e20dj41c.png',
    'c:\\Users\\mateu\\AppData\\Roaming\\Code\\User\\globalStorage\\github.copilot-chat\\copilot-cli-images\\1778278289656-00hg4dtv.png',
    'c:\\Users\\mateu\\AppData\\Roaming\\Code\\User\\globalStorage\\github.copilot-chat\\copilot-cli-images\\1778278289656-vaekesou.png',
];

const htmlPath = 'c:\\Users\\mateu\\Downloads\\fotos maezinha\\index.html';

console.log('🎞️  Atualizando fotos...\n');

let html = fs.readFileSync(htmlPath, 'utf-8');

images.forEach((imgPath, i) => {
    const num = i + 1;
    if (fs.existsSync(imgPath)) {
        const imgData = fs.readFileSync(imgPath);
        const base64 = imgData.toString('base64');
        const replacement = `window.IMG_${num}="data:image/jpeg;base64,${base64}"`;
        
        const regex = new RegExp(`window\\.IMG_${num}="data:image/[^"]*"`);
        html = html.replace(regex, replacement);
        
        console.log(`✓ Imagem ${num} atualizada (${base64.length} caracteres)`);
    } else {
        console.log(`✗ Imagem ${num} não encontrada`);
    }
});

fs.writeFileSync(htmlPath, html, 'utf-8');
console.log('\n✓ Arquivo atualizado com sucesso!');
