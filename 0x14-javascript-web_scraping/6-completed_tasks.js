#!/usr/bin/node
const request = require('request');
const result = {};
request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const list = JSON.parse(body);
  for (const b in list) {
    if (list[b].completed === true) {
      if (result[list[b].userId] === undefined) {
        result[list[b].userId] = 1;
      } else {
        result[list[b].userId]++;
      }
    }
  }
  console.log(result);
});
