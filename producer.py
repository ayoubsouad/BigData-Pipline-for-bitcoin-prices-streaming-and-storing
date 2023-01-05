import requests
from kafka import KafkaProducer
import json
import time

# Set up a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Set up the Binance API client
binance_api_key = 'UHp7lhuAGx*****************YkW3td20Xy54TMq1aOKwiUCwKZIZS3V5B21lv'
binance_api_secret = 'EOYmj*******************iLncpK1gFp6Me9EaxJAZBeY6i2xPkbix8FCrEJN'

# Set up an infinite loop to continuously fetch data from the Binance API and produce it to Kafka
while True:
  # Make a request to the Binance API and retrieve the JSON data
  response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",headers={'X-MBX-APIKEY': binance_api_key})
  data = response.json()

  # Produce the data to the Kafka topic
  data["price"]=float(data["price"])
  data=json.dumps(data).encode('utf-8')
  producer.send('binance-topic', value= data)
  producer.flush()
  
  time.sleep(5)
