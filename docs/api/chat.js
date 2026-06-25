// Vercel serverless: /api/chat — proxy chat completions
const PROVIDERS = {
  openai: 'https://api.openai.com/v1',
  deepseek: 'https://api.deepseek.com/v1',
};

export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  if (req.method === 'OPTIONS') return res.status(204).end();

  try {
    const { api_key, provider, base_url, model, temperature, messages } = req.body || {};
    if (!api_key) return res.status(401).json({ ok: false, error: 'No API key' });

    let base = base_url || PROVIDERS[provider] || PROVIDERS.openai;

    const r = await fetch(`${base}/chat/completions`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${api_key}`,
      },
      body: JSON.stringify({ model, temperature, messages }),
    });

    const data = await r.text();
    res.setHeader('Content-Type', 'application/json');
    res.status(r.status).send(data);
  } catch (e) {
    res.status(500).json({ ok: false, error: e.message });
  }
}
