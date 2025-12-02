
async function loadData() {
    const url = "https://your-backend-host/api/results?user_id=123";
    const data = await fetch(url).then(r=>r.json());

    document.getElementById("videos").innerText = "Раунд-видео: " + data.round_videos;
    document.getElementById("photos").innerText = "Фото: " + data.photos;
}
loadData();
