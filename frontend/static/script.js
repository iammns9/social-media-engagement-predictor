document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");
    const button = document.querySelector(".predict-btn");
    if (form) {
        form.addEventListener("submit", () => {
            button.disabled = true;
            button.innerHTML = `
                <i class="fa-solid fa-spinner fa-spin"></i>
                Predicting...
            `;
        });

    }
    const result = document.querySelector(".result-card");
    if (result) {
        result.scrollIntoView({
            behavior: "smooth",
            block: "center"
        });
    }
});