import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
print(url_busqueda)
# Queremos buscar animes
animes = driver.find_elements(
    By.XPATH, "//tr[@class='default']"
)  # animes almacenará una lista

# Recolectar los datos de los animes
for anime in animes:
    # Extraemos el nombre del anime
    nombre = anime.find_element(
        By.XPATH, ".//td[@colspan='2']/a[not(@class='comments')]"
    ).text
    fansub = nombre.split("]")[0] + "]"
    seeders = anime.find_element(By.XPATH, ".//td[@class='text-center'][4]").text
    torrent_link = anime.find_element(
        By.XPATH, ".//td[@class='text-center'][1]/a"
    ).get_attribute("href")
    release_date = anime.find_element(By.XPATH, ".//td[@class='text-center'][3]").text
    print(f"nombre: {nombre}")
    print(f"fansub: {fansub}")
    print(f"seeders: {seeders}")
    print(f"torrent link: {torrent_link}")
    print(f"release date: {release_date}")
    print("\n")

# Espera indefinida para mantener el navegador abierto
input("Presiona Enter para cerrar el navegador...")

# Cerrar el driver (opcional)
driver.quit()
