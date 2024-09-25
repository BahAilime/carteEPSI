
import qrcode   
import os

spots = [["Accueil", 0], ["Escalier_nord", 1], ["Escalier_nord", 2], ["Escalier_nord", 3], ["Escalier_sud", 1], ["Escalier_sud", 2], ["Escalier_sud", 3], ["Salle_100", 1], ["Face105", 1], ["face205", 2], ["Salle200", 2], ["Salle300", 3], ["Face304", 3]]
newspot = True

qr_folder = "QR_folder"
if not os.path.exists(qr_folder):
    os.makedirs(qr_folder)

for spot in spots:
    nomSpot = spot[0]
    numeroEtage = spot[1]
    full_url = f"https://bahailime.github.io/carteEPSI?etage={numeroEtage}&spot={nomSpot}/"
    img = qrcode.make(full_url)
    img.save(f"{qr_folder}/qr_spot_{spot[0]}_{spot[1]}.png")
    print(f"QR codes générés et enregistrés dans le dossier '{qr_folder}'.")




