import streamlit as st
import random

# Listado de preguntas
preguntas = [
"¿Cuál es la comida favorita de …?",
    "¿Dónde le gustaría viajar a …?",
    "¿Qué trabajo tendría … si pudiera hacer cualquier cosa?",
    "Si … fuera un animal, ¿qué animal sería?",
    "¿Qué superpoder querría tener …?",
    "¿Cuál es el color favorito de …?",
    "¿Qué le hace más feliz a …?",
    "¿Cuál es la canción que más escucha …?",
    "¿Qué música escucha más …?",
    "¿Qué hobby te gustaría que probara …?",
    "Si … fuera un personaje de dibujos animados, ¿quién sería?",
    "¿Cuál es el sabor de helado favorito de …?",
    "¿Qué crees que siempre lleva … en su bolsillo o bolso?",
    "¿De qué no podía separarse … cuando era pequeño/a?",
    "¿Cuál sería el título de la película de …?",
    "Si … ganara la lotería, ¿qué compraría primero?",
    "Si todos en esta mesa estuvieran en una isla desierta, ¿qué papel tendría …?",
    "¿Cuál es el mejor talento de … que pocos conocen?",
    "¿Qué mascota crees que le gustaría tener a …?",
    "¿Cómo describirías a … en tres palabras?",
    "¿Cuál es la película favorita de …?",
    "Si … tuviera un restaurante, ¿qué comida serviría?",
    "Si … pudiera vivir en otra época, ¿cuál sería?",
    "Si … pudiera vivir en otro lugar, ¿cuál sería?",
    "¿Qué crees que es lo que más valora … en la vida?",
    "¿Qué es lo que más te gusta de …?",
    "¿Qué crees que le gustaría mejorar a …?",
    "¿Cuál sería el mejor regalo para …?",
    "¿Cómo se llaman los suegros de …?",
    "¿Cuándo es el cumpleaños de …?",
    "¿A qué jugaba cuando era pequeño/a?",
    "¿Cuál era el juguete preferido de … era pequeño/a?",
    "¿Cuál es la gamberrada más sonada de la infancia de …?",
    "¿Cómo castigaban a …?",
    "¿Cuál era la asignatura favorita del colegio de …?",
    "¿Qué le daba miedo cuando era pequeño/a?",
    "¿Cómo se llama el mejor amigo o amiga de …?",
    "¿Cuál era el apodo de …?",
    "¿Cuál es el nombre del primer novio/a de …?",
    "¿Cuál fue el primer trabajo de …?",
    "¿A qué edad empezó a trabajar …?",
    "¿Cuál es la película que más le gustó ver en el cine …?",
    "¿Cuál es el viaje más lejano que ha hecho …?",
    "¿A qué edad se casó …?",
    "¿Cuál es el invento que más le gusta a …?",
    "¿A qué famoso/a le gustaría conocer a …?",
    "¿De qué se arrepiente …?",
    "¿Cómo es un día perfecto de …?",
    "¿Cuál es el puesto de trabajo de … y qué hace exactamente en su trabajo?",
    "¿Qué es lo que más le gusta hacer a …?",
    "¿Cuál es la típica pose en las fotos de …?",
    "¿Qué es lo que más le enfada a …?",
    "¿De qué se pone siempre malo/a …?",
    "¿Cuándo es el aniversario de novios y de boda de …?",
    "¿Qué mal hábito tiene …?",
    "¿Qué quiere hacer y nunca tiene tiempo …?",
    "¿Cuál es el tema del que más le gusta hablar a …?",
    "¿Cuál ha sido la experiencia más emocionante de …?",
    "¿Cuál es uno de los lugares más bonitos que ha visitado …?",
    "¿Con qué se ríe mucho …?",
    "¿Qué tenemos en común … y yo?",
    "¿Cuál es el rol o el rasgo característico de … en la familia?",
    "Cuenta un recuerdo bonito o gracioso que tengas en común con …",
    "¿Qué quería ser … de mayor?",
    "¿Qué costumbre rara tiene …?",
    "¿Cómo enfrenta los problemas …?",
    "¿Cuál es la excusa favorita de …?",
    "¿Qué cualidad de … te gustaría tener?",
    "¿Cuál es el momento favorito del día de …?",
    "¿Qué manía tiene …?",
    "¿Cómo expresa su cariño por los que quiere …?",
    "¿Cuáles son las vacaciones favoritas de …?",
    "¿Cuáles son los estudios de …?",
    "¿Cuál es la forma favorita de pasar un fin de semana de …?",
    "¿Qué es lo que más miedo le da a …?",
    "¿Qué le hace vomitar del asco a …?",
    "¿A qué tiene alergia …?"
    "Elige una canción para que … baile ahora",
]

# Título
st.title("🎉 Juego de Preguntas en Familia 🎉")

# Ingresar nombres de los participantes
nombres = st.text_area("Escribe los nombres de los participantes separados por comas:").split(",")

# Botón para generar pregunta y destinatario
if st.button("Nueva Pregunta"):
    if len(nombres) > 1:
        pregunta = random.choice(preguntas)
        quien = random.choice([nombre.strip() for nombre in nombres if nombre.strip()])
        pregunta_formateada = pregunta.replace("…", quien)
        st.subheader("Pregunta:")
        st.write(pregunta_formateada)
    else:
        st.warning("Por favor, introduce al menos dos nombres.")
