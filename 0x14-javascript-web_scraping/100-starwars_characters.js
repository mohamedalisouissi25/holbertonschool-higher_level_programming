#!/usr/bin/node
const request = require('request');
const lien = 'https://swapi-api.hbtn.io/api/films/';
request(lien + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const list = JSON.parse(body);
  for (const b in list.characters) {
    request(list.characters[b], function (err, responser, body2) {
      if (err) {
        console.log(err);
      }
      const list2 = JSON.parse(body2);
      console.log(list2.name);
    });
  }
});
