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

    def do_GET(self):
        if self.path in ("/", "/preview", "/preview/"):
            self.path = "/preview/index.html"
        return super().do_GET()

def main():
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        url = f"http://localhost:{PORT}/preview/index.html"
        print("=" * 60)
        print("🚀 GITHUB PROFILE LOCAL PREVIEW SERVER")
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
