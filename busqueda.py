import re
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from anime import Anime

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
animes = driver.find_elements(By.XPATH, "//tr[@class='default']")

best_seeders = 0
choosen_one = Anime()
# Recolectar los datos de los animes
for anime in animes:
    # Extraemos el nombre del anime
    nombre = anime.find_element(
        By.XPATH, ".//td[@colspan='2']/a[not(@class='comments')]"
    ).text
    fansub = nombre.split("]")[0] + "]"

    # Extraemos la calidad usando una expresión regular
    calidad_match = re.search(r"(\d{3,4}p)", nombre)
    calidad = calidad_match.group(0) if calidad_match else "N/A"

    # Extraemos el episodio usando una expresión regular
    episodio_match = re.search(
        r"S\d{1,2}E(\d{1,2})| - (\d{1,2})|(?:\(\d{4}\))? - (\d{2})|(\d{2})(?=[^\d]|$)",
        nombre,
    )
    episodio = next((g for g in episodio_match.groups() if g is not None), "N/A")

    seeders = anime.find_element(By.XPATH, ".//td[@class='text-center'][4]").text
    torrent_link = anime.find_element(
        By.XPATH, ".//td[@class='text-center'][1]/a[2]"
    ).get_attribute("href")
    release_date = anime.find_element(By.XPATH, ".//td[@class='text-center'][3]").text


    if int(seeders) > best_seeders:
        best_seeders = int(seeders)
        choosen_one.update_info(name=nombre , fansub=fansub ,quality=calidad , chapter=episodio ,release_date=release_date , torrent_link=torrent_link , season='Summer' , year='2024'  )
        print(f"Nombre: {nombre}")
        print(f"Fansub: {fansub}")
        print(f"Calidad: {calidad}")
        print(f"Episodio: {episodio}")
        print(f"Seeders: {seeders}")
        print(f"Torrent link: {torrent_link}")
        print(f"Fecha de publicación: {release_date}")
        print("\n")


# Espera indefinida para mantener el navegador abierto

print(f"El anime con mas seeders es: {choosen_one.name}")

input("Presiona Enter descargar tu virus ;3 ...")


choosen_one.downloader()


driver.quit()
