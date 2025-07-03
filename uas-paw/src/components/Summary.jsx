// src/components/Summary.jsx
import React from "react";

function Summary({ transactions }) {
  // Menghitung total pemasukan, pengeluaran, dan saldo
  const income = transactions
    .filter((t) => t.type === "income")
    .reduce((sum, t) => sum + t.amount, 0);

  const expense = transactions
    .filter((t) => t.type === "expense")
    .reduce((sum, t) => sum + t.amount, 0);

  const balance = income - expense;

  // Format Rupiah
  const formatRupiah = (angka) => `Rp${angka.toLocaleString("id-ID")}`;

  // Rekap bulanan (opsional)
  const monthlySummary = transactions.reduce((acc, t) => {
    const month = new Date(t.date).toLocaleString("id-ID", {
      month: "long",
      year: "numeric",
    });
    if (!acc[month]) {
      acc[month] = { income: 0, expense: 0 };
    }
    acc[month][t.type] += t.amount;
    return acc;
  }, {});

  return (
    <div className='summary'>
      <h2>Ringkasan Keuangan</h2>
      <p>
        <strong>Saldo:</strong> {formatRupiah(balance)}
      </p>
      <p>
        <strong>Total Pemasukan:</strong> {formatRupiah(income)}
      </p>
      <p>
        <strong>Total Pengeluaran:</strong> {formatRupiah(expense)}
      </p>

      <hr />
      <h3>Rekap Bulanan</h3>
      {Object.entries(monthlySummary).map(([month, data]) => (
        <div key={month}>
          <strong>{month}</strong>
          <p>Pemasukan: {formatRupiah(data.income)}</p>
          <p>Pengeluaran: {formatRupiah(data.expense)}</p>
          <hr />
        </div>
      ))}
    </div>
  );
}

export default Summary;
