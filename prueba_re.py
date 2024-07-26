import re

# Expresión regular para encontrar el episodio
episodio_pattern = re.compile(
    r"S(?:\d{1,2})?E(\d{1,2})|(?:S\d{1,2} - )(\d{1,2})|(?: - )(\d{1,2})|(\d{2})(?:[^\d]|$)"
)

# Ejemplos de nombres
nombres = [
    "[DantalianSubs] Oshi no Ko S2 - 03 [1080p HEVC] (Sub. Español)",
    "[HispaMux] Oshi no Ko S02E03 [1080p DSNP WEB-DL E-AC3] [Sub. Español]",
    "[Oshit] Oshi no Ko (2024) - 04 (WEB 720p) (Sub. Español)",
    "Oshi.No.Ko.S02E04.2160p.B-Global.WEB-DL.AAC2.0.H.264-NanDesuKa.mkv",
]

# Recolectar el número de episodio
for nombre in nombres:
    match = episodio_pattern.search(nombre)
    print("match: ", match)
    if match:
        episodio = next(group for group in match.groups() if group is not None)
        print(f"Nombre: {nombre}")
        print(f"Episodio: {episodio}")
    else:
        print(f"Nombre: {nombre}")
        print("Episodio: No encontrado")
    print("\n")
