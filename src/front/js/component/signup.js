import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

export const Signup = () => {
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const navigate = useNavigate();

	const handleSubmit = async (e) => {
		e.preventDefault();

		try {
			const response = await fetch("https://weary-spooky-crematorium-94pvxgrq5qwh7ggx-3001.app.github.dev/api/signup", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({ email, password }),
			});

			if (!response.ok) {
				const data = await response.json();
				throw new Error(data.error || "Error during signup");
			}

			// Si la respuesta es ok, redirige al login
			navigate("/login");
		} catch (error) {
			alert(error.message);
		}
	};

	return (
		<div className="container mt-5">
			<h2>Sign Up</h2>
			<form onSubmit={handleSubmit}>
				<div className="mb-3">
					<label htmlFor="email" className="form-label">Email</label>
					<input
						type="email"
						className="form-control"
						id="email"
						value={email}
						onChange={(e) => setEmail(e.target.value)}
						required
					/>
				</div>
				<div className="mb-3">
					<label htmlFor="password" className="form-label">Password</label>
					<input
						type="password"
						className="form-control"
						id="password"
						value={password}
						onChange={(e) => setPassword(e.target.value)}
						required
					/>
				</div>
				<button type="submit" className="btn btn-primary">Register</button>
			</form>
		</div>
	);
};
