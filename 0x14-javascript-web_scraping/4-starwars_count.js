#!/usr/bin/node
const request = require('request');
let comp = 0;
request(process.argv[2], function (err, response, body) {
  if (err) {
    return console.log(err);
  } else {
    const list = JSON.parse(body);
    for (const a in list.results) {
      for (const b in list.results[a].charachters) {
        if (list.results[a].charachters[b].include('18')) {
          comp++;
        }
      }
    }
    console.log(comp);
  }
});
