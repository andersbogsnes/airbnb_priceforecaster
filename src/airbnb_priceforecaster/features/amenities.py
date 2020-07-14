from ml_tooling.transformers import Select

amenities_list = ['cable_tv',
                  'paid_parking_off_premises',
                  'bed_linens',
                  'kitchen',
                  'garden_or_backyard',
                  'smoke_alarm',
                  'wifi',
                  'hair_dryer',
                  'oven',
                  'cooking_basics',
                  'translation_missing:_en.hosting_amenity_49',
                  'refrigerator',
                  'luggage_dropoff_allowed',
                  'washer',
                  'laptop-friendly_workspace',
                  'translation_missing:_en.hosting_amenity_50',
                  'dishwasher',
                  'stove',
                  'essentials',
                  'paid_parking_on_premises',
                  'dishes_and_silverware',
                  'hangers',
                  'room-darkening_shades',
                  'tv',
                  'iron',
                  'microwave',
                  'hot_water',
                  'heating',
                  'coffee_maker',
                  'high_chair',
                  'crib',
                  'bathtub',
                  'patio_or_balcony',
                  'shampoo',
                  'long_term_stays_allowed',
                  'family/kid_friendly',
                  'fire_extinguisher',
                  'indoor_fireplace',
                  'dryer',
                  'buzzer/wireless_intercom',
                  'self_check-in',
                  'internet',
                  'lockbox',
                  'children’s_dinnerware',
                  'baby_bath',
                  'children’s_books_and_toys',
                  'pack_’n_play/travel_crib',
                  'host_greets_you',
                  'changing_table',
                  'table_corner_guards',
                  'window_guards',
                  'other',
                  'first_aid_kit',
                  'hot_tub',
                  'carbon_monoxide_alarm',
                  'free_parking_on_premises',
                  'cat(s)',
                  'suitable_for_events',
                  'pets_live_on_this_property',
                  'baby_monitor',
                  'elevator',
                  'wheelchair_accessible',
                  'safety_card',
                  'outlet_covers',
                  '24-hour_check-in',
                  'smoking_allowed',
                  'private_entrance',
                  'air_conditioning',
                  'bbq_grill',
                  'babysitter_recommendations',
                  'private_living_room',
                  'waterfront',
                  'free_street_parking',
                  'keypad',
                  'trash_can',
                  'baking_sheet',
                  'pets_allowed',
                  'high-resolution_computer_monitor',
                  'convection_oven',
                  'outdoor_seating',
                  'extra_pillows_and_blankets',
                  'hbo_go',
                  'formal_dining_area',
                  'toilet_paper',
                  'full_kitchen',
                  'hot_water_kettle',
                  'netflix',
                  'heated_floors',
                  'day_bed',
                  'bath_towel',
                  'building_staff',
                  'bedroom_comforts',
                  'espresso_machine',
                  'body_soap',
                  'bathroom_essentials',
                  'dog(s)',
                  'lake_access',
                  'breakfast',
                  'other_pet(s)',
                  'shower_gel',
                  'gym',
                  'ethernet_connection',
                  'cleaning_before_checkout',
                  'lock_on_bedroom_door',
                  'game_console',
                  'ev_charger',
                  'single_level_home',
                  'well-lit_path_to_entrance',
                  'flat_path_to_guest_entrance',
                  'stair_gates',
                  'washer/dryer',
                  'no_stairs_or_steps_to_enter',
                  'ground_floor_access',
                  'pocket_wifi',
                  'firm_mattress',
                  'wide_hallways',
                  'barbecue_utensils',
                  'bread_maker',
                  'pool',
                  'beach_essentials',
                  '',
                  'beachfront',
                  'fireplace_guards',
                  'ski-in/ski-out',
                  'wide_entrance_for_guests',
                  'doorman',
                  'fixed_grab_bars_for_shower',
                  'fixed_grab_bars_for_toilet',
                  'electric_profiling_bed',
                  'handheld_shower_head',
                  'smart_lock',
                  'soaking_tub',
                  'smart_tv',
                  'balcony',
                  'sauna',
                  'terrace',
                  'murphy_bed',
                  'sound_system',
                  'rain_shower',
                  'wine_cooler',
                  'dvd_player',
                  'heated_towel_rack',
                  'walk-in_shower',
                  'breakfast_table',
                  'jetted_tub',
                  'wide_doorway_to_guest_bathroom',
                  'extra_space_around_bed',
                  'wide_entrance',
                  'disabled_parking_spot',
                  'accessible-height_toilet',
                  'wide_clearance_to_shower',
                  '_toilet',
                  'accessible-height_bed',
                  'wide_entryway',
                  'sun_loungers',
                  'outdoor_parking',
                  'tennis_court',
                  'outdoor_kitchen',
                  'air_purifier',
                  'kitchenette',
                  'roll-in_shower',
                  'gas_oven',
                  'steam_oven',
                  'pillow-top_mattress',
                  'fire_pit',
                  'printer',
                  'standing_valet',
                  'ceiling_fan',
                  'memory_foam_mattress',
                  'amazon_echo',
                  'projector_and_screen',
                  'en_suite_bathroom',
                  'central_air_conditioning',
                  'mini_fridge',
                  'beach_view',
                  'double_oven']

amenities = Select(amenities_list)