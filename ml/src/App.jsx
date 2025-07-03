import React from "react";
import HeroCard from "./HeroCard";
import { heroes } from "./data";

export default function App() {
  return (
    <div className="container my-4">
      <h1 className="text-start">Mobile Legends Heroes</h1>
      <div className="row">
        {heroes.map((hero) => (
          <div key={hero.id} className="col-md-4">
            <HeroCard
              name={hero.name}
              image={hero.image}
              description={hero.description}
            />
          </div>
        ))}
      </div>
    </div>
  );
}
