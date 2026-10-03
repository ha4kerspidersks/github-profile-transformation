#!/usr/bin/env python3
"""
Simple local HTTP preview server for GitHub Profile Transformation.
Serves preview/index.html with full asset access.
"""

import http.server
import socketserver
import webbrowser
import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
PORT = 4114

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def end_headers(self):
        # Force browser to never cache SVGs or HTML during local preview
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def do_GET(self):
        if self.path in ("/", "/preview", "/preview/"):
            self.path = "/preview/index.html"
        return super().do_GET()

def main():
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", PORT), CustomHandler) as httpd:
        httpd.daemon_threads = True
        url = f"http://localhost:{PORT}/preview/index.html"
        print("=" * 60)
        print("🚀 GITHUB PROFILE LOCAL PREVIEW SERVER (MULTI-THREADED, NO-CACHE)")
        print("=" * 60)
        print(f"  Preview URL: {url}")
        print("  Press Ctrl+C to stop server.")
        print("-" * 60)
        
        if "--open" in sys.argv or "-o" in sys.argv:
            webbrowser.open(url)
            
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down preview server.")

if __name__ == "__main__":
    main()

