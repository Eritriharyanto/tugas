import React, { useState, useEffect } from "react";
import TransactionForm from "./components/TransactionForm";
import TransactionList from "./components/TransactionList";
import Summary from "./components/Summary";
import { groupByDate } from "./utils/helpers";

// Fungsi untuk ambil data dari localStorage saat pertama kali aplikasi dijalankan
const getSavedTransactions = () => {
  const saved = localStorage.getItem("transactions");
  return saved ? JSON.parse(saved) : [];
};

function App() {
  // Gunakan state untuk menyimpan transaksi di memori
  // Data awal diambil dari localStorage jika ada
  const [transactions, setTransactions] = useState(getSavedTransactions);

  // Simpan ke localStorage setiap kali transaksi berubah
  useEffect(() => {
    localStorage.setItem("transactions", JSON.stringify(transactions));
  }, [transactions]);

  // Debug: Lihat isi array transaksi di console browser
  console.log("Data transaksi:", transactions);

  // Debug: Lihat data yang sudah dikelompokkan per tanggal
  console.log("Transaksi dikelompokkan:", groupByDate(transactions));

  // Fungsi untuk menambahkan transaksi baru
  const addTransaction = (newTransaction) => {
    setTransactions([...transactions, { id: Date.now(), ...newTransaction }]);
  };

  // Fungsi untuk menghapus transaksi berdasarkan ID
  const deleteTransaction = (id) => {
    setTransactions(transactions.filter((t) => t.id !== id));
  };

  // Fungsi untuk mengedit transaksi
  const editTransaction = (id, updatedData) => {
    setTransactions(
      transactions.map((t) => (t.id === id ? { ...t, ...updatedData } : t))
    );
  };

  return (
    <div style={{ maxWidth: "700px", margin: "0 auto", padding: "2rem" }}>
      <h1>Aplikasi Keuangan Harian</h1>

      {/* Form input transaksi */}
      <TransactionForm onAdd={addTransaction} />

      {/* Ringkasan total saldo, pemasukan, pengeluaran */}
      <Summary transactions={transactions} />

      {/* Daftar transaksi yang sudah dikelompokkan per tanggal */}
      <TransactionList
        transactions={groupByDate(transactions)}
        onDelete={deleteTransaction}
        onEdit={editTransaction}
      />
    </div>
  );
}

export default App;
