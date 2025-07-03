import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./pages/Navbar";
import Home from "./pages/Home";
import Pokemon from "./pages/PokemonList";
import About from "./pages/About";
import NoPage from "./pages/NoPage";
import PokemonDetail from "./pages/PokemonDetail";

export default function App() {
	return (
		<BrowserRouter>
			<Routes>
				<Route path="/" element={<Navbar />}>
					<Route index element={<Home />} />
					<Route path="PokemonList" element={<Pokemon />} />
					<Route path="/detail/:index" element={<PokemonDetail />} />
					<Route path="about" element={<About />} />
					<Route path="*" element={<NoPage />} />
				</Route>
			</Routes>
		</BrowserRouter>
	);
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
