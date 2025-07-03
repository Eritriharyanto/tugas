import React, { useState } from "react";

function TransactionList({ transactions, onDelete, onEdit }) {
  const [editingId, setEditingId] = useState(null);
  const [editData, setEditData] = useState({});

  // Fungsi untuk memformat angka menjadi Rupiah: Rp1.000
  const formatRupiah = (angka) => `Rp${angka.toLocaleString("id-ID")}`;

  const handleEdit = (transaction) => {
    setEditingId(transaction.id);
    setEditData({ ...transaction });
  };

  const handleSave = () => {
    onEdit(editingId, { ...editData, amount: parseFloat(editData.amount) });
    setEditingId(null);
  };

  return (
    <div className='mb-5'>
      <h3 className='mb-3'>Daftar Transaksi</h3>

      {/* Jika belum ada transaksi */}
      {Object.keys(transactions).length === 0 && <p>Belum ada transaksi</p>}

      {/* Menampilkan transaksi per tanggal */}
      {Object.entries(transactions).map(([date, items]) => (
        <div key={date} className='mb-3'>
          <h5 className='text-primary'>{date}</h5>

          <ul className='list-group'>
            {items.map((item) => (
              <li
                key={item.id}
                className={`list-group-item d-flex justify-content-between align-items-center ${
                  item.type === "income"
                    ? "list-group-item-success"
                    : "list-group-item-danger"
                }`}
              >
                {/* Mode edit */}
                {editingId === item.id ? (
                  <div className='w-100'>
                    <div className='row g-2 align-items-center'>
                      <div className='col-md-3'>
                        <input
                          type='number'
                          className='form-control'
                          value={editData.amount}
                          onChange={(e) =>
                            setEditData({ ...editData, amount: e.target.value })
                          }
                        />
                      </div>
                      <div className='col-md-3'>
                        <input
                          type='text'
                          className='form-control'
                          value={editData.description}
                          onChange={(e) =>
                            setEditData({
                              ...editData,
                              description: e.target.value,
                            })
                          }
                        />
                      </div>
                      <div className='col-md-3'>
                        <select
                          className='form-select'
                          value={editData.type}
                          onChange={(e) =>
                            setEditData({ ...editData, type: e.target.value })
                          }
                        >
                          <option value='income'>Pemasukan</option>
                          <option value='expense'>Pengeluaran</option>
                        </select>
                      </div>
                      <div className='col-md-3 d-flex gap-2'>
                        <button
                          onClick={handleSave}
                          className='btn btn-primary btn-sm'
                        >
                          Simpan
                        </button>
                        <button
                          onClick={() => setEditingId(null)}
                          className='btn btn-secondary btn-sm'
                        >
                          Batal
                        </button>
                      </div>
                    </div>
                  </div>
                ) : (
                  <>
                    <div>
                      {/* Format angka ke Rupiah */}
                      <strong>
                        {item.type === "income" ? "+" : "-"}{" "}
                        {formatRupiah(item.amount)}
                      </strong>{" "}
                      - {item.description}
                    </div>
                    <div className='d-flex gap-2'>
                      <button
                        onClick={() => handleEdit(item)}
                        className='btn btn-warning btn-sm'
                      >
                        Edit
                      </button>
                      <button
                        onClick={() => onDelete(item.id)}
                        className='btn btn-danger btn-sm'
                      >
                        Hapus
                      </button>
                    </div>
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
