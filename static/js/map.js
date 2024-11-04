document.addEventListener("DOMContentLoaded", function() {
    var map = L.map('map').setView([51.1694, 71.4491], 12);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);
});
