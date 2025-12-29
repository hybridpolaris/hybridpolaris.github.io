const textarea = document.getElementById("hpolish");

function backspace(textarea) {
    textarea.value = textarea.value.slice(0, textarea.value.length - 1);
}

function insert(textarea, text) {
    const start = textarea.selectionStart;
    textarea.value += text;
    textarea.selectionStart = textarea.selectionEnd = start + text.length;
}

let lastKey = "";
textarea.addEventListener("keydown", e => {
    const key = e.key;
    
    // Ignore modifiers & shortcuts
    if (e.ctrlKey || e.altKey || e.metaKey || !key) {
        lastKey = "";
        return;
    }
    
    const uppercase = e.shiftKey;
    const k = key.toLowerCase();
    
    // SPACEBAR special case
    if (key === " ") {
        e.preventDefault();
        if (lastKey === "s") {
            backspace(textarea);
            insert(textarea, "ς ");
        } else {
            insert(textarea, " ");
        }
        lastKey = "";
        return;
    }
    
    // BACKSPACE resets state
    if (key === "Backspace") {
        lastKey = "";
        return;
    }
    
    // Only letters
    if (k.length !== 1 || k < "a" || k > "z") return;
    
    e.preventDefault();
    
    // Double key → macron
    if (k === lastKey.toLowerCase()) {
        insert(textarea, "̄");
        lastKey = "";
        return;
    }
    
    let resetLastKey = false;

    switch (k) {
        case "a": insert(textarea, uppercase ? "A" : "α"); break;
        case "b": insert(textarea, uppercase ? "B" : "β"); break;
        case "c": insert(textarea, uppercase ? "C" : "c"); break;
        case "d": insert(textarea, uppercase ? "Δ" : "δ"); break;
        case "e": insert(textarea, uppercase ? "E" : "e"); break;
        case "f": insert(textarea, uppercase ? "Φ" : "φ"); break;

        case "g":
            if (lastKey === "n") {
                insert(textarea, "́");
                resetLastKey = true;
            } else {
                insert(textarea, uppercase ? "Γ" : "γ");
            }
            break;

        case "h":
            resetLastKey = true;
            if (lastKey === "t") { backspace(textarea); insert(textarea, "θ"); }
            else if (lastKey === "T") { backspace(textarea); insert(textarea, "Θ"); }
            else if (lastKey === "c") { backspace(textarea); insert(textarea, "χ̌"); }
            else if (lastKey === "C") { backspace(textarea); insert(textarea, "X̌"); }
            else if (lastKey === "s") { insert(textarea, "̌"); }
            else {
                resetLastKey = false;
                insert(textarea, uppercase ? "Ψ" : "ψ");
            }
            break;

        case "i": insert(textarea, uppercase ? "I" : "ι"); break;
        case "j": insert(textarea, uppercase ? "X" : "χ"); break;

        case "k":
            if (lastKey === "c" || lastKey === "C") {
                backspace(textarea);
                insert(textarea, uppercase ? "Ḱ" : "κ́");
                resetLastKey = true;
            } else {
                insert(textarea, uppercase ? "K" : "κ");
            }
            break;

        case "l": insert(textarea, uppercase ? "Λ" : "λ"); break;
        case "m": insert(textarea, uppercase ? "M" : "μ"); break;
        case "n": insert(textarea, uppercase ? "N" : "v"); break;
        case "o": insert(textarea, uppercase ? "O" : "o"); break;
        case "p": insert(textarea, uppercase ? "Π" : "π"); break;
        case "q": insert(textarea, uppercase ? "Ϟ" : "ϰ"); break;
        case "r": insert(textarea, uppercase ? "P" : "p"); break;

        case "s":
            if (lastKey === "c" || lastKey === "C") {
                backspace(textarea);
                insert(textarea, uppercase ? "Σ́" : "σ́");
                resetLastKey = true;
            } else {
                insert(textarea, uppercase ? "Σ" : "σ");
            }
            break;

        case "t": insert(textarea, uppercase ? "T" : "τ"); break;
        case "u": insert(textarea, uppercase ? "U" : "u"); break;
        case "v": insert(textarea, uppercase ? "B́" : "β́"); break;
        case "w": insert(textarea, uppercase ? "F" : "ω"); break;
        case "x": insert(textarea, uppercase ? "Ξ" : "ξ"); break;
        case "y": insert(textarea, uppercase ? "H" : "η"); break;
        case "z": insert(textarea, uppercase ? "Z" : "ζ"); break;
    }

    lastKey = resetLastKey ? "" : key;
});