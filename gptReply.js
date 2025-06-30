import axios from "axios";

const key = process.env.OPENAI_API_KEY;

export async function getReplyFromGPT(userComment) {
  const res = await axios.post("https://api.openai.com/v1/chat/completions", {
    model: "gpt-4",
    messages: [
      { role: "system", content: "คุณคือตัวแทนแอดมินเพจที่ตอบคอมเมนต์แบบสุภาพ ช่วยเหลือ และมีมารยาท" },
      { role: "user", content: userComment }
    ],
  }, {
    headers: {
      "Authorization": `Bearer ${key}`,
      "Content-Type": "application/json"
    }
  });

  return res.data.choices[0].message.content;
}
