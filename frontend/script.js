console.log("Script.js loaded");

document.getElementById("mfrForm").addEventListener("submit", async function (e) {
  e.preventDefault(); // Prevent default form submission

  const formData = new FormData(this);
  const data = {};
  formData.forEach((value, key) => data[key] = value);

  const endpoint = data.use_ai === "yes"
    ? "http://localhost:5000/generate-ai"
    : "http://localhost:5000/generate-docx";

  console.log("Submitting to:", endpoint);
  document.getElementById("status").innerText = "Generating MFR...";

  try {
    const response = await fetch(endpoint, {
      method: "POST", // POST is crucial here
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    if (!response.ok) throw new Error("Export failed: " + response.status);

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = data.use_ai === "yes" ? "mfr_ai.docx" : "mfr.docx";
    a.click();

    document.getElementById("status").innerText = "Download complete.";
  } catch (err) {
    document.getElementById("status").innerText = "Error: " + err.message;
    console.error("Fetch error:", err);
  }
});

