#!/usr/bin/node
/**
 * Computes number of tasks completed by user id
*/

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) throw error;
  const taskCompletion = {};
  const taskInfo = JSON.parse(body);
  for (let i = 0; i < taskInfo.length; i++) {
    if (taskInfo[i].completed) {
      if (taskInfo[i].userId in taskCompletion) {
        taskCompletion[taskInfo[i].userId]++;
      } else {
        taskCompletion[taskInfo[i].userId] = 1;
      }
    }
  }
  console.log(taskCompletion);
});
