#!/usr/bin/env python3
"""
 CHUNKED DOWNLOADER v7.3 (CLEAN UX)
✔ Preview first (title + size)
✔ Ask save location AFTER preview
✔ Clean output (no junk logs)
✔ Real-time progress (% + speed + ETA)
✔ First-run auto setup
✔ Self global installer
"""

import subprocess
import sys
import os
import json
import shutil
from datetime import datetime

SETUP_FLAG = os.path.expanduser("~/.ytd_setup_done")

# =========================
# SELF GLOBAL INSTALLER
# =========================
def is_in_path():
    script_name = "ytd"
    return shutil.which(script_name) is not None

def get_possible_bins():
    paths = os.environ.get("PATH", "").split(":")
    writable_bins = []

    for p in paths:
        if os.path.isdir(p) and os.access(p, os.W_OK):
            writable_bins.append(p)

    return writable_bins

def install_global():
    if is_in_path():
        return

    script_path = os.path.abspath(__file__)
    bins = get_possible_bins()

    if not bins:
        return

    preferred = None
    for b in bins:
        if "usr/bin" in b:
            preferred = b
            break

    target_dir = preferred if preferred else bins[0]
    target_path = os.path.join(target_dir, "ytd")

    print("\n GLOBAL INSTALL OPTION")
    print(f" Detected executable path: {target_dir}")
    print(" This will allow running the script as: ytd")

    choice = input("Install globally? (y/n): ").lower()
    if choice != 'y':
        return

    try:
        shutil.copy(script_path, target_path)
        os.chmod(target_path, 0o755)

        print(f" Installed as: {target_path}")
        print(" You can now run: ytd")

    except Exception as e:
        print(f" Install failed: {e}")

# =========================
# LOGGING
# =========================
def log(msg, level="INFO"):
    timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
    colors = {
        "INFO": "\033[96m",
        "WARN": "\033[93m",
        "ERROR": "\033[91m",
        "SUCCESS": "\033[92m"
    }
    print(f"[{timestamp}] {colors.get(level,'')}{level:8}\033[0m | {msg}", flush=True)

# =========================
# DEPENDENCIES
# =========================
def command_exists(cmd):
    return shutil.which(cmd) is not None

def dependencies_ok():
    return command_exists("yt-dlp") and command_exists("aria2c") and command_exists("node")

def run_install():
    log("📦 Installing dependencies...", "INFO")
    subprocess.run("pkg update -y", shell=True)
    subprocess.run("pkg install -y aria2 nodejs", shell=True)
    subprocess.run("pip install -U yt-dlp", shell=True)

def ensure_dependencies():
    if os.path.exists(SETUP_FLAG) and dependencies_ok():
        return

    log(" First-time setup or repair...", "WARN")
    run_install()

    if dependencies_ok():
        with open(SETUP_FLAG, "w") as f:
            f.write("ok")
        log(" Setup complete", "SUCCESS")
    else:
        log(" Setup failed", "ERROR")
        sys.exit(1)

# =========================
# INPUT
# =========================
def get_url():
    return input("\n📎 Video URL (q to quit):\n> ").strip()

def get_threads():
    while True:
        try:
            t = input("\n⚙️ Threads (1-16, Enter=8): ").strip()
            t = int(t) if t else 8
            return max(1, min(t, 16))
        except:
            print(" Enter 1–16")

def select_folder():
    print("\n Save location:")
    print("1. Current folder")
    print("2. New folder")

    choice = input("> ").strip()
    if choice == '2':
        folder = input(" Folder name: ").strip()
        if folder:
            os.makedirs(folder, exist_ok=True)
            os.chdir(folder)
            log(f" Using: {os.getcwd()}", "SUCCESS")
    else:
        log(f" Using current: {os.getcwd()}", "INFO")

# =========================
# PREVIEW
# =========================
def preview_video(url):
    log(" Fetching video info...", "INFO")

    try:
        cmd = ["yt-dlp", "--dump-json", "--no-download", "--quiet", url]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=15)

        info = json.loads(result.stdout.strip().split('\n')[0])

        title = info.get("title", "Unknown")
        uploader = info.get("uploader", "Unknown")
        duration = info.get("duration", 0)
        filesize = info.get("filesize_approx") or 0
        size_mb = filesize / 1024**2 if filesize else 0

        print(f"\n📹 {title[:60]}...")
        print(f" {uploader}")
        print(f"  {duration//60:02d}:{duration%60:02d}")
        print(f" {size_mb:.1f} MB" if size_mb else "📏 Unknown size")

        return title

    except Exception as e:
        log(f"Preview failed: {e}", "ERROR")
        return "video"

# =========================
# DOWNLOAD (FIXED)
# =========================
def download(url, threads):
    threads = min(threads, 16)

    log(" Starting download...", "chill")

    cmd = [
        "yt-dlp",
        url,
        "-f", "bv*+ba/best",
        "-o", "%(uploader)s - %(title)s.%(ext)s",

        "--downloader", "aria2c",
        "--downloader-args",
        f"aria2c:-x{threads} -s{threads} -k1M",

        "--newline",

        "--progress-template",
        "download:%(progress._percent_str)s | %(progress._speed_str)s | ETA %(progress._eta_str)s",

        "--no-warnings",
        "--merge-output-format", "mp4",
        "--continue",
        "--retries", "10",
        "--fragment-retries", "10"
    ]

    process = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    #  Character-by-character streaming (handles \r progress updates)
    while True:
        ch = process.stdout.read(1)
        if not ch:
            break
        sys.stdout.write(ch)
        sys.stdout.flush()

    process.wait()

    if process.returncode == 0:
        log(" Download complete", "SUCCESS")
        return True
    else:
        log(" Download failed", "ERROR")
        return False

# =========================
# MAIN
# =========================
def main():
    print("\n" + "CHUNKED DOWNLOADER v7.3".center(80, "="))
    print(" Clean UI • Fast • Smart")

    install_global()
    ensure_dependencies()

    while True:
        print("\n" + "─" * 80)

        url = get_url()
        if not url or url.lower() in ['q', 'quit']:
            print(" Bye!")
            break

        threads = get_threads()

        title = preview_video(url)

        confirm = input(f"\n Download '{title[:40]}...' ? (y/n): ").lower()
        if confirm != 'y':
            continue

        select_folder()

        success = download(url, threads)

        if success:
            print(f"\n Saved in: {os.getcwd()}")

        if input("\n Next download? (y/n): ").lower() != 'y':
            break

# =========================
if __name__ == "__main__":
    main()
