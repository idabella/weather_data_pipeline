# 🌦️ Weather Data Pipeline with Airflow, Docker, Postgres & Metabase

This is an end-to-end data pipeline that fetches daily weather data for Moroccan cities using the OpenWeatherMap API, stores it in a PostgreSQL database via Apache Airflow, and visualizes it using Metabase.

---

## 🛠️ Tech Stack

- **Airflow** (ETL Orchestration)
- **PostgreSQL** (Data Warehouse)
- **Docker Compose** (Containerized Infra)
- **Metabase** (Visualization)
- **pgAdmin** (DB GUI)

---

## 🧱 Architecture Overview

<p align="center">
  <img src="images/project_architecture_diagram.png" alt="Project Architecture Diagram" width="85%">
</p>

The pipeline follows a classic ETL pattern:

1. **Extract**: Airflow DAG fetches weather data from OpenWeatherMap API for Moroccan cities
2. **Transform**: Data is processed and normalized within the Airflow tasks
3. **Load**: Cleaned data is inserted into PostgreSQL database
4. **Visualize**: Metabase connects to PostgreSQL for real-time dashboards

---

## 🚀 Features

- ✅ Fetches real-time weather data for major Moroccan cities using lat/lon coordinates
- ✅ Inserts weather data into a normalized Postgres schema
- ✅ Automates and schedules via Airflow DAGs
- ✅ Easy setup using Docker Compose
- ✅ Clean, interactive dashboard via Metabase
- ✅ Includes pgAdmin for database management

---

## 📊 Dashboard Preview

<p align="center">
  <img src="images/metabase_dashboard.png" alt="Metabase Weather Dashboard" width="90%">
</p>

The Metabase dashboard provides insights into:
- Current temperature trends across Moroccan cities
- Humidity and pressure measurements
- Weather conditions and forecasts
- Historical weather patterns

---

## 🧪 Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/chiranjeevi-sagi/weather-data-pipeline.git
cd weather-data-pipeline
```

### 2. Create your .env file
```bash
cp .env.example .env
```

Then open `.env` and update with your credentials:
- Set secure passwords for PostgreSQL, Airflow, and pgAdmin
- Replace `YOUR_API_KEY_HERE` with your OpenWeatherMap API key

**Get your API key**: Sign up at [OpenWeatherMap](https://openweathermap.org/current) and copy your API key from the dashboard.

### 3. Start the services
```bash
docker compose up --build
```

This will start all services: Airflow, PostgreSQL, pgAdmin, and Metabase.

### 4. Access the tools

| Service | URL | Default Credentials |
|---------|-----|---------------------|
| **Airflow** | http://localhost:8080 | Username/Password from `.env` |
| **pgAdmin** | http://localhost:5050 | Email/Password from `.env` |
| **Metabase** | http://localhost:3000 | Set up on first visit |

### 5. Run the Pipeline

1. Log into Airflow at http://localhost:8080
2. Enable the weather data DAG
3. Trigger the DAG manually or wait for the scheduled run
4. Monitor the task execution in the Airflow UI

### 6. Set Up Metabase

1. Navigate to http://localhost:3000
2. Complete the initial setup wizard
3. Connect to PostgreSQL database using credentials from `.env`:
   - Host: `postgres` (Docker service name)
   - Port: `5432`
   - Database: `weather_db`
4. Create your dashboard and visualizations

---

## 📁 Project Structure

```
weather-data-pipeline/
├── dags/                    # Airflow DAG definitions
├── images/                  # Architecture and dashboard images
│   ├── project_architecture_diagram.png
│   └── metabase_dashboard.png
├── docker-compose.yml       # Docker services configuration
├── .env.example            # Environment variables template
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

---


## 🎯 Next Steps

- Add more cities or countries to the data pipeline
- Implement data quality checks
- Add alerting for extreme weather conditions
- Create additional visualizations for weather trends
- Schedule automated reports

---

## 📝 License

This project is open source and available under the MIT License.

---


**Congratulations on completing your ETL project!** 🎉

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/chiranjeevi-sagi/weather-data-pipeline/issues).

## ⭐ Show Your Support

Give a ⭐️ if this project helped you learn about data pipelines!