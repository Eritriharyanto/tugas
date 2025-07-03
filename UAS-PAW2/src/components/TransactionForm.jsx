import React, { useState } from "react";

function TransactionForm({ onAdd }) {
  const [formData, setFormData] = useState({
    date: "",
    amount: "",
    type: "income",
    description: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!formData.date || !formData.amount || !formData.description) return;
    onAdd({ ...formData, amount: parseFloat(formData.amount) });
    setFormData({ date: "", amount: "", type: "income", description: "" });
  };

  return (
    <form className='row g-2 mb-4' onSubmit={handleSubmit}>
      <div className='col-md-3'>
        <input
          type='date'
          className='form-control'
          value={formData.date}
          onChange={(e) => setFormData({ ...formData, date: e.target.value })}
          required
        />
      </div>
      <div className='col-md-2'>
        <input
          type='number'
          className='form-control'
          placeholder='Saldo'
          value={formData.amount}
          onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
          required
        />
      </div>
      <div className='col-md-2'>
        <select
          className='form-select'
          value={formData.type}
          onChange={(e) => setFormData({ ...formData, type: e.target.value })}
        >
          <option value='income'>Pemasukan</option>
          <option value='expense'>Pengeluaran</option>
        </select>
      </div>
      <div className='col-md-3'>
        <input
          type='text'
          className='form-control'
          placeholder='Deskripsi'
          value={formData.description}
          onChange={(e) =>
            setFormData({ ...formData, description: e.target.value })
          }
          required
        />
      </div>
      <div className='col-md-2 d-grid'>
        <button className='btn btn-success' type='submit'>
          Tambah
        </button>
      </div>
    </form>
  );
}

export default TransactionForm;
