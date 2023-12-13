#!/usr/bin/env python
# coding: utf-8

# <div align="right" style=" font-size: 80%; text-align: center; margin: 0 auto">
# <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ExploreAI_logos/Logo blue_dark.png"  style="width:25px" align="right";/>
# </div>

# # SQL Exam
# © ExploreAI Academy

# ## Instructions to students
# 
# This challenge is designed to determine how much you have learned so far and will test your knowledge on SQL.
# 
# The answers for this challenge should be selected on Athena for each corresponding multiple-choice question. The questions are included in this notebook and are numbered according to the Athena questions. The options for each question have also been included.
# 
# Do not add or remove cells in this notebook. Do not edit or remove the `%%sql` comment as it is required to run each cell.
# 
# **_Good luck!_**

# ## Honour code
# 
# I, YOUR NAME YOUR SURNAME, confirm – by submitting this document – that the solutions in this notebook are a result of my own work and that I abide by the EDSA honour code (https://drive.google.com/file/d/1QDCjGZJ8-FmJE3bZdIQNwnJyQKPhHZBn/view?usp=sharing).
# 
# Non-compliance with the honour code constitutes a material breach of contract.

# ## The TMDb database
# 
# In this supplementary exam, you will be exploring [The Movie Database](https://www.themoviedb.org/) – an online movie and TV show database that houses some of the most popular movies and TV shows at your fingertips. The TMDb database supports 39 official languages used in over 180 countries daily and dates back all the way to 2008. 
# 
# 
# <img src="https://github.com/Explore-AI/Pictures/blob/master/sql_tmdb.jpg?raw=true" width=80%/>
# 
# 
# Below is an Entity Relationship Diagram (ERD) of the TMDb database:
# 
# <img src="https://github.com/Explore-AI/Pictures/blob/master/TMDB_ER_diagram.png?raw=true" width=70%/>
# 
# As can be seen from the ERD, the TMDb database consists of `12 tables` containing information about movies, cast, genre, and so much more.  
# 
# Let's get started!

# ## Loading the database
# 
# Before you begin, you need to prepare your SQL environment.  You can do this by loading the magic command `%load_ext sql`.

# In[25]:


# Load and activate the SQL extension to allow us to execute SQL in a Jupyter notebook. 
# If you get an error here, make sure that mysql and pymysql are installed correctly. 

get_ipython().run_line_magic('load_ext', 'sql')


# Next, go ahead and load your database. To do this, you will need to ensure you have downloaded the `TMDB.db` sqlite file from Athena and have stored it in a known location.

# In[26]:


# Establish a connection to the local database using the '%sql' magic command.
# Replace 'password' with our connection password and `db_name` with our database name. 
# If you get an error here, please make sure the database name or password is correct.

get_ipython().run_line_magic('sql', 'sqlite:///TMDB-a-4006.db')


# If the above line didn't throw out any errors, then you should be good to go. Good luck with the exam! 

# ## Questions on SQL
# 
# Use the given cell below each question to execute your SQL queries to find the correct input from the options provided. Your solution should match one of the multiple-choice questions on Athena.

# ### Question 1
# 
# Who won the Oscar for “Actor in a Leading Role” in  2015?
# 
# (Hint: The winner is indicated as '1.0'.)
# 
# **Options:** 
# 
#   - Micheal Fassbender
#   - Natalie Portman
#   - Leonardo DiCaprio
#   - Eddie Redmayne
# 

# In[54]:


get_ipython().run_cell_magic('sql', '', '\nSELECT name\nFROM oscars\nWHERE award = "Actor in a Leading Role" and year = 2015 and winner = 1.0; \n')


# ### Question 2
# 
# What query will produce the ten oldest movies in the database?
# 
# **Options:**
# 
#  - SELECT TOP(10) * FROM movies WHERE release_date ORDER BY release_date ASC
# 
#  - SELECT  * FROM movies WHERE release_date IS NOT NULL ORDER BY release_date ASC LIMIT 10
# 
#  - SELECT * FROM movies WHERE release_date IS NOT NULL ORDER BY release_date DESC LIMIT 10
# 
#  -  SELECT * FROM movies WHERE release_date IS NULL ORDER BY release_date DESC LIMIT 10

# In[55]:


get_ipython().run_cell_magic('sql', '', 'SELECT  * \nFROM movies \nWHERE release_date IS NOT NULL \nORDER BY release_date ASC \nLIMIT 10;\n')


# ### Question 3
# 
# How many unique awards are there in the Oscars table?
# 
# **Options:**
#  - 141
#  - 53 
#  - 80
#  - 114

# In[56]:


get_ipython().run_cell_magic('sql', '', 'SELECT \nCOUNT(DISTINCT award) AS num_of_unique_awards\nFROM oscars;\n')


# ### Question 4
# 
# How many movies are there that contain the word “Spider” within their title?
# 
# **Options:**
#  - 0
#  - 5
#  - 1
#  - 9

# In[91]:


get_ipython().run_cell_magic('sql', '', 'SELECT \nCOUNT(title) AS num_of_movies_in_that\nFROM movies\nWHERE title LIKE "%Spider%";\n')


# ### Question 5
# 
# How many movies are there that are both in the "Thriller" genre and contain the word “love” anywhere in the keywords?
# 
# 
# **Options:**
#  - 48
#  - 38
#  - 14
#  - 1

# In[272]:


get_ipython().run_cell_magic('sql', '', "SELECT COUNT(DISTINCT m.movie_id) AS movie_count\nFROM movies m\nJOIN genremap gm ON m.movie_id = gm.movie_id\nJOIN genres g ON gm.genre_id = g.genre_id\nJOIN keywordmap km ON m.movie_id = km.movie_id\nJOIN keywords k ON km.keyword_id = k.keyword_id\nWHERE g.genre_name = 'Thriller' AND LOWER(k.keyword_name) LIKE '%love%';\n")


# ### Question 6
# 
# How many movies are there that were released between 1 August 2006 ('2006-08-01') and 1 October 2009 ('2009-10-01') that have a popularity score of more than 40 and a budget of less than 50 000 000?
# 
#  
# **Options:**
# 
#  - 29
#  - 23
#  - 28
#  - 35

# In[185]:


get_ipython().run_cell_magic('sql', '', 'select count(movie_id) as num_of_movies\nfrom movies\nwhere \n(release_date between "2006-08-01" and "2009-10-01")\nand \npopularity > 40\nand\nbudget < 50000000;\n')


# ### Question 7
# 
# How many unique characters has "Vin Diesel" played so far in the database?
# 
# **Options:**
#  - 24
#  - 19
#  - 18
#  - 16

# In[186]:


get_ipython().run_cell_magic('sql', '', 'SELECT actors.actor_name , count (distinct casts.characters) as Unique_Chars\nfrom actors\nright join casts\non actors.actor_id = casts.actor_id\nwhere actor_name = "Vin Diesel";\n')


# ### Question 8
# 
# What are the genres of the movie “The Royal Tenenbaums”?
# 
# 
# **Options:**
#  - Action, Romance
#  - Drama, Comedy
#  - Crime, Thriller
#  - Drama, Romance

# In[187]:


get_ipython().run_cell_magic('sql', '', 'SELECT movies.title ,genres.genre_name\nFROM movies\nLEFT JOIN genremap\nON movies.movie_id = genremap.movie_id\nLEFT JOIN genres\nON genremap.genre_id = genres.genre_id\nwhere title = "The Royal Tenenbaums"\ngroup by genre_name;\n')


# ### Question 9
# 
# What are the three production companies that have the highest movie popularity score on average, as recorded within the database?
# 
# 
# **Options:**
# 
#  - MCL Films S.A., Turner Pictures, and George Stevens Productions
#  - The Donners' Company, Bulletproof Cupid, and Kinberg Genre
#  - Bulletproof Cupid, The Donners' Company, and MCL Films S.A
#  - B.Sting Entertainment, Illumination Pictures, and Aztec Musique

# In[191]:


get_ipython().run_cell_magic('sql', '', 'SELECT movies.popularity , productioncompanies.production_company_name ,AVG(popularity) AS avg_popularity\nfrom movies\nright join productioncompanymap\non movies.movie_id = productioncompanymap.movie_id\nleft join productioncompanies\non productioncompanymap.production_company_id = productioncompanies.production_company_id\nGROUP BY production_company_name\nORDER BY avg_popularity desc\nlimit 3;\n')


# ### Question 10
# 
# How many female actors (i.e. gender = 1) have a name that starts with the letter "N"?
# 
# 
# **Options:**
# 
#  - 0
#  - 355
#  - 7335
#  - 1949

# In[204]:


get_ipython().run_cell_magic('sql', '', 'select count(*) AS f_count\nfrom actors\nwhere gender = 1\nand\nactor_name like "N%";\n')


# ### Question 11
# 
# Which genre has, on average, the lowest movie popularity score? 
# 
# 
# **Options:**
# 
#  - Science Fiction
#  - Animation
#  - Documentary
#  - Foreign

# In[273]:


get_ipython().run_cell_magic('sql', '', 'SELECT genre_name, AVG(popularity) AS avg_popularity\nFROM movies\nJOIN genremap ON movies.movie_id = genremap.movie_id\nJOIN genres ON genremap.genre_id = genres.genre_id\nGROUP BY genre_name\nORDER BY avg_popularity ASC\nLIMIT 1;\n')


# ### Question 12
# 
# Which award category has the highest number of actor nominations (actors can be male or female)? (Hint: `Oscars.name` contains both actors' names and film names.)
# 
# **Options:**
# 
# - Special Achievement Award
# - Actor in a Supporting Role
# - Actress in a Supporting Role
# - Best Picture
# 
# 

# In[290]:


get_ipython().run_cell_magic('sql', '', "SELECT award, COUNT(*) AS nomination_count\nFROM oscars\nWHERE award LIKE '%actor%'\n   OR award LIKE '%actress%'\nGROUP BY award\nORDER BY nomination_count DESC\nLIMIT 2;\n")


# ### Question 13
# 
# For all of the entries in the Oscars table before 1934, the year is stored differently than in all the subsequent years. For example, the year would be saved as “1932/1933” instead of just “1933” (the second indicated year).  Which of the following options would be the appropriate code to update this column to have the format of the year be consistent throughout the entire table (second indicated year only shown)?
# 
# 
# **Options:**
# 
# - `UPDATE Oscars SET year = RIGHT(year, -4)`
# - `UPDATE Oscars SET year = SELECT substr(year, -4)`
# - `UPDATE Oscars SET year = substr(year, -4)`
# - `UPDATE Oscars year =  substr(year, 4)`

# In[292]:


UPDATE Oscars SET year = substr(year, -4)


# ### Question 14
# 
# DStv will be having a special week dedicated to the actor Alan Rickman. Which of the following queries would create a new _view_ that shows the titles, release dates, taglines, and overviews of all movies that Alan Rickman has played in?
# 
# 
# 
# **Options:**
# 
# - SELECT title, release_date, tagline, overview 
# FROM Movies LEFT JOIN Casts ON Casts.movie_id = Movies.movie_id Left JOIN Actors ON Casts.actor_id = Actors.actor_id 
# WHERE Actors.actor_name = 'Alan Rickman'
# AS VIEW Alan_Rickman_Movies
# 
# - CREATE VIEW Alan_Rickman_Movies AS  
# SELECT title, release_date, tagline, overview FROM Movies  
# LEFT JOIN Casts ON Casts.movie_id = Movies.movie_id Left JOIN Actors
# ON Casts.actor_id = Actors.actor_id
# WHERE Actors.actor_name = 'Alan Rickman' 
# 
# 
# - CREATE NEW VIEW  Name  = Alan_Rickman_Movies AS SELECT title, release_date, tagline, overview FROM Movies LEFT JOIN Casts ON Casts.movie_id = Movies.movie_id Left JOIN Actors ON Casts.actor_id = Actors.actor_id WHERE Actors.actor_name = 'Alan Rickman'
# 
# - VIEW Alan_Rickman_Movies AS SELECT title, release_date, tagline, overview FROM Movies LEFT JOIN Casts ON Casts.movie_id = Movies.movie_id Left JOIN Actors ON Casts.actor_id = Actors.actor_id WHERE Actors.actor_name = 'Alan Rickman'

# In[285]:


CREATE VIEW Alan_Rickman_Movies AS
SELECT title, release_date, tagline, overview FROM Movies
LEFT JOIN Casts ON Casts.movie_id = Movies.movie_id Left JOIN Actors ON Casts.actor_id = Actors.actor_id WHERE Actors.actor_name = 'Alan Rickman'


# ### Question 15
# 
# Which of the statements about database normalisation are true?
# 
# **Statements:**
#  
# i) Database normalisation improves data redundancy, saves on storage space, and fulfils the requirement of records to be uniquely identified.
# 
# ii) Database normalisation supports up to the Third Normal Form and removes all data anomalies.
# 
# iii) Database normalisation removes inconsistencies that may cause the analysis of our data to be more complicated.
# 
# iv) Database normalisation increases data redundancy, saves on storage space, and fulfils the requirement of records to be uniquely identified.
# 
# **Options:**
# 
#  - (i) and (ii)
#  - (i) and (iii)
#  - (ii) and (iv)
#  - (iii) and (iv)

# In[ ]:


(i) and (iii)


# #  
# 
# <div align="center" style=" font-size: 80%; text-align: center; margin: 0 auto">
# <img src="https://raw.githubusercontent.com/Explore-AI/Pictures/master/ExploreAI_logos/EAI_Blue_Dark.png"  style="width:200px";/>
# </div>
