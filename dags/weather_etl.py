from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import requests
import psycopg2
import os


# Retrieve API key from environment variable (set via Docker Compose)
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# List of 10 principal Moroccan cities with coordinates for accurate weather data
MOROCCAN_CITIES = [
    {"name": "Casablanca", "lat": 33.5731, "lon": -7.5898},
    {"name": "Rabat", "lat": 34.0209, "lon": -6.8416},
    {"name": "Fes", "lat": 34.0181, "lon": -5.0078},
    {"name": "Marrakech", "lat": 31.6295, "lon": -7.9811},
    {"name": "Tangier", "lat": 35.7595, "lon": -5.8340},
    {"name": "Agadir", "lat": 30.4278, "lon": -9.5981},
    {"name": "Meknes", "lat": 33.8935, "lon": -5.5473},
    {"name": "Oujda", "lat": 34.6814, "lon": -1.9086},
    {"name": "Kenitra", "lat": 34.2610, "lon": -6.5802},
    {"name": "Tetouan", "lat": 35.5889, "lon": -5.3626}
]


# Function to fetch current weather data from OpenWeatherMap
def fetch_weather(lat, lon, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    weather = {
        "city": city_name,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "date": datetime.utcnow().date()
    }
    return weather


# Function to connect to PostgreSQL and store weather data
def store_weather():
    import logging

    # Connect to PostgreSQL container (host is service name in Docker Compose)
    conn = psycopg2.connect(
        host="postgres",
        database= os.getenv("POSTGRES_DB"),
        user= os.getenv("POSTGRES_USER"),
        password= os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()

    for city in MOROCCAN_CITIES:
        try:
            # Fetch and log weather data
            weather = fetch_weather(city["lat"], city["lon"], city["name"])
            logging.info(f"Fetched weather for {city['name']}: {weather}")

            # Insert weather data into the weather table
            insert_query = """
            INSERT INTO weather (city, temperature, humidity, weather_description, date)
            VALUES (%s, %s, %s, %s, %s)
            """
            cur.execute(insert_query, (
                weather["city"],
                weather["temperature"],
                weather["humidity"],
                weather["description"],
                weather["date"]
            ))

            logging.info(f"Inserted weather for {city['name']} successfully.")
        except Exception as e:
            logging.error(f"Error with {city['name']}: {e}")

    conn.commit()
    cur.close()
    conn.close()


# Define Airflow DAG
default_args = {
    "start_date": datetime(2024, 1, 1),
}

# DAG definition: runs daily and triggers weather fetch/store task
with DAG(
    dag_id="weather_etl",
    schedule_interval="@daily",
    default_args=default_args,
    catchup=False
) as dag:
    
    store_weather_task = PythonOperator(
        task_id="store_weather",
        python_callable=store_weather
    )

    store_weather_task
