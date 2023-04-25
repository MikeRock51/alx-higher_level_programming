#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
*/

const request = require("request");
const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`;

request(url, (error, response, body) => {
	if (error) throw error;
	const movieCharacters = JSON.parse(body).characters;
	for (let i = 0; i < movieCharacters.length; i++) {
		request(movieCharacters[i], (err, res, bd) => {
			if (err) throw err;
			console.log(JSON.parse(bd).name);
		});
	}
});
