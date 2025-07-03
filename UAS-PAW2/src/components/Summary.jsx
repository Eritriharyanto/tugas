import React from "react";

function Summary({ transactions }) {
  const income = transactions
    .filter((t) => t.type === "income")
    .reduce((sum, t) => sum + t.amount, 0);

  const expense = transactions
    .filter((t) => t.type === "expense")
    .reduce((sum, t) => sum + t.amount, 0);

  const saldo = income - expense;

  return (
    <div className='mb-4 p-3 bg-light rounded border'>
      <h4 className='mb-3'>Ringkasan Keuangan</h4>
      <p>
        <strong>Saldo: </strong>
        <span className='text-primary'>Rp{saldo.toLocaleString()}</span>
      </p>
      <p>
        <strong>Total Pemasukan: </strong>
        <span className='text-success'>Rp{income.toLocaleString()}</span>
      </p>
      <p>
        <strong>Total Pengeluaran: </strong>
        <span className='text-danger'>Rp{expense.toLocaleString()}</span>
      </p>
    </div>
  );
}

export default Summary;
