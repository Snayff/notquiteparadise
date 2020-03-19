Wed Mar 18 14:25:36 2020    logs/profiling/profile.dump

         2701188 function calls (2596303 primitive calls) in 43.541 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.214    0.214   43.498   43.498 main.py:78(game_loop)
      594    0.001    0.000   23.798    0.040 event_core.py:21(update)
        4    0.000    0.000   23.118    5.780 interaction_handler.py:25(process_event)
        2    0.000    0.000   23.118   11.559 interaction_handler.py:86(_process_entity_collision)
        2    0.000    0.000   23.117   11.559 interaction_handler.py:121(_apply_effects_to_tiles)
        2    0.000    0.000   23.116   11.558 skill.py:201(process_effect)
        2   23.111   11.555   23.115   11.557 skill.py:227(_process_trigger_skill_effect)
     1188   13.714    0.012   13.714    0.012 {method 'tick' of 'Clock' objects}
      594    0.003    0.000    7.042    0.012 state.py:63(update_clock)
      594    0.004    0.000    6.678    0.011 state.py:38(get_delta_time)
      594    0.010    0.000    2.855    0.005 manager.py:73(draw)
      594    0.003    0.000    2.694    0.005 manager.py:54(update)
      594    0.174    0.000    2.691    0.005 ui_manager.py:122(update)
   191765    2.026    0.000    2.026    0.000 {method 'blit' of 'pygame.Surface' objects}
      594    0.092    0.000    1.608    0.003 sprite.py:453(update)
      597    0.550    0.001    1.170    0.002 camera.py:79(update_game_map)
      593    0.004    0.000    1.167    0.002 camera.py:72(update)
      594    0.005    0.000    1.111    0.002 ui_manager.py:173(draw_ui)
      594    0.178    0.000    1.106    0.002 sprite.py:753(draw)
      598    0.793    0.001    0.793    0.001 {built-in method pygame.transform.scale}
    93284    0.388    0.000    0.701    0.000 ui_element.py:121(check_hover)
       19    0.000    0.000    0.662    0.035 ui_handler.py:30(process_event)
        4    0.000    0.000    0.644    0.161 ui_handler.py:207(update_camera)
        4    0.000    0.000    0.634    0.159 manager.py:295(update_camera_grid)
        4    0.004    0.001    0.634    0.159 camera.py:106(update_grid)
      605    0.008    0.000    0.622    0.001 ui_button.py:30(__init__)
      605    0.033    0.000    0.584    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        5    0.000    0.000    0.485    0.097 ui_handler.py:48(process_entity_event)
    17620    0.043    0.000    0.469    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
122460/17620    0.399    0.000    0.423    0.000 ui_appearance_theme.py:322(get_next_id_node)
    91915    0.178    0.000    0.310    0.000 ui_button.py:197(update)
     9110    0.024    0.000    0.265    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
      594    0.219    0.000    0.219    0.000 {built-in method pygame.display.flip}
    91915    0.108    0.000    0.218    0.000 ui_button.py:138(hover_point)
      594    0.189    0.000    0.189    0.000 {built-in method pygame.event.get}
     5737    0.174    0.000    0.184    0.000 sprite.py:913(get_sprites_from_layer)
       12    0.000    0.000    0.172    0.014 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.167    0.167 ui_handler.py:111(init_game_ui)
     5480    0.011    0.000    0.155    0.000 ui_appearance_theme.py:428(get_misc_data)
    89553    0.133    0.000    0.133    0.000 camera.py:234(world_to_screen_position)
    91915    0.097    0.000    0.109    0.000 rect_drawable_shape.py:84(collide_point)
    91915    0.049    0.000    0.096    0.000 drawable_shape.py:36(update)
      861    0.086    0.000    0.086    0.000 {method 'fill' of 'pygame.Surface' objects}
   189534    0.065    0.000    0.078    0.000 sprite.py:208(alive)
      605    0.004    0.000    0.072    0.000 ui_button.py:97(set_any_images_from_theme)
     2420    0.004    0.000    0.069    0.000 ui_appearance_theme.py:366(get_image)
     2880    0.018    0.000    0.055    0.000 rect_drawable_shape.py:118(redraw_state)
        1    0.000    0.000    0.043    0.043 main.py:183(initialise_game)
        2    0.000    0.000    0.039    0.020 entity.py:225(create_actor)
    91915    0.037    0.000    0.037    0.000 ui_button.py:154(can_hover)
      605    0.005    0.000    0.036    0.000 ui_button.py:537(rebuild_shape)
   425096    0.035    0.000    0.035    0.000 {method 'append' of 'list' objects}
        2    0.008    0.004    0.032    0.016 world.py:26(create_fov_map)
      610    0.002    0.000    0.032    0.000 rect_drawable_shape.py:22(__init__)
      620    0.006    0.000    0.029    0.000 ui_element.py:23(__init__)
      610    0.009    0.000    0.028    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      605    0.003    0.000    0.024    0.000 ui_appearance_theme.py:405(get_font)
      183    0.001    0.000    0.023    0.000 screen_message.py:34(update)
      776    0.006    0.000    0.020    0.000 ui_text_box.py:205(update)
      123    0.001    0.000    0.019    0.000 ui_text_box.py:347(redraw_from_chunks)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
    97619    0.018    0.000    0.018    0.000 ui_manager.py:167(get_mouse_position)
      610    0.003    0.000    0.017    0.000 drawable_shape.py:45(redraw_all_states)
       33    0.000    0.000    0.016    0.000 manager.py:60(process_ui_events)
     2898    0.016    0.000    0.016    0.000 {method 'copy' of 'pygame.Surface' objects}
   294037    0.016    0.000    0.016    0.000 {built-in method builtins.len}
       33    0.006    0.000    0.016    0.000 ui_manager.py:86(process_events)
     2880    0.015    0.000    0.015    0.000 surface_cache.py:119(build_cache_id)
    96843    0.014    0.000    0.014    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     3559    0.010    0.000    0.014    0.000 ui_container.py:124(check_hover)
    92831    0.014    0.000    0.014    0.000 {method 'union' of 'pygame.Rect' objects}
      620    0.002    0.000    0.014    0.000 ui_container.py:42(add_element)
   189534    0.013    0.000    0.013    0.000 {built-in method _operator.truth}
      123    0.002    0.000    0.013    0.000 ui_text_box.py:327(redraw_from_text_block)
     3616    0.008    0.000    0.013    0.000 world.py:55(get_tile)
       17    0.000    0.000    0.012    0.001 entity_handler.py:28(process_event)
    99400    0.012    0.000    0.012    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        4    0.002    0.001    0.011    0.003 ui_container.py:116(clear)
       90    0.001    0.000    0.011    0.000 __init__.py:1496(_log)
       76    0.000    0.000    0.010    0.000 __init__.py:1996(debug)
        5    0.000    0.000    0.010    0.002 ui_text_box.py:50(__init__)
     1074    0.010    0.000    0.010    0.000 ui_container.py:62(recalculate_container_layer_thickness)
       76    0.000    0.000    0.010    0.000 __init__.py:1361(debug)
        5    0.000    0.000    0.010    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     4504    0.009    0.000    0.009    0.000 {built-in method _warnings.warn}
      594    0.002    0.000    0.009    0.000 processors.py:16(process_all)
        5    0.000    0.000    0.009    0.002 ui_text_box.py:110(rebuild)
      620    0.001    0.000    0.008    0.000 sprite.py:121(__init__)
      450    0.001    0.000    0.008    0.000 ui_button.py:130(kill)
        3    0.000    0.000    0.008    0.003 entity_handler.py:53(_process_move)
      454    0.001    0.000    0.008    0.000 ui_element.py:114(kill)
        1    0.002    0.002    0.008    0.008 world.py:445(update_tile_visibility)
      620    0.003    0.000    0.007    0.000 sprite.py:126(add)
        5    0.000    0.000    0.007    0.001 ui_text_box.py:310(parse_html_into_style_data)
       62    0.000    0.000    0.007    0.000 ui_text_box.py:462(set_active_effect)
        4    0.000    0.000    0.007    0.002 manager.py:286(update_camera_game_map)
      594    0.007    0.000    0.007    0.000 processors.py:23(_process_aesthetic_update)
      627    0.004    0.000    0.006    0.000 sprite.py:814(layers)
        2    0.000    0.000    0.006    0.003 entity.py:328(build_characteristic_sprites)
        5    0.000    0.000    0.006    0.001 text_block.py:16(__init__)
        5    0.000    0.000    0.006    0.001 text_block.py:40(redraw)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
     2966    0.005    0.000    0.006    0.000 ui_window.py:97(update)
      620    0.001    0.000    0.006    0.000 ui_element.py:104(change_layer)
      123    0.002    0.000    0.006    0.000 text_block.py:265(redraw_from_chunks)
       90    0.000    0.000    0.006    0.000 __init__.py:1521(handle)
       90    0.000    0.000    0.005    0.000 __init__.py:1575(callHandlers)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      632    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
       90    0.000    0.000    0.005    0.000 __init__.py:892(handle)
      454    0.001    0.000    0.005    0.000 ui_container.py:52(remove_element)
     1188    0.005    0.000    0.005    0.000 sprite.py:745(sprites)
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
        3    0.000    0.000    0.005    0.002 message_log.py:49(add_message)
    70040    0.005    0.000    0.005    0.000 {method 'reverse' of 'list' objects}
      628    0.004    0.000    0.004    0.000 sprite.py:822(change_layer)
       90    0.000    0.000    0.004    0.000 __init__.py:1123(emit)
      594    0.003    0.000    0.004    0.000 ui_manager.py:158(update_mouse_position)
      620    0.004    0.000    0.004    0.000 sprite.py:646(add_internal)
     2880    0.004    0.000    0.004    0.000 drawable_shape.py:122(rebuild_images_and_text)
       90    0.000    0.000    0.004    0.000 __init__.py:1022(emit)
      594    0.002    0.000    0.004    0.000 ui_appearance_theme.py:158(update_shape_cache)
     3621    0.004    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
       12    0.000    0.000    0.004    0.000 game_handler.py:26(process_event)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
       90    0.000    0.000    0.004    0.000 __init__.py:1481(makeRecord)
       90    0.001    0.000    0.003    0.000 __init__.py:293(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
      593    0.002    0.000    0.003    0.000 skill_bar.py:45(update)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
        4    0.000    0.000    0.003    0.001 manager.py:275(update_cameras_tiles)
        4    0.001    0.000    0.003    0.001 camera.py:168(update_camera_tiles)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        2    0.000    0.000    0.003    0.001 ui_handler.py:155(process_ui_event)
        2    0.000    0.000    0.003    0.001 ui_handler.py:238(process_message)
        2    0.000    0.000    0.003    0.001 manager.py:444(add_to_message_log)
     1257    0.003    0.000    0.003    0.000 {built-in method builtins.sorted}
      594    0.001    0.000    0.003    0.000 surface_cache.py:24(update)
     3410    0.002    0.000    0.002    0.000 ui_button.py:257(process_event)
      454    0.001    0.000    0.002    0.000 sprite.py:183(kill)
      593    0.001    0.000    0.002    0.000 message_log.py:36(update)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       90    0.000    0.000    0.002    0.000 __init__.py:869(format)
      4/3    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
       90    0.000    0.000    0.002    0.000 __init__.py:606(format)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
     1369    0.001    0.000    0.002    0.000 ui_element.py:186(hover_point)
      593    0.001    0.000    0.002    0.000 entity_info.py:45(update)
     12/8    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
       14    0.000    0.000    0.002    0.000 __init__.py:1986(info)
       14    0.000    0.000    0.002    0.000 __init__.py:1373(info)
     1201    0.002    0.000    0.002    0.000 state.py:45(get_current)
       31    0.002    0.000    0.002    0.000 {built-in method nt.stat}
      610    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
        5    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
      454    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
        2    0.000    0.000    0.002    0.001 entity_handler.py:131(_process_skill)
     2880    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
        6    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        7    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
      216    0.001    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
       90    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
        3    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:233(_insert_code)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
      616    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
        2    0.000    0.000    0.001    0.001 __init__.py:133(reload)
       32    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.001    0.001 __init__.py:109(import_module)
      3/2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:994(_gcd_import)
       95    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
        5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
      594    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
       14    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
        8    0.000    0.000    0.001    0.000 game_handler.py:42(process_change_game_state)
        5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
     3598    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
        3    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
       95    0.001    0.000    0.001    0.000 ntpath.py:178(split)
     7242    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
        3    0.000    0.000    0.001    0.000 game_handler.py:81(process_end_turn)
       90    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
        3    0.000    0.000    0.001    0.000 chrono.py:50(next_turn)
        3    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
        9    0.001    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        5    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
       90    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
       90    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        7    0.000    0.000    0.001    0.000 state.py:71(set_new)
      633    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
        5    0.000    0.000    0.001    0.000 god_handler.py:26(process_event)
      610    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:610(_exec)
       20    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
    16/14    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
     1100    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       10    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.__import__}
     2440    0.001    0.000    0.001    0.000 {built-in method math.floor}
     4152    0.001    0.000    0.001    0.000 sprite.py:168(update)
        5    0.000    0.000    0.001    0.000 parser.py:104(feed)
        5    0.000    0.000    0.001    0.000 parser.py:134(goahead)
      597    0.001    0.000    0.001    0.000 {built-in method builtins.any}
     2966    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
       90    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
       91    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       33    0.000    0.000    0.001    0.000 processors.py:57(process_intent)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
       10    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:914(get_data)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
     4447    0.000    0.000    0.001    0.000 {built-in method builtins.isinstance}
       90    0.001    0.000    0.001    0.000 {built-in method time.strftime}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
      648    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
       11    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      610    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
      330    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.print}
      190    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
     2145    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
     2880    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        8    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 entity.py:294(create_projectile)
     1230    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       22    0.000    0.000    0.000    0.000 processors.py:138(_process_player_turn_intents)
        5    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
     1248    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
     1369    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
       90    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
      105    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
     1220    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        5    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        2    0.000    0.000    0.000    0.000 skill.py:73(can_afford_cost)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
      611    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       33    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        2    0.000    0.000    0.000    0.000 skill.py:92(pay_resource_cost)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 chrono.py:23(rebuild_turn_queue)
       26    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        7    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
       90    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        5    0.000    0.000    0.000    0.000 entity.py:166(create)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
     1249    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
      669    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       62    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
      620    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       90    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       19    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
       61    0.000    0.000    0.000    0.000 text_effects.py:88(update)
       90    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 basic_attack.py:8(use)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       43    0.000    0.000    0.000    0.000 entity.py:321(add_component)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
       90    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
     1212    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       13    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
       43    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
      180    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
      628    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       90    0.000    0.000    0.000    0.000 __init__.py:432(format)
       43    0.000    0.000    0.000    0.000 esper.py:196(add_component)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
       13    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        8    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
       21    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        7    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        6    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
        5    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
      620    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      128    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        8    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      619    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        7    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        2    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        2    0.000    0.000    0.000    0.000 entity.py:416(consider_intervening)
       15    0.000    0.000    0.000    0.000 entity.py:96(get_name)
      620    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
       90    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
      180    0.000    0.000    0.000    0.000 __init__.py:856(release)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        4    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      609    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
      487    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       90    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       30    0.000    0.000    0.000    0.000 entity.py:37(get_player)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        9    0.000    0.000    0.000    0.000 esper.py:270(get_component)
       90    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
      128    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
      180    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       22    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
       15    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       23    0.000    0.000    0.000    0.000 event_core.py:38(publish)
      270    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
       90    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       90    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       90    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      505    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      308    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        5    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        3    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
      330    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       90    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        9    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
       33    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
      121    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       22    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
      455    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        9    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
       33    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      182    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      258    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       95    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      288    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
       43    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
      454    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      118    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       35    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       17    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       90    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       10    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       29    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        1    0.000    0.000    0.000    0.000 main.py:210(initialise_event_handlers)
        3    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        3    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
      165    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        2    0.000    0.000    0.000    0.000 world.py:77(get_direction)
       62    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        7    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       23    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
      159    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       27    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
       49    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       93    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        2    0.000    0.000    0.000    0.000 random.py:344(choices)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        5    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      123    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
       61    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
      194    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       90    0.000    0.000    0.000    0.000 {built-in method time.time}
       22    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
       14    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       28    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       90    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       16    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        8    0.000    0.000    0.000    0.000 event.py:87(__init__)
       50    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        3    0.000    0.000    0.000    0.000 entity_handler.py:229(_process_end_turn)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
       23    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        8    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        2    0.000    0.000    0.000    0.000 entity.py:67(get_entities_and_components_in_area)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       30    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        3    0.000    0.000    0.000    0.000 event.py:53(__init__)
      182    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        5    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        8    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       43    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
       61    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       18    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        3    0.000    0.000    0.000    0.000 entity.py:366(spend_time)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        2    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       29    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       29    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       13    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
       86    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        6    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
       47    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        3    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
      144    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        9    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        2    0.000    0.000    0.000    0.000 event.py:30(__init__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       14    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
       17    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        7    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        2    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       16    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 event.py:126(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       23    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        3    0.000    0.000    0.000    0.000 event.py:69(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
       21    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
       36    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 {built-in method math.sin}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 event.py:108(__init__)
        8    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        2    0.000    0.000    0.000    0.000 event.py:174(__init__)
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
       10    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        4    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       15    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       25    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        5    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
        5    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       10    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        7    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
       53    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
        1    0.000    0.000    0.000    0.000 event.py:79(__init__)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        7    0.000    0.000    0.000    0.000 chrono.py:135(get_time)
        5    0.000    0.000    0.000    0.000 component.py:87(__init__)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
       10    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        1    0.000    0.000    0.000    0.000 main.py:160(disable_profiling)
       29    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        5    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        2    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       14    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        9    0.000    0.000    0.000    0.000 chrono.py:114(get_turn_holder)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 ai.py:34(__init__)
       20    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        1    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       29    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        4    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
       18    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
       11    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 chrono.py:105(add_time)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        9    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        5    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        5    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        5    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       17    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        7    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        2    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        4    0.000    0.000    0.000    0.000 component.py:37(__init__)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        4    0.000    0.000    0.000    0.000 component.py:61(__init__)
        6    0.000    0.000    0.000    0.000 entity.py:77(<genexpr>)
        3    0.000    0.000    0.000    0.000 component.py:138(__init__)
        9    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        5    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        6    0.000    0.000    0.000    0.000 chrono.py:128(get_time_in_round)
        2    0.000    0.000    0.000    0.000 chrono.py:158(set_turn_holder)
        2    0.000    0.000    0.000    0.000 component.py:188(__init__)
        3    0.000    0.000    0.000    0.000 component.py:69(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        9    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        3    0.000    0.000    0.000    0.000 chrono.py:142(get_time_of_last_turn)
        8    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        1    0.000    0.000    0.000    0.000 entity_handler.py:25(__init__)
        2    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        3    0.000    0.000    0.000    0.000 chrono.py:165(set_time_in_round)
        2    0.000    0.000    0.000    0.000 component.py:78(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        3    0.000    0.000    0.000    0.000 chrono.py:179(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        3    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF9662B9BA0}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        2    0.000    0.000    0.000    0.000 component.py:123(__init__)
        1    0.000    0.000    0.000    0.000 component.py:180(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:115(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:172(set_turn_queue)
        4    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 component.py:97(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 component.py:106(__init__)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 chrono.py:121(get_turn_queue)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


