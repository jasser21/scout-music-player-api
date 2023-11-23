## Tunisian Scout Music API
This Django REST API is designed to work with the Dropbox API to retrieve a list of songs from a Dropbox app and generate shared links for each song. The API is intended to be connected to a React frontend project that displays and plays music related to Tunisian Scout members.
## deployment details
* Deployment Platform: This Django REST API is deployed on Render.com, a cloud application hosting platform. The API utilizes a PostgreSQL database for data storage.
* API BaseURL :  [Tunisian Scout Music API](https://tunisian-scout-music-player-api.onrender.com)
* Database: PostgreSQL
## API Endpoints
The following endpoints are available:
* GET   /audioManger/get-auth-url : get the authentication url to authenticate to dropbox.
* POST  /audioManager/redirect : redirect from the dropbox site with the access_token and other details.
* GET /audio manager/is-authenticated: check if the user has successfully authenticated
* GET /audioManager/listit : Retrieves a list of songs from the connected Dropbox app.
* GET /get-song/{song_id} : Generates a shared link for the specified song.
## Features
* Retrieve a list of songs from a Dropbox app
* Generate shared links for each song
* Connects to a React frontend project for seamless integration and music playback
## React Frontend Application
To consume the Tunisian Scout Music API and display/play the music related to Tunisian Scout members, a React frontend application has been developed.

The React app is responsible for the following functionality:

* Connecting to the Tunisian Scout Music API to retrieve song lists and shared links
* Displaying and organizing the music albums and lyrics
* Providing an intuitive user interface for visitors to browse and listen to their favorite songs
The React frontend application is deployed separately and can be accessed using the following link : **[Tunisian Scout Music React App.](https://tunisian-scout-music-player-api.onrender.com)**
##  Contact Us 
If you have any questions, or feedback, or need assistance regarding the deployed API on Render.com, please don't hesitate to contact us:
Email: jasseramari21@gmail.com
Phone: +216 52 023 467
