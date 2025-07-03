import PokemonCard from "./PokemonCard.jsx";
import pokemonData from "./data.jsx";
export default function App() {
  return (
    <div className='container my-4'>
      <h1>Pokedex</h1>
      <div className='row'>
        {pokemonData.map((item, key) => (
          <div className='col' key={key}>
            <PokemonCard data={item} />
          </div>
        ))}
      </div>
    </div>
  );
}
