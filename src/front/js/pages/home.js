import React, { useContext } from "react";
import { Context } from "../store/appContext";
import rigoImageUrl from "../../img/rigo-baby.jpg";
import "../../styles/home.css";

export const Home = () => {
	const { store, actions } = useContext(Context);

	return (
		<div className="home-container text-center mt-5">
			<h1 className="home-title">Welcome to Your App!</h1>
			<p>
				<img src={rigoImageUrl} alt="Rigo Baby" className="home-image" />
			</p>
			<div className="alert alert-info home-message">
				{store.message || "Loading message from the backend (make sure your Python backend is running)..." }
			</div>
			<p className="home-description">
				This boilerplate comes with lots of documentation:{" "}
				<a href="https://start.4geeksacademy.com/starters/react-flask" className="home-link">
					Read documentation
				</a>
			</p>
		</div>
	);
};
