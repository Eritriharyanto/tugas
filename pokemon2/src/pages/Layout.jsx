import { Outlet, Link } from "react-router-dom";

export default function Layout() {
	return (
		<>
			<nav className="navbar navbar-expand-lg navbar-light bg-light">
				<div className="container-fluid">
					<Link className="navbar-brand" to="#">
						Pokedex
					</Link>
					<button
						className="navbar-toggler"
						type="button"
						data-bs-toggle="collapse"
						data-bs-target="#navbarNav"
						aria-controls="navbarNav"
						aria-expanded="false"
						aria-label="Toggle navigation"
					>
						<span className="navbar-toggler-icon"></span>
					</button>
					<div className="collapse navbar-collapse" id="navbarNav">
						<ul className="navbar-nav">
							<li className="nav-item">
								<Link className="nav-link active" to="/">
									Home <span className="visually-hidden">(current)</span>
								</Link>
							</li>
							<li className="nav-item">
								<Link className="nav-link" to="/PokemonList">
									Pokemon List
								</Link>
							</li>
							<li className="nav-item">
								<Link className="nav-link" to="/about">
									About
								</Link>
							</li>
						</ul>
					</div>
				</div>
			</nav>
			<div className="container mt-4">
				<Outlet />
			</div>
		</>
	);
}
