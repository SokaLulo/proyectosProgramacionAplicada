// public/script.js
// Pide /readings, parsea CSV y dibuja gráfica con Chart.js

const outputEl = document.getElementById("output");
const lastEl = document.getElementById("last");
const intervalSelect = document.getElementById("intervalSelect");
const maxPointsSelect = document.getElementById("maxPointsSelect");
const btnPause = document.getElementById("btnPause");

let pollingMs = parseInt(intervalSelect.value, 10);
let maxPoints = parseInt(maxPointsSelect.value, 10);
let paused = false;
let timerId = null;
let firstTimestampMs = null;

// Chart.js setup
const ctx = document.getElementById("distChart").getContext("2d");
const chartData = {
  labels: [], // etiquetas (segundos relativos)
  datasets: [{
    label: "Distancia (cm)",
    data: [], // valores numéricos o null
    spanGaps: false,
    tension: 0.2,
    pointRadius: 2,
    borderWidth: 2,
    fill: false
  }]
};
const config = {
  type: "line",
  data: chartData,
  options: {
    animation: false,
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      x: {
        title: { display: true, text: "Tiempo (s desde inicio de sesión del ESP)" }
      },
      y: {
        title: { display: true, text: "Distancia (cm)" },
        beginAtZero: true
      }
    },
    plugins: {
      legend: { display: true }
    }
  }
};
const distChart = new Chart(ctx, config);

// Función para parsear CSV pasado como texto
function parseCSV(text) {
  // Devuelve array de objetos: {timestamp_ms, duration_us, distance_cm}
  const lines = text.split("\n").map(l => l.trim()).filter(Boolean);
  if (lines.length <= 1) return []; // solo header o vacío
  const res = [];
  for (let i = 1; i < lines.length; i++) {
    const cols = lines[i].split(",").map(s => s.trim());
    // Acepta filas con 2 o 3 columnas
    const ts = cols[0] === "" ? null : Number(cols[0]);
    const dur = (cols[1] === "" || typeof cols[1] === "undefined") ? null : Number(cols[1]);
    const dist = (cols[2] === "" || typeof cols[2] === "undefined") ? null : Number(cols[2]);
    res.push({ timestamp_ms: ts, duration_us: dur, distance_cm: dist });
  }
  return res;
}

// Actualiza la gráfica con un array de lecturas (obj)
function updateChart(readings) {
  if (!readings || readings.length === 0) {
    lastEl.textContent = "Aun no hay lecturas.";
    return;
  }

  // Inicializar firstTimestampMs en la primera lectura válida
  if (firstTimestampMs === null) {
    const first = readings.find(r => r.timestamp_ms !== null);
    firstTimestampMs = first ? first.timestamp_ms : readings[0].timestamp_ms || 0;
  }

  // Convertir a arrays de etiquetas y datos (limitar a maxPoints)
  const series = [];
  const labels = [];
  for (let i = 0; i < readings.length; i++) {
    const r = readings[i];
    if (r.timestamp_ms === null) continue; // ignorar sin timestamp
    const sec = (r.timestamp_ms - firstTimestampMs) / 1000;
    labels.push(sec.toFixed(2));
    // si distance_cm es null -> push null para que Chart.js deje hueco
    series.push(r.distance_cm === null ? null : Number(r.distance_cm));
  }

  // Mantener solo últimas maxPoints
  const startIndex = Math.max(0, labels.length - maxPoints);
  const labelsSlice = labels.slice(startIndex);
  const seriesSlice = series.slice(startIndex);

  // Reemplazar datos del chart
  chartData.labels = labelsSlice;
  chartData.datasets[0].data = seriesSlice;
  distChart.update();

  // Mostrar última lectura en texto
  const lastValidIndex = seriesSlice.length - 1;
  const lastDist = seriesSlice[lastValidIndex];
  const lastTs = labelsSlice[lastValidIndex];
  lastEl.textContent = lastDist === null
    ? `Última: timeout/ninguna lectura (ts ${lastTs}s)`
    : `Última: ${lastDist} cm (ts ${lastTs}s)`;
}

// Función que pide /readings y actualiza todo
async function fetchAndUpdate() {
  if (paused) return;
  try {
    const resp = await fetch("/readings", { cache: "no-store" });
    if (!resp.ok) throw new Error("HTTP " + resp.status);
    const text = await resp.text();
    outputEl.textContent = text;
    const readings = parseCSV(text);
    updateChart(readings);
  } catch (err) {
    outputEl.textContent = "Error cargando lecturas:\n" + err;
    lastEl.textContent = "Error cargando lecturas";
    console.error(err);
  }
}

// Control de polling
function startPolling() {
  stopPolling();
  timerId = setInterval(fetchAndUpdate, pollingMs);
  fetchAndUpdate(); // primera ejecución inmediata
}
function stopPolling() {
  if (timerId !== null) {
    clearInterval(timerId);
    timerId = null;
  }
}

// UI events
intervalSelect.addEventListener("change", () => {
  pollingMs = parseInt(intervalSelect.value, 10);
  startPolling();
});
maxPointsSelect.addEventListener("change", () => {
  maxPoints = parseInt(maxPointsSelect.value, 10);
  // refrescar con nuevos límites inmediatamente
  fetchAndUpdate();
});
btnPause.addEventListener("click", () => {
  paused = !paused;
  btnPause.textContent = paused ? "Reanudar" : "Pausar";
  if (!paused) fetchAndUpdate();
});

// iniciar
startPolling();
