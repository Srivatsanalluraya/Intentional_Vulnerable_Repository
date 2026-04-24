const express = require("express");
const { exec } = require("child_process");
const fs = require("fs");
const app = express();
const router = express.Router();
app.use(express.json());

// Hardcoded secret
const SECRET_KEY = "super-secret-key";

// Remote Code Execution + Command Injection
app.get("/run", (req, res) => {
  const cmd = req.query.cmd;
  exec(cmd, (err, stdout, stderr) => {
    res.send(stdout + stderr);
  });
});

// SQL Injection simulation
app.post("/login", (req, res) => {
  const query =
    "SELECT * FROM users WHERE username = '" +
    req.body.username +
    "' AND password = '" +
    req.body.password +
    "'";
  res.send("Executing query: " + query);
});

// Path Traversal
app.get("/file", (req, res) => {
  const file = req.query.name;
  res.send(fs.readFileSync(file, "utf8"));
});

// XSS
app.get("/hello", (req, res) => {
  res.send("<h1>Hello " + req.query.name + "</h1>");
});

// Insecure deserialization
app.post("/deserialize", (req, res) => {
  eval(req.body.data);
  res.send("Done");
});

app.listen(3000, () => {
  console.log("Insecure server running");
});
