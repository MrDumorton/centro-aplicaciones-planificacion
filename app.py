import base64
from pathlib import Path

import streamlit as st


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================
st.set_page_config(
    page_title="Centro de Aplicaciones",
    page_icon="🟨",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# DIRECCIONES DE LAS APLICACIONES
# =========================================================
URL_VALIDACION_OT = "https://validacionot.streamlit.app/"
URL_PROCESADOR_EXCEL = "https://procesador-excel.streamlit.app/"
URL_REVISION_AMT = "https://revision-detenciones-amt.streamlit.app/"


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def archivo_a_base64(ruta: str) -> str:
    """
    Convierte un archivo local a una cadena Base64.
    Si el archivo no existe, retorna una cadena vacía.
    """
    archivo = Path(ruta)

    if not archivo.exists():
        return ""

    return base64.b64encode(archivo.read_bytes()).decode("utf-8")


# =========================================================
# CARGA DE IMÁGENES
# =========================================================
fondo_base64 = archivo_a_base64("static/fondo 1.jpg")
logo_base64 = archivo_a_base64("static/logo_finning.png")


# =========================================================
# PREPARACIÓN DEL LOGO
# =========================================================
if logo_base64:
    logo_html = (
        '<img '
        'class="header-logo" '
        f'src="data:image/png;base64,{logo_base64}" '
        'alt="Finning CAT">'
    )
else:
    logo_html = ""


# =========================================================
# CSS GENERAL
# =========================================================
st.html(
    f"""
<style>

/* =====================================================
   CONFIGURACIÓN GENERAL
===================================================== */

html,
body,
[data-testid="stAppViewContainer"],
.stApp {{
    min-height: 100%;
}}

body {{
    overflow-x: hidden;
}}

[data-testid="stAppViewContainer"] {{
    background:
        linear-gradient(
            rgba(255, 255, 255, 0.73),
            rgba(255, 255, 255, 0.73)
        ),
        url("data:image/jpeg;base64,{fondo_base64}");

    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-color: #efefef;
}}

.stApp {{
    background: transparent !important;
}}

.main {{
    background: transparent !important;
}}

[data-testid="stAppViewContainer"] > .main {{
    background: transparent !important;
}}

.block-container {{
    background: transparent !important;
}}

[data-testid="stHeader"] {{
    background: transparent;
    height: 0;
}}

[data-testid="stToolbar"] {{
    visibility: hidden;
}}

[data-testid="stSidebar"] {{
    display: none;
}}

[data-testid="collapsedControl"] {{
    display: none;
}}

[data-testid="stDecoration"] {{
    display: none;
}}

.block-container {{
    max-width: 1500px;
    padding-top: 10px;
    padding-bottom: 95px;
    padding-left: 42px;
    padding-right: 42px;
}}


/* =====================================================
   FRANJA SUPERIOR
===================================================== */

.top-yellow-line {{
    position: fixed;
    top: 0;
    left: 0;
    z-index: 9999;

    width: 100%;
    height: 14px;

    background: #ffb900;
}}


/* =====================================================
   ENCABEZADO
===================================================== */

.header-container {{
    display: flex;
    justify-content: space-between;
    align-items: center;

    width: 100%;

    margin-top: 6px;
    margin-bottom: 10px;
}}

.header-left {{
    display: flex;
    align-items: center;
    gap: 18px;
}}

.app-grid-icon {{
    display: grid;

    grid-template-columns: repeat(2, 14px);
    grid-template-rows: repeat(2, 14px);

    gap: 5px;
}}

.app-grid-icon span {{
    width: 14px;
    height: 14px;

    background: #171717;
    border-radius: 3px;
}}

.header-divider {{
    width: 3px;
    height: 54px;

    background: #ffb900;
}}

.header-title {{
    margin: 0;

    color: #171717;

    font-size: 24px;
    font-weight: 800;
    letter-spacing: 0.2px;
    line-height: 1.2;
}}

.header-subtitle {{
    margin-top: 5px;

    color: #414141;

    font-size: 16px;
    line-height: 1.2;
}}

.header-logo-container {{
    display: flex;
    justify-content: flex-end;
    align-items: center;

    min-width: 230px;
}}

.header-logo {{
    display: block;

    width: 210px;
    max-width: 100%;
    max-height: 72px;
    height: auto;

    object-fit: contain;
}}


/* =====================================================
   BIENVENIDA
===================================================== */

.welcome {{
    margin-top: 0;
    margin-bottom: 24px;

    text-align: center;
}}

.welcome h1 {{
    margin: 0;

    color: #111111;

    font-size: 46px;
    font-weight: 800;
    line-height: 1.1;
}}

.welcome p {{
    margin-top: 7px;
    margin-bottom: 0;

    color: #333333;

    font-size: 20px;
    line-height: 1.3;
}}


/* =====================================================
   CONTENEDOR DE TARJETAS
===================================================== */

.cards-wrapper {{
    display: grid;

    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 24px;

    align-items: stretch;

    width: 100%;
    margin: 0 auto;
}}


/* =====================================================
   TARJETAS
===================================================== */

.app-card {{
    position: relative;

    display: flex;
    flex-direction: column;

    min-height: 430px;

    padding: 30px 28px 26px 28px;

    background: rgba(255, 255, 255, 0.95);

    border: 1px solid rgba(20, 20, 20, 0.12);
    border-radius: 17px;

    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.14);

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}}

.app-card:hover {{
    transform: translateY(-5px);

    box-shadow: 0 15px 34px rgba(0, 0, 0, 0.18);
}}


/* =====================================================
   ETIQUETA PRIVADO
===================================================== */

.private-badge {{
    position: absolute;
    top: 27px;
    right: 24px;

    padding: 6px 13px;

    background: #f1f1f1;

    border: 1px solid #dddddd;
    border-radius: 18px;

    color: #222222;

    font-size: 13px;
    white-space: nowrap;
}}


/* =====================================================
   ENCABEZADO DE CADA TARJETA
===================================================== */

.card-header {{
    display: flex;
    align-items: center;
    gap: 18px;

    min-height: 90px;
    padding-right: 72px;
}}

.card-icon {{
    display: flex;
    align-items: center;
    justify-content: center;

    flex: 0 0 86px;

    width: 86px;
    height: 86px;

    background: linear-gradient(
        145deg,
        #ffc434,
        #f5a900
    );

    border-radius: 14px;

    color: #111111;

    font-size: 45px;
    line-height: 1;
}}

.card-title {{
    margin: 0;

    color: #111111;

    font-size: 23px;
    font-weight: 800;
    line-height: 1.2;
}}

.card-description {{
    margin-top: 8px;

    color: #515151;

    font-size: 15px;
    line-height: 1.45;
}}


/* =====================================================
   LÍNEA DIVISORIA
===================================================== */

.card-line {{
    height: 1px;

    margin: 22px 0 24px 0;

    background: #dedede;
}}


/* =====================================================
   LISTA DE FUNCIONALIDADES
===================================================== */

.feature-list {{
    flex-grow: 1;

    margin: 0;
    padding: 0;

    list-style: none;
}}

.feature-list li {{
    display: flex;
    align-items: center;
    gap: 14px;

    margin-bottom: 20px;

    color: #333333;

    font-size: 15px;
    line-height: 1.35;
}}

.feature-symbol {{
    display: inline-flex;
    align-items: center;
    justify-content: center;

    flex: 0 0 24px;

    width: 24px;

    color: #111111;

    font-size: 18px;
    text-align: center;
}}


/* =====================================================
   BOTONES
===================================================== */

.open-button {{
    position: relative;
    z-index: 20;
    pointer-events: auto !important;
    cursor: pointer;
    user-select: none;
    -webkit-tap-highlight-color: transparent;

    display: block;

    width: 100%;

    box-sizing: border-box;

    margin-top: 16px;
    padding: 13px 16px;

    background: linear-gradient(
        90deg,
        #ffb300,
        #ffc233
    );

    border-radius: 8px;

    color: #111111 !important;

    font-size: 17px;
    font-weight: 800;
    text-align: center;
    text-decoration: none !important;

    transition:
        filter 0.2s ease,
        transform 0.2s ease;
}}

.open-button:hover {{
    filter: brightness(0.96);
    transform: scale(1.01);

    color: #111111 !important;
    text-decoration: none !important;
}}


/* =====================================================
   PIE DE PÁGINA
===================================================== */

.footer {{
    position: fixed;
    bottom: 0;
    left: 0;
    z-index: 9998;

    display: flex;
    justify-content: space-between;
    align-items: center;

    width: 100%;

    box-sizing: border-box;

    padding: 14px 35px;

    background: rgba(255, 255, 255, 0.95);

    border-top: 1px solid #bcbcbc;

    backdrop-filter: blur(8px);
}}

.footer-left {{
    display: flex;
    align-items: center;
    gap: 12px;
}}

.footer-user-icon {{
    display: flex;
    align-items: center;
    justify-content: center;

    width: 35px;
    height: 35px;

    background: #1e1e1e;

    border-radius: 50%;

    color: #ffffff;

    font-size: 13px;
}}

.footer-name {{
    color: #111111;

    font-size: 15px;
    font-weight: 800;
    line-height: 1.2;
}}

.footer-role {{
    margin-top: 3px;

    color: #555555;

    font-size: 13px;
    line-height: 1.2;
}}

.footer-right {{
    color: #202020;

    font-size: 16px;
    font-weight: 800;
    text-align: right;
}}


/* =====================================================
   PANTALLAS MEDIANAS
===================================================== */

@media (max-width: 1100px) {{

    .cards-wrapper {{
        grid-template-columns: 1fr;
        max-width: 680px;
    }}

    .app-card {{
        min-height: auto;
    }}

    .welcome h1 {{
        font-size: 39px;
    }}

    .header-logo {{
        width: 180px;
    }}
}}


/* =====================================================
   DISPOSITIVOS MÓVILES
===================================================== */

@media (max-width: 700px) {{

    .block-container {{
        padding-top: 12px;
        padding-left: 16px;
        padding-right: 16px;
        padding-bottom: 135px;
    }}

    .header-container {{
        align-items: flex-start;
        margin-bottom: 18px;
    }}

    .header-left {{
        gap: 10px;
    }}

    .app-grid-icon {{
        grid-template-columns: repeat(2, 10px);
        grid-template-rows: repeat(2, 10px);
        gap: 4px;
    }}

    .app-grid-icon span {{
        width: 10px;
        height: 10px;
    }}

    .header-divider {{
        height: 46px;
    }}

    .header-title {{
        font-size: 17px;
    }}

    .header-subtitle {{
        font-size: 12px;
    }}

    .header-logo-container {{
        min-width: auto;
    }}

    .header-logo {{
        width: 125px;
        max-height: 55px;
    }}

    .welcome {{
        margin-bottom: 20px;
    }}

    .welcome h1 {{
        font-size: 34px;
    }}

    .welcome p {{
        font-size: 16px;
    }}

    .app-card {{
        min-height: auto;

        padding: 24px 20px;
    }}

    .private-badge {{
        top: 18px;
        right: 16px;

        font-size: 11px;
    }}

    .card-header {{
        align-items: flex-start;

        min-height: auto;
        padding-right: 70px;
    }}

    .card-icon {{
        flex-basis: 70px;

        width: 70px;
        height: 70px;

        font-size: 36px;
    }}

    .card-title {{
        font-size: 20px;
    }}

    .card-description {{
        font-size: 14px;
    }}

    .footer {{
        align-items: flex-start;

        padding: 12px 15px;
    }}

    .footer-right {{
        max-width: 45%;

        font-size: 13px;
    }}
}}

</style>
"""
)


# =========================================================
# ENCABEZADO
# =========================================================
st.html(
    f"""
<div class="top-yellow-line"></div>

<header class="header-container">

    <div class="header-left">

        <div class="app-grid-icon">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
        </div>

        <div class="header-divider"></div>

        <div>
            <div class="header-title">
                CENTRO DE APLICACIONES
            </div>

            <div class="header-subtitle">
                Validación y Procesamiento
            </div>
        </div>

    </div>
    
    <div class="header-logo-container">
        {logo_html}
    </div>

</header>

<section class="welcome">
    <h1>Bienvenido</h1>

    <p>
        Selecciona una aplicación para comenzar
    </p>
</section>
"""
)


# =========================================================
# TARJETAS DE LAS APLICACIONES
# =========================================================
st.html(
    f"""
<div class="cards-wrapper">

    <!-- =================================================
         VALIDACIÓN OT
    ================================================== -->
    <section class="app-card">

                
        

        <div class="card-header">

            <div class="card-icon">
                ☑
            </div>

            <div>
                <h2 class="card-title">
                    Validación OT
                </h2>

                <div class="card-description">
                    Validación de Órdenes de Trabajo
                </div>
            </div>

        </div>

        <div class="card-line"></div>

        <ul class="feature-list">

            <li>
                <span class="feature-symbol">
                    ☑
                </span>

                Validación de campos críticos
            </li>

            <li>
                <span class="feature-symbol">
                    ⚠
                </span>

                Detección de inconsistencias
            </li>

            <li>
                <span class="feature-symbol">
                    ▥
                </span>

                Reportes y estadísticas
            </li>

        </ul>

        <a
            class="open-button"
            href="{URL_VALIDACION_OT}"
            target="_top"
            
        >
            ▶&nbsp;&nbsp;Abrir aplicación
        </a>

    </section>


    <!-- =================================================
         PROCESADOR EXCEL
    ================================================== -->
    <section class="app-card">

                 
        

        <div class="card-header">

            <div class="card-icon">
                ▤
            </div>

            <div>
                <h2 class="card-title">
                    Procesador Excel
                </h2>

                <div class="card-description">
                    Procesador de archivos Excel
                </div>
            </div>

        </div>

        <div class="card-line"></div>

        <ul class="feature-list">

            <li>
                <span class="feature-symbol">
                    ▣
                </span>

                Procesamiento de archivos Excel
            </li>

            <li>
                <span class="feature-symbol">
                    ◉
                </span>

                Transformación de datos
            </li>

            <li>
                <span class="feature-symbol">
                    ⌁
                </span>

                Exportación de resultados
            </li>

        </ul>

        <a
            class="open-button"
            href="{URL_PROCESADOR_EXCEL}"
            target="_top"
        >
            ▶&nbsp;&nbsp;Abrir aplicación
        </a>

    </section>


    <!-- =================================================
         REVISIÓN DETENCIONES AMT
    ================================================== -->
    <section class="app-card">

                  
        

        <div class="card-header">

            <div class="card-icon">
                ▥
            </div>

            <div>
                <h2 class="card-title">
                    Revisión Detenciones AMT
                </h2>

                <div class="card-description">
                    Revisión detenciones AMT vs detenciones Collahuasi
                </div>
            </div>

        </div>

        <div class="card-line"></div>

        <ul class="feature-list">

            <li>
                <span class="feature-symbol">
                    ↔
                </span>

                Comparación de detenciones
            </li>

            <li>
                <span class="feature-symbol">
                    ◯
                </span>

                Análisis de discrepancias
            </li>

            <li>
                <span class="feature-symbol">
                    ▥
                </span>

                Reportes de revisión
            </li>

        </ul>

        <a
            class="open-button"
            href="{URL_REVISION_AMT}"
            target="_top"
        >
            ▶&nbsp;&nbsp;Abrir aplicación
        </a>

    </section>

</div>
"""
)


# =========================================================
# PIE DE PÁGINA
# =========================================================
st.html(
    """
<footer class="footer">

    <div class="footer-left">

        <div class="footer-user-icon">
            ●
        </div>

        <div>
            <div class="footer-name">
                Sergio Gacitúa
            </div>

            <div class="footer-role">
                Planificación | Finning - Collahuasi
            </div>
        </div>

    </div>

    <div class="footer-right">
    
    </div>

</footer>
"""
)
