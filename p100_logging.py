import logging

# Muss ausgeführt werden bevor die erste Log Nachricht abgeschickt wird
logging.basicConfig(level=logging.DEBUG, filename='test.log')

logging.warning('Eine Warnung')
logging.info('Eine Info Nachricht')
