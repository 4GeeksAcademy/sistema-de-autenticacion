import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export const Private = () => {
    const [message, setMessage] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        const fetchPrivateData = async () => {
            const token = sessionStorage.getItem("token");

            // Verificar si el token existe
            if (!token) {
                navigate("/login"); 
                return;
            }

            const response = await fetch("/api/private", {
                method: "GET",
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            if (response.ok) {
                const data = await response.json();
                setMessage(data.message);
            } else {
                navigate("/login"); 
            }
        };
        fetchPrivateData();
    }, [navigate]);

    return (
        <div className="container mt-5">
            <h2>Área Privada</h2>
            <div className="blog-post mt-4">
                <h3>Los Extraterrestres Entre Nosotros</h3>
                <p>
                    Desde tiempos inmemoriales, la humanidad ha mirado hacia las estrellas, preguntándose si estamos solos en el universo. Sin embargo, pocos saben que no solo hay vida en otros planetas, sino que esos seres ya caminan entre nosotros, ocultos a plena vista.
                </p>
                <p>
                    En esta clandestina sociedad, los extraterrestres han aprendido a adaptarse y vivir en nuestra sociedad, a menudo tomando formas humanas. Existen muchas teorías sobre su intención: algunos creen que vienen en paz, mientras que otros piensan que su objetivo es más siniestro.
                </p>
                <h3>La Sociedad de los Hombres de Negro</h3>
                <p>
                    Para mantener el secreto, ha surgido un grupo conocido como los Hombres de Negro. Esta sociedad secreta se encarga de vigilar a los extraterrestres, asegurándose de que no revelen su existencia y de que la humanidad permanezca en la ignorancia. Equipados con tecnología avanzada y un profundo conocimiento de la biología extraterrestre, son los guardianes del secreto.
                </p>
                <p>
                    Los Hombres de Negro son conocidos por sus trajes oscuros y su actitud intimidante. Se dice que tienen la capacidad de borrar recuerdos y manipular a quienes se cruzan en su camino. Sin embargo, sus verdaderas motivaciones son un misterio. ¿Son protectores de la humanidad o son cómplices de una agenda más grande?
                </p>
                <h3>La Verdad Oculta</h3>
                <p>
                    Aquellos que han tenido encuentros con estos seres a menudo reportan experiencias extrañas. Visiones de luces brillantes, encuentros en la oscuridad de la noche, y encuentros que desafían toda lógica. A medida que la tecnología avanza, la línea entre lo humano y lo alienígena se vuelve más difusa.
                </p>
                <p>
                    Esta es una advertencia para todos: siempre estén alerta. La próxima vez que vean a alguien que parece "diferente", pregúntense: ¿podría ser un extraterrestre camuflado? ¿Y si los Hombres de Negro están observando desde las sombras?
                </p>
            </div>
        </div>
    );
};
