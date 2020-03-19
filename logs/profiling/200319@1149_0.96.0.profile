Thu Mar 19 11:49:41 2020    logs/profiling/profile.dump

         3875015 function calls (3796264 primitive calls) in 33.835 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.372    0.372   33.794   33.794 main.py:79(game_loop)
     2006   23.402    0.012   23.402    0.012 {method 'tick' of 'Clock' objects}
     1003    0.005    0.000   12.003    0.012 state.py:63(update_clock)
     1003    0.007    0.000   11.411    0.011 state.py:38(get_delta_time)
     1003    0.016    0.000    4.768    0.005 manager.py:73(draw)
     1003    0.005    0.000    4.504    0.004 manager.py:54(update)
     1003    0.283    0.000    4.499    0.004 ui_manager.py:122(update)
   322889    3.330    0.000    3.330    0.000 {method 'blit' of 'pygame.Surface' objects}
     1003    0.158    0.000    2.683    0.003 sprite.py:453(update)
     1002    0.006    0.000    1.991    0.002 camera.py:72(update)
     1005    0.955    0.001    1.988    0.002 camera.py:79(update_game_map)
     1003    0.009    0.000    1.804    0.002 ui_manager.py:173(draw_ui)
     1003    0.292    0.000    1.795    0.002 sprite.py:753(draw)
     1007    1.368    0.001    1.368    0.001 {built-in method pygame.transform.scale}
   157495    0.672    0.000    1.195    0.000 ui_element.py:121(check_hover)
     1003    0.001    0.000    0.526    0.001 event_core.py:21(update)
       13    0.000    0.000    0.507    0.039 ui_handler.py:30(process_event)
        3    0.000    0.000    0.491    0.164 ui_handler.py:207(update_camera)
   155310    0.303    0.000    0.484    0.000 ui_button.py:197(update)
        3    0.000    0.000    0.483    0.161 manager.py:295(update_camera_grid)
        3    0.003    0.001    0.483    0.161 camera.py:106(update_grid)
      455    0.006    0.000    0.476    0.001 ui_button.py:30(__init__)
      455    0.025    0.000    0.447    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
     1003    0.373    0.000    0.373    0.000 {built-in method pygame.display.flip}
   155310    0.184    0.000    0.359    0.000 ui_button.py:138(hover_point)
    13255    0.033    0.000    0.358    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
        3    0.000    0.000    0.328    0.109 ui_handler.py:48(process_entity_event)
91965/13255    0.305    0.000    0.323    0.000 ui_appearance_theme.py:322(get_next_id_node)
     9712    0.284    0.000    0.300    0.000 sprite.py:913(get_sprites_from_layer)
   150753    0.218    0.000    0.218    0.000 camera.py:234(world_to_screen_position)
     6853    0.018    0.000    0.203    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
        9    0.000    0.000    0.176    0.020 ui_handler.py:72(process_game_event)
   155310    0.155    0.000    0.175    0.000 rect_drawable_shape.py:84(collide_point)
        1    0.000    0.000    0.171    0.171 ui_handler.py:111(init_game_ui)
     1003    0.149    0.000    0.149    0.000 {built-in method pygame.event.get}
     1265    0.142    0.000    0.142    0.000 {method 'fill' of 'pygame.Surface' objects}
   320001    0.110    0.000    0.132    0.000 sprite.py:208(alive)
   155310    0.079    0.000    0.123    0.000 drawable_shape.py:36(update)
     4123    0.008    0.000    0.119    0.000 ui_appearance_theme.py:428(get_misc_data)
   155310    0.064    0.000    0.064    0.000 ui_button.py:154(can_hover)
      455    0.003    0.000    0.055    0.000 ui_button.py:97(set_any_images_from_theme)
     1820    0.003    0.000    0.052    0.000 ui_appearance_theme.py:366(get_image)
   519133    0.048    0.000    0.048    0.000 {method 'append' of 'list' objects}
     2279    0.014    0.000    0.044    0.000 rect_drawable_shape.py:118(redraw_state)
        1    0.000    0.000    0.042    0.042 main.py:184(initialise_game)
       68    0.000    0.000    0.040    0.001 manager.py:60(process_ui_events)
       68    0.015    0.000    0.039    0.001 ui_manager.py:86(process_events)
        2    0.000    0.000    0.038    0.019 entity.py:225(create_actor)
        2    0.008    0.004    0.031    0.015 world.py:26(create_fov_map)
      455    0.004    0.000    0.029    0.000 ui_button.py:537(rebuild_shape)
   164691    0.028    0.000    0.028    0.000 ui_manager.py:167(get_mouse_position)
      459    0.002    0.000    0.025    0.000 rect_drawable_shape.py:22(__init__)
     6013    0.017    0.000    0.024    0.000 ui_container.py:124(check_hover)
   163508    0.023    0.000    0.023    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     1183    0.010    0.000    0.023    0.000 ui_text_box.py:205(update)
      459    0.007    0.000    0.022    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
   157193    0.022    0.000    0.022    0.000 {method 'union' of 'pygame.Rect' objects}
   320001    0.022    0.000    0.022    0.000 {built-in method _operator.truth}
      469    0.005    0.000    0.021    0.000 ui_element.py:23(__init__)
      181    0.001    0.000    0.021    0.000 screen_message.py:34(update)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
   168261    0.019    0.000    0.019    0.000 {method 'colliderect' of 'pygame.Rect' objects}
      455    0.002    0.000    0.018    0.000 ui_appearance_theme.py:405(get_font)
      121    0.001    0.000    0.018    0.000 ui_text_box.py:347(redraw_from_chunks)
   307260    0.017    0.000    0.017    0.000 {built-in method builtins.len}
     1003    0.004    0.000    0.017    0.000 processors.py:16(process_all)
      459    0.002    0.000    0.014    0.000 drawable_shape.py:45(redraw_all_states)
     2297    0.013    0.000    0.013    0.000 {method 'copy' of 'pygame.Surface' objects}
     1003    0.013    0.000    0.013    0.000 processors.py:23(_process_aesthetic_update)
       12    0.000    0.000    0.013    0.001 entity_handler.py:29(process_event)
      121    0.002    0.000    0.012    0.000 ui_text_box.py:327(redraw_from_text_block)
     2279    0.012    0.000    0.012    0.000 surface_cache.py:119(build_cache_id)
     3460    0.007    0.000    0.012    0.000 world.py:55(get_tile)
     5011    0.009    0.000    0.011    0.000 ui_window.py:97(update)
     1071    0.007    0.000    0.011    0.000 sprite.py:814(layers)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
      469    0.001    0.000    0.010    0.000 ui_container.py:42(add_element)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:50(__init__)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
        4    0.000    0.000    0.008    0.002 ui_text_box.py:110(rebuild)
        2    0.000    0.000    0.008    0.004 entity_handler.py:57(_process_move)
     2006    0.008    0.000    0.008    0.000 sprite.py:745(sprites)
        1    0.002    0.002    0.008    0.008 world.py:445(update_tile_visibility)
     1003    0.005    0.000    0.007    0.000 ui_manager.py:158(update_mouse_position)
       63    0.000    0.000    0.007    0.000 __init__.py:1496(_log)
        3    0.001    0.000    0.007    0.002 ui_container.py:116(clear)
        4    0.000    0.000    0.007    0.002 ui_text_box.py:310(parse_html_into_style_data)
      772    0.007    0.000    0.007    0.000 ui_container.py:62(recalculate_container_layer_thickness)
       54    0.000    0.000    0.007    0.000 __init__.py:1996(debug)
       54    0.000    0.000    0.007    0.000 __init__.py:1361(debug)
       61    0.000    0.000    0.006    0.000 ui_text_box.py:462(set_active_effect)
      469    0.001    0.000    0.006    0.000 sprite.py:121(__init__)
        4    0.000    0.000    0.006    0.002 text_block.py:16(__init__)
        4    0.000    0.000    0.006    0.002 text_block.py:40(redraw)
     1003    0.003    0.000    0.006    0.000 ui_appearance_theme.py:158(update_shape_cache)
        2    0.000    0.000    0.006    0.003 entity.py:329(build_characteristic_sprites)
     8370    0.006    0.000    0.006    0.000 ui_button.py:257(process_event)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
      300    0.000    0.000    0.006    0.000 ui_button.py:130(kill)
      469    0.002    0.000    0.006    0.000 sprite.py:126(add)
        3    0.000    0.000    0.006    0.002 manager.py:286(update_camera_game_map)
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
     1002    0.003    0.000    0.005    0.000 skill_bar.py:45(update)
      470    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
      303    0.001    0.000    0.005    0.000 ui_element.py:114(kill)
      121    0.002    0.000    0.005    0.000 text_block.py:265(redraw_from_chunks)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
     2143    0.005    0.000    0.005    0.000 {built-in method builtins.sorted}
     1002    0.002    0.000    0.005    0.000 message_log.py:36(update)
      469    0.001    0.000    0.004    0.000 ui_element.py:104(change_layer)
     3463    0.003    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
       63    0.000    0.000    0.004    0.000 __init__.py:1521(handle)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
      512    0.004    0.000    0.004    0.000 ui_manager.py:104(<listcomp>)
       63    0.000    0.000    0.004    0.000 __init__.py:1575(callHandlers)
     2016    0.004    0.000    0.004    0.000 state.py:45(get_current)
    52610    0.004    0.000    0.004    0.000 {method 'reverse' of 'list' objects}
     2279    0.003    0.000    0.003    0.000 drawable_shape.py:122(rebuild_images_and_text)
       63    0.000    0.000    0.003    0.000 __init__.py:892(handle)
     1002    0.002    0.000    0.003    0.000 entity_info.py:45(update)
      477    0.003    0.000    0.003    0.000 sprite.py:822(change_layer)
      469    0.003    0.000    0.003    0.000 sprite.py:646(add_internal)
     1003    0.001    0.000    0.003    0.000 surface_cache.py:24(update)
      303    0.001    0.000    0.003    0.000 ui_container.py:52(remove_element)
        2    0.000    0.000    0.003    0.002 message_log.py:49(add_message)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 entity_handler.py:135(_process_use_skill)
       63    0.000    0.000    0.003    0.000 __init__.py:1123(emit)
        9    0.000    0.000    0.003    0.000 game_handler.py:26(process_event)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
       63    0.000    0.000    0.003    0.000 __init__.py:1022(emit)
     2185    0.002    0.000    0.003    0.000 ui_element.py:186(hover_point)
        1    0.000    0.000    0.003    0.003 skill.py:111(use)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       63    0.000    0.000    0.002    0.000 __init__.py:1481(makeRecord)
     1003    0.002    0.000    0.002    0.000 {built-in method pygame.mouse.get_pos}
        1    0.000    0.000    0.002    0.002 skill.py:150(_call_skill_func)
       63    0.001    0.000    0.002    0.000 __init__.py:293(__init__)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        3    0.000    0.000    0.002    0.001 manager.py:275(update_cameras_tiles)
        3    0.001    0.000    0.002    0.001 camera.py:168(update_camera_tiles)
       29    0.002    0.000    0.002    0.000 {built-in method nt.stat}
     5492    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
        1    0.000    0.000    0.002    0.002 __init__.py:109(import_module)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:994(_gcd_import)
      303    0.000    0.000    0.002    0.000 sprite.py:183(kill)
       16    0.000    0.000    0.002    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:978(_find_and_load)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
       63    0.000    0.000    0.001    0.000 __init__.py:869(format)
       63    0.000    0.000    0.001    0.000 __init__.py:606(format)
        2    0.000    0.000    0.001    0.001 interaction_handler.py:25(process_event)
       29    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.001    0.001 ui_handler.py:155(process_ui_event)
        4    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 ui_handler.py:238(process_message)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
        1    0.000    0.000    0.001    0.001 manager.py:444(add_to_message_log)
       64    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     2279    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
      459    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
       68    0.000    0.000    0.001    0.000 processors.py:57(process_intent)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
     1005    0.001    0.000    0.001    0.000 {built-in method builtins.any}
     7015    0.001    0.000    0.001    0.000 sprite.py:168(update)
      465    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
        1    0.000    0.000    0.001    0.001 interaction_handler.py:86(_process_entity_collision)
        8    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.001    0.001 interaction_handler.py:121(_apply_effects_to_tiles)
      303    0.001    0.000    0.001    0.000 sprite.py:728(remove_internal)
      7/5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
     6927    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
        9    0.000    0.000    0.001    0.000 __init__.py:1986(info)
     5011    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
        9    0.000    0.000    0.001    0.000 __init__.py:1373(info)
       63    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
       68    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
        6    0.000    0.000    0.001    0.000 game_handler.py:42(process_change_game_state)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        2    0.000    0.000    0.001    0.000 game_handler.py:81(process_end_turn)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
       68    0.001    0.000    0.001    0.000 ntpath.py:178(split)
        2    0.000    0.000    0.001    0.000 chrono.py:50(next_turn)
       54    0.000    0.000    0.001    0.000 processors.py:138(_process_player_turn_intents)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       63    0.000    0.000    0.001    0.000 __init__.py:1451(findCaller)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
      459    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
       68    0.000    0.000    0.001    0.000 action.py:12(convert_to_intent)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
       63    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
        5    0.000    0.000    0.001    0.000 state.py:71(set_new)
      471    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
       63    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
     1836    0.001    0.000    0.001    0.000 {built-in method math.floor}
     2185    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
      797    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
        4    0.000    0.000    0.000    0.000 parser.py:104(feed)
        3    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        4    0.000    0.000    0.000    0.000 parser.py:134(goahead)
     4100    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
        1    0.000    0.000    0.000    0.000 __init__.py:133(reload)
     1146    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
      533    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
       63    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       63    0.000    0.000    0.000    0.000 {built-in method time.strftime}
      459    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
     2279    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
     1563    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:610(_exec)
      136    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
      236    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        4    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 chrono.py:23(rebuild_turn_queue)
       60    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      946    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        4    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
      928    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
      488    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       17    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       78    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      918    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 basic_attack.py:8(use)
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        1    0.000    0.000    0.000    0.000 skill.py:230(process_effect)
        1    0.000    0.000    0.000    0.000 entity.py:292(create_projectile)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       63    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        4    0.000    0.000    0.000    0.000 entity.py:166(create)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       61    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
      947    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        4    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
       60    0.000    0.000    0.000    0.000 entity.py:37(get_player)
       39    0.000    0.000    0.000    0.000 entity.py:322(add_component)
       63    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
      469    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
      284    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      120    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
      469    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
      912    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       13    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
       54    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
       63    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       63    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
       68    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       68    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
       39    0.000    0.000    0.000    0.000 esper.py:196(add_component)
        1    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
        1    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
      477    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       63    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       66    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
      126    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       63    0.000    0.000    0.000    0.000 __init__.py:432(format)
        7    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
        1    0.000    0.000    0.000    0.000 main.py:211(initialise_event_handlers)
       28    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
      392    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
      469    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       14    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       54    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
      469    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        4    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
        5    0.000    0.000    0.000    0.000 esper.py:274(get_components)
      126    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        7    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        4    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      458    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       10    0.000    0.000    0.000    0.000 entity.py:96(get_name)
      126    0.000    0.000    0.000    0.000 __init__.py:856(release)
        3    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       63    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        5    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        3    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        4    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
      455    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      329    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        1    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
       68    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
       63    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      364    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       16    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       63    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        6    0.000    0.000    0.000    0.000 esper.py:270(get_component)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
       10    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      126    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        1    0.000    0.000    0.000    0.000 entity.py:417(consider_intervening)
       63    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       63    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      189    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      225    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       63    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       15    0.000    0.000    0.000    0.000 event_core.py:38(publish)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
       66    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
       14    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
      247    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
       63    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
      216    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       13    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        6    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
       65    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        1    0.000    0.000    0.000    0.000 skill.py:256(_process_trigger_skill_effect)
       39    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
       68    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
      199    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
      128    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       12    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       88    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        2    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       61    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
      303    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       60    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
      121    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       63    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       15    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
        4    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      106    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        2    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
        4    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
       64    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
      132    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       32    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       63    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       60    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       63    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        6    0.000    0.000    0.000    0.000 event.py:97(__init__)
        4    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
       18    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
       10    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        4    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        2    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      128    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       15    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        6    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        1    0.000    0.000    0.000    0.000 entity.py:67(get_entities_and_components_in_area)
        2    0.000    0.000    0.000    0.000 event.py:63(__init__)
       33    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 entity.py:367(spend_time)
       11    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       28    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
       78    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
       37    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       16    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
       21    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        7    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        1    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        4    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        4    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       84    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       14    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
       18    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        9    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        4    0.000    0.000    0.000    0.000 {built-in method math.sin}
        2    0.000    0.000    0.000    0.000 event.py:79(__init__)
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
        4    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
        7    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        1    0.000    0.000    0.000    0.000 main.py:161(disable_profiling)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       11    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       26    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 event.py:136(__init__)
        1    0.000    0.000    0.000    0.000 event.py:89(__init__)
        1    0.000    0.000    0.000    0.000 event.py:29(__init__)
       43    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        4    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        9    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        5    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 event.py:118(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        4    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        1    0.000    0.000    0.000    0.000 event.py:184(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        3    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        4    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        4    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       15    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        7    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        4    0.000    0.000    0.000    0.000 component.py:87(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       10    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        6    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:114(get_turn_holder)
        5    0.000    0.000    0.000    0.000 chrono.py:135(get_time)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 component.py:189(__init__)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
       14    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        3    0.000    0.000    0.000    0.000 component.py:61(__init__)
        3    0.000    0.000    0.000    0.000 component.py:69(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:158(set_turn_holder)
        8    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        4    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       11    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        3    0.000    0.000    0.000    0.000 component.py:37(__init__)
        3    0.000    0.000    0.000    0.000 component.py:138(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       12    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       15    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:105(add_time)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        5    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        2    0.000    0.000    0.000    0.000 component.py:78(__init__)
        2    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        3    0.000    0.000    0.000    0.000 entity.py:77(<genexpr>)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        2    0.000    0.000    0.000    0.000 chrono.py:142(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 component.py:181(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        4    0.000    0.000    0.000    0.000 chrono.py:128(get_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:172(set_turn_queue)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:97(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        2    0.000    0.000    0.000    0.000 chrono.py:165(set_time_in_round)
        2    0.000    0.000    0.000    0.000 component.py:115(__init__)
        1    0.000    0.000    0.000    0.000 component.py:123(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:179(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF955F79BA0}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 component.py:106(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        1    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        1    0.000    0.000    0.000    0.000 chrono.py:121(get_turn_queue)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


