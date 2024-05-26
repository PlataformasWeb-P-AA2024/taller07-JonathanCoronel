from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()
# acceder al archivo
archivo = open('data/datos_clubs.txt', "r")

# obtener las líneas del archivo
data = archivo.readlines()
archivo.close()

# se crea los objetos de tipo Club 
for lineas in data:
    nombreClub, deporteClub, fundacionClub = lineas.strip().split(';')
    club = Club(nombre=nombreClub, deporte=deporteClub, \
        fundacion=fundacionClub)
    session.add(club)

session.commit()
# acceder al archivo
archivo2 = open('data/datos_jugadores.txt', "r")

# obtener las líneas del archivo
data2 = archivo2.readlines()
archivo2.close()
# Se crean objetos de tipo Jugador
for lineas2 in data2:
    clubJuga, posicionJuga, dorsalJuga, nombreJuga  = lineas2.strip().split(';')
    #Buscar el club correspondiente en la base de datos
    club = session.query(Club).filter_by(nombre=clubJuga).one()
    jugador = Jugador(nombre =nombreJuga, dorsal=dorsalJuga, posicion=posicionJuga, \
        club=club)
    session.add(jugador)
session.commit()