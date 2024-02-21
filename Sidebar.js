document.addEventListener("DOMContentLoaded", function() {
    const sidebar = document.querySelector(".sidebar"); // Adjusted selector to match the class name in the HTML
    const toggle = sidebar.querySelector(".toggle"); // Adjusted selector to match the structure in the HTML
    const searchBtn = sidebar.querySelector(".search-box"); // Adjusted selector to match the structure in the HTML
    const modeSwitch = sidebar.querySelector(".toggle-switch"); // Adjusted selector to match the structure in the HTML
    const modeText = sidebar.querySelector(".mode-text"); // Adjusted selector to match the structure in the HTML

    toggle.addEventListener("click", () => {
        sidebar.classList.toggle("close");
    });

    searchBtn.addEventListener("click", () => {
        sidebar.classList.remove("close");
    });

    modeSwitch.addEventListener("click", () => {
        document.body.classList.toggle("dark"); // Changed body to document.body to toggle dark mode on the whole page

        if (document.body.classList.contains("dark")) {
            modeText.innerText = "Light mode";
        } else {
            modeText.innerText = "Dark mode";
        }
    });
});
