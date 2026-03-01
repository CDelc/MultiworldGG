// Lobby client-side logic

(function () {
    "use strict";

    const chatMessages = document.getElementById("chat-messages");
    const chatInput = document.getElementById("chat-input");
    const chatSendBtn = document.getElementById("chat-send-btn");
    const generateBtn = document.getElementById("generate-btn");
    const leaveBtn = document.getElementById("leave-btn");
    const yamlUploadBtn = document.getElementById("yaml-upload-btn");
    const yamlFileInput = document.getElementById("yaml-file-input");
    const dropZone = document.getElementById("yaml-upload-drop");
    let pollTimer = null;

    // Scroll chat to bottom
    function scrollChatToBottom() {
        if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }
    scrollChatToBottom();

    // Poll lobby status
    function pollStatus() {
        fetch(API_BASE + "/status?after_message=" + lastMessageId)
            .then(res => res.json())
            .then(data => {
                currentState = data.state;
                updatePlayers(data.players);
                appendMessages(data.messages);
                updateGenerateButton(data);
                updateStatusDisplay(data);

                if (data.state === LOBBY_STATE_DONE) {
                    showResult(data);
                } else if (data.state === LOBBY_STATE_CLOSED) {
                    document.getElementById("lobby-container").innerHTML =
                        '<h1>Lobby Expired</h1><p>This lobby has been closed due to inactivity.</p>' +
                        '<p><a href="/lobbies">Back to Lobbies</a></p>';
                    clearInterval(pollTimer);
                }
            })
            .catch(err => console.error("Poll error:", err));
    }

    function updatePlayers(players) {
        const playerList = document.getElementById("lobby-players");
        if (!playerList) return;

        playerList.innerHTML = "";
        players.forEach(p => {
            const li = document.createElement("li");
            li.className = "lobby-player";
            li.dataset.playerId = p.id;

            let html = `<strong>${escapeHtml(p.name)}${p.is_owner ? " (Host)" : ""}</strong>`;
            html += '<ul class="player-yamls">';
            p.yamls.forEach(y => {
                let label = escapeHtml(y.filename);
                if (y.game) {
                    label += ` - <span class="yaml-game-name">${escapeHtml(y.game)}</span>`;
                }
                if (y.player_name) {
                    label += ` <span class="yaml-slot-name">(${escapeHtml(y.player_name)})</span>`;
                }
                html += `<li data-yaml-id="${y.id}">${label}`;
                // Only show delete for own YAMLs, or all if lobby owner
                if (currentState === LOBBY_STATE_OPEN && (IS_OWNER || p.id === MY_PLAYER_ID)) {
                    html += ` <button class="yaml-delete-btn" data-yaml-id="${y.id}" title="Remove YAML">&times;</button>`;
                }
                html += '</li>';
            });
            html += '</ul>';

            if (IS_OWNER && !p.is_owner && currentState === LOBBY_STATE_OPEN) {
                html += `<button class="kick-btn" data-player-id="${p.id}" title="Kick player">Kick</button>`;
            }

            li.innerHTML = html;
            playerList.appendChild(li);
        });

        // Re-bind delete and kick buttons
        bindYamlDeleteButtons();
        bindKickButtons();
    }

    function appendMessages(messages) {
        if (!chatMessages || !messages.length) return;
        messages.forEach(msg => {
            if (msg.id > lastMessageId) {
                lastMessageId = msg.id;
                const div = document.createElement("div");
                div.className = "chat-msg" + (msg.system ? " chat-system" : "");
                const time = new Date(msg.time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                if (msg.system) {
                    div.innerHTML = `<span class="chat-time">${time}</span><span class="chat-system-text">${escapeHtml(msg.content)}</span>`;
                } else {
                    div.innerHTML = `<span class="chat-time">${time}</span><strong class="chat-sender">${escapeHtml(msg.sender)}:</strong> <span class="chat-text">${escapeHtml(msg.content)}</span>`;
                }
                chatMessages.appendChild(div);
            }
        });
        scrollChatToBottom();
    }

    function updateGenerateButton(data) {
        if (!generateBtn) return;
        const hasYamls = data.total_yamls > 0;
        generateBtn.disabled = !hasYamls || currentState !== LOBBY_STATE_OPEN;

        const info = document.getElementById("generate-info");
        if (info) {
            info.textContent = `${data.total_yamls} YAML(s) from ${data.player_count} player(s)`;
        }

        if (currentState === LOBBY_STATE_GENERATING) {
            generateBtn.textContent = "Generating...";
            generateBtn.disabled = true;
        }
    }

    function updateStatusDisplay(data) {
        const statusEl = document.getElementById("lobby-status");
        if (!statusEl) return;

        statusEl.className = "lobby-status-" + data.state;
        if (data.state === LOBBY_STATE_OPEN) statusEl.textContent = "Open";
        else if (data.state === LOBBY_STATE_GENERATING) statusEl.textContent = "Generating...";
        else if (data.state === LOBBY_STATE_DONE) statusEl.textContent = "Done";
        else if (data.state === LOBBY_STATE_CLOSED) statusEl.textContent = "Closed";

        // Hide upload area during generation or done
        const uploadArea = document.getElementById("yaml-upload-area");
        if (uploadArea && data.state !== LOBBY_STATE_OPEN) {
            uploadArea.style.display = "none";
        }

        // Hide generate section during generation or done
        const genSection = document.getElementById("lobby-generate");
        if (genSection && data.state !== LOBBY_STATE_OPEN) {
            genSection.style.display = "none";
        }
    }

    function showResult(data) {
        const resultDiv = document.getElementById("lobby-result");
        if (!resultDiv) return;

        let html = '<h2>Seed Ready!</h2>';
        if (data.seed_id) {
            html += `<p><a href="/seed/${data.seed_id}">View Seed</a></p>`;
        }
        if (data.room_id) {
            html += `<p><a href="/room/${data.room_id}" class="lobby-btn lobby-btn-primary">Go to Room</a></p>`;
        }
        resultDiv.innerHTML = html;
        resultDiv.style.display = "block";
    }

    // Chat
    function sendChat() {
        if (!chatInput) return;
        const message = chatInput.value.trim();
        if (!message) return;

        fetch(API_BASE + "/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        })
            .then(res => res.json())
            .then(data => {
                if (!data.error) {
                    chatInput.value = "";
                    // Message will appear on next poll, but show immediately for responsiveness
                    if (data.id > lastMessageId) {
                        lastMessageId = data.id;
                        const div = document.createElement("div");
                        div.className = "chat-msg";
                        const time = new Date(data.time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                        div.innerHTML = `<span class="chat-time">${time}</span><strong class="chat-sender">${escapeHtml(data.sender)}:</strong> <span class="chat-text">${escapeHtml(data.content)}</span>`;
                        chatMessages.appendChild(div);
                        scrollChatToBottom();
                    }
                }
            })
            .catch(err => console.error("Chat error:", err));
    }

    if (chatSendBtn) {
        chatSendBtn.addEventListener("click", sendChat);
    }
    if (chatInput) {
        chatInput.addEventListener("keypress", e => {
            if (e.key === "Enter") sendChat();
        });
    }

    // YAML Upload
    function uploadFiles(files) {
        if (!files || files.length === 0) return;

        const formData = new FormData();
        for (const file of files) {
            formData.append("file", file);
        }

        fetch(API_BASE + "/upload", {
            method: "POST",
            body: formData,
        })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    alert("Upload error: " + data.error);
                } else {
                    if (yamlFileInput) yamlFileInput.value = "";
                    pollStatus(); // Refresh immediately
                }
            })
            .catch(err => {
                console.error("Upload error:", err);
                alert("Upload failed. Please try again.");
            });
    }

    if (yamlUploadBtn) {
        yamlUploadBtn.addEventListener("click", () => {
            if (yamlFileInput && yamlFileInput.files.length > 0) {
                uploadFiles(yamlFileInput.files);
            }
        });
    }

    // Drag & drop
    if (dropZone) {
        dropZone.addEventListener("dragover", e => {
            e.preventDefault();
            dropZone.classList.add("drag-over");
        });
        dropZone.addEventListener("dragleave", () => {
            dropZone.classList.remove("drag-over");
        });
        dropZone.addEventListener("drop", e => {
            e.preventDefault();
            dropZone.classList.remove("drag-over");
            uploadFiles(e.dataTransfer.files);
        });
    }

    // YAML Delete
    function bindYamlDeleteButtons() {
        document.querySelectorAll(".yaml-delete-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                const yamlId = this.dataset.yamlId;
                if (!confirm("Remove this YAML?")) return;

                fetch(API_BASE + "/yaml/" + yamlId, { method: "DELETE" })
                    .then(res => res.json())
                    .then(data => {
                        if (data.error) alert(data.error);
                        else pollStatus();
                    })
                    .catch(err => console.error("Delete error:", err));
            });
        });
    }
    bindYamlDeleteButtons();

    // Kick
    function bindKickButtons() {
        document.querySelectorAll(".kick-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                const playerId = this.dataset.playerId;
                if (!confirm("Kick this player?")) return;

                fetch(API_BASE + "/kick/" + playerId, { method: "POST" })
                    .then(res => res.json())
                    .then(data => {
                        if (data.error) alert(data.error);
                        else pollStatus();
                    })
                    .catch(err => console.error("Kick error:", err));
            });
        });
    }
    bindKickButtons();

    // Leave
    if (leaveBtn) {
        leaveBtn.addEventListener("click", () => {
            if (!confirm("Leave this lobby?")) return;

            fetch(API_BASE + "/leave", { method: "POST" })
                .then(res => res.json())
                .then(data => {
                    if (data.error) alert(data.error);
                    else window.location.href = "/lobbies";
                })
                .catch(err => console.error("Leave error:", err));
        });
    }

    // Close lobby
    const closeBtn = document.getElementById("close-btn");
    if (closeBtn) {
        closeBtn.addEventListener("click", () => {
            if (!confirm("Close this lobby? This cannot be undone.")) return;

            fetch(API_BASE + "/close", { method: "POST" })
                .then(res => res.json())
                .then(data => {
                    if (data.error) alert(data.error);
                    else window.location.href = "/lobbies";
                })
                .catch(err => console.error("Close error:", err));
        });
    }

    // Generate
    if (generateBtn) {
        generateBtn.addEventListener("click", () => {
            if (!confirm("Generate the seed with all uploaded YAMLs?")) return;

            generateBtn.disabled = true;
            generateBtn.textContent = "Generating...";

            fetch(API_BASE + "/generate", { method: "POST" })
                .then(res => res.json())
                .then(data => {
                    if (data.error) {
                        alert("Generation error: " + data.error);
                        generateBtn.disabled = false;
                        generateBtn.textContent = "Generate Seed";
                    }
                    // Status will update via polling
                })
                .catch(err => {
                    console.error("Generate error:", err);
                    generateBtn.disabled = false;
                    generateBtn.textContent = "Generate Seed";
                });
        });
    }

    // Utility
    function escapeHtml(text) {
        const div = document.createElement("div");
        div.appendChild(document.createTextNode(text));
        return div.innerHTML;
    }

    // Start polling
    pollTimer = setInterval(pollStatus, 3000);
})();
