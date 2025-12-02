// Telegram WebApp integration + fetching backend stats, rendering, and exporting image
const tg = window.Telegram.WebApp;
tg.expand();

const init = tg.initDataUnsafe || {};
const user = init.user || null;

document.getElementById('greet').innerText = user ? `Привет, ${user.first_name || ''}` : 'Привет!';

async function loadStats(uid){
    try{
        const base = (window.API_BASE_URL || window.location.origin);
        const res = await fetch(base + '/api/results?user_id=' + encodeURIComponent(uid));
        const json = await res.json();
        return json;
    }catch(e){
        console.error(e);
        return null;
    }
}

function render(stats){
    if(!stats) return;
    document.getElementById('rounds').innerText = stats.rounds;
    document.getElementById('messages').innerText = stats.messages;
    document.getElementById('photos').innerText = stats.photos;
}

(async ()=>{
    const uid = user ? user.id : prompt('Введите свой Telegram ID для демонстрации');
    const stats = await loadStats(uid || '0');
    render(stats);
})();

// Save card as PNG using html2canvas (we include small inline)
document.getElementById('saveBtn').addEventListener('click', async ()=>{
    // simple snapshot via SVG foreignObject fallback
    const node = document.querySelector('.card');
    const rect = node.getBoundingClientRect();
    const svg = `<svg xmlns='http://www.w3.org/2000/svg' width='${rect.width}' height='${rect.height}'><foreignObject width='100%' height='100%'>${new XMLSerializer().serializeToString(node)}</foreignObject></svg>`;
    const blob = new Blob([svg], {type: 'image/svg+xml;charset=utf-8'});
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'year_review.png';
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
});
