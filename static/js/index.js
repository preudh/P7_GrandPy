/* Main JavaScript file */
/* The getElementById() method returns the element that has the ID attribute in the HTML with the specified value.
input id="input", Variables defined with const behave like let variables, except they cannot be reassigned */
const input = document.getElementById("input");
// div id="container"> contain all answers and google map
let container = document.getElementById("container");
const button = document.getElementById("button-addon2");
const spinner = document.getElementById('spinner');


const displayInputValue = () => {
    /* Display the user's input value
    the variable const is used as an arrow function without parameters written with a couple of parentheses
    The function is an anonymous function (i.e a function without a name)
    create dynamically div element and assigns it to div variable */
    if (input.value !== '') {
        let div = document.createElement("div");
        //setAttribute to div variable (attribute name, attribute value)
        div.setAttribute("id", "input_value");
        // attach the div element to the document body (container) to make it visible on the screen
        container.appendChild(div);
        // change the HTML content of a div element with input value
        div.innerHTML = input.value;
        // reset user input
        input.value = '';
        // The setTimeout() method calls a function or evaluates an expression after a specified number of milliseconds.delay scrolling
        setTimeout(function () {
            div.scrollIntoView({behavior: "smooth"});
        }, 100);
    }
}

//answer as a parameter is a json (dictionary) built in view.py with responses from parser, wiki API and google map API
const displayAddress = (answer) => {
    /* Display address from google
    create dynamically div element and assigns it to div1 variable */
    let div1 = document.createElement("div");
    div1.setAttribute("id", "address");
    container.appendChild(div1);
    /* answer is dictionary created in view.py
     address is the key for bot messages and address is the key for ggmap['address'] ie. 'formatted_address' */
    div1.innerHTML = answer['chat_address_ok'] + answer['address'];
}

const messageError = (answer) => {
    //Return a random sentence when no result is found, see view.py
    let div = document.createElement("div");
    div.setAttribute("id", "address");
    div.innerHTML = answer['chat_address_ko'];

    container.appendChild(div);

}

const displayWiki = (answer) => {
    //Display Wikipedia article
    let div2 = document.createElement("div");
    div2.setAttribute("id", "wiki");
    container.appendChild(div2);
    // change the HTML content of div2 element with the keys wik_ko of the dictionary answer in view.py
        if (answer['wik_ko'] === undefined)
        div2.innerHTML = answer['wik_ok'] + answer['sum'];
    else
     div2.innerHTML = answer['wik_ko'];
}

const messageErrorWiki = (answer) => {
    //Displayed if no answers are found
    let div4 = document.createElement("div");
    // div4.setAttribute("id", "address");
    div4.setAttribute("id", "wiki");
    //Return a random sentence when no result is found in wiki, see view.py
    div4.innerHTML = answer['wiki_ko'];
    container.appendChild(div4);
}

const initMap = (lat, lng) => {
    //Display the google's map
    let div3 = document.createElement("div");
    //setAttribute to div3, ie <div id="map"></div>
    div3.setAttribute("id", "map");
     // attach the div3 element to the document body (container) to make it visible on the screen
    container.appendChild(div3);
    /* create dictionary and affect to variable place with answer dictionary keys values : 'lat': ggmap['latitude'],
     'lng': ggmap['longitude']*/
    let place = {lat: lat, lng: lng};
    /* create an variable named "map" to hold the map.
     JavaScript function that creates a map in the map variable.
     two required options for every map: center and zoom.
     zoom is the initial resolution at which to display the map.
     center contains the lat & lng, in our case the above dictionary place
     new = constructor =  specify method that allows to create an object */
    let map = new google.maps.Map(div3, {zoom: 10, center: place});
    /* A marker identifies a location on a map. The google.maps.Marker constructor takes a single Marker options object
    position (required) specifies a Lat/Lng identifying the initial location of the marker
    map (optional) specifies the Map on which to place the marker */
    let marker = new google.maps.Marker({position: place, map: map});
}

const emptyInput = () => {
    //Displayed if user validated without writing anything
    let div = document.createElement("div");
    div.setAttribute("id", "address");
    container.appendChild(div);
    div.innerHTML = "Merci de saisir un lieu!";// ok
}

const grandybot = () => {
    //Main function for displaying answers
    if (input.value == ""){
        displayInputValue();// 2 function calls
        emptyInput();
    }
    else{
        let request = new XMLHttpRequest(); // The XMLHttpRequest object is used to exchange data with a web server behind the scenes
        container = document.getElementById('container');
        container.style.display = 'block';
        spinner.style.display = 'block';
        //escaping special chars for XSS security
        input.value = input.value.replace(/<|>|#|&/g, "");
        // send a Request to the server - use the open() method of the XMLHttpRequest object
        // ? =  norm rest (to create API) question = key ; input value in the dictionary request
        request.open("post", "/api?question=" + input.value);
        // The requests.Response() Object contains the server's response to the HTTP request.
        request.responseType = "json"; //jsonify the answer - to valid
        // Sends the request to the server (used for POST)
        request.send();

        request.onload = function(){// what to do while loading spinner
            spinner.style.display = 'block'; // start the spinner
            let answer = this.response; // analyse the response
            // check size list dictionary and goes to else
            // function calls with their parameters
            if (Object.keys(answer).length > 2){
                displayInputValue();
                displayAddress(answer);
                displayWiki(answer);
                initMap(answer['lat'], answer['lng']);
            }
            else{
                displayInputValue();
                messageError(answer);
                messageErrorWiki(answer);
            }
            spinner.style.display = 'none'; // stop the spinner at the end of the onload as soon as the response request is loaded
            // container.style.display = 'block';
        }
    }
}


button.addEventListener("click", () => {
    //in case of click
    grandybot();
});

input.addEventListener('keyup', (event) => {
    // in case of key is pushed
    if (event.key == 'Enter') {
        grandybot();
    }
});

