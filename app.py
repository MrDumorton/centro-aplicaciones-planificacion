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
# Reemplazar por las URLs definitivas de Streamlit Cloud
# =========================================================
URL_VALIDACION_OT = "https://validacionot.streamlit.app/"
URL_PROCESADOR_EXCEL = "https://procesador-excel.streamlit.app/"
URL_REVISION_AMT = "https://revision-detenciones-amt.streamlit.app/"


# =========================================================
# FUNCIONES AUXILIARES
# =========================================================
def archivo_a_base64(ruta: str) -> str:
    """
    Convierte una imagen local a Base64 para poder utilizarla
    como fondo dentro del CSS.
    """
    archivo = Path(ruta)

    if not archivo.exists():
        return ""

    return base64.b64encode(archivo.read_bytes()).decode("utf-8")


fondo_base64 = archivo_a_base64("static/fondo.jpg")
logo_base64 = archivo_a_base64("static/logo.png")


# =========================================================
# CSS
# =========================================================
st.html(
    f"""
    <style>
    /* -----------------------------------------------------
       CONFIGURACIÓN GENERAL
    ----------------------------------------------------- */

    html,
    body,
    [data-testid="stAppViewContainer"],
    .stApp {{
        min-height: 100%;
    }}

    [data-testid="stAppViewContainer"] {{
        background:
            linear-gradient(
                rgba(255, 255, 255, 0.79),
                rgba(255, 255, 255, 0.79)
            ),
            url("data:image/jpeg;base64,{fondo_base64}");

        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
        background: transparent;
    }}

    [data-testid="stToolbar"] {{
        visibility: hidden;
    }}

    [data-testid="stSidebar"] {{
        display: none;
    }}

    .block-container {{
        max-width: 1500px;
        padding-top: 24px;
        padding-bottom: 95px;
        padding-left: 42px;
        padding-right: 42px;
    }}


    /* -----------------------------------------------------
       FRANJA SUPERIOR
    ----------------------------------------------------- */

    .top-yellow-line {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 16px;
        background: #ffb900;
        z-index: 9999;
    }}


    /* -----------------------------------------------------
       ENCABEZADO
    ----------------------------------------------------- */

    .header-container {{
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        width: 100%;
        margin-top: 6px;
        margin-bottom: 45px;
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
    }}

    .header-subtitle {{
        margin-top: 4px;
        color: #414141;
        font-size: 16px;
    }}

    .header-logo {{
        width: 205px;
        height: auto;
        object-fit: contain;
    }}


    /* -----------------------------------------------------
       BIENVENIDA
    ----------------------------------------------------- */

    .welcome {{
        text-align: center;
        margin-bottom: 40px;
    }}

    .welcome h1 {{
        margin: 0;
        font-size: 48px;
        font-weight: 800;
        color: #111111;
    }}

    .welcome p {{
        margin-top: 8px;
        font-size: 21px;
        color: #333333;
    }}


    /* -----------------------------------------------------
       TARJETAS
    ----------------------------------------------------- */

    .cards-wrapper {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 24px;
        align-items: stretch;
        margin: 0 auto;
    }}

    .app-card {{
        position: relative;
        display: flex;
        flex-direction: column;
        min-height: 470px;
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
    }}

    .card-header {{
        display: flex;
        align-items: center;
        gap: 18px;
        padding-right: 55px;
    }}

    .card-icon {{
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 0 0 86px;
        width: 86px;
        height: 86px;
        background: linear-gradient(145deg, #ffc434, #f5a900);
        border-radius: 14px;
        color: #111111;
        font-size: 45px;
    }}

    .card-title {{
        margin: 0;
        font-size: 23px;
        font-weight: 800;
        color: #111111;
        line-height: 1.2;
    }}

    .card-description {{
        margin-top: 8px;
        color: #515151;
        font-size: 15px;
        line-height: 1.45;
    }}

    .repository-name {{
        margin-top: 24px;
        margin-left: 104px;
        color: #f4a900;
        font-size: 17px;
        font-weight: 700;
        overflow-wrap: anywhere;
    }}

    .card-line {{
        height: 1px;
        margin: 30px 0 26px 0;
        background: #dedede;
    }}

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
    }}

    .feature-symbol {{
        width: 24px;
        color: #111111;
        font-size: 18px;
        text-align: center;
    }}

    .open-button {{
        display: block;
        width: 100%;
        box-sizing: border-box;
        margin-top: 16px;
        padding: 13px 16px;
        background: linear-gradient(90deg, #ffb300, #ffc233);
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
    }}


    /* -----------------------------------------------------
       PIE DE PÁGINA
    ----------------------------------------------------- */

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
        background: rgba(255, 255, 255, 0.94);
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
        color: white;
        font-size: 20px;
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


    /* -----------------------------------------------------
       RESPONSIVE
    ----------------------------------------------------- */

    @media (max-width: 1050px) {{
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
    }}

    @media (max-width: 700px) {{
        .block-container {{
            padding-left: 16px;
            padding-right: 16px;
            padding-bottom: 135px;
        }}

        .header-container {{
            margin-bottom: 32px;
        }}

        .header-logo {{
            width: 140px;
        }}

        .header-title {{
            font-size: 18px;
        }}

        .header-subtitle {{
            font-size: 13px;
        }}

        .welcome h1 {{
            font-size: 34px;
        }}

        .welcome p {{
            font-size: 17px;
        }}

        .app-card {{
            padding: 24px 20px;
        }}

        .card-header {{
            padding-right: 0;
        }}

        .card-icon {{
            flex-basis: 70px;
            width: 70px;
            height: 70px;
            font-size: 36px;
        }}

        .repository-name {{
            margin-left: 0;
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
    """,
    unsafe_allow_html=True,
)


# =========================================================
# COMPONENTES HTML
# =========================================================
logo_html = ""

if logo_base64:
    logo_html = (
        f'<img class="header-logo" '
        f'src="data:image/png;base64,{logo_base64}" '
        f'alt="Finning CAT">'
    )


st.markdown('<div class="top-yellow-line"></div>', unsafe_allow_html=True)


st.html(
    f"""
<div class="top-yellow-line"></div>

<div class="header-container">
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
</div>

<div class="welcome">
    <h1>Bienvenido</h1>
    <p>Selecciona una aplicación para comenzar</p>
</div>
"""
)


# =========================================================
# TARJETAS DE LAS APLICACIONES
# =========================================================
st.html(
    f"""
    <div class="cards-wrapper">

        <section class="app-card">
            <div class="private-badge">🔒 Privado</div>

            <div class="card-header">
                <div class="card-icon">☑</div>

                <div>
                    <h2 class="card-title">Validación OT</h2>
                    <div class="card-description">
                        Validación de Órdenes de Trabajo
                    </div>
                </div>
            </div>

            <div class="repository-name">
                validacion_ot
            </div>

            <div class="card-line"></div>

            <ul class="feature-list">
                <li>
                    <span class="feature-symbol">☑</span>
                    Validación de campos críticos
                </li>

                <li>
                    <span class="feature-symbol">⚠</span>
                    Detección de inconsistencias
                </li>

                <li>
                    <span class="feature-symbol">▥</span>
                    Reportes y estadísticas
                </li>
            </ul>

            <a
                class="open-button"
                href="{URL_VALIDACION_OT}"
                target="_blank"
                rel="noopener noreferrer"
            >
                ▶&nbsp;&nbsp;Abrir aplicación
            </a>
        </section>


        <section class="app-card">
            <div class="private-badge">🔒 Privado</div>

            <div class="card-header">
                <div class="card-icon">▤</div>

                <div>
                    <h2 class="card-title">Procesador Excel</h2>
                    <div class="card-description">
                        Procesador de archivos Excel
                    </div>
                </div>
            </div>

            <div class="repository-name">
                procesador-excel-streamlit
            </div>

            <div class="card-line"></div>

            <ul class="feature-list">
                <li>
                    <span class="feature-symbol">▣</span>
                    Procesamiento de archivos Excel
                </li>

                <li>
                    <span class="feature-symbol">◉</span>
                    Transformación de datos
                </li>

                <li>
                    <span class="feature-symbol">⌁</span>
                    Exportación de resultados
                </li>
            </ul>

            <a
                class="open-button"
                href="{URL_PROCESADOR_EXCEL}"
                target="_blank"
                rel="noopener noreferrer"
            >
                ▶&nbsp;&nbsp;Abrir aplicación
            </a>
        </section>


        <section class="app-card">
            <div class="private-badge">🔒 Privado</div>

            <div class="card-header">
                <div class="card-icon">▥</div>

                <div>
                    <h2 class="card-title">
                        Revisión Detenciones AMT
                    </h2>

                    <div class="card-description">
                        Revisión detenciones AMT vs detenciones Collahuasi
                    </div>
                </div>
            </div>

            <div class="repository-name">
                revision-detenciones-amt
            </div>

            <div class="card-line"></div>

            <ul class="feature-list">
                <li>
                    <span class="feature-symbol">↔</span>
                    Comparación de detenciones
                </li>

                <li>
                    <span class="feature-symbol">◯</span>
                    Análisis de discrepancias
                </li>

                <li>
                    <span class="feature-symbol">▥</span>
                    Reportes de revisión
                </li>
            </ul>

            <a
                class="open-button"
                href="{URL_REVISION_AMT}"
                target="_blank"
                rel="noopener noreferrer"
            >
                ▶&nbsp;&nbsp;Abrir aplicación
            </a>
        </section>

    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# PIE DE PÁGINA
# =========================================================
st.html(
    """
    <footer class="footer">

        <div class="footer-left">
            <div class="footer-user-icon">●</div>

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
            Centro de Aplicaciones Área Planificación
        </div>

    </footer>
    """,
    unsafe_allow_html=True,
)
