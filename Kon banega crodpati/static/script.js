let currentQuestion = 0;

function loadQuestion() {
    fetch(`/get_question/${currentQuestion}`)
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById("question-text").innerText = "Game Over!";
            document.getElementById("prize-level").innerText = "";
            document.getElementById("options").style.display = 'none';
            document.getElementById("message").innerText = data.message;
        } else {
            document.getElementById("question-text").innerText = data.question.question;
            document.getElementById("prize-level").innerText = `This question is for ₹${data.level}`;
            let options = document.querySelectorAll(".option-btn");
            data.question.options.forEach((opt, index) => {
                options[index].innerText = opt;
            });
            document.getElementById("options").style.display = 'grid';
            document.getElementById("message").innerText = '';
            document.getElementById("video-container").style.display = 'none';
        }
    });
}

function submitAnswer(choice) {
    fetch("/check_answer", {
        method: "POST",
        body: JSON.stringify({ q_index: currentQuestion, answer: choice }),
        headers: { "Content-Type": "application/json" }
    })
    .then(response => response.json())
    .then(data => {
        if (data.correct) {
            if (data.next_level === "7 Crore") {
                document.getElementById("question-container").style.display = 'none';
                document.getElementById("message").innerText = 'Congratulations! You’ve won ₹7 Crore!';
                document.getElementById("video-container").style.display = 'block';
                document.getElementById("win-video").play();
            } else {
                document.getElementById("message").innerText = `Correct! You've won ₹${data.next_level}`;
                currentQuestion++;
                setTimeout(loadQuestion, 1000);
            }
        } else {
            document.getElementById("message").innerText = "Wrong answer. Game Over!";
            document.getElementById("question-container").style.display = 'none';
        }
    });
}

document.addEventListener("DOMContentLoaded", loadQuestion);