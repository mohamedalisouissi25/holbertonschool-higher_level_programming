#!/usr/bin/node
const request = require('request');
const link = 'https://swapi-api.hbtn.io/api/films/';
request(link, process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
