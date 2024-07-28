import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime

# prueba de paginación

# Ruta del ejecutable de ChromeDriver
chrome_driver_path = "./chromedriver.exe"

# Configuramos el servicio de ChromeDriver
service = Service(executable_path=chrome_driver_path)

# Inicializamos el driver de Chrome
driver = webdriver.Chrome(service=service)

# Solicitar la búsqueda al usuario
# busqueda = input("¿Qué anime quieres buscar? ")

# Construir la URL de búsqueda
url_busqueda = f"https://nyaa.si"

# Página donde queremos hacer el scraping
driver.get(url_busqueda)

# Obtener la fecha actual
hoy = datetime.now().strftime("%Y-%m-%d")
print(f"Fecha actual: {hoy}")

# Función para recolectar los datos de los animes en la página actual
def recolectar_animes():
    animes = driver.find_elements(By.XPATH, "//tr[@class='default']")
    print(f"Animes encontrados: {len(animes)}")
    for anime in animes:
        # Extraemos el nombre del anime
        release_date = anime.find_element(By.XPATH, ".//td[@class='text-center'][3]").text
        if release_date.startswith(hoy):
            nombre = anime.find_element(
                By.XPATH, ".//td[@colspan='2']/a[not(@class='comments')]"
            ).text            
            print(f"Nombre: {nombre}")
            print(f"Fecha de lanzamiento: {release_date}")
            print("\n")
        else:
            return False
    return True


# Recolectar datos de la primera página
continuar = recolectar_animes()

# Navegar a través de todas las páginas de resultados
pagina = 2
while continuar:
    try:
        # Intentar encontrar y hacer clic en el botón "Siguiente"
        print(f"Pagina: {pagina}")
        siguiente = driver.find_element(
            By.XPATH, "//ul[@class='pagination']/li/a[text()='»']"
        )
        siguiente.click()

        # Esperar a que la nueva página cargue
        sleep(2)  # puedes ajustar este tiempo según sea necesario

        # Recolectar datos de la nueva página
        pagina += 1
        continuar = recolectar_animes()
    except Exception as e:
        print("No se encontró el botón 'Siguiente'. Fin de los resultados.")
        print(f"Error: {e}")
        break

# Espera indefinida para mantener el navegador abierto
input("Presiona Enter para cerrar el navegador...")

# Cerrar el driver (opcional)
driver.quit()
