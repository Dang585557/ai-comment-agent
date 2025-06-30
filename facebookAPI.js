import axios from "axios";

const token = process.env.PAGE_ACCESS_TOKEN;
const pageID = process.env.PAGE_ID;
const postID = process.env.POST_ID;

export async function getComments() {
  const url = `https://graph.facebook.com/v18.0/${postID}/comments?access_token=${token}`;
  const res = await axios.get(url);
  return res.data.data.map(c => ({
    id: c.id,
    message: c.message,
    replied: !!c.comment_count,
  }));
}

export async function replyToComment(commentID, message) {
  const url = `https://graph.facebook.com/v18.0/${commentID}/comments`;
  await axios.post(url, {
    message,
    access_token: token
  });
}
