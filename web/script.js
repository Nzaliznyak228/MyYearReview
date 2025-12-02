fetch('../api/user').then(r=>r.json()).then(d=>{
 document.getElementById('count').innerText = 'Videos: ' + d.videos;
});