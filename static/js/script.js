var map = L.map('map').setView([50.2649, 19.0238], 12);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([50.2649, 19.0238]).addTo(map)
  .bindPopup('Hello world!<br> I have attended this conference.')
  .openPopup();
