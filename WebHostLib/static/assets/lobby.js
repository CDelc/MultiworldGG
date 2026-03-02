(function () {
    "use strict";

    const chatMessages = document.getElementById("chat-messages");
    const chatInput = document.getElementById("chat-input");
    const chatSendBtn = document.getElementById("chat-send-btn");
    const generateBtn = document.getElementById("generate-btn");
    const leaveBtn = document.getElementById("leave-btn");
    const yamlFileInput = document.getElementById("yaml-file-input");
    const dropZone = document.getElementById("yaml-upload-drop");
    const generateStandard = document.getElementById("generate-standard");
    const generateCustom = document.getElementById("generate-custom");
    const downloadPackageBtn = document.getElementById("download-package-btn");
    const uploadGameZone = document.getElementById("upload-game-zone");
    const gameFileInput = document.getElementById("game-file-input");
    let pollTimer = null;
    let pollInterval = 3000;
    let idleCycles = 0;
    let currentPlayerCount = 0;
    let knownVersion = null;
    let pollErrorCount = 0;
    let lastReadyCount = 0;
    let lastTotalCount = 0;
    const renderedMessageIds = new Set();

    // Returns { fast, slow, idleThreshold } based on lobby size.
    // Small lobby  (<20 players): 3s → 10s after ~15s idle
    // Large lobby (>=20 players): 10s → 30s after ~60s idle
    function getPollTiers() {
        if (currentPlayerCount >= 20) {
            return { fast: 10000, slow: 30000, idleThreshold: 6 };
        }
        return { fast: 3000, slow: 10000, idleThreshold: 5 };
    }

    // Scroll chat to bottom
    function scrollChatToBottom() {
        if (chatMessages) {
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    }
    scrollChatToBottom();

    function pollStatus() {
        fetch(API_BASE + "/status?after_message=" + lastMessageId)
            .then(res => res.json())
            .then(data => {
                knownVersion = data.version;
                currentState = data.state;
                hasCustomYamls = data.has_custom || false;
                updatePlayers(data.players);
                appendMessages(data.messages);
                updateGenerateButton(data);
                updateStatusDisplay(data);

                const readyLabel = document.getElementById("ready-count-label");
                if (readyLabel) {
                    readyLabel.textContent = `${data.ready_count} / ${data.player_count} players ready`;
                }

                if (MY_PLAYER_ID !== null &&
                    (currentState === LOBBY_STATE_OPEN || currentState === LOBBY_STATE_GENERATING)) {
                    const stillMember = data.players.some(p => p.id === MY_PLAYER_ID);
                    if (!stillMember) {
                        clearInterval(pollTimer);
                        document.getElementById("lobby-container").innerHTML =
                            '<h2>You have been removed from this lobby.</h2>' +
                            '<a href="/lobbies" class="lobby-back-link">&larr; Back to lobby list</a>';
                        return;
                    }
                }

                if (data.state === LOBBY_STATE_DONE) {
                    showResult(data);
                } else if (data.state === LOBBY_STATE_CLOSED) {
                    document.getElementById("lobby-container").innerHTML =
                        '<h1>Lobby Expired</h1><p>This lobby has been closed due to inactivity.</p>' +
                        '<p><a href="/lobbies">Back to Lobbies</a></p>';
                    clearInterval(pollTimer);
                    return;
                }

                currentPlayerCount = data.players.length;
                lastReadyCount = data.ready_count || 0;
                lastTotalCount = data.player_count || 0;
                pollErrorCount = 0;
            })
            .catch(err => {
                pollErrorCount++;
                console.error("Poll error:", err);
                if (pollErrorCount >= 3) {
                    clearInterval(pollTimer);
                    alert("Connection to the lobby was lost after repeated failures. Please refresh the page to reconnect.");
                }
            });
    }

    function pingAndMaybePoll() {
        fetch(API_BASE + "/ping")
            .then(res => res.json())
            .then(data => {
                const stateChanged = data.state !== currentState;
                const versionChanged = data.version !== knownVersion;
                knownVersion = data.version;
                if (currentState === LOBBY_STATE_GENERATING || stateChanged || versionChanged) {
                    idleCycles = 0;
                    pollStatus();
                } else {
                    idleCycles++;
                    adjustPollInterval();
                }
            })
            .catch(err => console.error("Ping error:", err));
    }

    function adjustPollInterval() {
        const tiers = getPollTiers();
        const newInterval = idleCycles >= tiers.idleThreshold ? tiers.slow : tiers.fast;
        if (newInterval !== pollInterval) {
            pollInterval = newInterval;
            clearInterval(pollTimer);
            pollTimer = setInterval(pingAndMaybePoll, pollInterval);
        }
    }

    function resetPollRate() {
        idleCycles = 0;
        const fast = getPollTiers().fast;
        if (pollInterval !== fast) {
            pollInterval = fast;
            clearInterval(pollTimer);
            pollTimer = setInterval(pingAndMaybePoll, pollInterval);
        }
    }

    function updatePlayers(players) {
        const playerList = document.getElementById("lobby-players");
        if (!playerList) return;

        playerList.innerHTML = "";
        players.forEach(p => {
            const li = document.createElement("li");
            li.className = "lobby-player";
            li.dataset.playerId = p.id;

            let html = '<div class="lobby-player-header">';
            html += `<strong>${escapeHtml(p.name)}${p.is_owner ? " (Host)" : ""}</strong>`;
            if (IS_OWNER && !p.is_owner && currentState === LOBBY_STATE_OPEN) {
                html += `<button class="kick-btn" data-player-id="${p.id}" title="Kick player">Kick</button>`;
            }
            if (p.id === MY_PLAYER_ID && currentState === LOBBY_STATE_OPEN) {
                const readyClass = p.is_ready ? " ready-btn-on" : "";
                const readyLabel = p.is_ready ? "Ready ✓" : "Mark Ready";
                const hasYamls = p.yamls && p.yamls.length > 0;
                const disabledAttr = hasYamls ? "" : " disabled title=\"Upload at least one YAML first\"";
                html += `<button class="ready-btn${readyClass}"${disabledAttr} data-player-id="${p.id}">${readyLabel}</button>`;
            } else if (p.is_ready) {
                html += `<span class="ready-indicator" title="Ready">✓</span>`;
            }
            html += '</div>';
            html += '<ul class="player-yamls">';
            p.yamls.forEach(y => {
                const slotName = escapeHtml(y.player_name || '');
                const isCustom = !!y.is_custom;
                const customTag = isCustom ? '<span class="yaml-custom-tag" title="Custom APWorld">&#x1F9E9;</span>' : '';
                const gameDisplay = y.game
                    ? (isCustom
                        ? `<span class="yaml-game-name yaml-game-custom">${escapeHtml(y.game)}</span>`
                        : `<a class="yaml-game-name" href="/games/${encodeURIComponent(y.game)}/player-options">${escapeHtml(y.game)}</a>`)
                    : `<span class="yaml-game-name">${escapeHtml(y.filename)}</span>`;
                const downloadHref = `/api/lobby/${LOBBY_ID}/yaml/${y.id}`;
                html += `<li data-yaml-id="${y.id}">`;
                html += `<span class="yaml-slot-name" data-tooltip="${escapeHtml(y.filename)}"><span>${slotName}</span></span>`;
                html += customTag;
                html += gameDisplay;
                html += `<a class="yaml-download-btn" href="${downloadHref}" title="Download YAML" download>&#x2B07;</a>`;

                if (isCustom && currentState === LOBBY_STATE_OPEN) {
                    const apw = y.apworld;
                    if (apw) {
                        const verLabel = apw.world_version ? `v${escapeHtml(apw.world_version)}` : "APWorld";
                        html += `<span class="apworld-status-ok" title="${escapeHtml(apw.filename)}">&#10003; ${verLabel}</span>`;
                    } else if (p.id === MY_PLAYER_ID) {
                        html += `<button class="apworld-upload-btn" data-yaml-id="${y.id}" title="Upload APWorld for this game">&#x2B06; APWorld</button>`;
                    } else {
                        html += `<span class="apworld-missing" title="APWorld not yet uploaded">&#9888;</span>`;
                    }
                }

                if (currentState === LOBBY_STATE_OPEN && (IS_OWNER || p.id === MY_PLAYER_ID)) {
                    html += `<button class="yaml-delete-btn" data-yaml-id="${y.id}" title="Remove YAML">&times;</button>`;
                }
                html += '</li>';
            });
            html += '</ul>';

            li.innerHTML = html;
            playerList.appendChild(li);
        });

        // Re-bind delete, kick, apworld upload, and ready buttons
        bindYamlDeleteButtons();
        bindKickButtons();
        bindApworldUploadButtons();
        bindReadyButtons();
    }

    function appendMessages(messages) {
        if (!chatMessages || !messages.length) return;
        messages.forEach(msg => {
            if (msg.id > lastMessageId) lastMessageId = msg.id;
            if (renderedMessageIds.has(msg.id)) return;
            renderedMessageIds.add(msg.id);
            const div = document.createElement("div");
            div.className = "chat-msg" + (msg.system ? " chat-system" : "");
            div.dataset.messageId = msg.id;
            const time = new Date(msg.time).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
            const isTrueSystem = msg.system && msg.sender === "System";
            const deleteBtn = (!isTrueSystem && IS_OWNER)
                ? `<button class="msg-delete-btn" data-message-id="${msg.id}" title="Delete message">&times;</button>`
                : "";
            if (isTrueSystem) {
                div.innerHTML = `<span class="chat-time">${time}</span><span class="chat-system-text">${escapeHtml(msg.content)}</span>`;
            } else {
                div.innerHTML = `${deleteBtn}<span class="chat-time">${time}</span><strong class="chat-sender">${escapeHtml(msg.sender)}:</strong> <span class="chat-text">${escapeHtml(msg.content)}</span>`;
            }
            chatMessages.appendChild(div);
        });
        scrollChatToBottom();
    }

    function updateGenerateButton(data) {
        const info = document.getElementById("generate-info");
        if (info) {
            info.textContent = `${data.total_yamls} YAML(s) from ${data.player_count} player(s)`;
        }

        const isCustomMode = hasCustomYamls && currentState === LOBBY_STATE_OPEN;
        if (generateStandard) generateStandard.style.display = isCustomMode ? "none" : "";
        if (generateCustom) generateCustom.style.display = isCustomMode ? "" : "none";

        const missingNotice = document.getElementById("missing-apworlds-notice");
        const missingList = document.getElementById("missing-apworlds-list");
        if (missingNotice && missingList) {
            if (isCustomMode) {
                const missingGames = new Set();
                (data.players || []).forEach(p => {
                    (p.yamls || []).forEach(y => {
                        if (y.is_custom && !y.apworld) {
                            missingGames.add(y.game || y.filename);
                        }
                    });
                });
                if (missingGames.size > 0) {
                    missingList.innerHTML = [...missingGames]
                        .map(g => `<li>${escapeHtml(g)}</li>`).join("");
                    missingNotice.style.display = "";
                } else {
                    missingNotice.style.display = "none";
                }
            } else {
                missingNotice.style.display = "none";
            }
        }

        if (generateBtn) {
            const hasYamls = data.total_yamls > 0;
            generateBtn.disabled = !hasYamls || currentState !== LOBBY_STATE_OPEN;
            if (currentState === LOBBY_STATE_GENERATING) {
                generateBtn.textContent = "Generating...";
                generateBtn.disabled = true;
            } else {
                generateBtn.textContent = "Generate Seed";
            }
        }
    }

    function updateStatusDisplay(data) {
        const statusEl = document.getElementById("lobby-status");
        if (!statusEl) return;

        statusEl.className = "lobby-status-" + data.state;
        if (data.state === LOBBY_STATE_OPEN) statusEl.textContent = "Open";
        else if (data.state === LOBBY_STATE_GENERATING) statusEl.textContent = "Generating...";
        else if (data.state === LOBBY_STATE_DONE) statusEl.textContent = "Seed created, Lobby locked";
        else if (data.state === LOBBY_STATE_CLOSED) statusEl.textContent = "Closed";

        const uploadArea = document.getElementById("yaml-upload-area");
        if (uploadArea) {
            uploadArea.style.display = data.state === LOBBY_STATE_OPEN ? "" : "none";
        }

        const genSection = document.getElementById("lobby-generate");
        if (genSection) {
            genSection.style.display = data.state === LOBBY_STATE_OPEN ? "" : "none";
        }

        const generatingDiv = document.getElementById("lobby-generating");
        if (generatingDiv) {
            generatingDiv.style.display = data.state === LOBBY_STATE_GENERATING ? "block" : "none";
        }

        if (leaveBtn) {
            leaveBtn.style.display = data.state === LOBBY_STATE_OPEN ? "" : "none";
        }
    }

    function showResult(data) {
        const resultDiv = document.getElementById("lobby-result");
        if (!resultDiv) return;

        let html = '<h2>Seed Ready!</h2>';
        if (IS_OWNER && data.seed_id) {
            html += `<p><a href="/seed/${data.seed_id}">View Seed</a></p>`;
        }
        if (data.room_id) {
            html += `<p><a href="/room/${data.room_id}" class="lobby-btn lobby-btn-primary">Go to Room</a></p>`;
        }
        if (data.server_password) {
            const pw = data.server_password.replace(/"/g, "&quot;");
            html += `<p class="server-password-row">Server Password:
                <span class="server-password-reveal">
                    <span class="password-placeholder">hover to reveal</span>
                    <span class="password-value">${pw}</span>
                </span></p>`;
        }
        resultDiv.innerHTML = html;
        resultDiv.style.display = "block";
    }

    // Chat
    function sendChat() {
        if (!chatInput) return;
        const message = chatInput.value.trim();
        if (!message) return;

        resetPollRate();
        fetch(API_BASE + "/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message }),
        })
            .then(res => res.json())
            .then(data => {
                if (!data.error) {
                    chatInput.value = "";

                    if (!renderedMessageIds.has(data.id)) {
                        renderedMessageIds.add(data.id);
                        const div = document.createElement("div");
                        div.className = "chat-msg";
                        div.dataset.messageId = data.id;
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

    if (chatMessages && IS_OWNER) {
        chatMessages.addEventListener("click", e => {
            const btn = e.target.closest(".msg-delete-btn");
            if (!btn) return;
            const messageId = btn.dataset.messageId;
            if (!confirm("Delete this message?")) return;

            fetch(`${API_BASE}/message/${messageId}`, { method: "DELETE" })
                .then(res => res.json())
                .then(data => {
                    if (data.error) {
                        alert(data.error);
                    } else {
                        const div = chatMessages.querySelector(`[data-message-id="${messageId}"]`);
                        if (div) {
                            div.className = "chat-msg chat-system";
                            const time = div.querySelector(".chat-time").outerHTML;
                            div.innerHTML = `${time}<span class="chat-system-text">${escapeHtml(data.content)}</span>`;
                        }
                    }
                })
                .catch(err => console.error("Message delete error:", err));
        });
    }

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
                    const customUploaded = (data.uploaded || []).filter(u => u.is_custom);
                    if (customUploaded.length > 0) {
                        alert(`Uploaded ${customUploaded.length} custom game YAML(s). ` +
                              `Please upload the corresponding .apworld file(s) using the ` +
                              `"⬆ APWorld" button next to each custom YAML.`);
                    }
                    resetPollRate();
                    pollStatus();
                }
            })
            .catch(err => {
                console.error("Upload error:", err);
                alert("Upload failed. Please try again.");
            });
    }

    if (yamlFileInput) {
        yamlFileInput.addEventListener("change", e => {
            if (e.target.files.length > 0) uploadFiles(e.target.files);
        });
    }

    function uploadApworld(yamlId, file) {
        const formData = new FormData();
        formData.append("file", file);

        fetch(`${API_BASE}/apworld/${yamlId}`, { method: "POST", body: formData })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    alert("APWorld upload error: " + data.error);
                } else {
                    resetPollRate();
                    pollStatus();
                }
            })
            .catch(err => {
                console.error("APWorld upload error:", err);
                alert("APWorld upload failed. Please try again.");
            });
    }

    function bindApworldUploadButtons() {
        document.querySelectorAll(".apworld-upload-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                const yamlId = this.dataset.yamlId;
                const input = document.createElement("input");
                input.type = "file";
                input.accept = ".apworld";
                input.onchange = e => {
                    const file = e.target.files[0];
                    if (file) uploadApworld(yamlId, file);
                };
                input.click();
            });
        });
    }
    bindApworldUploadButtons();

    if (downloadPackageBtn) {
        downloadPackageBtn.addEventListener("click", () => {
            if (lastReadyCount < lastTotalCount) {
                const unready = lastTotalCount - lastReadyCount;
                if (!confirm(`${unready} player(s) are not ready yet. Download package anyway?`)) return;
            }
            window.location.href = `${API_BASE}/download-package`;
        });
    }

    function uploadGameFile(file) {
        const formData = new FormData();
        formData.append("file", file);

        if (uploadGameZone) uploadGameZone.classList.add("uploading");

        fetch(`${API_BASE}/upload-game`, { method: "POST", body: formData })
            .then(res => res.json())
            .then(data => {
                if (uploadGameZone) uploadGameZone.classList.remove("uploading");
                if (data.error) {
                    alert("Upload error: " + data.error);
                } else {
                    resetPollRate();
                    pollStatus();
                }
            })
            .catch(err => {
                if (uploadGameZone) uploadGameZone.classList.remove("uploading");
                console.error("Game upload error:", err);
                alert("Upload failed. Please try again.");
            });
    }

    if (uploadGameZone) {
        uploadGameZone.addEventListener("dragover", e => {
            e.preventDefault();
            uploadGameZone.classList.add("drag-over");
        });
        uploadGameZone.addEventListener("dragleave", () => {
            uploadGameZone.classList.remove("drag-over");
        });
        uploadGameZone.addEventListener("drop", e => {
            e.preventDefault();
            uploadGameZone.classList.remove("drag-over");
            if (e.dataTransfer.files.length > 0) uploadGameFile(e.dataTransfer.files[0]);
        });
    }

    if (gameFileInput) {
        gameFileInput.addEventListener("change", e => {
            if (e.target.files.length > 0) uploadGameFile(e.target.files[0]);
        });
    }

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

    function bindYamlDeleteButtons() {
        document.querySelectorAll(".yaml-delete-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                const yamlId = this.dataset.yamlId;
                if (!confirm("Remove this YAML?")) return;

                resetPollRate();
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

    function bindKickButtons() {
        document.querySelectorAll(".kick-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                const playerId = this.dataset.playerId;
                if (!confirm("Kick this player?")) return;

                resetPollRate();
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

    function bindReadyButtons() {
        document.querySelectorAll(".ready-btn").forEach(btn => {
            btn.addEventListener("click", function () {
                btn.disabled = true;
                fetch(API_BASE + "/ready", { method: "POST" })
                    .then(res => res.json())
                    .then(data => {
                        if (!data.error) {
                            resetPollRate();
                            pollStatus();
                        }
                    })
                    .catch(err => console.error("Ready toggle error:", err))
                    .finally(() => {
                        setTimeout(() => { btn.disabled = false; }, 1500);
                    });
            });
        });
    }
    bindReadyButtons();

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

    if (generateBtn) {
        generateBtn.addEventListener("click", () => {
            if (lastReadyCount < lastTotalCount) {
                const unready = lastTotalCount - lastReadyCount;
                if (!confirm(`${unready} player(s) are not ready yet. Generate anyway?`)) return;
            } else {
                if (!confirm("Generate the seed with all uploaded YAMLs?")) return;
            }

            generateBtn.disabled = true;
            generateBtn.textContent = "Generating...";

            fetch(API_BASE + "/generate", { method: "POST" })
                .then(res => res.json())
                .then(data => {
                    if (data.error) {
                        alert("Generation error: " + data.error);
                        generateBtn.disabled = false;
                        generateBtn.textContent = "Generate Seed";
                    } else {
                        resetPollRate();
                        pollStatus();
                    }
                })
                .catch(err => {
                    console.error("Generate error:", err);
                    generateBtn.disabled = false;
                    generateBtn.textContent = "Generate Seed";
                });
        });
    }

    function escapeHtml(text) {
        const div = document.createElement("div");
        div.appendChild(document.createTextNode(text));
        return div.innerHTML;
    }

    const settingsModal = document.getElementById("settings-modal");
    const settingsEditBtn = document.getElementById("settings-edit-btn");
    const settingsSaveBtn = document.getElementById("settings-save-btn");
    const settingsCancelBtn = document.getElementById("settings-cancel-btn");

    function openSettingsModal() {
        if (settingsModal) settingsModal.classList.add("open");
    }

    function closeSettingsModal() {
        if (settingsModal) settingsModal.classList.remove("open");
    }

    if (settingsEditBtn) {
        settingsEditBtn.addEventListener("click", openSettingsModal);
    }
    if (settingsCancelBtn) {
        settingsCancelBtn.addEventListener("click", closeSettingsModal);
    }
    if (settingsModal) {
        settingsModal.addEventListener("click", e => {
            if (e.target === settingsModal) closeSettingsModal();
        });
    }
    if (settingsSaveBtn) {
        settingsSaveBtn.addEventListener("click", () => {
            const maxPlayersEl = document.getElementById("edit-max-players");
            const payload = {
                title: document.getElementById("edit-title").value.trim(),
                max_yamls_per_player: parseInt(document.getElementById("edit-max-yamls").value),
                timeout_minutes: parseInt(document.getElementById("edit-timeout").value),
                max_players: maxPlayersEl ? parseInt(maxPlayersEl.value) || 0 : undefined,
                release_mode: document.getElementById("edit-release-mode").value,
                collect_mode: document.getElementById("edit-collect-mode").value,
                remaining_mode: document.getElementById("edit-remaining-mode").value,
                countdown_mode: document.getElementById("edit-countdown-mode").value,
                hint_mode: document.getElementById("edit-hint-mode").value,
                hint_cost: parseInt(document.getElementById("edit-hint-cost").value),
                item_cheat: document.getElementById("edit-item-cheat").value === "1",
                spoiler: parseInt(document.getElementById("edit-spoiler").value),
            };

            settingsSaveBtn.disabled = true;
            settingsSaveBtn.textContent = "Saving…";

            fetch(API_BASE + "/settings", {
                method: "PATCH",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(payload),
            })
                .then(res => res.json())
                .then(data => {
                    if (data.error) {
                        alert("Error: " + data.error);
                        settingsSaveBtn.disabled = false;
                        settingsSaveBtn.textContent = "Save";
                    } else {
                        location.reload();
                    }
                })
                .catch(err => {
                    console.error("Settings error:", err);
                    settingsSaveBtn.disabled = false;
                    settingsSaveBtn.textContent = "Save";
                });
        });
    }

    if (generateStandard && generateCustom) {
        const isCustomMode = hasCustomYamls && currentState === LOBBY_STATE_OPEN;
        generateStandard.style.display = isCustomMode ? "none" : "";
        generateCustom.style.display = isCustomMode ? "" : "none";
    }

    pollStatus();
    pollTimer = setInterval(pingAndMaybePoll, pollInterval);
})();
