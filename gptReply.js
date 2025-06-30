import axios from "axios";
const key = process.env.OPENAI_API_KEY;

export async function getReplyFromGPT(userMsg) {
  const res = await axios.post("https://api.openai.com/v1/chat/completions", {
    model: "gpt-4",
    messages: [
      { role: "system", content: "You are a friendly Facebook page admin." },
      { role: "user", content: userMsg }
    ],
  }, { headers: { Authorization: `Bearer ${key}` } });
  return res.data.choices[0].message.content;
}
