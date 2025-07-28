
function addCreditNote() {
   
    const existing = document.getElementById("server-credit-text");
    if (existing) existing.remove();

  
    const credit = document.createElement("p");
    credit.id = "server-credit-text";
    credit.style = "text-align: center; font-size: 12px; color: #888; margin-top: 40px;";
    credit.textContent = "© 2025 CYBERNEOGEN CTF. Crafted with ♥ by Gurudatt Choudhary";


    const target = document.querySelector("footer") || document.body;
    target.appendChild(credit);
}
