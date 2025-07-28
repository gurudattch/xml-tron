function addCreditNote() {
    const existing = document.getElementById("server-credit-text");
    if (existing) existing.remove();

    const credit = document.createElement("p");
    credit.id = "server-credit-text";
    credit.style = `
        margin-top: 10px;
        font-size: 0.85em;
        color: #a0aec0;
    `;
    credit.innerHTML = "© 2025 CYBERNOGEN · Crafted by <a href='https://github.com/gurudattch' target='_blank' style='color: #718096; text-decoration: none;'>Gurudatt Choudhary</a>";

    // Target the last div inside .container (your empty styled div)
    const targetContainer = document.querySelector(".container");
    const targetDivs = targetContainer.querySelectorAll("div");
    const lastDiv = targetDivs[targetDivs.length - 1];

    lastDiv.appendChild(credit);
}
