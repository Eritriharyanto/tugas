// src/App.jsx
import React, { useState } from "react";
import TransactionForm from "./components/TransactionForm";
import TransactionList from "./components/TransactionList";
import Summary from "./components/Summary";

function App() {
  const [transactions, setTransactions] = useState([]);

  // Menambahkan transaksi baru
  const handleAddTransaction = (newTransaction) => {
    setTransactions((prev) => [...prev, newTransaction]);
  };

  // Menghapus transaksi berdasarkan id
  const handleDeleteTransaction = (id) => {
    setTransactions((prev) => prev.filter((t) => t.id !== id));
  };

  // Mengedit transaksi berdasarkan id
  const handleEditTransaction = (id, updatedData) => {
    setTransactions((prev) =>
      prev.map((t) => (t.id === id ? { ...t, ...updatedData } : t))
    );
  };

  return (
    <div className='container'>
      <h1>📒 Aplikasi Keuangan Harian</h1>

      <TransactionForm onAddTransaction={handleAddTransaction} />

      <Summary transactions={transactions} />

      <TransactionList
        transactions={transactions}
        onDelete={handleDeleteTransaction}
        onEdit={handleEditTransaction}
      />
    </div>
  );
}

export default App;
