#!/usr/bin/node
const request = require('request');
let lien = 'http://swapi.co/api/films/';
request(lien, process.argv[2], function (err, response, body) {
  if (err) {
    return console.log(err);
  }
  console.log(JSON.parse(body).title);
});
