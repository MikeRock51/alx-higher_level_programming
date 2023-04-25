#!/usr/bin/node
/**
 * Prints the number of movies where Wedge Antilles is featured
*/

const request = require('request');
const url = process.argv[2];
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (error, response, body) => {
  if (error) pass;
  const filmInfo = JSON.parse(body).results;
  let movieCount = 0;
  for (let i = 0; i < filmInfo.length; i++) {
    const filmCharacters = filmInfo[i].characters;
    for (let j = 0; j < filmCharacters.length; j++) {
      if (wedgeUrl === filmCharacters[j]) {
        movieCount++;
      }
    }
  }
  console.log(movieCount);
});
