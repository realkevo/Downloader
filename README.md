<!DOCTYPE html><html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>YTD YouTube Video Downloader README</title>
<style>
    body {
        font-family: Arial, sans-serif;
        background: #0f172a;
        color: #e2e8f0;
        margin: 0;
        padding: 0;
        line-height: 1.6;
    }
    header {
        background: linear-gradient(135deg, #2563eb, #7c3aed);
        padding: 30px;
        text-align: center;
    }
    header h1 {
        margin: 0;
        font-size: 28px;
    }
    header p {
        opacity: 0.9;
    }
    .container {
        max-width: 900px;
        margin: auto;
        padding: 20px;
    }
    .card {
        background: #1e293b;
        padding: 20px;
        margin: 15px 0;
        border-radius: 12px;
        box-shadow: 0 0 10px rgba(0,0,0,0.3);
    }
    h2 {
        color: #60a5fa;
        border-bottom: 1px solid #334155;
        padding-bottom: 5px;
    }
    code {
        background: #0b1220;
        padding: 3px 6px;
        border-radius: 5px;
        color: #fbbf24;
    }
    pre {
        background: #0b1220;
        padding: 10px;
        border-radius: 8px;
        overflow-x: auto;
        color: #34d399;
    }
    .highlight {
        color: #f472b6;
        font-weight: bold;
    }
    footer {
        text-align: center;
        padding: 20px;
        opacity: 0.6;
    }
</style>
</head>
<body><header>
    <h1> YTD YouTube Video Downloader</h1>
    <p>Fast • Multi-platform • Terminal Native • YouTube & Social Media Video Downloader</p>
</header><div class="container"><div class="card">
<h2> Overview</h2>
<p>
<b>YTD (YouTube Video Downloader)</b> is a high-performance terminal-based video downloader built on <span class="highlight">yt-dlp</span>. 
It is designed to download videos from <b>YouTube and supported social media platforms</b> including TikTok, Instagram, Facebook, Twitter/X, and more.
</p>
<p>
It uses optimized download handling to ensure fast, stable, and reliable media downloads with real-time feedback.
</p>
</div><div class="card">
<h2>Supported Environment</h2>
<ul>
<li>Termux (Android terminal environment)</li>
<li>Linux distributions (Ubuntu, Debian, Arch, etc.)</li>
<li>Python 3.8+</li>
<li>Active internet connection</li>
</ul>
</div><div class="card">
<h2> Dependencies (Auto-Handled)</h2>
<p>
This tool automatically installs required dependencies on first run.
</p>
<ul>
<li>yt-dlp (core download engine)</li>
<li>Required Python modules</li>
</ul>
<p><i>If auto-install fails, manual pip installation is supported.</i></p>
</div><div class="card">
<h2>Global Installation</h2>
<p>Once installed globally, the tool becomes available as a system command:</p>
<pre>ytd</pre>
<p>You can run it from any directory without typing Python or file paths.</p>
</div><div class="card">
<h2> How to Run</h2>
<pre>ytd</pre>
<p>Launches the interactive downloader interface.</p>
</div><div class="card">
<h2> Step-by-Step Execution Flow</h2>
<ol>
<li><b>Launch</b> – User runs <code>ytd</code></li>
<li><b>Environment Check</b> – Verifies Python and dependencies</li>
<li><b>Auto-Install</b> – Installs missing packages (like yt-dlp)</li>
<li><b>User Input</b> – Prompts for video URL</li>
<li><b>Validation</b> – Checks supported platform URL</li>
<li><b>Thread Setup</b> – Selects or defaults download threads</li>
<li><b>Metadata Fetch</b> – Retrieves video information</li>
<li><b>Download Process</b> – Downloads video data efficiently</li>
<li><b>Merge Process</b> – Combines downloaded segments</li>
<li><b>Save Output</b> – Stores file in current directory</li>
<li><b>Completion</b> – Displays success, speed, and location</li>
</ol>
</div><div class="card">
<h2>Features</h2>
<ul>
<li>YouTube + social media video downloads</li>
<li>High-speed optimized downloading</li>
<li>Auto dependency installation</li>
<li>Live progress, speed, and ETA display</li>
<li>Lightweight terminal interface</li>
<li>Global CLI command: <code>ytd</code></li>
</ul>
</div><div class="card">
<h2> Output Behavior</h2>
<p>All downloaded videos are saved in the current working directory unless changed in configuration.</p>
</div><div class="card">
<h2>Notes</h2>
<ul>
<li>Speed depends on internet and server limits</li>
<li>Some content may be restricted by platform policies</li>
<li>Thread count does not always guarantee faster speed</li>
</ul>
</div><div class="card">
<h2> Troubleshooting</h2>
<p><b>Command not found (ytd)</b></p>
<pre>which ytd</pre><p><b>Missing yt-dlp</b></p>
<pre>pip install yt-dlp</pre><p><b>Permission issues</b></p>
<pre>chmod +x /data/data/com.termux/files/usr/bin/ytd</pre>
</div><div class="card">
<h2> Summary</h2>
<p>
YTD turns your terminal into a powerful <b>YouTube video downloader</b> with support for multiple platforms, automation, and global access.
    Vibecoded using jailbroken Blackbox ai
</p>
<p><b>Global Command:</b> <code>ytd</code></p>
</div></div><footer>
    Built for fast terminal video downloading • Command: ytd
</footer></body>
</html>
