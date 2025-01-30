-- models/stg_telegram_data.sql
WITH raw_data AS (
    SELECT
        date,
        text,
        media_type
    FROM {{ source('raw', 'telegram_raw_data') }}
)

SELECT
    date,
    LOWER(TRIM(text)) AS text,  -- Clean and standardize text
    media_type
FROM raw_data
WHERE text IS NOT NULL  -- Remove rows with missing text
  AND LENGTH(text) > 5  -- Filter entries with text length > 5