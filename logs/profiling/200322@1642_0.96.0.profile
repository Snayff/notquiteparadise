Sun Mar 22 16:42:01 2020    logs/profiling/profile.dump

         3709790 function calls (3496629 primitive calls) in 22.797 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.231    0.231   22.755   22.755 main.py:104(game_loop)
     1298   14.827    0.011   14.827    0.011 {method 'tick' of 'Clock' objects}
      649    0.002    0.000    7.485    0.012 state.py:63(update_clock)
      649    0.003    0.000    7.348    0.011 state.py:38(get_delta_time)
      649    0.009    0.000    3.085    0.005 manager.py:73(draw)
      649    0.002    0.000    2.908    0.004 manager.py:54(update)
      649    0.185    0.000    2.905    0.004 ui_manager.py:122(update)
   213750    2.228    0.000    2.228    0.000 {method 'blit' of 'pygame.Surface' objects}
      649    0.101    0.000    1.719    0.003 sprite.py:453(update)
      649    0.001    0.000    1.393    0.002 event_core.py:24(update)
       46    0.000    0.000    1.359    0.030 ui_handler.py:31(process_event)
        8    0.000    0.000    1.306    0.163 ui_handler.py:201(_update_camera)
        8    0.000    0.000    1.284    0.161 manager.py:295(update_camera_grid)
        8    0.008    0.001    1.284    0.161 camera.py:105(update_grid)
     1220    0.015    0.000    1.272    0.001 ui_button.py:30(__init__)
     1220    0.065    0.000    1.197    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
      649    0.005    0.000    1.185    0.002 ui_manager.py:173(draw_ui)
      649    0.185    0.000    1.180    0.002 sprite.py:753(draw)
      656    0.482    0.001    1.176    0.002 camera.py:79(update_game_map)
      648    0.004    0.000    1.166    0.002 camera.py:72(update)
       11    0.000    0.000    1.139    0.104 ui_handler.py:44(process_entity_event)
    35605    0.089    0.000    0.968    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
248685/35605    0.825    0.000    0.871    0.000 ui_appearance_theme.py:322(get_next_id_node)
      653    0.868    0.001    0.868    0.001 {built-in method pygame.transform.scale}
   104624    0.440    0.000    0.778    0.000 ui_element.py:121(check_hover)
    18404    0.048    0.000    0.546    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   102330    0.194    0.000    0.354    0.000 ui_button.py:197(update)
    11084    0.021    0.000    0.320    0.000 ui_appearance_theme.py:428(get_misc_data)
      649    0.240    0.000    0.240    0.000 {built-in method pygame.display.flip}
   102054    0.120    0.000    0.232    0.000 ui_button.py:138(hover_point)
     6885    0.202    0.000    0.213    0.000 sprite.py:913(get_sprites_from_layer)
       27    0.000    0.000    0.181    0.007 ui_handler.py:68(process_game_event)
      649    0.180    0.000    0.180    0.000 {built-in method pygame.event.get}
        1    0.000    0.000    0.175    0.175 ui_handler.py:107(init_game_ui)
     1220    0.007    0.000    0.150    0.000 ui_button.py:97(set_any_images_from_theme)
     4880    0.009    0.000    0.142    0.000 ui_appearance_theme.py:366(get_image)
    98403    0.141    0.000    0.141    0.000 camera.py:233(world_to_screen_position)
   102330    0.055    0.000    0.122    0.000 drawable_shape.py:36(update)
   102304    0.099    0.000    0.112    0.000 rect_drawable_shape.py:84(collide_point)
     1456    0.099    0.000    0.099    0.000 {method 'fill' of 'pygame.Surface' objects}
   212489    0.073    0.000    0.088    0.000 sprite.py:208(alive)
     4296    0.029    0.000    0.086    0.000 rect_drawable_shape.py:118(redraw_state)
     1220    0.010    0.000    0.072    0.000 ui_button.py:537(rebuild_shape)
      104    0.000    0.000    0.071    0.001 manager.py:60(process_ui_events)
      104    0.025    0.000    0.071    0.001 ui_manager.py:86(process_events)
     1237    0.004    0.000    0.063    0.000 rect_drawable_shape.py:22(__init__)
     1016    0.016    0.000    0.063    0.000 ui_text_box.py:205(update)
     1247    0.012    0.000    0.057    0.000 ui_element.py:23(__init__)
     1237    0.018    0.000    0.056    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
   683304    0.051    0.000    0.051    0.000 {method 'append' of 'list' objects}
     1220    0.005    0.000    0.047    0.000 ui_appearance_theme.py:405(get_font)
       12    0.000    0.000    0.047    0.004 ui_text_box.py:50(__init__)
       12    0.000    0.000    0.046    0.004 ui_text_box.py:492(rebuild_from_changed_theme_data)
       12    0.001    0.000    0.044    0.004 ui_text_box.py:110(rebuild)
        1    0.000    0.000    0.042    0.042 main.py:212(initialise_game)
        9    0.000    0.000    0.041    0.005 message_log.py:49(add_message)
      368    0.002    0.000    0.040    0.000 screen_message.py:34(update)
   102330    0.039    0.000    0.039    0.000 ui_button.py:154(can_hover)
        8    0.000    0.000    0.039    0.005 ui_handler.py:151(process_ui_event)
        8    0.000    0.000    0.039    0.005 ui_handler.py:232(_process_message)
        8    0.000    0.000    0.039    0.005 manager.py:444(add_to_message_log)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      649    0.002    0.000    0.036    0.000 processors.py:18(process_all)
      246    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
     1237    0.006    0.000    0.034    0.000 drawable_shape.py:45(redraw_all_states)
      649    0.018    0.000    0.034    0.000 processors.py:25(_process_aesthetic_update)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
     1247    0.003    0.000    0.027    0.000 ui_container.py:42(add_element)
   510326    0.027    0.000    0.027    0.000 {built-in method builtins.len}
        8    0.005    0.001    0.026    0.003 ui_container.py:116(clear)
      246    0.003    0.000    0.024    0.000 ui_text_box.py:327(redraw_from_text_block)
     4296    0.024    0.000    0.024    0.000 surface_cache.py:119(build_cache_id)
     4356    0.023    0.000    0.023    0.000 {method 'copy' of 'pygame.Surface' objects}
     2324    0.022    0.000    0.022    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     1062    0.001    0.000    0.021    0.000 ui_button.py:130(kill)
        5    0.000    0.000    0.021    0.004 ui_vertical_scroll_bar.py:22(__init__)
     1077    0.002    0.000    0.020    0.000 ui_element.py:114(kill)
     4870    0.015    0.000    0.020    0.000 query.py:212(__iter__)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
       17    0.000    0.000    0.019    0.001 ui_text_box.py:310(parse_html_into_style_data)
   109883    0.018    0.000    0.018    0.000 ui_manager.py:167(get_mouse_position)
     1247    0.002    0.000    0.017    0.000 sprite.py:121(__init__)
       38    0.000    0.000    0.016    0.000 entity_handler.py:26(process_event)
        8    0.000    0.000    0.015    0.002 manager.py:286(update_camera_game_map)
     4222    0.009    0.000    0.015    0.000 world.py:55(get_tile)
   212489    0.015    0.000    0.015    0.000 {built-in method _operator.truth}
   108515    0.015    0.000    0.015    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     1247    0.005    0.000    0.015    0.000 sprite.py:126(add)
     3889    0.011    0.000    0.015    0.000 ui_container.py:124(check_hover)
   103548    0.014    0.000    0.014    0.000 {method 'union' of 'pygame.Rect' objects}
      111    0.001    0.000    0.014    0.000 __init__.py:1496(_log)
       17    0.000    0.000    0.013    0.001 text_block.py:16(__init__)
       17    0.003    0.000    0.013    0.001 text_block.py:40(redraw)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
     1077    0.002    0.000    0.012    0.000 ui_container.py:52(remove_element)
   111087    0.012    0.000    0.012    0.000 {method 'colliderect' of 'pygame.Rect' objects}
     1247    0.003    0.000    0.011    0.000 ui_element.py:104(change_layer)
    14688    0.010    0.000    0.010    0.000 ui_button.py:257(process_event)
      649    0.002    0.000    0.010    0.000 ui_appearance_theme.py:158(update_shape_cache)
        5    0.000    0.000    0.010    0.002 entity_handler.py:45(_process_move)
       74    0.000    0.000    0.010    0.000 __init__.py:1996(debug)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
       74    0.000    0.000    0.010    0.000 __init__.py:1361(debug)
      630    0.006    0.000    0.010    0.000 ui_vertical_scroll_bar.py:228(update)
      246    0.003    0.000    0.009    0.000 text_block.py:265(redraw_from_chunks)
   141680    0.009    0.000    0.009    0.000 {method 'reverse' of 'list' objects}
        1    0.002    0.002    0.009    0.009 world.py:433(update_tile_visibility)
     1247    0.008    0.000    0.009    0.000 sprite.py:646(add_internal)
     1255    0.008    0.000    0.009    0.000 sprite.py:822(change_layer)
       27    0.000    0.000    0.009    0.000 game_handler.py:26(process_event)
      649    0.005    0.000    0.009    0.000 ecs.py:265(process_pending_deletions)
      649    0.001    0.000    0.009    0.000 surface_cache.py:24(update)
     1546    0.003    0.000    0.008    0.000 ui_font_dictionary.py:89(find_font)
     2099    0.007    0.000    0.008    0.000 typing.py:806(__new__)
        4    0.000    0.000    0.007    0.002 interaction_handler.py:27(process_event)
        4    0.000    0.000    0.007    0.002 interaction_handler.py:85(_process_entity_collision)
     4296    0.006    0.000    0.007    0.000 drawable_shape.py:122(rebuild_images_and_text)
      868    0.007    0.000    0.007    0.000 ui_manager.py:104(<listcomp>)
      111    0.000    0.000    0.007    0.000 __init__.py:1521(handle)
       30    0.005    0.000    0.007    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        4    0.000    0.000    0.007    0.002 skill.py:138(_call_skill_func)
     2099    0.005    0.000    0.007    0.000 query.py:170(__init__)
        8    0.000    0.000    0.007    0.001 manager.py:275(update_cameras_tiles)
      111    0.000    0.000    0.007    0.000 __init__.py:1575(callHandlers)
        8    0.002    0.000    0.007    0.001 camera.py:167(update_camera_tiles)
      753    0.005    0.000    0.006    0.000 sprite.py:814(layers)
        4    0.000    0.000    0.006    0.002 interaction_handler.py:135(_apply_effects_to_tiles)
      111    0.000    0.000    0.006    0.000 __init__.py:892(handle)
     3241    0.005    0.000    0.006    0.000 ui_window.py:97(update)
     1077    0.002    0.000    0.006    0.000 sprite.py:183(kill)
        8    0.000    0.000    0.006    0.001 game_handler.py:81(_process_end_turn)
        8    0.000    0.000    0.006    0.001 chrono.py:47(next_turn)
      111    0.000    0.000    0.006    0.000 __init__.py:1123(emit)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
        2    0.000    0.000    0.005    0.003 entity.py:339(build_characteristic_sprites)
      104    0.000    0.000    0.005    0.000 processors.py:59(process_intent)
      111    0.000    0.000    0.005    0.000 __init__.py:1022(emit)
       40    0.000    0.000    0.005    0.000 utility.py:13(get_image)
     4244    0.005    0.000    0.005    0.000 world.py:347(_is_tile_in_bounds)
      6/4    0.000    0.000    0.005    0.001 skill.py:218(process_effect)
       17    0.000    0.000    0.005    0.000 parser.py:104(feed)
       17    0.001    0.000    0.005    0.000 parser.py:134(goahead)
       93    0.001    0.000    0.005    0.000 processors.py:140(_process_player_turn_intents)
       82    0.002    0.000    0.005    0.000 styled_chunk.py:8(__init__)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      111    0.000    0.000    0.005    0.000 __init__.py:1481(makeRecord)
       41    0.004    0.000    0.004    0.000 {built-in method pygame.imageext.load_extended}
       35    0.000    0.000    0.004    0.000 __init__.py:1986(info)
        2    0.000    0.000    0.004    0.002 skill.py:259(_process_activate_skill)
     1298    0.004    0.000    0.004    0.000 sprite.py:745(sprites)
       35    0.000    0.000    0.004    0.000 __init__.py:1373(info)
      649    0.003    0.000    0.004    0.000 ui_manager.py:158(update_mouse_position)
      111    0.002    0.000    0.004    0.000 __init__.py:293(__init__)
        2    0.000    0.000    0.004    0.002 entity_handler.py:119(_process_use_skill)
     1077    0.002    0.000    0.004    0.000 sprite.py:728(remove_internal)
        2    0.000    0.000    0.004    0.002 skill.py:113(use)
      112    0.002    0.000    0.004    0.000 entity.py:43(get_player)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     1047    0.003    0.000    0.004    0.000 ecs.py:247(delete_entity_immediately)
     1237    0.003    0.000    0.003    0.000 drawable_shape.py:11(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
       10    0.000    0.000    0.003    0.000 chrono.py:24(rebuild_turn_queue)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
     1243    0.002    0.000    0.003    0.000 ui_element.py:68(create_valid_ids)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
       18    0.000    0.000    0.003    0.000 game_handler.py:39(_process_change_game_state)
      648    0.001    0.000    0.003    0.000 skill_bar.py:45(update)
        4    0.000    0.000    0.003    0.001 __init__.py:133(reload)
     4296    0.003    0.000    0.003    0.000 surface_cache.py:109(find_surface_in_cache)
      111    0.000    0.000    0.003    0.000 __init__.py:869(format)
        6    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       82    0.001    0.000    0.003    0.000 parser.py:301(parse_starttag)
      111    0.001    0.000    0.003    0.000 __init__.py:606(format)
     1507    0.003    0.000    0.003    0.000 {built-in method builtins.sorted}
     2294    0.002    0.000    0.002    0.000 ui_element.py:186(hover_point)
     3427    0.002    0.000    0.002    0.000 query.py:243(<listcomp>)
       17    0.000    0.000    0.002    0.000 state.py:71(set_new)
      249    0.001    0.000    0.002    0.000 ui_button.py:226(set_position)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      648    0.001    0.000    0.002    0.000 message_log.py:36(update)
        6    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:793(get_code)
        8    0.000    0.000    0.002    0.000 entity.py:482(take_turn)
    13/11    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        4    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:610(_exec)
      143    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
     2414    0.002    0.000    0.002    0.000 {method 'remove' of 'list' objects}
      164    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     1547    0.002    0.000    0.002    0.000 ui_font_dictionary.py:133(create_font_id)
      162    0.000    0.000    0.002    0.000 html_parser.py:118(add_text)
      648    0.001    0.000    0.002    0.000 entity_info.py:47(update)
        4    0.000    0.000    0.002    0.000 __init__.py:109(import_module)
      5/4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:994(_gcd_import)
      5/4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:978(_find_and_load)
     2099    0.002    0.000    0.002    0.000 query.py:50(__init__)
        2    0.000    0.000    0.002    0.001 skill.py:413(_process_damage_effect)
      111    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
       32    0.002    0.000    0.002    0.000 {built-in method nt.stat}
      162    0.001    0.000    0.002    0.000 html_parser.py:123(add_indexed_style)
      116    0.000    0.000    0.002    0.000 ntpath.py:212(basename)
     1321    0.002    0.000    0.002    0.000 state.py:45(get_current)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
       82    0.000    0.000    0.002    0.000 html_parser.py:213(handle_starttag)
     4948    0.002    0.000    0.002    0.000 {built-in method math.floor}
     1237    0.001    0.000    0.002    0.000 drawable_shape.py:50(compute_aligned_text_rect)
      649    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
     3349    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}
      116    0.001    0.000    0.001    0.000 ntpath.py:178(split)
      111    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
     8475    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      665    0.001    0.000    0.001    0.000 query.py:225(<listcomp>)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
      111    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
      104    0.001    0.000    0.001    0.000 action.py:12(convert_to_intent)
        8    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
       17    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
     4496    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       17    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
      111    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
     1335    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
        5    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
  273/271    0.001    0.000    0.001    0.000 entity.py:93(get_entitys_component)
       82    0.000    0.000    0.001    0.000 html_parser.py:283(handle_data)
     2100    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FF84D989BA0}
        1    0.000    0.000    0.001    0.001 basic_attack.py:17(activate)
     2547    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
        2    0.000    0.000    0.001    0.000 entity_handler.py:145(_process_die)
      244    0.001    0.000    0.001    0.000 ui_button.py:381(in_hold_range)
     2628    0.001    0.000    0.001    0.000 {built-in method builtins.max}
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
     2747    0.001    0.000    0.001    0.000 {built-in method builtins.min}
       21    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
     1237    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
     4137    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
     4537    0.001    0.000    0.001    0.000 sprite.py:168(update)
       47    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
     5389    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
        2    0.000    0.000    0.001    0.000 skill.py:530(_calculate_to_hit_score)
     2502    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     8554    0.001    0.000    0.001    0.000 {method 'contains' of 'pygame.Rect' objects}
      249    0.001    0.000    0.001    0.000 ui_element.py:160(set_position)
      111    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
     1265    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
      112    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
       10    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        2    0.000    0.000    0.001    0.000 skill.py:478(_calculate_damage)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
      111    0.001    0.000    0.001    0.000 {built-in method time.strftime}
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
     4296    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
     3241    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
       12    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:914(get_data)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:128(_update_label_offsets)
      249    0.001    0.000    0.001    0.000 rect_drawable_shape.py:107(set_position)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      651    0.001    0.000    0.001    0.000 {built-in method builtins.any}
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      232    0.000    0.000    0.001    0.000 ntpath.py:44(normcase)
       81    0.000    0.000    0.001    0.000 entity.py:104(get_name)
       11    0.000    0.000    0.001    0.000 ui_text_box.py:102(kill)
     2503    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
      261    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       43    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
       55    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
      126    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
      111    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        2    0.000    0.000    0.000    0.000 entity_handler.py:165(_process_want_to_use_skill)
     1247    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        2    0.000    0.000    0.000    0.000 entity.py:300(create_projectile)
     2294    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       81    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
       49    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       89    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
       93    0.000    0.000    0.000    0.000 processors.py:73(_get_pressed_direction)
     2452    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        5    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      630    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
       49    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
      111    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
  461/425    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      116    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      111    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
       10    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      474    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
      868    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 debug.py:28(log_component_not_found)
      340    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       14    0.000    0.000    0.000    0.000 world.py:268(tile_has_tag)
        2    0.000    0.000    0.000    0.000 skill.py:76(can_afford_cost)
        4    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        2    0.000    0.000    0.000    0.000 skill.py:95(pay_resource_cost)
      111    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       17    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        2    0.000    0.000    0.000    0.000 entity.py:189(delete)
     1247    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
     1235    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        2    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
       11    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        2    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
      111    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       10    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
      168    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
      104    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
     1247    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
       82    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
     1116    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      222    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        2    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
      111    0.000    0.000    0.000    0.000 __init__.py:432(format)
      662    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
     1231    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      101    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       30    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        6    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        2    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
       10    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
     1077    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
      104    0.000    0.000    0.000    0.000 processors.py:120(_process_stateless_intents)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
       11    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        9    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       93    0.000    0.000    0.000    0.000 processors.py:100(_get_pressed_skills_number)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
       50    0.000    0.000    0.000    0.000 event_core.py:41(publish)
      179    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        9    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        9    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        9    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        6    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
        5    0.000    0.000    0.000    0.000 world.py:366(_tile_has_any_entity)
      281    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
      162    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
      154    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
      111    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        2    0.000    0.000    0.000    0.000 god_handler.py:70(process_interventions)
      222    0.000    0.000    0.000    0.000 __init__.py:856(release)
       30    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        5    0.000    0.000    0.000    0.000 entity.py:174(create)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      111    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       30    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
      111    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        4    0.000    0.000    0.000    0.000 ai.py:42(act)
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        2    0.000    0.000    0.000    0.000 entity.py:425(consider_intervening)
        4    0.000    0.000    0.000    0.000 ai.py:68(act)
     1601    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
      611    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        5    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
      222    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      111    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        4    0.000    0.000    0.000    0.000 world.py:315(tile_has_tags)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      333    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      111    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      613    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
      271    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
      215    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        8    0.000    0.000    0.000    0.000 entity_handler.py:224(_process_end_turn)
       17    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      111    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       60    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      101    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
      369    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        6    0.000    0.000    0.000    0.000 world.py:83(get_tiles)
      504    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
       50    0.000    0.000    0.000    0.000 event_core.py:15(notify)
      111    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
      225    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
      116    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
      100    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        2    0.000    0.000    0.000    0.000 skill.py:246(_process_trigger_skill_effect)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        8    0.000    0.000    0.000    0.000 entity.py:377(spend_time)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       60    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      190    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       17    0.000    0.000    0.000    0.000 parser.py:96(reset)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
      111    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 world.py:426(recompute_fov)
       82    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
      166    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       37    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       30    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       18    0.000    0.000    0.000    0.000 event.py:90(__init__)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
       12    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 main.py:239(initialise_event_handlers)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       82    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        3    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       50    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
      112    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
      236    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
        2    0.000    0.000    0.000    0.000 world.py:381(_tile_has_specific_entity)
       24    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       89    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
      246    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        5    0.000    0.000    0.000    0.000 event.py:55(__init__)
      111    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       10    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
      111    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
        8    0.000    0.000    0.000    0.000 event.py:168(__init__)
       88    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
      120    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
       30    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       12    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
      225    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        6    0.000    0.000    0.000    0.000 entity.py:332(add_component)
       29    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
       47    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        2    0.000    0.000    0.000    0.000 random.py:344(choices)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        2    0.000    0.000    0.000    0.000 random.py:218(randint)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       17    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        2    0.000    0.000    0.000    0.000 world.py:103(get_direction)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
      244    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       12    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       99    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
       23    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        8    0.000    0.000    0.000    0.000 event.py:72(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
      172    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       90    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        7    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        4    0.000    0.000    0.000    0.000 event.py:120(__init__)
       49    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        2    0.000    0.000    0.000    0.000 random.py:174(randrange)
       49    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
       54    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        5    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       12    0.000    0.000    0.000    0.000 {built-in method math.sin}
       82    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        6    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
       17    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
       49    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       49    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        6    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       83    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       30    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       16    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       10    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        3    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        2    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       17    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       54    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
       17    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        2    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
        8    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
       29    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        2    0.000    0.000    0.000    0.000 event.py:19(__init__)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        6    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        2    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        2    0.000    0.000    0.000    0.000 event.py:46(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       30    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <string>:1(__init__)
       22    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        4    0.000    0.000    0.000    0.000 {built-in method builtins.format}
        8    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
       12    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        2    0.000    0.000    0.000    0.000 event.py:33(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
       20    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
       42    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        2    0.000    0.000    0.000    0.000 ui_button.py:340(select)
        9    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
       11    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
       24    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        5    0.000    0.000    0.000    0.000 component.py:82(__init__)
       45    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        1    0.000    0.000    0.000    0.000 main.py:189(disable_profiling)
       52    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
       42    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        7    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 god_handler.py:45(process_judgements)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
       28    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        7    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        6    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
       16    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        2    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        1    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
        1    0.000    0.000    0.000    0.000 event.py:82(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        8    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        6    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       12    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        2    0.000    0.000    0.000    0.000 skill.py:204(_get_hit_type)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        2    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
        8    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        4    0.000    0.000    0.000    0.000 component.py:31(__init__)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        8    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        4    0.000    0.000    0.000    0.000 component.py:56(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        2    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        8    0.000    0.000    0.000    0.000 world.py:326(<genexpr>)
        8    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
       12    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        3    0.000    0.000    0.000    0.000 component.py:118(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        1    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        5    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        2    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 component.py:199(__init__)
        3    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 ui_handler.py:28(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        2    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        2    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 ui_element.py:220(select)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 ui_element.py:226(unselect)
        1    0.000    0.000    0.000    0.000 basic_attack.py:13(use)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


