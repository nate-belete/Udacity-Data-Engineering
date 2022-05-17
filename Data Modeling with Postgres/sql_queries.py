# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fct_songplays"
user_table_drop = "DROP TABLE IF EXISTS dim_users"
song_table_drop = "DROP TABLE IF EXISTS dim_songs"
artist_table_drop = "DROP TABLE IF EXISTS dim_artists"
time_table_drop = "DROP TABLE IF EXISTS dim_time"

# CREATE TABLES

songplay_table_create = ("""
                            CREATE TABLE IF NOT EXISTS fct_songplays(
                                songplay_id SERIAL PRIMARY KEY, 
                                start_time TIMESTAMP, 
                                user_id INT, 
                                level VARCHAR, 
                                song_id VARCHAR, 
                                artist_id VARCHAR, 
                                session_id VARCHAR, 
                                location TEXT, 
                                user_agent VARCHAR
                                )
                        """)

user_table_create = ("""
                            CREATE TABLE IF NOT EXISTS dim_users(
                                user_id INT PRIMARY KEY,
                                first_name VARCHAR, 
                                last_name VARCHAR, 
                                gender VARCHAR, 
                                level TEXT
                            )
""")

song_table_create = ("""
                            CREATE TABLE IF NOT EXISTS dim_songs(
                                song_id VARCHAR PRIMARY KEY, 
                                title VARCHAR, 
                                artist_id VARCHAR NOT NULL, 
                                year INT, 
                                duration FLOAT

                            )
""")

artist_table_create = ("""
                            CREATE TABLE IF NOT EXISTS dim_artists(
                                artist_id VARCHAR PRIMARY KEY,
                                name VARCHAR, 
                                location VARCHAR, 
                                latitude FLOAT, 
                                longitude FLOAT

                            )
""")

time_table_create = ("""                            
                            CREATE TABLE IF NOT EXISTS dim_time(
                                start_time TIMESTAMP PRIMARY KEY, 
                                hour INT, 
                                day INT, 
                                week INT, 
                                month INT, 
                                year INT, 
                                weekday VARCHAR

                            )

""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO fct_songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO dim_users (user_id, first_name, last_name, gender, level)
    VALUES (%s,%s,%s,%s,%s)
     ON CONFLICT (user_id) 
       DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO dim_songs (song_id, title, artist_id, year, duration)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (song_id) DO NOTHING
    
""")

artist_table_insert = ("""
    INSERT INTO dim_artists (artist_id, name, location, latitude, longitude)
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""
    INSERT INTO dim_time (start_time, hour, day, week, month, year, weekday)
    VALUES (%s,%s,%s,%s,%s,%s,%s)
    ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
song_select = ("""
    select
        tb2.song_id,
        tb2.artist_id
        
    from dim_songs as tb2
    join dim_artists as tb3
     on tb2.artist_id = tb3.artist_id
    where tb2.title = %s
     and tb3.name = %s
     and tb2.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

print('it worked')