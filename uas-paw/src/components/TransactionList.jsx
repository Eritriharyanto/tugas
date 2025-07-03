// src/components/TransactionList.jsx
import React, { useState } from "react";

function TransactionList({ transactions, onDelete, onEdit }) {
  const [editingId, setEditingId] = useState(null);
  const [editData, setEditData] = useState({});

  // Format angka ke Rupiah
  const formatRupiah = (angka) => `Rp${angka.toLocaleString("id-ID")}`;

  // Mengelompokkan transaksi berdasarkan tanggal
  const groupedByDate = transactions.reduce((acc, transaksi) => {
    const { date } = transaksi;
    if (!acc[date]) acc[date] = [];
    acc[date].push(transaksi);
    return acc;
  }, {});

  const handleEditClick = (transaksi) => {
    setEditingId(transaksi.id);
    setEditData({ ...transaksi });
  };

  const handleEditChange = (e) => {
    const { name, value } = e.target;
    setEditData((prev) => ({
      ...prev,
      [name]: name === "amount" ? parseFloat(value) : value,
    }));
  };

  const handleEditSave = () => {
    onEdit(editingId, editData);
    setEditingId(null);
  };

  const handleCancelEdit = () => {
    setEditingId(null);
    setEditData({});
  };

  return (
    <div className='transaction-list'>
      <h2>Daftar Transaksi</h2>
      {Object.keys(groupedByDate)
        .sort((a, b) => new Date(b) - new Date(a))
        .map((date) => (
          <div key={date}>
            <h4>{date}</h4>
            <ul>
              {groupedByDate[date].map((t) => (
                <li key={t.id}>
                  {editingId === t.id ? (
                    <>
                      <select
                        name='type'
                        value={editData.type}
                        onChange={handleEditChange}
                      >
                        <option value='income'>Pemasukan</option>
                        <option value='expense'>Pengeluaran</option>
                      </select>
                      <input
                        type='number'
                        name='amount'
                        value={editData.amount}
                        onChange={handleEditChange}
                      />
                      <input
                        type='text'
                        name='description'
                        value={editData.description}
                        onChange={handleEditChange}
                      />
                      <button onClick={handleEditSave}>Simpan</button>
                      <button onClick={handleCancelEdit}>Batal</button>
                    </>
                  ) : (
                    <>
                      <strong>
                        [{t.type === "income" ? "➕" : "➖"}]{" "}
                        {formatRupiah(t.amount)}
                      </strong>{" "}
                      - {t.description}
                      <button onClick={() => handleEditClick(t)}>Edit</button>
                      <button onClick={() => onDelete(t.id)}>Hapus</button>
                    </>
                  )}
                </li>
              ))}
            </ul>
          </div>
        ))}
    </div>
  );
}

export default TransactionList;
