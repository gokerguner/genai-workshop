// Frontend mantığı — fetch ile backend'i çağırır, sonucu render eder.
// Harici bağımlılık yok, build step yok. Kendi endpoint'ine göre düzenle.

const queryInput = document.getElementById("query");
const runBtn = document.getElementById("run-btn");
const resultBox = document.getElementById("result");

function showResult(text, isError = false) {
  resultBox.textContent = text;
  resultBox.className = "show" + (isError ? " error" : "");
}

function showResultHTML(html) {
  resultBox.innerHTML = html;
  resultBox.className = "show";
}

async function run() {
  const query = queryInput.value.trim();
  if (!query) {
    showResult("Lütfen bir girdi yaz.", true);
    return;
  }

  runBtn.disabled = true;
  showResult("Çalışıyor...");

  try {
    // TODO: endpoint adını ve gönderdiğin alanları kendi API'ne göre değiştir.
    const res = await fetch("/process", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ query }),
    });

    if (!res.ok) {
      const err = await res.json().catch(() => ({}));
      showResult(err.detail || `Hata: ${res.status}`, true);
      return;
    }

    const data = await res.json();
    // TODO: response alanlarını kendi şemana göre render et.
    let html = `<div>${data.result ?? ""}</div>`;
    if (data.source_url) {
      html += `<div class="source">Kaynak: <a href="${data.source_url}" target="_blank" rel="noopener">${data.source_url}</a></div>`;
    }
    showResultHTML(html);
  } catch (e) {
    showResult("Ağ hatası: " + e.message, true);
  } finally {
    runBtn.disabled = false;
  }
}

runBtn.addEventListener("click", run);
queryInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") run();
});
