import tldextract
import socket
import dns
import dns.resolver

#txt = raw_input("Introduzca el Archivo TXT:\n")

enfila = open("dominios.txt", 'r')
output = open("salida.txt", "w")


infile = enfila.readlines()

for line in infile:
    try:
        linesremplazadas = line.replace("\n","")
        #if line[-1] == "\n":
            #dato = line[:-1]
        #if lines[0:7] == "http://":
            #print lines[7:]
        linesremplazadas = linesremplazadas.replace("http://","")
        linesremplazadas = linesremplazadas.replace("https://","")
        linesremplazadas = linesremplazadas.replace("/","")

        print linesremplazadas
        dnssalida = socket.gethostbyname(linesremplazadas)

        angel = linesremplazadas +","+ dnssalida +"\n"

        output.write(angel)
    except (RuntimeError, socket.gaierror):

        angel_error = linesremplazadas + "," + "----" + "\n"
        print angel_error
        output.write(angel_error)



enfila.close()
