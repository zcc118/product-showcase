"""Run with Python 3: python3 preview.py [port]. Static local preview only."""
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
import sys
port = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
handler = partial(SimpleHTTPRequestHandler, directory=str(Path(__file__).parent / 'public'))
print(f'Open http://127.0.0.1:{port} — press Ctrl+C to stop.', flush=True)
try:
    ThreadingHTTPServer(('127.0.0.1', port), handler).serve_forever()
except KeyboardInterrupt:
    pass
