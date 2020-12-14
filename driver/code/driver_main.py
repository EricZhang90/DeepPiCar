from deep_pi_car import DeepPiCar
import logging
import sys

def main():
    # print system info
    logging.info('Starting DeepPiCar, system info: ' + sys.version)
    
    with DeepPiCar() as car:
        car.drive(25)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
