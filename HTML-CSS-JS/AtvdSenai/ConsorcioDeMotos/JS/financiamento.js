// Taxa de juros fixa em 1.49% ao mês
const fixedInterestRate = 0.0149;

function calculateLoan() {
    const loanAmount = parseFloat(document.getElementById("loanAmount").value);
    const interestRate = fixedInterestRate;
    const loanTerm = parseInt(document.getElementById("loanTerm").value);
    const downPayment = parseFloat(document.getElementById("downPayment").value) || 0;

    if (isNaN(loanAmount) || isNaN(loanTerm)) {
        window.alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    if (downPayment < 2000) {
        window.alert("O valor mínimo de entrada é de R$ 2.000.");
        return;
    }

    const monthlyInterestRate = interestRate;
    const totalLoanAmount = loanAmount - downPayment;

    if (loanAmount <= 0 || loanTerm <= 0) {
        window.alert("Por favor, preencha todos os campos corretamente.");
        return;
    }

    const monthlyPayment = (totalLoanAmount * monthlyInterestRate) / (1 - Math.pow(1 + monthlyInterestRate, -loanTerm));
    const totalPayment = monthlyPayment * loanTerm;

    document.getElementById("monthlyPayment").textContent = "R$ " + monthlyPayment.toFixed(2);
    document.getElementById("totalPayment").textContent = "R$ " + totalPayment.toFixed(2);
}