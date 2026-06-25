import http.server, json, os, sys, urllib.request, urllib.error

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
PORT = 18765

PROVIDERS = {
    "openai":   "https://api.openai.com/v1",
    "deepseek": "https://api.deepseek.com/v1",
    "custom":   None,  # user provides full URL
}

class H(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self):
        self._cors(); self.send_response(204); self.end_headers()

    def do_GET(self):
        if self.path == "/api/health":
            self._json(200, {"ok":True,"server":"running","port":PORT})
        else:
            if self.path in ("/", ""): self.path = "/index.html"
            super().do_GET()

    def do_POST(self):
        if self.path == "/api/chat":   self._proxy()
        elif self.path == "/api/check": self._check_key()
        else: self._json(404, {"ok":False,"error":"not found"})

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type,Authorization,X-Provider,X-Base-URL")

    def _json(self, code, data):
        self.send_response(code); self._cors()
        self.send_header("Content-Type","application/json"); self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode())

    def _get_base_url(self, body):
        """Determine the API base URL from provider or custom URL"""
        provider = body.get("provider", "openai")
        custom_url = body.get("base_url", "")
        if provider == "custom" and custom_url:
            return custom_url.rstrip("/")
        return PROVIDERS.get(provider, PROVIDERS["openai"])

    def _check_key(self):
        """Verify API key and list available models"""
        length = int(self.headers.get("Content-Length",0))
        body = json.loads(self.rfile.read(length))
        api_key = (body or {}).get("api_key","")
        provider = (body or {}).get("provider","openai")
        base_url = self._get_base_url(body or {})

        if not api_key:
            self._json(400, {"ok":False,"error":"No API key provided"})
            return
        if not base_url:
            self._json(400, {"ok":False,"error":"No base URL configured"})
            return

        try:
            # Fetch available models
            req = urllib.request.Request(
                f"{base_url}/models",
                headers={"Authorization": f"Bearer {api_key}"})
            with urllib.request.urlopen(req, timeout=15) as r:
                data = json.loads(r.read())

            models = [m["id"] for m in data.get("data",[])]
            # Filter to chat-capable models, put the common ones first
            chat_models = [m for m in models if "chat" in m.lower() or "flash" in m.lower() or "pro" in m.lower()]
            all_chat = chat_models if chat_models else models[:20]

            self._json(200, {"ok":True,"provider":provider,"models":all_chat})
        except urllib.error.HTTPError as e:
            eb = e.read().decode(errors="replace")
            self._json(e.code, {"ok":False,"error":f"API rejected: {eb[:300]}"})
        except Exception as e:
            self._json(500, {"ok":False,"error":str(e)})

    def _proxy(self):
        auth = self.headers.get("Authorization","")
        length = int(self.headers.get("Content-Length",0))
        body = json.loads(self.rfile.read(length))

        api_key = body.pop("api_key","") or auth.replace("Bearer ","")
        provider = body.pop("provider","openai")
        base_url = self._get_base_url({"provider":provider,"base_url":body.pop("base_url","")})

        if not api_key:
            self._json(401, {"ok":False,"error":"No API key"})
            return
        if not base_url:
            self._json(400, {"ok":False,"error":"No base URL"})
            return

        try:
            req = urllib.request.Request(
                f"{base_url}/chat/completions",
                data=json.dumps(body).encode(),
                headers={
                    "Content-Type":"application/json",
                    "Authorization":f"Bearer {api_key}"
                })
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
            self.send_response(200); self._cors()
            self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(data)
        except urllib.error.HTTPError as e:
            err = e.read().decode(errors="replace")
            self.send_response(e.code); self._cors()
            self.send_header("Content-Type","application/json"); self.end_headers()
            self.wfile.write(err.encode())
        except Exception as e:
            self._json(500, {"ok":False,"error":str(e)})

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    print(f"Symbiote Demo Server", flush=True)
    print(f"-> http://localhost:{PORT}", flush=True)
    print(f"-> Ctrl+C to stop", flush=True)
    srv = http.server.HTTPServer(("0.0.0.0",PORT), H)
    try: srv.serve_forever()
    except KeyboardInterrupt: print("Stopped", flush=True); srv.server_close()

if __name__ == "__main__":
    main()
