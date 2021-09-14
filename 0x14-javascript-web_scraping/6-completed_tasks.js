#!/usr/bin/node
/* computes the number of tasks completed by user id. */

const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const completedTasks = {};
    const tasks = JSON.parse(body);
    for (const i in tasks) {
      const task = tasks[i];
      if (task.completed === true) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
