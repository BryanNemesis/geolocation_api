# Geolocation API
An API for retrieving and storing geolocation data for IP addresses from ipstack.com.
## Authentication
All API endpoints are authenticated via JWT access token.

To obtain a token, visit the /register/ url to create a user.
Then, send a POST request with the following content to /api/token/:
```
{
    "username": <username>,
    "password": <password>
}
```
Use the obtained access token preceded by text 'Bearer' in the 'Authorization' header of your requests, like this:
```
curl http://127.0.0.1:8000/api/list/ -Headers "Authorization: Bearer eyJ0eXAiOiJK[...]"
```
## Available endpoints
### /store/\<ip>
* allowed methods: POST

Retrieves data for the given IP address and stores it in the database, if it's not there already.
### /detail/\<ip>
* allowed methods: GET

Shows geolocation data for a given IP, if it's saved in the database.
### /list/
* allowed methods: GET

Shows all saved geolocation data.

### /delete/\<ip>/
* allowed methods: DELETE

Deletes saved data for a given IP.
 
