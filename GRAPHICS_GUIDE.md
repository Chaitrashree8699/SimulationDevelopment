# Graphics Improvement Guide

This guide explains how to improve the tractor and other graphics in your simulation using image textures and 3D models.

## 3D Model Support (.OBJ Files)

The simulation now supports loading 3D models in Wavefront OBJ format for the tractor!

### Quick Start: Using the Included 3D Tractor Model

The project includes a 3D tractor model that is **automatically detected and used** when you run the simulation:

- **Model file**: `assets/models/tractor.obj`
- **Texture file**: `assets/models/tractor.jpg`

**No code changes needed!** The tractor will automatically use the 3D model when you start the simulation.

### How It Works

1. When the tractor is first rendered, the system checks for `assets/models/tractor.obj`
2. If found, it loads the model and compiles it for efficient rendering
3. If a `tractor.jpg` texture exists in the same folder, it's automatically applied
4. If the model fails to load, the system falls back to the simple cube-based rendering

### Console Messages

When running the simulation, you'll see:
```
Loaded OBJ model: 2973 vertices, 2719 faces
Loaded 3D tractor model from assets/models/tractor.obj
Loaded tractor texture from assets/models/tractor.jpg (512x512) -> ID 1
```

### Creating Your Own 3D Models

You can replace the tractor model with your own:

1. **Export from Blender** (free 3D software at blender.org):
   - Model your tractor
   - File → Export → Wavefront (.obj)
   - Enable "Triangulate Faces" and "Write Normals"
   - Save as `assets/models/tractor.obj`

2. **Create a texture**:
   - In Blender, UV unwrap your model
   - Export UV layout
   - Paint texture in GIMP/Photoshop
   - Save as `assets/models/tractor.jpg`

3. **Adjust scale if needed**:
   - Edit `farm_sim/render/draw.py`
   - In `draw_tractor_3d_model()`, change `glScalef(0.5, 0.5, 0.5)` values

### Technical Details

**Supported OBJ features:**
- Vertices (v)
- Texture coordinates (vt)
- Normals (vn)
- Faces (f) - triangles, quads, and polygons
- Materials (uses texture if available)

**Model loader location**: `farm_sim/render/model_loader.py`
**Texture loader location**: `farm_sim/render/texture_loader.py`

---

## Supported Image Formats

- **BMP** - Windows Bitmap (simple, no compression)
- **PNG** - Portable Network Graphics (supports transparency)
- **JPG/JPEG** - Joint Photographic Experts Group (compressed photos)
- **TGA** - Targa (gaming industry standard)
- **GIF** - Graphics Interchange Format

## Quick Start: Adding Tractor Textures

### 1. Create Assets Directory Structure

```
john-deere-vehicle-simulation-main/
├── assets/
│   └── textures/
│       ├── tractor_body.png
│       ├── tractor_wheel.png
│       ├── ground.png
│       └── cab_glass.png
```

### 2. Prepare Your Images

**Recommended sizes:**
- Tractor body: 512x512 or 1024x1024 pixels
- Wheels: 256x256 pixels
- Ground tiles: 512x512 pixels (will tile)

**Tips for best results:**
- Use power-of-2 dimensions (256, 512, 1024, 2048)
- PNG format for objects that need transparency
- JPG for photos/ground textures (smaller file size)
- Keep file sizes reasonable (< 2MB each)

### 3. Load Textures in Your Code

#### Option A: Use the Texture Manager (Recommended)

```python
from farm_sim.render.textures import load_texture

# In your initialization code (e.g., in game.py or main.py)
def load_game_assets():
    load_texture("assets/textures/tractor_body.png", "tractor_body")
    load_texture("assets/textures/tractor_wheel.png", "tractor_wheel")
    load_texture("assets/textures/ground.png", "ground_tile")
```

#### Option B: Enable Textures for Tractor

In your game rendering code, pass `use_textures=True`:

```python
from farm_sim.render.draw import draw_tractor_john_deere

# In your render loop
draw_tractor_john_deere(tractor, use_textures=True)
```

## Creating Your Own Textures

### Method 1: Find Free Images Online

**Good sources:**
- OpenGameArt.org
- Textures.com (free account)
- FreePBR.com
- Pixabay.com (photos)
- Unsplash.com (photos)

### Method 2: Create in Image Editor

**Free tools:**
- GIMP (gimp.org) - Photoshop alternative
- Paint.NET (getpaint.net) - Windows only
- Krita (krita.org) - Digital painting

**Steps:**
1. Create new image (e.g., 512x512)
2. Paint/design your texture
3. For tractors: Use John Deere green (#367C2B)
4. Add details: panels, lights, logos
5. Save as PNG

### Method 3: Use AI Image Generators

**Free options:**
- Bing Image Creator (free)
- Leonardo.ai (free tier)
- Stable Diffusion (local)

**Example prompt:**
"Top view of John Deere tractor, green paint, simple texture, flat lighting, game asset"

### Method 4: Take Photos

1. Find a real tractor (or use Google Images)
2. Take/download photo
3. Crop to square in image editor
4. Adjust brightness/contrast
5. Save as PNG or JPG

## Example: Converting Simple Shape to Textured Object

### Before (current code):
```python
# Just colored cubes
glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, (0.07, 0.45, 0.12, 1))
draw_cube(1.2, 0.5, 2.2)
```

### After (with textures):
```python
# Textured cube
from farm_sim.render.textures import bind_texture, unbind_texture

glEnable(GL_TEXTURE_2D)
bind_texture("tractor_body")
draw_cube(1.2, 0.5, 2.2, textured=True)
unbind_texture()
glDisable(GL_TEXTURE_2D)
```

## Advanced: Sprite-Based 2D Overlay (Alternative Method)

If you prefer 2D images that always face the camera:

```python
import pygame
from OpenGL.GL import *

def draw_sprite_tractor(tractor, image_surface):
    """Draw a 2D sprite that always faces camera (billboard)."""
    glDisable(GL_LIGHTING)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    
    glPushMatrix()
    glTranslatef(tractor.x, tractor.y + 1.0, tractor.z)
    
    # Billboard effect (always face camera)
    glRotatef(camera_yaw, 0, 1, 0)
    
    # Draw textured quad
    glEnable(GL_TEXTURE_2D)
    bind_texture("tractor_sprite")
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0); glVertex3f(-1, -1, 0)
    glTexCoord2f(1, 0); glVertex3f(1, -1, 0)
    glTexCoord2f(1, 1); glVertex3f(1, 1, 0)
    glTexCoord2f(0, 1); glVertex3f(-1, 1, 0)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    
    glPopMatrix()
    glEnable(GL_LIGHTING)
```

## Testing Your Textures

1. Start with one simple texture (ground or wheel)
2. Use small images first (256x256) for testing
3. Check console for "Loaded texture:" messages
4. If texture doesn't appear:
   - Check file path is correct
   - Verify image file exists
   - Check image dimensions are power-of-2
   - Look for error messages in console

## Troubleshooting

### Texture appears white or wrong color
- Enable `GL_TEXTURE_2D` before binding
- Make sure lighting is enabled
- Check that texture coordinates are specified

### Texture appears black
- May be an alpha/transparency issue
- Try using JPG instead of PNG
- Check texture loading succeeded (console messages)

### Texture is stretched or distorted
- Adjust texture coordinates in `draw_cube()`
- Use different UV mapping
- Try different image aspect ratio

### Performance issues with many textures
- Reduce texture sizes
- Use JPG instead of PNG for non-transparent objects
- Load textures once at startup, not every frame

## Next Steps

1. **Start simple**: Add one ground texture first
2. **Test thoroughly**: Make sure it loads and displays
3. **Add more**: Gradually add tractor, wheel, and obstacle textures
4. **Optimize**: Adjust sizes and formats for best performance
5. **Polish**: Add normal maps, specular maps for advanced effects

## Sample Texture Creation Commands

### Convert photo to game texture with ImageMagick:
```bash
# Resize and crop to square
magick input.jpg -resize 512x512^ -gravity center -extent 512x512 output.png

# Make seamless tileable texture
magick input.jpg -resize 512x512 -virtual-pixel tile -blur 0x1 tileable.png
```

### Using Python/PIL to create simple texture:
```python
from PIL import Image, ImageDraw

# Create simple green texture for tractor
img = Image.new('RGB', (512, 512), color=(54, 124, 43))  # JD Green
draw = ImageDraw.Draw(img)

# Add some panel lines
for i in range(4):
    y = i * 128
    draw.line([(0, y), (512, y)], fill=(30, 70, 25), width=3)

img.save('assets/textures/tractor_body.png')
```

## Resources

- **OpenGL Texture Tutorial**: learnopengl.com/Getting-started/Textures
- **Pygame Image Handling**: pygame.org/docs/ref/image.html
- **Free Texture Sources**: Listed in "Method 1" above
- **Blender for 3D Models**: blender.org (if you want to go beyond textures)
