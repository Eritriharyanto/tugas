// src/components/TransactionForm.jsx
import React, { useState } from "react";

function TransactionForm({ onAddTransaction }) {
  const [formData, setFormData] = useState({
    date: "",
    type: "income",
    amount: "",
    description: "",
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.date || !formData.amount || !formData.description) {
      alert("Semua field harus diisi!");
      return;
    }

    onAddTransaction({
      ...formData,
      amount: parseFloat(formData.amount),
      id: Date.now(),
    });

    setFormData({
      date: "",
      type: "income",
      amount: "",
      description: "",
    });
  };

  return (
    <form onSubmit={handleSubmit} className='transaction-form'>
      <h2>Catat Transaksi</h2>
      <input
        type='date'
        name='date'
        value={formData.date}
        onChange={handleChange}
        required
      />
      <select name='type' value={formData.type} onChange={handleChange}>
        <option value='income'>Pemasukan</option>
        <option value='expense'>Pengeluaran</option>
      </select>
      <input
        type='number'
        name='amount'
        value={formData.amount}
        onChange={handleChange}
        placeholder='Jumlah uang'
        required
      />
      <input
        type='text'
        name='description'
        value={formData.description}
        onChange={handleChange}
        placeholder='Deskripsi'
        required
      />
      <button type='submit'>Tambah</button>
    </form>
  );
}

export default TransactionForm;
