// credit.js

function addCreditNote() {
    const existing = document.getElementById("server-credit-text");
    if (existing) existing.remove();

    const credit = document.createElement("p");
    credit.id = "server-credit-text";
    credit.style = `
        text-align: center;
        font-size: 0.85em;
        color: #cbd5e0;
        margin: 50px 0 10px 0;
    `;
    credit.innerHTML = "© 2025 SecureApp · Crafted by <a href='https://github.com/gurudattch' target='_blank' style='color: #a0aec0; text-decoration: none;'>Gurudatt Choudhary</a>";

    const target = document.querySelector("footer") || document.body;
    target.appendChild(credit);
}
