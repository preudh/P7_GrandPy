# GrandpyBot - Project 7

## Description

Web application developed during the Python developer training with OpenClassrooms. This application allows users to find the address of a place by inputting a message. It then displays a map and a summary of the location. The user's message is parsed to extract key information. Interactions are executed via AJAX: users submit their question by pressing "Enter", and the response is displayed directly on the screen without a reload. The Google Maps API and the Media Wiki API are leveraged to fetch the data. Nothing is saved. If users refresh the page, the entire history is lost. GrandPyBot has a range of diverse response phrases to make the interaction dynamic and engaging.

## Usage

The project is deployed on Heroku: [Heroku Deployment](https://p7grandpy-811172f837bb.herokuapp.com/)

For local usage:
1. Fork and clone this repository.
2. Install the dependencies using `pip install -r requirements.txt`.
3. Launch the project with `python main.py` (remember to configure your Google Map API key).

## Resources and Guides:

### Back-end
- [Flask Documentation](https://flask.palletsprojects.com/en/1.1.x/)
- **Test-Driven Development (TDD)**
  - [TestDrivenDevelopment by Martin Fowler](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
  - [Unittest - Official Python Documentation](https://docs.python.org/fr/3.7/library/unittest.html)

### Front-end
- [Bootstrap - Introduction](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [JavaScript Introduction - W3Schools](https://www.w3schools.com/js/js_intro.asp)
- [AJAX Introduction - W3Schools](https://www.w3schools.com/xml/ajax_intro.asp)
- [HTML Introduction - W3Schools](https://www.w3schools.com/html/default.asp)
- [CSS Introduction - W3Schools](https://www.w3schools.com/css/default.asp)

### API
- [Google Maps API Documentation](https://developers.google.com/maps/documentation)
- [google-maps-services-python on GitHub](https://github.com/googlemaps/google-maps-services-python)
- [Wikipedia Python Package](https://pypi.org/project/wikipedia/)

### Deployment
- [Getting started with Python on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)

## Support

For any questions or support, please contact me at: preudhomme.patrice@gmail.com

## Roadmap:

In future releases, the Chatbot could integrate Natural Language Processing (NLP) capabilities to better recognize the intent behind queries and assist users accordingly. Additionally, there's potential for data storage to refine and improve interactions.




