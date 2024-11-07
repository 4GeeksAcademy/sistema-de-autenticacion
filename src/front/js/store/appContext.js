import React, { useState, useEffect } from "react";
import getState from "./flux.js";

// Inicializamos el contexto
export const Context = React.createContext(null);

// Función para inyectar el contexto
const injectContext = (PassedComponent) => {
	const StoreWrapper = (props) => {
		const [state, setState] = useState(
			getState({
				getStore: () => state.store,
				getActions: () => state.actions,
				setStore: (updatedStore) =>
					setState({
						store: Object.assign(state.store, updatedStore),
						actions: { ...state.actions },
					}),
			})
		);

		useEffect(() => {
			// Esta función se ejecuta una vez cuando se monta el componente
			state.actions.getMessage();
		}, []);
		return (
			<Context.Provider value={state}>
				<PassedComponent {...props} />
			</Context.Provider>
		);
	};
	return StoreWrapper;
};

export default injectContext;
