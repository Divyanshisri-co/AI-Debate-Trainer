function displayMessage(sender, text) {
    let chatBox = document.getElementById("chat-box");

    let msgDiv = document.createElement("div");
    msgDiv.classList.add("message");

    if (sender === "You") {
        msgDiv.classList.add("user");
    } else {
        msgDiv.classList.add("ai");
    }

    msgDiv.innerText = sender + ": " + text;

    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}


function sendMessage() {
    let input = document.getElementById("userInput");
    let text = input.value;

    if (!text) return;

    displayMessage("You", text);

    fetch("/chat_api/", {
    method: "POST",
    headers: {
        "Content-Type": "application/x-www-form-urlencoded"
    },
    body: "message=" + encodeURIComponent(text)
})
.then(async res => {
    let data = await res.json();
    if (!res.ok) {
        throw new Error(data.reply || "Server error");
    }
    return data;
})
.then(data => {
    displayMessage("AI", data.reply);
})
.catch(err => {
    console.error("FULL ERROR:", err);
    alert("Check console (F12)");
});

    input.value = "";
}


function getCSRFToken() {
    let cookies = document.cookie.split(";");
    for (let c of cookies) {
        if (c.trim().startsWith("csrftoken=")) {
            return c.split("=")[1];
        }
    }
}
