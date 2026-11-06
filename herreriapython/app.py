from flask import Flask, render_template_string, url_for

app = Flask(__name__)

productos = [
    {
        "nombre": "Sillas de herrería",
        "descripcion": "Fabricación de sillas resistentes y personalizadas.",
        "imagen": "img/silla.jpg"
    },
    {
        "nombre": "Bases para tinacos",
        "descripcion": "Bases metálicas resistentes y seguras.",
        "imagen": "img/tinaco.jpg"
    },
    {
        "nombre": "Protecciones",
        "descripcion": "Protecciones para ventanas y espacios del hogar.",
        "imagen": "img/proteccion.jpg"
    },
    {
        "nombre": "Puertas",
        "descripcion": "Puertas metálicas con diseños personalizados.",
        "imagen": "img/puerta.jpg"
    },
    {
        "nombre": "Portones",
        "descripcion": "Portones resistentes para casas y negocios.",
        "imagen": "img/porton.jpg"
    },
    {
        "nombre": "Ventanas",
        "descripcion": "Ventanas metálicas fabricadas a la medida.",
        "imagen": "img/ventana.jpg"
    },
    {
        "nombre": "Barandales",
        "descripcion": "Barandales seguros para escaleras y balcones.",
        "imagen": "img/barandal.jpg"
    },
    {
        "nombre": "Escaleras",
        "descripcion": "Escaleras metálicas funcionales y resistentes.",
        "imagen": "img/escalera.jpg"
    },
    {
        "nombre": "Mesas",
        "descripcion": "Mesas metálicas para diferentes espacios.",
        "imagen": "img/mesa.jpg"
    },
    {
        "nombre": "Estructuras metálicas",
        "descripcion": "Fabricación de estructuras para diferentes proyectos.",
        "imagen": "img/estructura.jpg"
    }
]

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casa Ferro | Herrería en general</title>

    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: 'DM Sans', sans-serif;
            background: #111315;
            color: #f5f5f5;
        }

        header {
            width: 100%;
            padding: 22px 8%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: #171a1d;
            position: fixed;
            top: 0;
            z-index: 1000;
            border-bottom: 1px solid #303438;
        }

        .logo {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 25px;
            font-weight: bold;
            color: #f28c28;
            letter-spacing: 1px;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin-left: 25px;
            font-size: 14px;
            transition: 0.3s;
        }

        nav a:hover {
            color: #f28c28;
        }

        .inicio {
            min-height: 100vh;
            display: flex;
            align-items: center;
            padding: 130px 8% 80px;
            background:
                linear-gradient(90deg, rgba(0,0,0,.9), rgba(0,0,0,.45)),
                url("{{ url_for('static', filename='portada.jpg') }}");
            background-size: cover;
            background-position: center;
        }

        .contenido-inicio {
            max-width: 650px;
        }

        .contenido-inicio span {
            color: #f28c28;
            font-weight: bold;
            letter-spacing: 3px;
        }

        h1 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 65px;
            line-height: 1.1;
            margin: 20px 0;
        }

        .contenido-inicio p {
            color: #dddddd;
            font-size: 18px;
            line-height: 1.8;
            margin-bottom: 30px;
        }

        .boton {
            display: inline-block;
            background: #f28c28;
            color: #111;
            padding: 14px 25px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .boton:hover {
            background: #ffad50;
            transform: translateY(-3px);
        }

        section {
            padding: 90px 8%;
        }

        .titulo {
            text-align: center;
            margin-bottom: 50px;
        }

        .titulo span {
            color: #f28c28;
            text-transform: uppercase;
            letter-spacing: 3px;
            font-size: 13px;
            font-weight: bold;
        }

        .titulo h2 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 38px;
            margin-top: 12px;
        }

        .nosotros {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 50px;
            align-items: center;
            background: #191d20;
        }

        .nosotros h2 {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 38px;
            margin-bottom: 20px;
        }

        .nosotros h2 span {
            color: #f28c28;
        }

        .nosotros p {
            color: #c5c5c5;
            line-height: 1.9;
            margin-bottom: 15px;
        }

        .experiencia {
            background: #252a2e;
            padding: 35px;
            border-left: 5px solid #f28c28;
            border-radius: 8px;
        }

        .experiencia h3 {
            color: #f28c28;
            font-size: 28px;
            margin-bottom: 12px;
        }

        .experiencia p {
            color: #ddd;
            line-height: 1.7;
        }

        .productos {
            background: #111315;
        }

        .galeria {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 25px;
        }

        .producto {
            background: #1d2226;
            border-radius: 10px;
            overflow: hidden;
            transition: 0.3s;
            border: 1px solid #303438;
        }

        .producto:hover {
            transform: translateY(-8px);
            border-color: #f28c28;
        }

        .producto img {
            width: 100%;
            height: 190px;
            object-fit: cover;
            display: block;
        }

        .producto-info {
            padding: 22px;
        }

        .producto h3 {
            color: #f28c28;
            margin-bottom: 10px;
        }

        .producto p {
            color: #c5c5c5;
            font-size: 14px;
            line-height: 1.6;
        }

        .servicios {
            background: #191d20;
        }

        .servicios-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 25px;
        }

        .servicio {
            background: #252a2e;
            padding: 30px;
            border-radius: 10px;
            border-bottom: 4px solid #f28c28;
        }

        .servicio h3 {
            color: #f28c28;
            margin-bottom: 15px;
        }

        .servicio p {
            color: #ccc;
            line-height: 1.7;
        }

        .contacto {
            text-align: center;
            background: #111315;
        }

        .contacto p {
            color: #ccc;
            line-height: 1.8;
            margin: 15px auto 25px;
            max-width: 600px;
        }

        footer {
            text-align: center;
            padding: 25px;
            background: #080909;
            color: #888;
            font-size: 13px;
        }

        @media(max-width: 800px) {
            header {
                flex-direction: column;
                gap: 15px;
            }

            nav {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                gap: 12px;
            }

            nav a {
                margin: 0;
            }

            h1 {
                font-size: 43px;
            }

            .nosotros {
                grid-template-columns: 1fr;
            }

            .titulo h2 {
                font-size: 30px;
            }
        }
    </style>
</head>

<body>

<header>
    <div class="logo">CASA FERRO</div>

    <nav>
        <a href="#inicio">Inicio</a>
        <a href="#nosotros">Conócenos</a>
        <a href="#productos">Nuestros trabajos</a>
        <a href="#servicios">Servicios</a>
        <a href="#contacto">Contacto</a>
    </nav>
</header>

<section class="inicio" id="inicio">
    <div class="contenido-inicio">
        <span>CALIDAD Y EXPERIENCIA</span>
        <h1>CASA FERRO</h1>
        <p>
            Herrería en general. Creamos trabajos de metal resistentes,
            funcionales y personalizados para tu hogar o negocio.
        </p>
        <a href="#productos" class="boton">Conoce nuestros trabajos</a>
    </div>
</section>

<section class="nosotros" id="nosotros">

    <div>
        <span style="color:#f28c28; font-weight:bold; letter-spacing:2px;">
            CONÓCENOS
        </span>

        <h2>Tradición, trabajo y <span>dedicación</span></h2>

        <p>
            ¡Hola! Mi nombre es Rigoberto y cuento con 6 años de experiencia
            trabajando en el área de la herrería en general.
        </p>

        <p>
            A lo largo de este tiempo he realizado diferentes trabajos
            utilizando materiales metálicos para crear productos resistentes,
            útiles y con buenos acabados.
        </p>

        <p>
            En Casa Ferro buscamos ofrecer trabajos de calidad, tomando en
            cuenta las necesidades de cada cliente y poniendo dedicación
            en cada proyecto.
        </p>
    </div>

    <div class="experiencia">
        <h3>6 años de experiencia</h3>
        <p>
            Cada proyecto representa una oportunidad para demostrar nuestro
            compromiso con el trabajo bien hecho. Nos enfocamos en la
            resistencia, funcionalidad y presentación de cada pieza.
        </p>
    </div>

</section>

<section class="productos" id="productos">

    <div class="titulo">
        <span>Nuestros trabajos</span>
        <h2>Lo que podemos fabricar</h2>
    </div>

    <div class="galeria">

        {% for producto in productos %}
        <div class="producto">

            <img
                src="{{ url_for('static', filename=producto.imagen) }}"
                alt="{{ producto.nombre }}"
                onerror="this.style.display='none'"
            >

            <div class="producto-info">
                <h3>{{ producto.nombre }}</h3>
                <p>{{ producto.descripcion }}</p>
            </div>

        </div>
        {% endfor %}

    </div>

</section>

<section class="servicios" id="servicios">

    <div class="titulo">
        <span>¿Qué hacemos?</span>
        <h2>Nuestros servicios</h2>
    </div>

    <div class="servicios-grid">

        <div class="servicio">
            <h3>Fabricación</h3>
            <p>
                Elaboramos productos metálicos para diferentes necesidades,
                cuidando su resistencia y acabado.
            </p>
        </div>

        <div class="servicio">
            <h3>Trabajos para el hogar</h3>
            <p>
                Realizamos puertas, protecciones, barandales y otros
                productos para mejorar tu vivienda.
            </p>
        </div>

        <div class="servicio">
            <h3>Diseños personalizados</h3>
            <p>
                Adaptamos nuestros trabajos a las medidas y características
                que necesita cada cliente.
            </p>
        </div>

        <div class="servicio">
            <h3>Estructuras metálicas</h3>
            <p>
                Fabricamos estructuras y soportes metálicos para distintos
                espacios y proyectos.
            </p>
        </div>

    </div>

</section>

<section class="contacto" id="contacto">

    <div class="titulo">
        <span>Estamos para ayudarte</span>
        <h2>Hagamos realidad tu proyecto</h2>
    </div>

    <p>
        En Casa Ferro estamos interesados en conocer tus ideas y ayudarte
        a encontrar una solución de herrería para tu hogar o negocio.
    </p>

    <p>
        Gracias por visitar nuestra página y conocer un poco más sobre
        nuestro trabajo.
    </p>

</section>

<footer>
    © 2026 Casa Ferro | Herrería en general
</footer>

</body>
</html>
"""


@app.route("/")
def inicio():
    return render_template_string(HTML, productos=productos)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
