#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie_ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve movie information. Status Code:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;
  async function getCharacterData (characterUrl) {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else if (response.statusCode !== 200) {
          reject(`Failed to retrieve character information. Status Code: ${response.statusCode}`);
        } else {
          resolve(JSON.parse(body));
        }
      });
    });
  }

  (async function printCharacters () {
    for (const characterUrl of characters) {
      try {
        const characterData = await getCharacterData(characterUrl);
        console.log(characterData.name);
      } catch (error) {
        console.error('Error:', error);
        process.exit(1);
      }
    }
  })();
});
