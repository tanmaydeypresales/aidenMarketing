---
name: animated-diagram
description: >-
  Generates animated architecture diagrams as GIF files using Pillow and imageio.
  Dark-themed with moving dashed arrows showing data/process flow between components.
  Use when the user needs animated flow diagrams for presentations, demos, or proposals.
  Supports custom nodes, arrows, icons, and color schemes matching Aiden AI brand.
license: "Internal use"
---

# Animated Architecture Diagram Skill

Generates professional animated GIF diagrams with moving dashed-line arrows showing data flow between architecture components. Uses Pillow (PIL) for rendering and imageio for GIF assembly.

---

## Part 1: Design System

### 1.1 Canvas & Background

```python
CANVAS_WIDTH = 1400
CANVAS_HEIGHT = 900
BG_COLOR = "#0F1B2D"           # Dark navy background
BG_GRADIENT_TOP = "#0F1B2D"    # Top gradient
BG_GRADIENT_BOTTOM = "#1A365D" # Bottom gradient
```

### 1.2 Color Palette

| Name | Hex | Usage |
|------|-----|-------|
| **Brand Blue** | `#003781` | Primary boxes, headers |
| **Light Blue** | `#5BA4E6` | Highlights, active states |
| **Orange** | `#ED7D31` | Accent, call-to-action, arrows |
| **Green** | `#27AE60` | Success, approved states |
| **Teal** | `#1ABC9C` | Data flow, pipeline stages |
| **Purple** | `#8E44AD` | AI/ML components |
| **Red** | `#E74C3C` | Warnings, decline states |
| **Yellow** | `#F39C12` | Caution, review states |
| **Dark Card** | `#1A1A2E` | Card/box background |
| **Card Border** | `#2C3E50` | Card borders |
| **Text White** | `#FFFFFF` | Primary text |
| **Text Light** | `#B0BEC5` | Secondary text |
| **Text Muted** | `#7F8C8D` | Labels, footnotes |

### 1.3 Typography

```python
# Font loading order (try each, fall back to next)
FONT_PATHS = [
    "C:/Windows/Fonts/segoeui.ttf",      # Segoe UI (Windows)
    "C:/Windows/Fonts/arial.ttf",          # Arial fallback
    "C:/Windows/Fonts/calibri.ttf",        # Calibri fallback
]

FONT_SIZES = {
    "title": 28,
    "subtitle": 20,
    "heading": 18,
    "body": 14,
    "label": 12,
    "small": 10,
    "icon_emoji": 24,
}
```

---

## Part 2: Component Library

### 2.1 Node (Box/Card)

```python
class Node:
    """A labeled box representing a system component."""
    def __init__(self, x, y, width, height, label, sublabel="",
                 bg_color="#1A1A2E", border_color="#2C3E50",
                 accent_color="#003781", icon="", text_color="#FFFFFF"):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.sublabel = sublabel
        self.bg_color = bg_color
        self.border_color = border_color
        self.accent_color = accent_color
        self.icon = icon
        self.text_color = text_color

    @property
    def center(self):
        return (self.x + self.width // 2, self.y + self.height // 2)

    @property
    def top(self):
        return (self.x + self.width // 2, self.y)

    @property
    def bottom(self):
        return (self.x + self.width // 2, self.y + self.height)

    @property
    def left(self):
        return (self.x, self.y + self.height // 2)

    @property
    def right(self):
        return (self.x + self.width, self.y + self.height // 2)
```

### 2.2 Arrow (Animated Flow)

```python
class Arrow:
    """An animated dashed arrow between two points."""
    def __init__(self, start, end, color="#ED7D31", dash_length=12,
                 gap_length=8, thickness=2, label="", curve=None):
        self.start = start    # (x, y) tuple
        self.end = end        # (x, y) tuple
        self.color = color
        self.dash_length = dash_length
        self.gap_length = gap_length
        self.thickness = thickness
        self.label = label
        self.curve = curve    # None for straight, "up"/"down" for curved
```

### 2.3 Layer (Container Group)

```python
class Layer:
    """A container grouping multiple nodes with a header."""
    def __init__(self, x, y, width, height, label,
                 bg_color="#162238", border_color="#2C3E50",
                 accent_color="#003781", header_height=35):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = label
        self.bg_color = bg_color
        self.border_color = border_color
        self.accent_color = accent_color
        self.header_height = header_height
```

---

## Part 3: Rendering Functions

### 3.1 Draw Rounded Rectangle

```python
def draw_rounded_rect(draw, xy, radius, fill, outline=None, width=1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    r = radius
    # Corners
    draw.ellipse([x1, y1, x1 + 2*r, y1 + 2*r], fill=fill, outline=outline, width=width)
    draw.ellipse([x2 - 2*r, y1, x2, y1 + 2*r], fill=fill, outline=outline, width=width)
    draw.ellipse([x1, y2 - 2*r, x1 + 2*r, y2], fill=fill, outline=outline, width=width)
    draw.ellipse([x2 - 2*r, y2 - 2*r, x2, y2], fill=fill, outline=outline, width=width)
    # Rectangles to fill gaps
    draw.rectangle([x1 + r, y1, x2 - r, y2], fill=fill)
    draw.rectangle([x1, y1 + r, x1 + r, y2 - r], fill=fill)
    draw.rectangle([x2 - r, y1 + r, x2, y2 - r], fill=fill)
    # Outline edges (if needed)
    if outline:
        draw.line([x1 + r, y1, x2 - r, y1], fill=outline, width=width)
        draw.line([x1 + r, y2, x2 - r, y2], fill=outline, width=width)
        draw.line([x1, y1 + r, x1, y2 - r], fill=outline, width=width)
        draw.line([x2, y1 + r, x2, y2 - r], fill=outline, width=width)
```

### 3.2 Draw Node

```python
def draw_node(draw, node, font_body, font_small):
    """Draw a node card with accent bar, label, and sublabel."""
    # Background
    draw_rounded_rect(draw,
        [node.x, node.y, node.x + node.width, node.y + node.height],
        radius=8, fill=node.bg_color, outline=node.border_color, width=1)
    # Left accent bar
    draw.rectangle([node.x, node.y + 8, node.x + 4, node.y + node.height - 8],
                   fill=node.accent_color)
    # Icon (if present)
    text_x = node.x + 15
    if node.icon:
        draw.text((node.x + 12, node.y + 10), node.icon, fill=node.accent_color,
                  font=font_body)
        text_x = node.x + 35
    # Label
    draw.text((text_x, node.y + 12), node.label, fill=node.text_color, font=font_body)
    # Sublabel
    if node.sublabel:
        draw.text((text_x, node.y + 32), node.sublabel, fill="#B0BEC5", font=font_small)
```

### 3.3 Draw Animated Arrow

```python
import math

def draw_animated_arrow(draw, arrow, frame_offset):
    """Draw a dashed arrow with moving dash pattern based on frame offset."""
    x1, y1 = arrow.start
    x2, y2 = arrow.end
    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx*dx + dy*dy)
    if length == 0:
        return

    ux = dx / length  # unit vector x
    uy = dy / length  # unit vector y

    cycle = arrow.dash_length + arrow.gap_length
    offset = frame_offset % cycle  # shift dashes each frame

    pos = -offset  # start before the line to create seamless scroll
    while pos < length:
        dash_start = max(0, pos)
        dash_end = min(length, pos + arrow.dash_length)
        if dash_end > dash_start:
            sx = x1 + ux * dash_start
            sy = y1 + uy * dash_start
            ex = x1 + ux * dash_end
            ey = y1 + uy * dash_end
            draw.line([(sx, sy), (ex, ey)], fill=arrow.color, width=arrow.thickness)
        pos += cycle

    # Arrowhead
    head_size = 10
    angle = math.atan2(dy, dx)
    ax1 = x2 - head_size * math.cos(angle - 0.4)
    ay1 = y2 - head_size * math.sin(angle - 0.4)
    ax2 = x2 - head_size * math.cos(angle + 0.4)
    ay2 = y2 - head_size * math.sin(angle + 0.4)
    draw.polygon([(x2, y2), (ax1, ay1), (ax2, ay2)], fill=arrow.color)

    # Label on arrow
    if arrow.label:
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2 - 12
        draw.text((mid_x, mid_y), arrow.label, fill=arrow.color, font=font_small, anchor="mm")
```

### 3.4 Draw Layer Container

```python
def draw_layer(draw, layer, font_heading):
    """Draw a layer container with header bar."""
    # Background
    draw_rounded_rect(draw,
        [layer.x, layer.y, layer.x + layer.width, layer.y + layer.height],
        radius=10, fill=layer.bg_color, outline=layer.border_color, width=1)
    # Header bar
    draw_rounded_rect(draw,
        [layer.x, layer.y, layer.x + layer.width, layer.y + layer.header_height],
        radius=10, fill=layer.accent_color)
    # Fix bottom corners of header
    draw.rectangle([layer.x, layer.y + layer.header_height - 10,
                    layer.x + layer.width, layer.y + layer.header_height],
                   fill=layer.accent_color)
    # Header text
    draw.text((layer.x + 15, layer.y + 8), layer.label, fill="#FFFFFF", font=font_heading)
```

---

## Part 4: GIF Assembly

### 4.1 Frame Generation

```python
TOTAL_FRAMES = 24          # Total frames in the GIF loop
FRAME_DURATION_MS = 80     # Duration per frame (80ms = ~12.5 FPS)
DASH_SPEED = 3             # Pixels of dash offset per frame

def generate_frames(nodes, arrows, layers, title, subtitle=""):
    """Generate all frames for the animated diagram."""
    frames = []
    for frame_idx in range(TOTAL_FRAMES):
        img = Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), BG_COLOR)
        draw = ImageDraw.Draw(img)

        # Draw gradient background
        draw_gradient_bg(draw)

        # Draw title
        draw.text((CANVAS_WIDTH // 2, 30), title, fill="#5BA4E6",
                  font=font_title, anchor="mt")
        if subtitle:
            draw.text((CANVAS_WIDTH // 2, 60), subtitle, fill="#B0BEC5",
                      font=font_body, anchor="mt")

        # Draw layers (background containers)
        for layer in layers:
            draw_layer(draw, layer, font_heading)

        # Draw nodes
        for node in nodes:
            draw_node(draw, node, font_body, font_small)

        # Draw animated arrows
        offset = frame_idx * DASH_SPEED
        for arrow in arrows:
            draw_animated_arrow(draw, arrow, offset)

        # Branding footer
        draw.text((CANVAS_WIDTH - 10, CANVAS_HEIGHT - 20),
                  "Aiden AI | Confidential",
                  fill="#4A5568", font=font_small, anchor="rm")

        frames.append(img)
    return frames
```

### 4.2 Save GIF

```python
import imageio

def save_animated_gif(frames, output_path, duration_ms=80):
    """Save frames as an animated GIF."""
    imageio.mimsave(
        output_path,
        [np.array(f) for f in frames],
        duration=duration_ms / 1000.0,
        loop=0  # infinite loop
    )
```

---

## Part 5: Curved Arrow Support

For arrows that need to route around nodes:

```python
def draw_animated_curved_arrow(draw, start, end, control, color, frame_offset,
                                dash_length=12, gap_length=8, thickness=2, steps=100):
    """Draw an animated dashed quadratic Bezier curve arrow."""
    points = []
    for i in range(steps + 1):
        t = i / steps
        x = (1-t)**2 * start[0] + 2*(1-t)*t * control[0] + t**2 * end[0]
        y = (1-t)**2 * start[1] + 2*(1-t)*t * control[1] + t**2 * end[1]
        points.append((x, y))

    # Calculate cumulative distances
    distances = [0]
    for i in range(1, len(points)):
        d = math.sqrt((points[i][0]-points[i-1][0])**2 + (points[i][1]-points[i-1][1])**2)
        distances.append(distances[-1] + d)

    total_length = distances[-1]
    cycle = dash_length + gap_length
    offset = frame_offset % cycle

    # Draw dashes along the curve
    pos = -offset
    while pos < total_length:
        dash_start = max(0, pos)
        dash_end = min(total_length, pos + dash_length)
        if dash_end > dash_start:
            # Find points on curve at these distances
            seg_points = []
            for d in [dash_start, dash_end]:
                for j in range(len(distances) - 1):
                    if distances[j] <= d <= distances[j+1]:
                        t = (d - distances[j]) / max(0.001, distances[j+1] - distances[j])
                        px = points[j][0] + t * (points[j+1][0] - points[j][0])
                        py = points[j][1] + t * (points[j+1][1] - points[j][1])
                        seg_points.append((px, py))
                        break
            if len(seg_points) == 2:
                draw.line(seg_points, fill=color, width=thickness)
        pos += cycle

    # Arrowhead at end
    if len(points) >= 2:
        dx = points[-1][0] - points[-2][0]
        dy = points[-1][1] - points[-2][1]
        angle = math.atan2(dy, dx)
        head_size = 10
        ax1 = end[0] - head_size * math.cos(angle - 0.4)
        ay1 = end[1] - head_size * math.sin(angle - 0.4)
        ax2 = end[0] - head_size * math.cos(angle + 0.4)
        ay2 = end[1] - head_size * math.sin(angle + 0.4)
        draw.polygon([end, (ax1, ay1), (ax2, ay2)], fill=color)
```

---

## Part 6: Output Specification

### File Naming
```
RFP/<client-name>/<client>_Animated_<diagram-name>.gif
RFP/<client-name>/generate_animated_diagrams.py   (source for regeneration)
```

### Quality Rules
1. Canvas size: minimum 1400x900 for readability
2. All text must be legible — minimum 12px font
3. GIF must loop seamlessly (frame 0 and frame N-1 must flow into each other)
4. Maximum GIF file size: ~5MB (optimize frame count and dimensions if needed)
5. Every arrow must have a clear direction with arrowhead
6. Node labels must not overlap
7. Use layers/containers to group related nodes
8. Include title, subtitle, and Aiden AI branding
9. Color-code arrows by flow type (data=teal, control=orange, API=blue)
10. Maintain consistent spacing between nodes (minimum 40px gap)

### Dependencies
```bash
pip install Pillow imageio numpy
```
