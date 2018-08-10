window.onload = setupRefresh();
        
function setupRefresh(){
    setInterval("refreshBlock();", 1000);
}
function refreshBlock(){
    var d = new Date();
    document.getElementById('timeS').innerHTML = d.toLocaleTimeString();
}