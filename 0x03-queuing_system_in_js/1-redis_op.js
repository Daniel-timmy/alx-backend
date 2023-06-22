import { createClient } from "redis";

const client = createClient();

client.on("connect", () => {
    console.log("Redis client connected to the server");
}).on("error", () => {
    console.log("Redis client not connected to the server: ${error}");
});

function setNewSchool(schoolName, value){
    client.set(schoolName, value, print);
}

function displaySchoolValue(schoolName){
    client.get(schoolName, (err, val) => {
        if (err) {
            console.error(err);
            throw error;
        }
        console.log(val);
    });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");