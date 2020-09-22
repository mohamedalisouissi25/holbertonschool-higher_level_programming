#!/usr/bin/node
const request = require('request');
const link = 'http://swapi.co/api/films/';
request(link, process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).title);
  }
});
