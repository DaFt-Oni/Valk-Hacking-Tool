// Mostrar datos recibidos
function showData() {
    fetch("/api/data")
        .then(response => response.json())
        .then(data => {
            const dataOutput = document.getElementById("dataOutput");
            dataOutput.innerHTML = data.map(row => `
                <div class="data-row">
                    <strong>ID:</strong> ${row.id}<br>
                    <strong>Ejecutable:</strong> ${row.executable_name}<br>
                    <strong>Datos:</strong> ${row.data}<br>
                </div>
            `).join("");
            document.getElementById("dataSection").style.display = "block";
            document.getElementById("hackingToolSection").style.display = "none";
        });
}

// Mostrar la sección de la herramienta de hacking
function showHackingTool() {
    document.getElementById("dataSection").style.display = "none";
    document.getElementById("hackingToolSection").style.display = "block";
}

// Ejecutar comandos de hacking
function executeHackingCommand() {
    const command = document.getElementById("hackingInput").value;
    fetch("/api/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ command: `python main.py ${command}` }),
    })
    .then(response => response.json())
    .then(data => {
        const hackingOutput = document.getElementById("hackingOutput");
        hackingOutput.innerHTML += `<pre>${data.output || data.error}</pre>`;
    });
}

// Consola interactiva
document.getElementById("consoleInput").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        const command = this.value;
        fetch("/api/command", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ command: command }),
        })
        .then(response => response.json())
        .then(data => {
            const consoleOutput = document.getElementById("consoleOutput");
            consoleOutput.innerHTML += `<pre>> ${command}\n${data.output || data.error}</pre>`;
            this.value = "";
        });
    }
});