-- Create airflow user if it doesn't exist (for compatibility)
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'airflow'
   ) THEN
      CREATE ROLE airflow WITH LOGIN PASSWORD 'airflow';
   END IF;
END
$$;

-- Create Airflow metadata database if it doesn't exist
SELECT 'CREATE DATABASE airflow'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'airflow')\gexec

-- Note: weather_db is created automatically by POSTGRES_DB env variable

-- Grant privileges on airflow database to airflow user
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

-- Grant privileges on weather_db database to airflow user
GRANT ALL PRIVILEGES ON DATABASE weather_db TO airflow;

-- Connect to weather_db to create tables there
\c weather_db;

-- Create weather table in the weather_db database
CREATE TABLE IF NOT EXISTS weather (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INTEGER,
    weather_description TEXT,
    date DATE
);

-- Grant privileges to airflow user on weather_db
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO airflow;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO airflow;
