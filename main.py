import sys
sys.dont_write_bytecode = True
import pygame
from farm_sim.config import WINDOW_SIZE
from farm_sim.ui.menu import start_menu
from farm_sim.core.game import Game

if __name__ == "__main__":
    (
        field_w,
        field_h,
        vehicle_key,
        field_map_key,
        field_map_name,
        obstacles_enabled,
        season,
        implement_key,  # <- already returned, now actually used
    ) = start_menu()  # user chooses dimensions + vehicle + map + season + implement
    w, h = WINDOW_SIZE
    
    # Handle GPS field selections
    gps_boundary = None
    gps_converter = None
    
    if field_map_key == "sample_gps_fields":
        from farm_sim.ui.field_selector import select_sample_gps_field
        result = select_sample_gps_field()
        
        if result:
            field_w, field_h, gps_converter, gps_boundary = result
            field_map_name = "Sample GPS Field"
            print(f"Loaded sample GPS field: {field_w:.1f}m x {field_h:.1f}m")
        else:
            print("Sample GPS field selection cancelled, using default field")
            field_map_key = "open_field"
            field_map_name = "Open Field"
    
    elif field_map_key == "john_deere_field":
        from farm_sim.ui.field_selector import select_john_deere_field
        result = select_john_deere_field()
        
        if result:
            field_w, field_h, gps_converter, gps_boundary = result
            field_map_name = "John Deere Field"
            print(f"Loaded John Deere field: {field_w:.1f}m x {field_h:.1f}m")
        else:
            print("John Deere field selection cancelled. Exiting simulation.")
            pygame.quit()
            sys.exit(0)
    
    Game(
        w,
        h,
        field_w=field_w,
        field_h=field_h,
        vehicle_key=vehicle_key,
        field_map_key=field_map_key,
        field_map_name=field_map_name,
        obstacles_enabled=obstacles_enabled,
        season=season,
        gps_boundary=gps_boundary,
        john_deere_token=None,
        field_id=None,
        implement_key=implement_key or None,  # explicit None => no implement
    ).run()
