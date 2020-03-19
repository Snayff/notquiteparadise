Thu Mar 19 11:53:24 2020    logs/profiling/profile.dump

         8024182 function calls (7945431 primitive calls) in 80.198 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.833    0.833   80.156   80.156 main.py:79(game_loop)
     4532   51.996    0.011   51.996    0.011 {method 'tick' of 'Clock' objects}
     2266    0.011    0.000   26.935    0.012 state.py:63(update_clock)
     2266    0.015    0.000   25.087    0.011 state.py:38(get_delta_time)
     2266    0.038    0.000   11.291    0.005 manager.py:73(draw)
     2266    0.011    0.000   10.330    0.005 manager.py:54(update)
     2266    0.641    0.000   10.319    0.005 ui_manager.py:122(update)
   728321    7.914    0.000    7.914    0.000 {method 'blit' of 'pygame.Surface' objects}
     2266    0.363    0.000    6.115    0.003 sprite.py:453(update)
     2266    0.003    0.000    4.866    0.002 event_core.py:21(update)
     2265    0.014    0.000    4.602    0.002 camera.py:72(update)
     2268    2.183    0.001    4.590    0.002 camera.py:79(update_game_map)
     2266    0.020    0.000    4.397    0.002 ui_manager.py:173(draw_ui)
     2266    0.712    0.000    4.376    0.002 sprite.py:753(draw)
       13    0.000    0.000    4.349    0.335 entity_handler.py:29(process_event)
        1    4.335    4.335    4.336    4.336 entity_handler.py:244(_process_created_timed_entity)
     2270    3.174    0.001    3.174    0.001 {built-in method pygame.transform.scale}
   355789    1.556    0.000    2.772    0.000 ui_element.py:121(check_hover)
   351075    0.692    0.000    1.063    0.000 ui_button.py:197(update)
     2266    0.848    0.000    0.848    0.000 {built-in method pygame.display.flip}
   351072    0.432    0.000    0.843    0.000 ui_button.py:138(hover_point)
    21473    0.660    0.000    0.698    0.000 sprite.py:913(get_sprites_from_layer)
     2266    0.694    0.000    0.694    0.000 {built-in method pygame.event.get}
   340203    0.515    0.000    0.515    0.000 camera.py:234(world_to_screen_position)
       15    0.000    0.000    0.509    0.034 ui_handler.py:30(process_event)
        3    0.000    0.000    0.492    0.164 ui_handler.py:207(update_camera)
        3    0.000    0.000    0.485    0.162 manager.py:295(update_camera_grid)
        3    0.003    0.001    0.485    0.162 camera.py:106(update_grid)
      455    0.006    0.000    0.477    0.001 ui_button.py:30(__init__)
      455    0.025    0.000    0.448    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
   351231    0.362    0.000    0.411    0.000 rect_drawable_shape.py:84(collide_point)
    13255    0.033    0.000    0.358    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
        4    0.000    0.000    0.332    0.083 ui_handler.py:48(process_entity_event)
     2532    0.329    0.000    0.329    0.000 {method 'fill' of 'pygame.Surface' objects}
91965/13255    0.305    0.000    0.323    0.000 ui_appearance_theme.py:322(get_next_id_node)
   722904    0.257    0.000    0.309    0.000 sprite.py:208(alive)
   351075    0.175    0.000    0.232    0.000 drawable_shape.py:36(update)
     6853    0.018    0.000    0.203    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
        9    0.000    0.000    0.174    0.019 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.168    0.168 ui_handler.py:111(init_game_ui)
   351075    0.146    0.000    0.146    0.000 ui_button.py:154(can_hover)
     4123    0.008    0.000    0.118    0.000 ui_appearance_theme.py:428(get_misc_data)
   964316    0.100    0.000    0.100    0.000 {method 'append' of 'list' objects}
      110    0.001    0.000    0.074    0.001 manager.py:60(process_ui_events)
      110    0.026    0.000    0.074    0.001 ui_manager.py:86(process_events)
   371826    0.061    0.000    0.061    0.000 ui_manager.py:167(get_mouse_position)
    13591    0.041    0.000    0.057    0.000 ui_container.py:124(check_hover)
      455    0.003    0.000    0.055    0.000 ui_button.py:97(set_any_images_from_theme)
   355487    0.055    0.000    0.055    0.000 {method 'union' of 'pygame.Rect' objects}
   369623    0.054    0.000    0.054    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     1820    0.003    0.000    0.052    0.000 ui_appearance_theme.py:366(get_image)
   722904    0.052    0.000    0.052    0.000 {built-in method _operator.truth}
   380448    0.045    0.000    0.045    0.000 {method 'colliderect' of 'pygame.Rect' objects}
     2279    0.015    0.000    0.044    0.000 rect_drawable_shape.py:118(redraw_state)
        1    0.000    0.000    0.042    0.042 main.py:184(initialise_game)
        2    0.000    0.000    0.039    0.019 entity.py:225(create_actor)
     2266    0.009    0.000    0.037    0.000 processors.py:16(process_all)
     2449    0.020    0.000    0.035    0.000 ui_text_box.py:205(update)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
   503120    0.030    0.000    0.030    0.000 {built-in method builtins.len}
      455    0.004    0.000    0.029    0.000 ui_button.py:537(rebuild_shape)
     2266    0.028    0.000    0.028    0.000 processors.py:23(_process_aesthetic_update)
    11326    0.022    0.000    0.026    0.000 ui_window.py:97(update)
      459    0.002    0.000    0.026    0.000 rect_drawable_shape.py:22(__init__)
     2376    0.017    0.000    0.025    0.000 sprite.py:814(layers)
      459    0.007    0.000    0.023    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      469    0.005    0.000    0.022    0.000 ui_element.py:23(__init__)
      184    0.001    0.000    0.022    0.000 screen_message.py:34(update)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
      123    0.001    0.000    0.018    0.000 ui_text_box.py:347(redraw_from_chunks)
      455    0.002    0.000    0.018    0.000 ui_appearance_theme.py:405(get_font)
     4532    0.017    0.000    0.017    0.000 sprite.py:745(sprites)
     2266    0.011    0.000    0.017    0.000 ui_manager.py:158(update_mouse_position)
     2266    0.007    0.000    0.014    0.000 ui_appearance_theme.py:158(update_shape_cache)
      459    0.002    0.000    0.014    0.000 drawable_shape.py:45(redraw_all_states)
     2265    0.006    0.000    0.013    0.000 skill_bar.py:45(update)
     2297    0.013    0.000    0.013    0.000 {method 'copy' of 'pygame.Surface' objects}
      123    0.002    0.000    0.013    0.000 ui_text_box.py:327(redraw_from_text_block)
     2279    0.012    0.000    0.012    0.000 surface_cache.py:119(build_cache_id)
     3460    0.007    0.000    0.012    0.000 world.py:55(get_tile)
    14573    0.011    0.000    0.011    0.000 ui_button.py:257(process_event)
     4754    0.010    0.000    0.010    0.000 {built-in method builtins.sorted}
      469    0.001    0.000    0.010    0.000 ui_container.py:42(add_element)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
     2265    0.005    0.000    0.010    0.000 message_log.py:36(update)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:50(__init__)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
       68    0.000    0.000    0.009    0.000 __init__.py:1496(_log)
       59    0.000    0.000    0.008    0.000 __init__.py:1996(debug)
        4    0.000    0.000    0.008    0.002 ui_text_box.py:110(rebuild)
       59    0.000    0.000    0.008    0.000 __init__.py:1361(debug)
        2    0.000    0.000    0.008    0.004 entity_handler.py:57(_process_move)
        1    0.002    0.002    0.008    0.008 world.py:445(update_tile_visibility)
     2265    0.004    0.000    0.007    0.000 entity_info.py:45(update)
        3    0.001    0.000    0.007    0.002 ui_container.py:116(clear)
      772    0.007    0.000    0.007    0.000 ui_container.py:62(recalculate_container_layer_thickness)
        4    0.000    0.000    0.007    0.002 ui_text_box.py:310(parse_html_into_style_data)
      903    0.007    0.000    0.007    0.000 ui_manager.py:104(<listcomp>)
       62    0.000    0.000    0.007    0.000 ui_text_box.py:462(set_active_effect)
      469    0.001    0.000    0.007    0.000 sprite.py:121(__init__)
     2266    0.003    0.000    0.006    0.000 surface_cache.py:24(update)
        4    0.000    0.000    0.006    0.002 text_block.py:16(__init__)
        4    0.000    0.000    0.006    0.002 text_block.py:40(redraw)
        2    0.000    0.000    0.006    0.003 entity.py:329(build_characteristic_sprites)
     4543    0.006    0.000    0.006    0.000 state.py:45(get_current)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
     4714    0.005    0.000    0.006    0.000 ui_element.py:186(hover_point)
      300    0.000    0.000    0.006    0.000 ui_button.py:130(kill)
      469    0.002    0.000    0.006    0.000 sprite.py:126(add)
      303    0.001    0.000    0.005    0.000 ui_element.py:114(kill)
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
      123    0.002    0.000    0.005    0.000 text_block.py:265(redraw_from_chunks)
     2266    0.005    0.000    0.005    0.000 {built-in method pygame.mouse.get_pos}
        3    0.000    0.000    0.005    0.002 manager.py:286(update_camera_game_map)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      470    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
       68    0.000    0.000    0.005    0.000 __init__.py:1521(handle)
      469    0.001    0.000    0.004    0.000 ui_element.py:104(change_layer)
       68    0.000    0.000    0.004    0.000 __init__.py:1575(callHandlers)
    11807    0.004    0.000    0.004    0.000 ui_window.py:107(get_container)
       68    0.000    0.000    0.004    0.000 __init__.py:892(handle)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     3463    0.003    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
       50    0.004    0.000    0.004    0.000 {built-in method nt.stat}
       68    0.000    0.000    0.004    0.000 __init__.py:1123(emit)
     2279    0.003    0.000    0.004    0.000 drawable_shape.py:122(rebuild_images_and_text)
       68    0.000    0.000    0.004    0.000 __init__.py:1022(emit)
    52610    0.004    0.000    0.004    0.000 {method 'reverse' of 'list' objects}
        9    0.000    0.000    0.003    0.000 game_handler.py:26(process_event)
      469    0.003    0.000    0.003    0.000 sprite.py:646(add_internal)
      477    0.003    0.000    0.003    0.000 sprite.py:822(change_layer)
       37    0.000    0.000    0.003    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      303    0.001    0.000    0.003    0.000 ui_container.py:52(remove_element)
        2    0.000    0.000    0.003    0.002 message_log.py:49(add_message)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 entity_handler.py:135(_process_use_skill)
       68    0.000    0.000    0.003    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
    15856    0.003    0.000    0.003    0.000 sprite.py:168(update)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        1    0.000    0.000    0.003    0.003 skill.py:111(use)
       68    0.001    0.000    0.003    0.000 __init__.py:293(__init__)
     2268    0.003    0.000    0.003    0.000 {built-in method builtins.any}
        1    0.000    0.000    0.002    0.002 skill.py:150(_call_skill_func)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
    11326    0.002    0.000    0.002    0.000 ui_window.py:116(check_hover)
        3    0.000    0.000    0.002    0.001 manager.py:275(update_cameras_tiles)
        3    0.001    0.000    0.002    0.001 camera.py:168(update_camera_tiles)
       68    0.000    0.000    0.002    0.000 __init__.py:869(format)
       68    0.000    0.000    0.002    0.000 __init__.py:606(format)
      303    0.000    0.000    0.002    0.000 sprite.py:183(kill)
        1    0.000    0.000    0.002    0.002 __init__.py:109(import_module)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:994(_gcd_import)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
      459    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
     4714    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
      783    0.001    0.000    0.001    0.000 ui_button.py:170(while_hovering)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
        2    0.000    0.000    0.001    0.001 ui_handler.py:155(process_ui_event)
        1    0.000    0.000    0.001    0.001 ui_handler.py:238(process_message)
       29    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.001    0.001 manager.py:444(add_to_message_log)
        4    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
      110    0.001    0.000    0.001    0.000 action.py:12(convert_to_intent)
        1    0.000    0.000    0.001    0.001 interaction_handler.py:25(process_event)
     2279    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
       69    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
       68    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      465    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
        9    0.000    0.000    0.001    0.000 __init__.py:1986(info)
       73    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
      303    0.001    0.000    0.001    0.000 sprite.py:728(remove_internal)
        9    0.000    0.000    0.001    0.000 __init__.py:1373(info)
        1    0.000    0.000    0.001    0.001 interaction_handler.py:86(_process_entity_collision)
        1    0.000    0.000    0.001    0.001 interaction_handler.py:121(_apply_effects_to_tiles)
        8    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        6    0.000    0.000    0.001    0.000 game_handler.py:42(process_change_game_state)
      7/5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
     2495    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}
     6927    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
       73    0.001    0.000    0.001    0.000 ntpath.py:178(split)
       68    0.000    0.000    0.001    0.000 __init__.py:1451(findCaller)
        2    0.000    0.000    0.001    0.000 game_handler.py:81(process_end_turn)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
       68    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
        2    0.000    0.000    0.001    0.000 chrono.py:50(next_turn)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
       68    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        5    0.000    0.000    0.001    0.000 state.py:71(set_new)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
      459    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
        3    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:233(_insert_code)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
        2    0.000    0.000    0.001    0.000 chrono.py:23(rebuild_turn_queue)
      471    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
     1836    0.001    0.000    0.001    0.000 {built-in method math.floor}
        4    0.000    0.000    0.001    0.000 god_handler.py:26(process_event)
      797    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      110    0.000    0.000    0.001    0.000 processors.py:57(process_intent)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
      575    0.000    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
        4    0.000    0.000    0.000    0.000 parser.py:104(feed)
        4    0.000    0.000    0.000    0.000 parser.py:134(goahead)
       68    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
     4133    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 __init__.py:133(reload)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
       68    0.000    0.000    0.000    0.000 {built-in method time.strftime}
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      146    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
      459    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
     2279    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
     1583    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
      929    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:610(_exec)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        4    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
      946    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
       83    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      484    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       62    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
      505    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        4    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
       17    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
       68    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        1    0.000    0.000    0.000    0.000 basic_attack.py:8(use)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      923    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      110    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        1    0.000    0.000    0.000    0.000 skill.py:230(process_effect)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      128    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        1    0.000    0.000    0.000    0.000 entity.py:292(create_projectile)
        4    0.000    0.000    0.000    0.000 entity.py:166(create)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        2    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
      947    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       68    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       39    0.000    0.000    0.000    0.000 entity.py:322(add_component)
      672    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      110    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
       61    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        4    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
       68    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      127    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
       68    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
      469    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       13    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
       68    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
      912    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       39    0.000    0.000    0.000    0.000 esper.py:196(add_component)
      159    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
      136    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
      477    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        1    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
       68    0.000    0.000    0.000    0.000 __init__.py:432(format)
        1    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        1    0.000    0.000    0.000    0.000 main.py:211(initialise_event_handlers)
        7    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
       14    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
       31    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
      469    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      469    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 processors.py:138(_process_player_turn_intents)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        5    0.000    0.000    0.000    0.000 esper.py:274(get_components)
      128    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      103    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
       13    0.000    0.000    0.000    0.000 entity.py:96(get_name)
      469    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
      136    0.000    0.000    0.000    0.000 __init__.py:856(release)
       68    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        7    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        4    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
      458    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        5    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
        3    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
      102    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        4    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        3    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       68    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        7    0.000    0.000    0.000    0.000 esper.py:270(get_component)
       23    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        4    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       68    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
      455    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        3    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
      330    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
       68    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       13    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
      136    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
       68    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       19    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
       16    0.000    0.000    0.000    0.000 event_core.py:38(publish)
       69    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      241    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      204    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      389    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      262    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
       14    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
        1    0.000    0.000    0.000    0.000 entity.py:417(consider_intervening)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        7    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
       68    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
       68    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      138    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
      226    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       73    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        6    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       39    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
       93    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      207    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        1    0.000    0.000    0.000    0.000 skill.py:256(_process_trigger_skill_effect)
        1    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       62    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        2    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
       12    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       68    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
      303    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        9    0.000    0.000    0.000    0.000 entity.py:37(get_player)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
       61    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        1    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:52(_pydev_stop_at_break)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
       16    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
      123    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        4    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      111    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       71    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       22    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       68    0.000    0.000    0.000    0.000 {built-in method time.time}
        6    0.000    0.000    0.000    0.000 event.py:106(__init__)
        4    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
      143    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
       35    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       61    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       16    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
       16    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        1    0.000    0.000    0.000    0.000 camera.py:58(handle_events)
        4    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
       10    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
      138    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
        4    0.000    0.000    0.000    0.000 parser.py:96(reset)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
       34    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        1    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 event.py:63(__init__)
       39    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        2    0.000    0.000    0.000    0.000 entity.py:367(spend_time)
       31    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        6    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 entity.py:67(get_entities_and_components_in_area)
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        3    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
       11    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
       21    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        1    0.000    0.000    0.000    0.000 _collections_abc.py:657(get)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        7    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
       16    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       78    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       84    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        1    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
        1    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       18    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        9    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        1    0.000    0.000    0.000    0.000 os.py:673(__getitem__)
        1    0.000    0.000    0.000    0.000 main.py:161(disable_profiling)
        4    0.000    0.000    0.000    0.000 {built-in method math.sin}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
       14    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        4    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       27    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 event.py:29(__init__)
       11    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
        2    0.000    0.000    0.000    0.000 event.py:88(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        1    0.000    0.000    0.000    0.000 event.py:174(__init__)
        5    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        1    0.000    0.000    0.000    0.000 event.py:136(__init__)
        4    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        4    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        9    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        7    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        3    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        4    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       45    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 ui_button.py:340(select)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        1    0.000    0.000    0.000    0.000 event.py:184(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        9    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        1    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        4    0.000    0.000    0.000    0.000 component.py:87(__init__)
        4    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
       15    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        4    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        7    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        5    0.000    0.000    0.000    0.000 chrono.py:135(get_time)
        1    0.000    0.000    0.000    0.000 event.py:77(__init__)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        3    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        1    0.000    0.000    0.000    0.000 <string>:1(__init__)
       16    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        1    0.000    0.000    0.000    0.000 os.py:743(encodekey)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:114(get_turn_holder)
        2    0.000    0.000    0.000    0.000 chrono.py:172(set_turn_queue)
        3    0.000    0.000    0.000    0.000 chrono.py:158(set_turn_holder)
        8    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        3    0.000    0.000    0.000    0.000 component.py:69(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        4    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        2    0.000    0.000    0.000    0.000 component.py:189(__init__)
        6    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
       11    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        3    0.000    0.000    0.000    0.000 component.py:37(__init__)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
       12    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        1    0.000    0.000    0.000    0.000 ui_button.py:348(unselect)
        1    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
        1    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        3    0.000    0.000    0.000    0.000 component.py:138(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        1    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
       15    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        3    0.000    0.000    0.000    0.000 component.py:61(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
       15    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:21(update_globals_dict)
        2    0.000    0.000    0.000    0.000 chrono.py:105(add_time)
        4    0.000    0.000    0.000    0.000 chrono.py:128(get_time_in_round)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        4    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        5    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        1    0.000    0.000    0.000    0.000 pydev_log.py:16(debug)
        2    0.000    0.000    0.000    0.000 component.py:78(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:142(get_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        6    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        6    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 component.py:97(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:121(get_turn_queue)
        1    0.000    0.000    0.000    0.000 component.py:181(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.post}
        1    0.000    0.000    0.000    0.000 os.py:737(check_str)
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 component.py:123(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        3    0.000    0.000    0.000    0.000 entity.py:77(<genexpr>)
        2    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF955F79BA0}
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.Event}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        2    0.000    0.000    0.000    0.000 chrono.py:165(set_time_in_round)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:115(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:179(set_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_constants.py:479(get_global_debugger)
        1    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        3    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        2    0.000    0.000    0.000    0.000 component.py:106(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {_pydevd_frame_eval.pydevd_frame_evaluator_win32_37_64.get_thread_info_py}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)
        1    0.000    0.000    0.000    0.000 entity_info.py:51(handle_events)
        1    0.000    0.000    0.000    0.000 message_log.py:42(handle_events)
        1    0.000    0.000    0.000    0.000 skill_bar.py:51(handle_events)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


