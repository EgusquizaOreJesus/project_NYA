import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# prueba de paginación

# Ruta del ejecutable de ChromeDriver
chrome_driver_path = "C:\\Users\\Jesus Egusquiza\\Desktop\\PROYECTOS\\WEB_SCRAPPING_SELENIUM\\chromedriver.exe"

# Configuramos el servicio de ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializamos el driver de Chrome
driver = webdriver.Chrome(service=service)

# Solicitar la búsqueda al usuario
busqueda = input("¿Qué anime quieres buscar? ")

# Construir la URL de búsqueda
url_busqueda = f"https://nyaa.si/?f=0&c=0_0&q={busqueda.replace(' ', '+')}"

# Página donde queremos hacer el scraping
driver.get(url_busqueda)


# Función para recolectar los datos de los animes en la página actual
def recolectar_animes():
    animes = driver.find_elements(By.XPATH, "//tr[@class='default']")
    for anime in animes:
        # Extraemos el nombre del anime
        nombre = anime.find_element(By.XPATH, ".//td[@colspan='2']/a").text
        print(f"Nombre: {nombre}")
        print("\n")


# Recolectar datos de la primera página
recolectar_animes()

# Navegar a través de todas las páginas de resultados
while True:
    try:
        # Intentar encontrar y hacer clic en el botón "Siguiente"
        siguiente = driver.find_element(
            By.XPATH, "//ul[@class='pagination']/li/a[text()='»']"
        )
        siguiente.click()

        # Esperar a que la nueva página cargue
        sleep(10)  # puedes ajustar este tiempo según sea necesario

        # Recolectar datos de la nueva página
        recolectar_animes()
    except Exception as e:
        print("No se encontró el botón 'Siguiente'. Fin de los resultados.")
        print(f"Error: {e}")
        break

# Espera indefinida para mantener el navegador abierto
input("Presiona Enter para cerrar el navegador...")

# Cerrar el driver (opcional)
driver.quit()
