// Vercel serverless: /api/health
export default function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.status(200).json({ ok: true, server: 'running', port: 443 });
}
