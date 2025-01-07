# Music Genre Categorization Model

This k-nearest neighbors classification machine learning model intakes 10 features of a song (danceability, energy, key, loudness, speechiness, acousticness, instrumentalness, liveness, valence, and tempo) and predicts the genre of a song.

## Training and Testing

A labeled data set containing the artist, title, genre, and features of over 2000 songs was used to create the model. 80% of the data was used to train the model, and the remaining 20% was used to test the model. The model predicted genres with an accuracy of 68.5%.

## Web Application

The model is loaded to a web application that allows the user to search for any song, input it into the model, and obtain the predicted genre. A widget with the user's inputted song title, artist, album cover, and sample of the music is also displayed on the resulting page.

## Technologies

The libraries NumPy, Matplotlib, Pandas, TensorFlow, and Scikit-learn were used to create the model. The web application utilizes Spotify API to retrieve song data from Spotify's database, HTML and CSS to style the webpage, and Python Flask backend architecture with server side rendering to deploy the application through Render.

Link to the web application: https://kyla-shivani-music-genre-categorization.onrender.com
