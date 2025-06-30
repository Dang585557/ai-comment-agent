import dotenv from "dotenv";
import { getComments, replyToComment } from "./facebookAPI.js";
import { getReplyFromGPT } from "./gptReply.js";

dotenv.config();

const runBot = async () => {
  const comments = await getComments();

  for (const comment of comments) {
    if (!comment.message || comment.replied) continue;

    const reply = await getReplyFromGPT(comment.message);
    await replyToComment(comment.id, reply);
    console.log(`💬 ตอบคอมเมนต์: "${comment.message}" → "${reply}"`);
  }
};

runBot();
