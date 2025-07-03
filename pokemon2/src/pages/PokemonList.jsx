import { Link } from "react-router-dom";
import pokemonData from "../data/PokemonData";

const formatIndex = (index) => {
  return index.toString().padStart(3, "0");
};

export default function PokemonList() {
  return (
    <div className='container mt-4'>
      <div className='row'>
        {pokemonData.map((pokemon) => (
          <div className='col-md-4 text-center mb-4' key={pokemon.index}>
            <img
              src={`https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/${formatIndex(
                pokemon.index
              )}.png`}
              alt={pokemon.name}
              className='img-fluid'
              style={{ maxHeight: "200px" }}
            />
            <p>
              <Link to={`/detail/${pokemon.index}`} className='text-primary'>
                {pokemon.name}
              </Link>
            </p>
          </div>
        ))}
      </div>
    </div>
  );
}
