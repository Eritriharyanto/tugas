import { useState } from "react";
export default function PokemonCard({ data }) {
  const [detailVisible, setDetailVisible] = useState(false);
  const url =
    "https://www.pokemon.com/static-assets/" +
    "content-assets/cms2/img/pokedex/detail/" +
    `${String(data.index).padStart(3, "0")}.png`;
  const showDetail = (e) => setDetailVisible(true);
  const hideDetail = (e) => setDetailVisible(false);

  return (
    <div className='card mb-4' style={{ width: "12rem" }}>
      <img src={url} className='card-img-top' />
      <div className='card-body'>
        <h5 className='card-title'>{data.name}</h5>
        {detailVisible && <p className='card-text'>{data.description}</p>}
        <a
          href='#'
          class='card-link'
          onClick={detailVisible ? hideDetail : showDetail}
        >
          {detailVisible ? "Sembunyikan" : "Lihat"} Detail
        </a>
      </div>
    </div>
  );
}
