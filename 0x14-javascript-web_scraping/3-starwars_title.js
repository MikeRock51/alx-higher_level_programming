#!/usr/bin/node
/**
 * Prints the title of a Star Wars movie
 * where the episode number matches a given integer
*/

const request = require("request");
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request(url, (error, response, body) => {
	if (error) throw error
	console.log(JSON.parse(body).title);
});
