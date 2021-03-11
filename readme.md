# Geolocation API
An API for retrieving and storing geolocation data for IP addresses from ipstack.com.

Available at http://safe-crag-58806.herokuapp.com/.

## Authentication
All API endpoints are authenticated via JWT access token.

To obtain a token, visit the /register/ url to create a user (or use an already existing user with credentials user/pass).
Then, send a POST request with the following JSON content to /api/token/:
```
{
  "username":"<username>",
  "password":"<password>"
}
```
Use the obtained access token preceded by text 'Bearer' in the 'Authorization' header of your requests, like this:
```
curl http://127.0.0.1:8000/api/list/ -H "Authorization: Bearer eyJ0eXAiOiJK[...]"
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

## Local deployment
To deploy the API locally, follow these steps:

* clone the repo and cd into its folder:
```
git clone https://github.com/BryanNemesis/cars_api.git
cd cars_api
```
* build and run the container using the included dockerfile. Use a randomly generated string for the key value (you can use http://www.unit-conversion.info/texttools/random-string-generator/):
```
docker build -t web:latest .
docker run -d --name geolocation_api -e "PORT=8765" -e "DEBUG=0" -e "SECRET_KEY=<key>" -p 8008:8765 web:latest gunicorn geolocation_api.wsgi:application --bind 0.0.0.0:8765
```
The API will be accessible under http://localhost:8008/.
 