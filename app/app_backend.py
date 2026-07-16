# -*- coding: utf-8 -*-
import http.server
import json
import os
import urllib.request
import urllib.parse
import subprocess
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_FILE = os.path.join(BASE_DIR, "instagram_cache.json")
IDEAS_FILE = os.path.join(BASE_DIR, "ideas_database.json")
CRM_FILE = os.path.join(BASE_DIR, "crm_database.json")

def get_gemini_api_key():
    # 1. Tentar das variáveis de ambiente
    key = os.environ.get("GEMINI_API_KEY")
    if key:
        return key
    # 2. Tentar ler do arquivo .env no diretório pai
    env_path = os.path.join(os.path.dirname(BASE_DIR), ".env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1].strip().strip('"').strip("'")
    return ""

def query_rag(query_str):
    try:
        url = f"http://127.0.0.1:8799/query?q={urllib.parse.quote(query_str)}&k=5"
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=3) as res:
            return json.loads(res.read().decode("utf-8"))
    except Exception:
        try:
            url = f"http://host.docker.internal:8799/query?q={urllib.parse.quote(query_str)}&k=5"
            req = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(req, timeout=3) as res:
                return json.loads(res.read().decode("utf-8"))
        except Exception as e:
            print("RAG Server query failed:", e)
            return []

def get_agent_system_prompt(agent_name):
    # Carrega a definição do agente (.agents/agents/{agent}/agent.json)
    agents_dir = os.path.join(os.path.dirname(BASE_DIR), ".agents", "agents")
    agent_path = os.path.join(agents_dir, agent_name, "agent.json")
    if os.path.exists(agent_path):
        try:
            with open(agent_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            sections = data.get("config", {}).get("customAgent", {}).get("systemPromptSections", [])
            if sections:
                return sections[0].get("content", "")
        except Exception as e:
            print(f"Error loading agent prompt for {agent_name}:", e)
    return "Você é um assistente de I.A. sênior."

def call_gemini_api(api_key, system_instruction, user_prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": user_prompt}]
            }
        ],
        "systemInstruction": {
            "parts": [{"text": system_instruction}]
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=15) as res:
        response_data = json.loads(res.read().decode("utf-8"))
        try:
            return response_data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Erro: não foi possível extrair a resposta do modelo."

class MetricsHandler(http.server.BaseHTTPRequestHandler):
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, DELETE")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        if self.path == "/api/metrics":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            
            data = {"profile": {}, "posts": [], "insights_7d": {}}
            if os.path.exists(CACHE_FILE):
                try:
                    with open(CACHE_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading cache file:", e)
            self.wfile.write(json.dumps(data).encode("utf-8"))
            
        elif self.path.startswith("/api/crm/leads"):
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            
            data = {"leads": []}
            if os.path.exists(CRM_FILE):
                try:
                    with open(CRM_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            self.wfile.write(json.dumps(data).encode("utf-8"))
            
        elif self.path == "/api/ideas":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            
            data = []
            if os.path.exists(IDEAS_FILE):
                try:
                    with open(IDEAS_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading ideas file:", e)
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/api/preview/carousel":
            preview_path = os.path.join(BASE_DIR, "preview_carousel.html")
            if os.path.exists(preview_path):
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_cors_headers()
                self.end_headers()
                with open(preview_path, "r", encoding="utf-8") as f:
                    self.wfile.write(f.read().encode("utf-8"))
            else:
                # Caso não exista, serve o template vazio
                tmpl_path = os.path.join(os.path.dirname(BASE_DIR), "templates", "carrossel_template.html")
                if os.path.exists(tmpl_path):
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_cors_headers()
                    self.end_headers()
                    with open(tmpl_path, "r", encoding="utf-8") as f:
                        self.wfile.write(f.read().encode("utf-8"))
                else:
                    self.send_response(404)
                    self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length) if content_length > 0 else b""

        if self.path == "/api/metrics":
            try:
                new_data = json.loads(post_data.decode("utf-8"))
            except Exception:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return

            cache = {"profile": {}, "posts": [], "insights_7d": {}, "insights_30d": {}, "audience": {}, "daily_insights": []}
            if os.path.exists(CACHE_FILE):
                try:
                    with open(CACHE_FILE, "r", encoding="utf-8") as f:
                        cache = json.load(f)
                except Exception as e:
                    print("Error reading cache file:", e)

            for key, val in new_data.items():
                if key == "posts":
                    existing_posts = {p["id"]: p for p in cache.get("posts", [])}
                    for np in val:
                        pid = np["id"]
                        if pid in existing_posts:
                            existing_posts[pid].update(np)
                        else:
                            existing_posts[pid] = np
                    cache["posts"] = list(existing_posts.values())
                elif key == "daily_insights":
                    existing_days = {d["date"]: d for d in cache.get("daily_insights", [])}
                    for nd in val:
                        dkey = nd["date"]
                        if dkey in existing_days:
                            existing_days[dkey].update(nd)
                        else:
                            existing_days[dkey] = nd
                    cache["daily_insights"] = sorted(existing_days.values(), key=lambda x: x["date"], reverse=True)
                elif isinstance(val, dict):
                    if key not in cache or not isinstance(cache[key], dict):
                        cache[key] = {}
                    cache[key].update(val)
                else:
                    cache[key] = val

            cache["last_saved"] = datetime.now().isoformat()

            try:
                with open(CACHE_FILE, "w", encoding="utf-8") as f:
                    json.dump(cache, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing cache file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))

        elif self.path == "/api/crm/leads":
            try:
                new_lead = json.loads(post_data.decode("utf-8"))
            except Exception:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            
            data = {"leads": []}
            if os.path.exists(CRM_FILE):
                try:
                    with open(CRM_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            
            leads = data.setdefault("leads", [])
            lead_id = new_lead.get("id")
            if not lead_id:
                import uuid
                new_lead["id"] = "lead-" + str(uuid.uuid4())[:8]
                new_lead["date_created"] = datetime.now().isoformat()
            
            found = False
            for i, p in enumerate(leads):
                if p["id"] == new_lead["id"]:
                    leads[i].update(new_lead)
                    found = True
                    break
            if not found:
                leads.append(new_lead)
                
            try:
                with open(CRM_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing CRM file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps(new_lead).encode("utf-8"))

        elif self.path == "/api/ideas":
            try:
                new_ideas = json.loads(post_data.decode("utf-8"))
            except Exception:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            
            try:
                with open(IDEAS_FILE, "w", encoding="utf-8") as f:
                    json.dump(new_ideas, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing ideas file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))

        elif self.path == "/api/chat":
            # API de Chat integrada com RAG e Gemini
            try:
                req_data = json.loads(post_data.decode("utf-8"))
            except Exception:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            
            agent = req_data.get("agent", "orchestrator")
            message = req_data.get("message", "")
            use_rag = req_data.get("use_rag", True)
            
            api_key = get_gemini_api_key()
            if not api_key:
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Chave API do Gemini nao configurada. Adicione GEMINI_API_KEY no arquivo .env"}).encode("utf-8"))
                return
            
            # 1. Obter instrução de sistema
            system_instruction = get_agent_system_prompt(agent)
            
            # 2. Obter contexto RAG se ativo
            rag_context = ""
            if use_rag:
                rag_results = query_rag(message)
                if rag_results:
                    rag_context = "\n".join([f"FONTE ({r['rel']}): {r['text']}" for r in rag_results])
            
            # 3. Montar o prompt de envio
            user_prompt = message
            if rag_context:
                user_prompt = f"Contexto recuperado da base de dados local da empresa:\n{rag_context}\n\nPergunta do usuário:\n{message}"
            
            try:
                response_text = call_gemini_api(api_key, system_instruction, user_prompt)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"response": response_text}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

        elif self.path == "/api/generate-carousel":
            # API de geração automática de carrossel
            try:
                req_data = json.loads(post_data.decode("utf-8"))
            except Exception:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Invalid JSON")
                return
            
            theme = req_data.get("theme", "Posicionamento estratégico")
            
            api_key = get_gemini_api_key()
            if not api_key:
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": "Chave API do Gemini nao configurada."}).encode("utf-8"))
                return
                
            system_instruction = "Você é Doug, Diretor de Copywriting da Vértice. Seu trabalho é estruturar carrosséis de alta conversão. Você deve retornar EXCLUSIVAMENTE um formato JSON puro que corresponda ao seguinte esquema, sem nenhum texto introdutório, marcas de markdown ou explicações:\n\n{\n  \"title\": \"Título principal do carrossel\",\n  \"subtitle\": \"Subtítulo da capa\",\n  \"slides\": [\n    {\n      \"tag\": \"Categoria (ex: Posicionamento)\",\n      \"h1\": \"Headline curta com acento em ouro usando em (ex: IA <em>local</em>)\",\n      \"body\": \"Texto de apoio muito curto (máximo de 2 linhas)\"\n    }\n  ],\n  \"caption\": \"Legenda do post para o Instagram, sem emojis e com CTAs assertivos\"\n}\n\nGere exatamente de 5 a 8 slides. O primeiro é a capa, o último deve ser o CTA de fechamento."
            user_prompt = f"Gere um carrossel completo de conteúdo de alta autoridade sobre o seguinte tema: '{theme}'. Lembre-se de não usar emojis sob hipótese alguma, manter títulos curtos em caixa alta e usar tons de contraste 'Antes vs Depois' nas dicas."
            
            try:
                response_text = call_gemini_api(api_key, system_instruction, user_prompt)
                
                # Tratar potenciais blocos de markdown no retorno do modelo
                if "```json" in response_text:
                    response_text = response_text.split("```json")[1].split("```")[0].strip()
                elif "```" in response_text:
                    response_text = response_text.split("```")[1].split("```")[0].strip()
                
                carousel_data = json.loads(response_text.strip())
                
                # Carregar o template de carrossel
                tmpl_path = os.path.join(os.path.dirname(BASE_DIR), "templates", "carrossel_template.html")
                if not os.path.exists(tmpl_path):
                    self.send_response(500)
                    self.send_cors_headers()
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Template de carrossel não encontrado."}).encode("utf-8"))
                    return
                    
                with open(tmpl_path, "r", encoding="utf-8") as f:
                    tmpl_html = f.read()
                
                # Compilar os slides
                slides_list = []
                total = len(carousel_data["slides"])
                for idx, s in enumerate(carousel_data["slides"], 1):
                    # Slide normal
                    tag_html = f'<span class="tag">{s.get("tag", "Vértice")}</span>'
                    h1_html = f'<h1 class="h1">{s.get("h1", "")}</h1>'
                    body_html = f'<p class="body-text">{s.get("body", "")}</p>'
                    
                    # Se for o último slide, insere formato de CTA especial
                    if idx == total:
                        cta_box = f'<div class="cta-gold-card" style="margin-top:20px"><div class="h1" style="font-size:20px;margin-top:0">Responda <em>VÉRTICE</em> no Direct</div></div>'
                        slide_html = f"""
                        <div class="slide">
                          <div class="glow" style="width:320px;height:320px;bottom:-80px;left:-80px;background:radial-gradient(circle, rgba(139,105,20,0.06) 0%, transparent 70%);position:absolute"></div>
                          {tag_html}
                          {h1_html}
                          {body_html}
                          {cta_box}
                          <div class="prog-wrap">
                            <div class="prog-track"><div class="prog-fill" style="width: 100%"></div></div>
                          </div>
                          <span class="slide-num">{idx} / {total}</span>
                        </div>
                        """
                    else:
                        # Slide com glow se for o primeiro
                        glow_div = '<div class="glow glow-gold" style="width:320px;height:320px;top:-80px;right:-80px"></div>' if idx == 1 else ''
                        prog_pct = int((idx / total) * 100)
                        slide_html = f"""
                        <div class="slide">
                          {glow_div}
                          {tag_html}
                          {h1_html}
                          {body_html}
                          <div class="prog-wrap">
                            <div class="prog-track"><div class="prog-fill" style="width: {prog_pct}%"></div></div>
                          </div>
                          <span class="slide-num">{idx} / {total}</span>
                        </div>
                        """
                    slides_list.append(slide_html)
                
                # Montar dots
                dots_list = []
                for i in range(total):
                    active_class = "active" if i == 0 else ""
                    dots_list.append(f'<div class="dot {active_class}" onclick="goTo({i})"></div>')
                
                # Substituir no template
                replacements = {
                    "{{FONT_LINKS}}": '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">',
                    "{{COLOR_BG}}": "#F3F2EE",
                    "{{COLOR_SLIDE_BG}}": "#F9F8F6",
                    "{{COLOR_ACCENT}}": "#8B6914",
                    "{{COLOR_TEXT_MAIN}}": "#111827",
                    "{{COLOR_TEXT_MUTED}}": "#4B5563",
                    "{{COLOR_CARD_BORDER}}": "rgba(0,0,0,0.04)",
                    "{{FONT_TITLE}}": "'Cormorant Garamond', serif",
                    "{{FONT_BODY}}": "'Inter', sans-serif",
                    "{{BORDER_RADIUS}}": "12px",
                    "{{SLIDES_HTML}}": "\n".join(slides_list),
                    "{{DOTS_HTML}}": "\n".join(dots_list),
                    "{{HANDLE}}": "@leocauchiolli",
                    "{{CAPTION}}": carousel_data.get("caption", ""),
                    "{{TOTAL_SLIDES}}": str(total)
                }
                
                output_html = tmpl_html
                for k, v in replacements.items():
                    output_html = output_html.replace(k, v)
                
                # Salvar temporariamente para visualização no iframe
                preview_path = os.path.join(BASE_DIR, "preview_carousel.html")
                with open(preview_path, "w", encoding="utf-8") as f:
                    f.write(output_html)
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "success",
                    "title": carousel_data.get("title", ""),
                    "caption": carousel_data.get("caption", ""),
                    "preview_url": "http://localhost:5000/api/preview/carousel"
                }).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))

        elif self.path == "/api/deploy":
            # API de Deploy
            project_root = os.path.dirname(BASE_DIR)
            try:
                # Adicionar, commitar e enviar ao Git
                subprocess.run(["git", "add", "."], cwd=project_root, check=True)
                subprocess.run(["git", "commit", "-m", "deploy: Vértice OS Hub automated release"], cwd=project_root, check=True)
                subprocess.run(["git", "push", "origin", "main"], cwd=project_root, check=True)
                
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success", "message": "Deploy realizado com sucesso no branch main!"}).encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(json.dumps({"error": f"Erro ao executar deploy no Git: {str(e)}"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        if self.path.startswith("/api/crm/leads"):
            import urllib.parse
            parsed = urllib.parse.urlparse(self.path)
            params = urllib.parse.parse_qs(parsed.query)
            lead_id = params.get("id", [None])[0]
            if not lead_id:
                parts = parsed.path.split("/")
                if len(parts) > 4:
                    lead_id = parts[4]
            
            if not lead_id:
                self.send_response(400)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Missing ID")
                return
                
            data = {"leads": []}
            if os.path.exists(CRM_FILE):
                try:
                    with open(CRM_FILE, "r", encoding="utf-8") as f:
                        data = json.load(f)
                except Exception as e:
                    print("Error reading CRM file:", e)
            
            leads = data.get("leads", [])
            initial_len = len(leads)
            data["leads"] = [p for p in leads if p["id"] != lead_id]
            
            if len(data["leads"]) == initial_len:
                self.send_response(404)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Lead not found")
                return
                
            try:
                with open(CRM_FILE, "w", encoding="utf-8") as f:
                    json.dump(data, f, indent=2, ensure_ascii=False)
            except Exception as e:
                print("Error writing CRM file:", e)
                self.send_response(500)
                self.send_cors_headers()
                self.end_headers()
                self.wfile.write(b"Error saving data")
                return
                
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

def run():
    server_class = http.server.HTTPServer
    if hasattr(http.server, "ThreadingHTTPServer"):
        server_class = http.server.ThreadingHTTPServer
        
    with server_class(("", 5000), MetricsHandler) as httpd:
        print("Server backend running at http://localhost:5000")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")

if __name__ == "__main__":
    run()
