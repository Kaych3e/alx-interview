#!/usr/bin/node


const requests = require('request');
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

function printCharacter(movieId) {
    // Get movie data from SWAPI
    request(movieId, (error, response, body) => {
        if (!error && response.statusCode == 200) {
            const data = JSON.parse(body);

            // Get character URLs list
            const characterUrls = data.characters;

            // Fetch each character's name and print
            characterUrls.forEach(url => {
                request(url, (error, response, body) => {
                    if (!error && response.statusCode == 200) {
                        const data = JSON.parse(body);
                        console.log(data.name);
                    }
                });
            });
        }
    });
}

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Print the character names
printCharacter(movieId);
