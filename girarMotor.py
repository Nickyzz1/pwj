import RPi.GPIO as GPIO
import time

# Configuração dos pinos de controle
IN1 = 17  # GPIO 17
IN2 = 18  # GPIO 18
IN3 = 22  # GPIO 22
IN4 = 23  # GPIO 23

# Configuração do modo de numeração dos pinos
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Função para mover o motor 1 para frente
def motor1_frente():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

# Função para mover o motor 1 para trás
def motor1_tras():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)

# Função para mover o motor 2 para frente
def motor2_frente():
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Função para mover o motor 2 para trás
def motor2_tras():
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# Função para parar ambos os motores
def parar_motores():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Programa principal
try:
    while True:
        motor1_frente()  # Motor 1 para frente
        motor2_frente()  # Motor 2 para frente
        print("Motores girando para frente")
        time.sleep(2)

        motor1_tras()  # Motor 1 para trás
        motor2_tras()  # Motor 2 para trás
        print("Motores girando para trás")
        time.sleep(2)

        parar_motores()  # Parar os motores
        print("Motores parados")
        time.sleep(2)

except KeyboardInterrupt:
    print("Programa interrompido pelo usuário")

finally:
    GPIO.cleanup()  # Libera os pinos GPIO usados
