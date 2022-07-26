import shutil
import os

utilisateur = os.getlogin()
print ("Utilisateur: " + utilisateur)

pathTest = rf"C:\Users\{utilisateur}\AppData\Local\FiveM\FiveM.app\data\cache"

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")

pathTest = rf"C:\Users\{utilisateur}\AppData\Local\FiveM\FiveM.app\data\nui-storage"

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")



pathTest = rf"C:\Users\{utilisateur}\AppData\Local\FiveM\FiveM.app\data\server-cache"

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")



pathTest = rf"C:\Users\{utilisateur}\AppData\Local\FiveM\FiveM.app\data\server-cache-priv"

try:
    shutil.rmtree(pathTest)
except OSError as e:
    print(e)
else:
    print("The directory is deleted successfully")


input ("Entrer pour quitter")
