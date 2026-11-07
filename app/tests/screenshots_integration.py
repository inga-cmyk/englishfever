"""Run path/session regression in a disposable app copy, never the working DB."""
import os, pathlib, shutil, socket, subprocess, tempfile, time, urllib.request
ROOT = pathlib.Path(__file__).resolve().parents[2]
with tempfile.TemporaryDirectory(prefix='ef-session-test-') as tmp:
    app = pathlib.Path(tmp) / 'app'
    shutil.copytree(ROOT / 'app', app, ignore=shutil.ignore_patterns('var', 'vendor', 'config.php', '__pycache__'))
    # The existing tests use this port. Refuse to reuse somebody else's server.
    with socket.socket() as probe:
        probe.bind(('127.0.0.1', 8099))
    server = subprocess.Popen(['php', '-S', '127.0.0.1:8099', '-t', str(app)],
                              env={**os.environ, 'EF_DEV': '1'}, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(50):
            if server.poll() is not None:
                raise RuntimeError('The disposable PHP server did not start')
            try:
                urllib.request.urlopen('http://127.0.0.1:8099/index.html', timeout=1)
                break
            except OSError:
                time.sleep(.1)
        else:
            raise RuntimeError('The disposable PHP server did not become ready')
        subprocess.run(['python3', str(app / 'tests/path_review_test.py')], check=True)
    finally:
        server.terminate()
        server.wait()
