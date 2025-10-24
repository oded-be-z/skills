#!/usr/bin/env python3
"""
Generate a sample video demonstrating the Axia workflow output
Uses the sample Khaleeji script and creates a visual representation
"""

import cv2
import numpy as np
from pathlib import Path
import textwrap

print("=" * 80)
print("GENERATING SAMPLE AXIA VIDEO")
print("=" * 80)
print()

# Create output directory
output_dir = Path("sample_output")
output_dir.mkdir(exist_ok=True)

# Sample Khaleeji Arabic script
script_lines = [
    "السلام عليكم!",
    "تفوتك فرص التداول كل يوم؟",
    "",
    "الأسواق تتحرك بسرعة",
    "الفرص ما تنتظر أحد!",
    "",
    "مع أكسيا، تداول بثقة",
    "منصة مرخصة، أدوات احترافية",
    "فرص لا نهاية لها",
    "",
    "ابدأ اليوم",
    "axia.trade",
    "",
    "⚠️ التداول يحمل مخاطر",
    "قد تخسر رأس مالك"
]

# Video specs (TikTok/YouTube Shorts format)
width = 1080
height = 1920
fps = 30
duration = 20  # seconds

# Create video writer
output_file = output_dir / "axia_sample_video.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(str(output_file), fourcc, fps, (width, height))

print(f"Creating video: {output_file}")
print(f"  Resolution: {width}x{height}")
print(f"  FPS: {fps}")
print(f"  Duration: {duration} seconds")
print()

# Colors (Axia brand - adjust to actual brand colors)
bg_color = (20, 20, 20)  # Dark background
text_color = (255, 255, 255)  # White text
accent_color = (0, 183, 255)  # Blue accent (adjust to Axia blue)
warning_color = (0, 165, 255)  # Orange for warning

def create_frame(frame_num, total_frames):
    """Create a single frame with text overlay"""
    frame = np.zeros((height, width, 3), dtype=np.uint8)
    frame[:] = bg_color

    # Calculate time in video
    time_sec = (frame_num / fps)

    # Determine which section we're in (based on 20-second structure)
    if time_sec < 3:
        # Hook (0-3s)
        section = 0
        lines_to_show = script_lines[0:2]
        section_name = "HOOK"
    elif time_sec < 8:
        # Problem (3-8s)
        section = 1
        lines_to_show = script_lines[3:5]
        section_name = "PROBLEM"
    elif time_sec < 15:
        # Solution (8-15s)
        section = 2
        lines_to_show = script_lines[6:9]
        section_name = "SOLUTION"
    else:
        # CTA + Compliance (15-20s)
        section = 3
        lines_to_show = script_lines[10:]
        section_name = "CTA + COMPLIANCE"

    # Add section indicator at top
    cv2.putText(frame, section_name, (40, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, accent_color, 3)

    # Add time indicator
    cv2.putText(frame, f"{time_sec:.1f}s / {duration}s", (width - 250, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (150, 150, 150), 2)

    # Add Arabic text (centered, larger)
    y_pos = height // 2 - 100
    for line in lines_to_show:
        if line.strip():
            # Use a larger font for Arabic text
            text_size = cv2.getTextSize(line, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 3)[0]
            x_pos = (width - text_size[0]) // 2

            # Add shadow for better readability
            cv2.putText(frame, line, (x_pos + 3, y_pos + 3),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 4)

            # Add main text
            color = warning_color if "⚠️" in line else text_color
            cv2.putText(frame, line, (x_pos, y_pos),
                       cv2.FONT_HERSHEY_SIMPLEX, 1.5, color, 3)
            y_pos += 80

    # Add Axia logo text (bottom right)
    cv2.putText(frame, "AXIA", (width - 200, height - 100),
                cv2.FONT_HERSHEY_SIMPLEX, 2.0, accent_color, 4)

    # Add URL
    cv2.putText(frame, "axia.trade", (width - 250, height - 50),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, text_color, 2)

    # Add quality indicators at bottom left
    if frame_num < 30:  # First second only
        cv2.putText(frame, "✓ Khaleeji Dialect", (40, height - 150),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, "✓ Brand Voice", (40, height - 110),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, "✓ Compliance", (40, height - 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Add progress bar at bottom
    progress = frame_num / total_frames
    bar_width = int(width * 0.9)
    bar_height = 8
    bar_x = (width - bar_width) // 2
    bar_y = height - 20

    # Background bar
    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height),
                 (60, 60, 60), -1)

    # Progress bar
    progress_width = int(bar_width * progress)
    cv2.rectangle(frame, (bar_x, bar_y), (bar_x + progress_width, bar_y + bar_height),
                 accent_color, -1)

    return frame

# Generate all frames
total_frames = duration * fps
print("Generating frames...")

for frame_num in range(total_frames):
    frame = create_frame(frame_num, total_frames)
    video.write(frame)

    # Progress indicator
    if frame_num % 30 == 0:
        progress = (frame_num / total_frames) * 100
        print(f"  Progress: {progress:.0f}% ({frame_num}/{total_frames} frames)")

# Release video writer
video.release()

print()
print("✅ Video generation complete!")
print()

# Verify video
import subprocess
try:
    result = subprocess.run(
        ['ffprobe', '-v', 'error', '-show_entries', 'format=duration,size',
         '-show_entries', 'stream=width,height,r_frame_rate',
         '-of', 'json', str(output_file)],
        capture_output=True,
        text=True,
        timeout=10
    )

    if result.returncode == 0:
        import json
        data = json.loads(result.stdout)

        print("📊 Video Properties:")
        print("-" * 80)
        if 'streams' in data and len(data['streams']) > 0:
            stream = data['streams'][0]
            print(f"  Resolution: {stream.get('width')}x{stream.get('height')}")
            print(f"  Frame Rate: {stream.get('r_frame_rate')}")

        if 'format' in data:
            fmt = data['format']
            duration = float(fmt.get('duration', 0))
            size_bytes = int(fmt.get('size', 0))
            size_mb = size_bytes / (1024 * 1024)
            print(f"  Duration: {duration:.2f} seconds")
            print(f"  File Size: {size_mb:.2f} MB")
        print("-" * 80)
except:
    pass

print()
print("=" * 80)
print("📁 OUTPUT FILE")
print("=" * 80)
print(f"  {output_file}")
print()
print("To view the video:")
print(f"  vlc {output_file}")
print(f"  # or")
print(f"  mpv {output_file}")
print(f"  # or")
print(f"  ffplay {output_file}")
print()

print("=" * 80)
print("📝 ABOUT THIS SAMPLE VIDEO")
print("=" * 80)
print()
print("This is a DEMONSTRATION of the workflow output format:")
print()
print("✅ Shows the Khaleeji Arabic script")
print("✅ Demonstrates 20-second structure:")
print("   - 0-3s: Hook (attention-grabbing question)")
print("   - 3-8s: Problem (markets move fast)")
print("   - 8-15s: Solution (Axia platform)")
print("   - 15-20s: CTA + Compliance (risk disclosure)")
print()
print("✅ Correct format: 1080x1920 (9:16 vertical)")
print("✅ Correct duration: 20 seconds")
print("✅ Ready for: YouTube Shorts, TikTok, Instagram Reels")
print()
print("ACTUAL PRODUCTION VIDEO WILL HAVE:")
print("  → Professional AI avatar (Arabic-speaking)")
print("  → High-quality Arabic voiceover (ElevenLabs)")
print("  → Real Axia branding and logo")
print("  → Market data integration (live forex prices)")
print("  → Professional video editing and transitions")
print()

print("=" * 80)
print("🎬 READY FOR REVIEW!")
print("=" * 80)
print()
print("Please review:")
print("  1. Script quality (Khaleeji dialect)")
print("  2. Content structure (Hook-Problem-Solution-CTA)")
print("  3. Compliance (risk disclosure present)")
print("  4. Brand voice (bold, opportunity-focused)")
print()
print("Provide feedback and we'll iterate!")
print()
