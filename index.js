import dotenv from "dotenv";
import { getComments, replyToComment } from "./facebookAPI.js";
import { getReplyFromGPT } from "./gptReply.js";

dotenv.config();

async function runBot() {
  try {
    const comments = await getComments();
    for (const c of comments) {
      if (!c.message || c.replied) continue;
      const reply = await getReplyFromGPT(c.message);
      await replyToComment(c.id, reply);
      console.log(`💬 ตอบ: "${c.message}" → "${reply}"`);
    }
  } catch (e) {
    console.error("❌ Error:", e.message);
  }
}

runBot();
setInterval(runBot, 10 * 60 * 1000);
