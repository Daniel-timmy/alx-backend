import { createClient } from "redis";

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
}).on("error", () => {
    console.log("Redis client not connected to the server: ${error}");
});

client.subscribe('holberton school channel');

// Handle Redis client message event
client.on('message', (channel, message) => {
  console.log(message);

  // Check if the message is 'KILL_SERVER'
  if (message === 'KILL_SERVER') {
    // Unsubscribe from the channel
    client.unsubscribe();

    // Close the Redis connection
    client.quit();
  }
});