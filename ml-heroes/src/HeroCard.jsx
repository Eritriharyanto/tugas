import { useState } from "react";
export default function HeroCard({ name, image, description }) {
  const [detailVisible, setDetailVisible] = useState(false);
  const showDetail = (e) => setDetailVisible(true);
  const hideDetail = (e) => setDetailVisible(false);
  return (
    <div
      className='card mb-4'
      style={{ width: "18rem", boxShadow: "0px 4px 10px rgba(255, 0, 0, 0.5)" }}
    >
      <img src={image} className='card-img-top' alt={name} />
      <div className='card-body'>
        <h5 className='card-title'>{name}</h5>
        <p className='card-text'>{description}</p>
        {detailVisible && <p className='card-text'>{data.description}</p>}
        <a
          href='https://m.mobilelegends.com/hero'
          class='card-link'
          onClick={detailVisible ? hideDetail : showDetail}
        >
          {detailVisible ? "Sembunyikan" : "Lihat"} Detail
        </a>
      </div>
    </div>
  );
}
