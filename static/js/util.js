function copyPasta(room_id) {
    navigator.clipboard.writeText("Estou te convidando ao meu grupo de amigo oculto!! ID da sala: " + room_id)
        .then(() => {
            const msg = document.getElementById("copy-message");
            msg.innerText = "Mensagem copiada!";
            msg.style.display = "block";
            setTimeout(() => msg.style.display = "none", 3000);
        })
        .catch(err => alert("Erro em copiar código: " + err));
}



function next(event, input, keydown) {

    const inputs = document.querySelectorAll(".code-input");
    const index = Array.prototype.indexOf.call(inputs, input);

    if(!keydown)
    {
        if (event.inputType === "deleteContentBackward") {
            input.value = "";

            if (index > 0) inputs[index - 1].focus();
            return;
        }
        if (input.value.length === 1)
        {
            let next = input.nextElementSibling;
            if (next) next.focus();
        }
        input.value = input.value.toUpperCase();
    }
    else
    {
        if (event.key === "Backspace") {
            if (input.value !== "") {
                input.value = "";
                event.preventDefault();
                return;
            }
            if (index > 0) inputs[index - 1].focus();
            event.preventDefault();
        }
    }
}



function paste() {
    const inputs = document.querySelectorAll(".code-input");

    inputs.forEach(input => {
        input.addEventListener("paste", function (event) {
            event.preventDefault();

            let paste = (event.clipboardData || window.clipboardData).getData("text");
            paste = paste.toUpperCase().replace(/[^A-Z0-9]/g, "");

            for (let i = 0; i < inputs.length; i++) {
                inputs[i].value = paste[i] || "";
            }

            const lastIndex = Math.min(paste.length, inputs.length) - 1;
            if (lastIndex >= 0) inputs[lastIndex].focus();

            join();
        });
    });
}



document.addEventListener("DOMContentLoaded", paste);




function join() {
    const inputs = document.querySelectorAll(".code-input");
    let code = "";
    inputs.forEach(i => code += i.value.toUpperCase());

    document.getElementById("room_id").value = code;
}