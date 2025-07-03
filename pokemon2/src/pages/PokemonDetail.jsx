import { useParams } from "react-router-dom";
import pokemonData from "../data/PokemonData";

const formatIndex = (index) => {
  return index.toString().padStart(3, "0");
};

export default function PokemonDetail() {
  const { index } = useParams();
  const pokemon = pokemonData.find((p) => p.index === parseInt(index));

  if (!pokemon) {
    return <div className='container mt-4'>Pokemon not found</div>;
  }

  return (
    <div className='container text-center mt-5' key={pokemon.index}>
      <img
        src={`https://www.pokemon.com/static-assets/content-assets/cms2/img/pokedex/full/${formatIndex(
          pokemon.index
        )}.png`}
        alt={pokemon.name}
        className='img-fluid mb-4'
        style={{ maxHeight: "300px" }}
      />
      <h2>{pokemon.name}</h2>
      <p className='text-muted'>{pokemon.description}</p>
    </div>
  );
}
