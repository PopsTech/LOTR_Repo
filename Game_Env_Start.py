from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.config import Config
import os

# Enable full-screen mode
Config.set('graphics', 'fullscreen', 'auto')

# Define the correct path to your map
world_map_path = r"C:\Users\ericl\Python_And_Repository\LOTR\kivy_venv\Middle_Earth.png"

if not os.path.exists(world_map_path):
    print("Warning: Map file not found! Check the path and ensure it's correct.")
else:
    print("Map loaded successfully.")

class GameWorld(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.original_map_size = (1920, 1939)  # Original size of the map
        self.scroll_speed = 10  # Speed of scrolling
        self.zoom_level = 1.0  # Default zoom level
        self.keys_pressed = set()

        # Track window size
        self.view_width, self.view_height = Window.size

        with self.canvas:
            Color(1, 1, 1, 1)
            self.bg = Rectangle(source=world_map_path, pos=(0, 0), size=self.original_map_size)

        # Mini-map
        self.mini_map_size = (200, 200)
        self.mini_map = Image(source=world_map_path, size=self.mini_map_size)
        self.add_widget(self.mini_map)

        # Mini-map player marker
        self.mini_map_marker = Label(text="⬤", font_size=20)
        self.add_widget(self.mini_map_marker)

        # Zoom buttons
        self.zoom_in_button = Button(text="Zoom In", size=(100, 50))
        self.zoom_out_button = Button(text="Zoom Out", size=(100, 50))
        self.zoom_in_button.bind(on_press=self.zoom_in)
        self.zoom_out_button.bind(on_press=self.zoom_out)
        self.add_widget(self.zoom_in_button)
        self.add_widget(self.zoom_out_button)

        # Bind window resize event
        Window.bind(on_resize=self.update_layout)

        # Start game loop
        Clock.schedule_interval(self.update, 1/60)
        Window.bind(on_key_down=self.on_key_down, on_key_up=self.on_key_up)

        # Set initial layout
        self.update_layout(Window, Window.width, Window.height)

    def update_layout(self, window, width, height):
        """Resize the map dynamically when the window is resized."""
        self.view_width, self.view_height = width, height

        # Calculate new background size while maintaining aspect ratio
        aspect_ratio = self.original_map_size[0] / self.original_map_size[1]
        new_width = width
        new_height = int(new_width / aspect_ratio)

        if new_height < height:
            new_height = height
            new_width = int(new_height * aspect_ratio)

        # Update background size
        self.bg.size = (new_width, new_height)
        self.bg.pos = ((width - new_width) / 2, (height - new_height) / 2)  # Center the map

        # Update mini-map position
        self.mini_map.pos = (width * 0.9 - self.mini_map_size[0], height * 0.9 - self.mini_map_size[1])
        self.mini_map_marker.pos = (self.mini_map.pos[0] + 90, self.mini_map.pos[1] + 90)

        # Position zoom buttons near the mini-map
        self.zoom_in_button.pos = (self.mini_map.pos[0], self.mini_map.pos[1] - 60)
        self.zoom_out_button.pos = (self.mini_map.pos[0] + 120, self.mini_map.pos[1] - 60)

    def zoom_in(self, instance):
        """Zoom in and keep the map centered."""
        if self.zoom_level < 3.0:
            self.zoom_level += 0.2
            self.update_zoom()

    def zoom_out(self, instance):
        """Zoom out and keep the map centered."""
        if self.zoom_level > 1.0:
            self.zoom_level -= 0.2
            self.update_zoom()

    def update_zoom(self):
        """Resize the map according to the zoom level and keep it centered."""
        new_width = self.original_map_size[0] * self.zoom_level
        new_height = self.original_map_size[1] * self.zoom_level

        # Keep the zoom centered
        self.bg.size = (new_width, new_height)
        self.bg.pos = ((self.view_width - new_width) / 2, (self.view_height - new_height) / 2)

    def on_key_down(self, window, key, *args):
        """Handle key press events for scrolling."""
        movement_keys = {273, 274, 276, 275}  # Up, Down, Left, Right
        if key in movement_keys:
            self.keys_pressed.add(key)

    def on_key_up(self, window, key, *args):
        """Handle key release events."""
        if key in self.keys_pressed:
            self.keys_pressed.remove(key)

    def update(self, dt):
        """Move the background with arrow keys."""
        bg_x, bg_y = self.bg.pos

        if 273 in self.keys_pressed:  # Up arrow
            bg_y -= self.scroll_speed
        if 274 in self.keys_pressed:  # Down arrow
            bg_y += self.scroll_speed
        if 276 in self.keys_pressed:  # Left arrow
            bg_x += self.scroll_speed
        if 275 in self.keys_pressed:  # Right arrow
            bg_x -= self.scroll_speed

        # Keep the background within view
        max_x = self.view_width - self.bg.size[0]
        max_y = self.view_height - self.bg.size[1]

        bg_x = max(max_x, min(0, bg_x))
        bg_y = max(max_y, min(0, bg_y))

        self.bg.pos = (bg_x, bg_y)

        # Update mini-map marker
        mini_x = ((-bg_x) / self.bg.size[0]) * self.mini_map.width + self.mini_map.pos[0]
        mini_y = ((-bg_y) / self.bg.size[1]) * self.mini_map.height + self.mini_map.pos[1]
        self.mini_map_marker.pos = (mini_x, mini_y)

class LOTRGameApp(App):
    def build(self):
        Window.maximize()  # Makes the window fill the screen
        Window.borderless = True  # Removes borders for a clean full-screen experience
        return GameWorld()


if __name__ == "__main__":
    LOTRGameApp().run()
