#!/usr/bin/node
/**
 * Displays the status code of a GET request
*/

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    throw error;
  }
  console.log('code: ' + response.statusCode);
});
