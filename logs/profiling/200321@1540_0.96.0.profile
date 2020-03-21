Sat Mar 21 15:40:06 2020    logs/profiling/profile.dump

         4008238 function calls (3875666 primitive calls) in 30.746 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.321    0.321   30.703   30.703 main.py:85(game_loop)
     1806   20.508    0.011   20.508    0.011 {method 'tick' of 'Clock' objects}
      903    0.003    0.000   10.380    0.011 state.py:63(update_clock)
      903    0.005    0.000   10.136    0.011 state.py:38(get_delta_time)
      903    0.013    0.000    4.355    0.005 manager.py:73(draw)
      903    0.004    0.000    4.196    0.005 manager.py:54(update)
      903    0.267    0.000    4.192    0.005 ui_manager.py:122(update)
   295235    3.121    0.000    3.121    0.000 {method 'blit' of 'pygame.Surface' objects}
      903    0.143    0.000    2.505    0.003 sprite.py:453(update)
      907    0.852    0.001    1.826    0.002 camera.py:79(update_game_map)
      902    0.005    0.000    1.824    0.002 camera.py:72(update)
      903    0.007    0.000    1.715    0.002 ui_manager.py:173(draw_ui)
      903    0.269    0.000    1.708    0.002 sprite.py:753(draw)
      907    1.200    0.001    1.200    0.001 {built-in method pygame.transform.scale}
   145486    0.623    0.000    1.107    0.000 ui_element.py:121(check_hover)
      903    0.001    0.000    0.853    0.001 event_core.py:24(update)
       32    0.000    0.000    0.829    0.026 ui_handler.py:30(process_event)
        5    0.000    0.000    0.797    0.159 ui_handler.py:202(update_camera)
        5    0.000    0.000    0.785    0.157 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.785    0.157 camera.py:105(update_grid)
      761    0.010    0.000    0.777    0.001 ui_button.py:30(__init__)
      761    0.041    0.000    0.731    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        6    0.000    0.000    0.637    0.106 ui_handler.py:43(process_entity_event)
    22222    0.054    0.000    0.591    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
154734/22222    0.504    0.000    0.533    0.000 ui_appearance_theme.py:322(get_next_id_node)
   142438    0.276    0.000    0.463    0.000 ui_button.py:197(update)
      903    0.338    0.000    0.338    0.000 {built-in method pygame.event.get}
      903    0.337    0.000    0.337    0.000 {built-in method pygame.display.flip}
    11486    0.029    0.000    0.333    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   142438    0.171    0.000    0.327    0.000 ui_button.py:138(hover_point)
     8929    0.270    0.000    0.285    0.000 sprite.py:913(get_sprites_from_layer)
   136053    0.197    0.000    0.197    0.000 camera.py:233(world_to_screen_position)
     6920    0.013    0.000    0.196    0.000 ui_appearance_theme.py:428(get_misc_data)
       21    0.000    0.000    0.174    0.008 ui_handler.py:67(process_game_event)
        1    0.000    0.000    0.168    0.168 ui_handler.py:106(init_game_ui)
   142438    0.137    0.000    0.156    0.000 rect_drawable_shape.py:84(collide_point)
     1442    0.135    0.000    0.135    0.000 {method 'fill' of 'pygame.Surface' objects}
   142438    0.075    0.000    0.133    0.000 drawable_shape.py:36(update)
   295483    0.103    0.000    0.125    0.000 sprite.py:208(alive)
      761    0.005    0.000    0.091    0.000 ui_button.py:97(set_any_images_from_theme)
     3044    0.005    0.000    0.086    0.000 ui_appearance_theme.py:366(get_image)
     2910    0.021    0.000    0.065    0.000 rect_drawable_shape.py:118(redraw_state)
   142438    0.060    0.000    0.060    0.000 ui_button.py:154(can_hover)
      903    0.003    0.000    0.054    0.000 processors.py:16(process_all)
   603705    0.051    0.000    0.051    0.000 {method 'append' of 'list' objects}
       73    0.000    0.000    0.051    0.001 manager.py:60(process_ui_events)
      903    0.027    0.000    0.051    0.000 processors.py:23(_process_aesthetic_update)
       73    0.018    0.000    0.050    0.001 ui_manager.py:86(process_events)
      761    0.006    0.000    0.044    0.000 ui_button.py:537(rebuild_shape)
        1    0.000    0.000    0.043    0.043 main.py:193(initialise_game)
      368    0.002    0.000    0.042    0.000 screen_message.py:34(update)
        2    0.000    0.000    0.039    0.020 entity.py:232(create_actor)
     1270    0.013    0.000    0.039    0.000 ui_text_box.py:205(update)
      772    0.003    0.000    0.039    0.000 rect_drawable_shape.py:22(__init__)
      246    0.001    0.000    0.036    0.000 ui_text_box.py:347(redraw_from_chunks)
      782    0.008    0.000    0.035    0.000 ui_element.py:23(__init__)
      772    0.011    0.000    0.034    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        2    0.008    0.004    0.032    0.016 world.py:26(create_fov_map)
      761    0.003    0.000    0.029    0.000 ui_appearance_theme.py:405(get_font)
   153045    0.028    0.000    0.028    0.000 ui_manager.py:167(get_mouse_position)
     6541    0.021    0.000    0.027    0.000 query.py:212(__iter__)
        9    0.000    0.000    0.026    0.003 ui_text_box.py:50(__init__)
      246    0.003    0.000    0.025    0.000 ui_text_box.py:327(redraw_from_text_block)
        9    0.000    0.000    0.025    0.003 ui_text_box.py:492(rebuild_from_changed_theme_data)
        9    0.000    0.000    0.023    0.003 ui_text_box.py:110(rebuild)
   295483    0.022    0.000    0.022    0.000 {built-in method _operator.truth}
   396634    0.021    0.000    0.021    0.000 {built-in method builtins.len}
     5413    0.015    0.000    0.021    0.000 ui_container.py:124(check_hover)
      772    0.003    0.000    0.021    0.000 drawable_shape.py:45(redraw_all_states)
   150899    0.021    0.000    0.021    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     4503    0.006    0.000    0.020    0.000 _internal.py:24(wrapper)
        6    0.000    0.000    0.020    0.003 message_log.py:49(add_message)
   144875    0.020    0.000    0.020    0.000 {method 'union' of 'pygame.Rect' objects}
     2910    0.018    0.000    0.018    0.000 surface_cache.py:119(build_cache_id)
     2952    0.018    0.000    0.018    0.000 {method 'copy' of 'pygame.Surface' objects}
        5    0.000    0.000    0.018    0.004 ui_handler.py:150(process_ui_event)
        5    0.000    0.000    0.018    0.004 ui_handler.py:233(process_message)
        5    0.000    0.000    0.018    0.004 manager.py:444(add_to_message_log)
   155004    0.017    0.000    0.017    0.000 {method 'colliderect' of 'pygame.Rect' objects}
      782    0.002    0.000    0.016    0.000 ui_container.py:42(add_element)
        5    0.003    0.001    0.014    0.003 ui_container.py:116(clear)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
     3765    0.008    0.000    0.013    0.000 world.py:55(get_tile)
       27    0.000    0.000    0.013    0.000 entity_handler.py:27(process_event)
     1394    0.012    0.000    0.012    0.000 ui_container.py:62(recalculate_container_layer_thickness)
       11    0.000    0.000    0.012    0.001 ui_text_box.py:310(parse_html_into_style_data)
      603    0.001    0.000    0.011    0.000 ui_button.py:130(kill)
      612    0.001    0.000    0.011    0.000 ui_element.py:114(kill)
      903    0.006    0.000    0.011    0.000 ecs.py:265(process_pending_deletions)
      782    0.001    0.000    0.010    0.000 sprite.py:121(__init__)
     2811    0.009    0.000    0.010    0.000 typing.py:806(__new__)
      246    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
     2811    0.007    0.000    0.009    0.000 query.py:170(__init__)
       74    0.000    0.000    0.009    0.000 __init__.py:1496(_log)
      782    0.003    0.000    0.009    0.000 sprite.py:126(add)
     4511    0.008    0.000    0.009    0.000 ui_window.py:97(update)
      976    0.006    0.000    0.009    0.000 sprite.py:814(layers)
        3    0.000    0.000    0.009    0.003 entity_handler.py:49(_process_move)
       11    0.000    0.000    0.009    0.001 text_block.py:16(__init__)
       11    0.001    0.000    0.009    0.001 text_block.py:40(redraw)
        2    0.000    0.000    0.009    0.004 ui_vertical_scroll_bar.py:22(__init__)
        5    0.000    0.000    0.008    0.002 manager.py:286(update_camera_game_map)
        1    0.002    0.002    0.008    0.008 world.py:446(update_tile_visibility)
      903    0.002    0.000    0.008    0.000 ui_appearance_theme.py:158(update_shape_cache)
    10100    0.007    0.000    0.007    0.000 ui_button.py:257(process_event)
      782    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
       50    0.000    0.000    0.007    0.000 __init__.py:1996(debug)
       21    0.000    0.000    0.007    0.000 game_handler.py:26(process_event)
       50    0.000    0.000    0.007    0.000 __init__.py:1361(debug)
      612    0.001    0.000    0.006    0.000 ui_container.py:52(remove_element)
      903    0.004    0.000    0.006    0.000 ui_manager.py:158(update_mouse_position)
     1806    0.006    0.000    0.006    0.000 sprite.py:745(sprites)
      895    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
    88292    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
        2    0.000    0.000    0.006    0.003 entity.py:342(build_characteristic_sprites)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      903    0.001    0.000    0.006    0.000 surface_cache.py:24(update)
       40    0.000    0.000    0.005    0.000 utility.py:13(get_image)
      782    0.005    0.000    0.005    0.000 sprite.py:646(add_internal)
      790    0.005    0.000    0.005    0.000 sprite.py:822(change_layer)
     2910    0.005    0.000    0.005    0.000 drawable_shape.py:122(rebuild_images_and_text)
      876    0.004    0.000    0.005    0.000 ui_vertical_scroll_bar.py:228(update)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       74    0.000    0.000    0.005    0.000 __init__.py:1521(handle)
      626    0.005    0.000    0.005    0.000 ui_manager.py:104(<listcomp>)
      902    0.002    0.000    0.005    0.000 skill_bar.py:45(update)
      875    0.004    0.000    0.005    0.000 ecs.py:247(delete_entity_immediately)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
       74    0.000    0.000    0.005    0.000 __init__.py:1575(callHandlers)
       74    0.000    0.000    0.004    0.000 __init__.py:892(handle)
        6    0.000    0.000    0.004    0.001 game_handler.py:78(process_end_turn)
        2    0.000    0.000    0.004    0.002 skill.py:139(_call_skill_func)
     3771    0.004    0.000    0.004    0.000 world.py:348(_is_tile_in_bounds)
        6    0.000    0.000    0.004    0.001 chrono.py:47(next_turn)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:27(process_event)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:85(_process_entity_collision)
       74    0.000    0.000    0.004    0.000 __init__.py:1123(emit)
        5    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
        5    0.001    0.000    0.004    0.001 camera.py:167(update_camera_tiles)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
       74    0.000    0.000    0.004    0.000 __init__.py:1022(emit)
       21    0.002    0.000    0.004    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     1953    0.004    0.000    0.004    0.000 {built-in method builtins.sorted}
        2    0.000    0.000    0.004    0.002 interaction_handler.py:135(_apply_effects_to_tiles)
     3000    0.001    0.000    0.004    0.000 libtcodpy.py:3254(map_set_properties)
     4637    0.003    0.000    0.003    0.000 query.py:243(<listcomp>)
       73    0.000    0.000    0.003    0.000 processors.py:57(process_intent)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
      902    0.002    0.000    0.003    0.000 message_log.py:36(update)
       24    0.000    0.000    0.003    0.000 __init__.py:1986(info)
     3048    0.002    0.000    0.003    0.000 ui_element.py:186(hover_point)
      612    0.001    0.000    0.003    0.000 sprite.py:183(kill)
       24    0.000    0.000    0.003    0.000 __init__.py:1373(info)
       74    0.000    0.000    0.003    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.003    0.003 entity_handler.py:127(_process_use_skill)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
       63    0.000    0.000    0.003    0.000 processors.py:138(_process_player_turn_intents)
       34    0.001    0.000    0.003    0.000 styled_chunk.py:8(__init__)
       74    0.001    0.000    0.003    0.000 __init__.py:293(__init__)
      902    0.001    0.000    0.003    0.000 entity_info.py:45(update)
      3/2    0.000    0.000    0.003    0.001 skill.py:219(process_effect)
        1    0.000    0.000    0.003    0.003 skill.py:111(use)
     2811    0.003    0.000    0.003    0.000 query.py:50(__init__)
     1825    0.002    0.000    0.002    0.000 state.py:45(get_current)
       11    0.000    0.000    0.002    0.000 parser.py:104(feed)
       14    0.000    0.000    0.002    0.000 game_handler.py:39(process_change_game_state)
       11    0.000    0.000    0.002    0.000 parser.py:134(goahead)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       75    0.001    0.000    0.002    0.000 entity.py:43(get_player)
        1    0.000    0.000    0.002    0.002 skill.py:261(_process_activate_skill)
      903    0.002    0.000    0.002    0.000 {built-in method pygame.mouse.get_pos}
        7    0.000    0.000    0.002    0.000 chrono.py:24(rebuild_turn_queue)
     3000    0.002    0.000    0.002    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
      612    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
      915    0.001    0.000    0.002    0.000 query.py:225(<listcomp>)
       74    0.000    0.000    0.002    0.000 __init__.py:869(format)
      772    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
     2910    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
       75    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
       31    0.002    0.000    0.002    0.000 {built-in method nt.stat}
      778    0.001    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
       74    0.000    0.000    0.002    0.000 __init__.py:606(format)
        4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
        2    0.000    0.000    0.002    0.001 __init__.py:109(import_module)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:994(_gcd_import)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
     5304    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
       68    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      9/7    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
     3135    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     2540    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}
        2    0.000    0.000    0.001    0.001 __init__.py:133(reload)
     2812    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FF84F319BA0}
        5    0.000    0.000    0.001    0.000 entity.py:485(take_turn)
       15    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       74    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
        1    0.000    0.000    0.001    0.001 basic_attack.py:17(activate)
       34    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
     6315    0.001    0.000    0.001    0.000 sprite.py:168(update)
      896    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
     7542    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
     1448    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
       79    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
      772    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
        2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:610(_exec)
        1    0.000    0.000    0.001    0.001 skill.py:415(_process_damage_effect)
       74    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
       79    0.001    0.000    0.001    0.000 ntpath.py:178(split)
     3088    0.001    0.000    0.001    0.000 {built-in method math.floor}
     4511    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
       74    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
       66    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
       74    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       11    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
       73    0.000    0.000    0.001    0.000 action.py:12(convert_to_intent)
       11    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        6    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
      905    0.001    0.000    0.001    0.000 {built-in method builtins.any}
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       34    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
       66    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
     3048    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
      845    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
     4649    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
       15    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       36    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
       75    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      772    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
      189    0.000    0.000    0.001    0.000 entity.py:93(get_entitys_component)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        1    0.000    0.000    0.001    0.001 entity_handler.py:164(_process_die)
       34    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       74    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
     2570    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
     2910    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
      817    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
       74    0.000    0.000    0.000    0.000 {built-in method time.strftime}
     1564    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     1503    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     1572    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      111    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       46    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
      876    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        1    0.000    0.000    0.000    0.000 skill.py:532(_calculate_to_hit_score)
        1    0.000    0.000    0.000    0.000 skill.py:480(_calculate_damage)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
      158    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
     2944    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       48    0.000    0.000    0.000    0.000 entity.py:103(get_name)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       89    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
     1573    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       30    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
     1057    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       34    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
      782    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       74    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
       60    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
     1528    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       48    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
        8    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       63    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
       74    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        7    0.000    0.000    0.000    0.000 world.py:261(tile_has_tag)
       33    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
      146    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        1    0.000    0.000    0.000    0.000 entity.py:303(create_projectile)
       74    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      329    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       21    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
       74    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        7    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
  336/318    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       56    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        8    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
       74    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       11    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
      782    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        7    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
      148    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
      776    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
       73    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       74    0.000    0.000    0.000    0.000 __init__.py:432(format)
      148    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
      782    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
       73    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        7    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
      156    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
        1    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
        1    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      650    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      457    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        1    0.000    0.000    0.000    0.000 entity.py:189(delete)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        7    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      769    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        7    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        7    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        7    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        1    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       34    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       34    0.000    0.000    0.000    0.000 event_core.py:41(publish)
        4    0.000    0.000    0.000    0.000 entity.py:174(create)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
       80    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
       72    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       21    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        3    0.000    0.000    0.000    0.000 world.py:360(_is_tile_blocking_movement)
      148    0.000    0.000    0.000    0.000 __init__.py:856(release)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
       74    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        4    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        3    0.000    0.000    0.000    0.000 ai.py:68(act)
        4    0.000    0.000    0.000    0.000 world.py:396(_tile_has_other_entity)
       63    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        4    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
        6    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        3    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
       74    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
      668    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
      194    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      458    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      148    0.000    0.000    0.000    0.000 __init__.py:747(filter)
       74    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
       21    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
       74    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        1    0.000    0.000    0.000    0.000 god_handler.py:71(process_interventions)
      188    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
      612    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
      222    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       74    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       51    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
       22    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
       23    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        6    0.000    0.000    0.000    0.000 entity_handler.py:217(_process_end_turn)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        1    0.000    0.000    0.000    0.000 entity.py:428(consider_intervening)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      422    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       74    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       11    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       66    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
      258    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       77    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       74    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
      315    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       71    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
      130    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
       34    0.000    0.000    0.000    0.000 event_core.py:15(notify)
      150    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        2    0.000    0.000    0.000    0.000 ai.py:42(act)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
       51    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       79    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        6    0.000    0.000    0.000    0.000 entity.py:380(spend_time)
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
       70    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       74    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       11    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 world.py:439(recompute_fov)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        1    0.000    0.000    0.000    0.000 skill.py:247(_process_trigger_skill_effect)
       14    0.000    0.000    0.000    0.000 event.py:106(__init__)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        1    0.000    0.000    0.000    0.000 world.py:300(tile_has_tags)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
       34    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
       21    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      129    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       75    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        7    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
       34    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
      160    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       70    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       74    0.000    0.000    0.000    0.000 {built-in method time.time}
       60    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        5    0.000    0.000    0.000    0.000 event.py:184(__init__)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
       74    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        5    0.000    0.000    0.000    0.000 entity.py:335(add_component)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
       21    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
      116    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       34    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        3    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        6    0.000    0.000    0.000    0.000 event.py:88(__init__)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       70    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
      150    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       31    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
        2    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        3    0.000    0.000    0.000    0.000 event.py:63(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        9    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        4    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       49    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
       40    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        1    0.000    0.000    0.000    0.000 random.py:218(randint)
        5    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
        5    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
       38    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       40    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 world.py:77(get_direction)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       11    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
      100    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       33    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        9    0.000    0.000    0.000    0.000 {built-in method math.sin}
       38    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
       38    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       42    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       21    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       20    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       20    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        2    0.000    0.000    0.000    0.000 event.py:136(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       34    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       76    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       11    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
       48    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       10    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        7    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
       35    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
       15    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        5    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
       11    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
        3    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       15    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        7    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        1    0.000    0.000    0.000    0.000 event.py:29(__init__)
       20    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        6    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        1    0.000    0.000    0.000    0.000 event.py:54(__init__)
        8    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
       18    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
       45    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       22    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        8    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       30    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.format}
        6    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 event.py:77(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:24(__init__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        4    0.000    0.000    0.000    0.000 component.py:82(__init__)
        5    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       24    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        2    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        6    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        6    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 skill.py:205(_get_hit_type)
        6    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        3    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:46(process_judgements)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        3    0.000    0.000    0.000    0.000 component.py:31(__init__)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        2    0.000    0.000    0.000    0.000 component.py:118(__init__)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 component.py:199(__init__)
        6    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        4    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 world.py:311(<genexpr>)
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        2    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 entity_handler.py:225(_process_created_timed_entity)
        1    0.000    0.000    0.000    0.000 basic_attack.py:13(use)
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}


