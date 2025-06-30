import dotenv from "dotenv";
import { getComments, replyToComment } from "./facebookAPI.js";
import { getReplyFromGPT } from "./gptReply.js";

dotenv.config();

async function runBot() {
  const comments = await getComments();

  for (const comment of comments) {
    if (!comment.message || comment.replied) continue;

    const reply = await getReplyFromGPT(comment.message);
    await replyToComment(comment.id, reply);
    console.log(`💬 ตอบ: "${comment.message}" → "${reply}"`);
  }
}

// 🔁 ทำงานรอบแรก
runBot();

// 🔁 ทำซ้ำทุก 10 นาที
setInterval(runBot, 10 * 60 * 1000);
