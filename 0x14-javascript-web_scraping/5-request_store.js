#!/usr/bin/node
/**
 * Gets the content of a web page and stores it in a file
*/

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) console.log(error);
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) throw err;
  });
});
