import { createClient } from "redis";

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
}).on("error", () => {
    console.log("Redis client not connected to the server: ${error}");
});

function publishMessage(message, time){
    console.log('About to send MESSAGE');

  // Schedule the publication of the message after the specified delay
  setTimeout(() => {
    // Publish the message to the 'holberton school channel'
    client.publish('holberton school channel', message);

    // Close the Redis connection
    client.quit();
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);