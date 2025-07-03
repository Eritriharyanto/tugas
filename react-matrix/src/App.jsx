import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.bundle.min.js";

function App() {
  const [message, setMessage] = useState(
    "Tekan tombol Proses untuk melakukan perhitungan"
  );

  const doProcess = (e) => {
    setMessage("Maaf fitur perhitungan belum diimplementasikan");
  };

  return (
    <div className='container'>
      <h1>Penjumlahan Baris dan Kolom Matriks</h1>
      <hr />
      <div className='alert alert-info'>{message}</div>
      <div className='row mb-4'>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input readOnly className='form-control' />
        </div>
      </div>
      <div className='row mb-4'>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input readOnly className='form-control' />
        </div>
      </div>
      <div className='row mb-4'>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input type='number' className='form-control' />
        </div>
        <div className='col'>
          <input readOnly className='form-control' />
        </div>
      </div>
      <div className='row mb-4'>
        <div className='col'>
          <input readOnly className='form-control' />
        </div>
        <div className='col'>
          <input readOnly className='form-control' />
        </div>
        <div className='col'>
          <input readOnly className='form-control' />
        </div>
        <div className='col'>
          <button className='btn btn-primary' onClick={doProcess}>
            Proses
          </button>
        </div>
      </div>
    </div>
  );
}

export default App;
