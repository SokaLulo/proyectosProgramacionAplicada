// server.js
const express = require("express");
const bodyParser = require("body-parser");
const fs = require("fs");
const path = require("path");

const app = express();
const PORT = 3000;
const CSV_FILE = path.join(__dirname, "distancias.csv");
const PUBLIC_DIR = path.join(__dirname, "public");

app.use(bodyParser.json());
app.use(express.static(PUBLIC_DIR));

// Crear CSV con cabecera si no existe
if (!fs.existsSync(CSV_FILE)) {
  fs.writeFileSync(CSV_FILE, "timestamp_ms,duration_us,distance_cm\n", "utf8");
  console.log("Archivo CSV creado:", CSV_FILE);
}

// Recibe POST JSON del ESP32
app.post("/data", (req, res) => {
  const data = req.body || {};
  console.log("Datos recibidos:", data);

  const ts = typeof data.timestamp_ms !== "undefined" ? data.timestamp_ms : "";
  const dur = typeof data.duration_us !== "undefined" ? data.duration_us : "";
  const dist = typeof data.distance_cm !== "undefined" ? data.distance_cm : "";

  const line = `${ts},${dur},${dist}\n`;
  try {
    fs.appendFileSync(CSV_FILE, line, "utf8");
  } catch (err) {
    console.error("Error escribiendo CSV:", err);
    return res.status(500).json({ ok: false, error: "write_error" });
  }

  res.json({ ok: true });
});

// Endpoint que devuelve el CSV (útil para fetch desde JS)
app.get("/readings", (req, res) => {
  try {
    const txt = fs.readFileSync(CSV_FILE, "utf8");
    res.type("text/plain").send(txt);
  } catch (err) {
    res.status(500).send("Error leyendo CSV");
  }
});

// También exponer /distancias.csv por compatibilidad
app.get("/distancias.csv", (req, res) => {
  try {
    const txt = fs.readFileSync(CSV_FILE, "utf8");
    res.type("text/csv").send(txt);
  } catch (err) {
    res.status(500).send("Error leyendo CSV");
  }
});

app.listen(PORT, () => {
  console.log(`Servidor listo en http://0.0.0.0:${PORT}  (usa http://192.168.1.15:${PORT})`);
});
