#!/usr/bin/node


const request = require('request');
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;


function printCharacter(movieId) {
  // Get movie data from SWAPI
  return new Promise((resolve, reject) => {
    request(movieId, (error, response, body) => {
      if (!error && response.statusCode == 200) {
        const data = JSON.parse(body);
	resolve(data.name);
	}
      });
    });
  }


function fetchAndPrintCharNames(movieUrls) {
  // Fetch each character's name and print
  request(movieUrls, (error, response, body) => {
    if (!error && response.statusCode == 200) {
      const CharData = JSON.parse(body);
      // Get character URLs list
      const characterUrls = CharData.characters;

      const promises = characterUrls.map(printCharacter);
        
      Promise.all(promises)
        .then(charNames => {
          charNames.forEach(name => console.log(name));
        });
      }
  });
}

// Print the character names
fetchAndPrintCharNames(movieUrl);
