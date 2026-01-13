const express = require("express");
const axios = require("axios");
const app = express();
app.use(express.json());

app.post("/voice", async (req, res) => {
  const userSpeech = req.body.SpeechResult || "";

  const aiResponse = await axios.post("http://localhost:8000/ai", {
    text: userSpeech
  });

  res.set("Content-Type", "text/xml");
  res.send(`
    <Response>
      <Say>${aiResponse.data.response}</Say>
      <Gather input="speech" action="/voice" />
    </Response>
  `);
});

app.listen(3000, () => console.log("Node server running on port 3000"));
