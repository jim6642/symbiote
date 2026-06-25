// Vercel serverless: /api/check — verify API key and list models
const PROVIDERS = {
  openai: 'https://api.openai.com/v1',
  deepseek: 'https://api.deepseek.com/v1',
};

export default async function handler(req, res) {
  // CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  if (req.method === 'OPTIONS') return res.status(204).end();

  try {
    const { api_key, provider, base_url } = req.body || {};
    if (!api_key) return res.status(400).json({ ok: false, error: 'No API key' });

    let base = base_url || PROVIDERS[provider] || PROVIDERS.openai;
    if (!base) return res.status(400).json({ ok: false, error: 'Unknown provider' });

    const r = await fetch(`${base}/models`, {
      headers: { Authorization: `Bearer ${api_key}` },
    });
    if (!r.ok) {
      const err = await r.text();
      return res.status(r.status).json({ ok: false, error: err.substring(0, 300) });
    }

    const data = await r.json();
    const models = (data.data || []).map((m) => m.id);
    const chat = models.filter((m) => /chat|flash|pro/i.test(m));
    res.status(200).json({ ok: true, provider, models: chat.length > 0 ? chat : models.slice(0, 10) });
  } catch (e) {
    res.status(500).json({ ok: false, error: e.message });
  }
}
