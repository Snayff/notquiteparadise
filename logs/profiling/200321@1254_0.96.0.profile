Sat Mar 21 12:54:23 2020    logs/profiling/profile.dump

         5375698 function calls (5056665 primitive calls) in 32.369 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.333    0.333   32.327   32.327 main.py:85(game_loop)
     1832   20.473    0.011   20.473    0.011 {method 'tick' of 'Clock' objects}
      916    0.005    0.000   10.313    0.011 state.py:38(get_delta_time)
      916    0.003    0.000   10.169    0.011 state.py:63(update_clock)
      916    0.004    0.000    4.408    0.005 manager.py:54(update)
      916    0.269    0.000    4.405    0.005 ui_manager.py:122(update)
      916    0.013    0.000    4.392    0.005 manager.py:73(draw)
   300669    3.142    0.000    3.142    0.000 {method 'blit' of 'pygame.Surface' objects}
      916    0.149    0.000    2.626    0.003 sprite.py:453(update)
      916    0.001    0.000    2.120    0.002 event_core.py:21(update)
       77    0.000    0.000    2.027    0.026 ui_handler.py:30(process_event)
       12    0.000    0.000    1.940    0.162 ui_handler.py:207(update_camera)
       12    0.000    0.000    1.910    0.159 manager.py:295(update_camera_grid)
       12    0.012    0.001    1.910    0.159 camera.py:105(update_grid)
     1826    0.023    0.000    1.894    0.001 ui_button.py:30(__init__)
      927    0.869    0.001    1.884    0.002 camera.py:79(update_game_map)
      915    0.006    0.000    1.870    0.002 camera.py:72(update)
     1826    0.098    0.000    1.781    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
       15    0.000    0.000    1.780    0.119 ui_handler.py:48(process_entity_event)
      916    0.007    0.000    1.692    0.002 ui_manager.py:173(draw_ui)
      916    0.266    0.000    1.686    0.002 sprite.py:753(draw)
    53227    0.131    0.000    1.438    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
372219/53227    1.225    0.000    1.296    0.000 ui_appearance_theme.py:322(get_next_id_node)
      920    1.244    0.001    1.244    0.001 {built-in method pygame.transform.scale}
   147541    0.656    0.000    1.173    0.000 ui_element.py:121(check_hover)
    27516    0.071    0.000    0.812    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   144465    0.288    0.000    0.533    0.000 ui_button.py:197(update)
    16560    0.031    0.000    0.475    0.000 ui_appearance_theme.py:428(get_misc_data)
      916    0.450    0.000    0.450    0.000 {built-in method pygame.event.get}
   144465    0.183    0.000    0.348    0.000 ui_button.py:138(hover_point)
      916    0.341    0.000    0.341    0.000 {built-in method pygame.display.flip}
     9243    0.282    0.000    0.299    0.000 sprite.py:913(get_sprites_from_layer)
     1826    0.011    0.000    0.221    0.000 ui_button.py:97(set_any_images_from_theme)
     7304    0.013    0.000    0.210    0.000 ui_appearance_theme.py:366(get_image)
   139057    0.203    0.000    0.203    0.000 camera.py:233(world_to_screen_position)
   144465    0.083    0.000    0.190    0.000 drawable_shape.py:36(update)
       52    0.000    0.000    0.176    0.003 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.169    0.169 ui_handler.py:111(init_game_ui)
   144465    0.146    0.000    0.166    0.000 rect_drawable_shape.py:84(collide_point)
   299658    0.114    0.000    0.136    0.000 sprite.py:208(alive)
     1507    0.136    0.000    0.136    0.000 {method 'fill' of 'pygame.Surface' objects}
     7348    0.047    0.000    0.135    0.000 rect_drawable_shape.py:118(redraw_state)
     1826    0.014    0.000    0.109    0.000 ui_button.py:537(rebuild_shape)
     1847    0.007    0.000    0.096    0.000 rect_drawable_shape.py:22(__init__)
     1857    0.019    0.000    0.085    0.000 ui_element.py:23(__init__)
     1847    0.025    0.000    0.085    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
   992776    0.079    0.000    0.079    0.000 {method 'append' of 'list' objects}
       14    0.000    0.000    0.070    0.005 ui_text_box.py:50(__init__)
     1826    0.008    0.000    0.070    0.000 ui_appearance_theme.py:405(get_font)
       14    0.000    0.000    0.069    0.005 ui_text_box.py:492(rebuild_from_changed_theme_data)
       14    0.001    0.000    0.067    0.005 ui_text_box.py:110(rebuild)
       11    0.000    0.000    0.065    0.006 message_log.py:49(add_message)
       96    0.000    0.000    0.063    0.001 manager.py:60(process_ui_events)
       96    0.023    0.000    0.063    0.001 ui_manager.py:86(process_events)
       10    0.000    0.000    0.062    0.006 ui_handler.py:155(process_ui_event)
       10    0.000    0.000    0.062    0.006 ui_handler.py:238(process_message)
       10    0.000    0.000    0.062    0.006 manager.py:444(add_to_message_log)
       67    0.000    0.000    0.062    0.001 entity_handler.py:27(process_event)
   144465    0.062    0.000    0.062    0.000 ui_button.py:154(can_hover)
      916    0.003    0.000    0.055    0.000 processors.py:16(process_all)
      916    0.026    0.000    0.052    0.000 processors.py:23(_process_aesthetic_update)
     1847    0.008    0.000    0.049    0.000 drawable_shape.py:45(redraw_all_states)
    10507    0.014    0.000    0.046    0.000 _internal.py:24(wrapper)
        9    0.000    0.000    0.046    0.005 entity_handler.py:55(_process_move)
      375    0.002    0.000    0.044    0.000 __init__.py:1496(_log)
        5    0.011    0.002    0.043    0.009 world.py:445(update_tile_visibility)
        1    0.000    0.000    0.042    0.042 main.py:193(initialise_game)
      315    0.001    0.000    0.040    0.000 __init__.py:1996(debug)
     1857    0.005    0.000    0.040    0.000 ui_container.py:42(add_element)
   757189    0.040    0.000    0.040    0.000 {built-in method builtins.len}
       12    0.007    0.001    0.040    0.003 ui_container.py:116(clear)
      315    0.001    0.000    0.039    0.000 __init__.py:1361(debug)
      366    0.001    0.000    0.039    0.000 screen_message.py:34(update)
     7348    0.039    0.000    0.039    0.000 surface_cache.py:119(build_cache_id)
        2    0.000    0.000    0.039    0.019 entity.py:230(create_actor)
     1281    0.013    0.000    0.038    0.000 ui_text_box.py:205(update)
        7    0.001    0.000    0.036    0.005 ui_vertical_scroll_bar.py:22(__init__)
      246    0.001    0.000    0.034    0.000 ui_text_box.py:347(redraw_from_chunks)
     7432    0.034    0.000    0.034    0.000 {method 'copy' of 'pygame.Surface' objects}
     3544    0.032    0.000    0.032    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     1668    0.002    0.000    0.032    0.000 ui_button.py:130(kill)
        2    0.008    0.004    0.032    0.016 world.py:26(create_fov_map)
     1687    0.003    0.000    0.030    0.000 ui_element.py:114(kill)
     6812    0.023    0.000    0.029    0.000 query.py:212(__iter__)
   155193    0.028    0.000    0.028    0.000 ui_manager.py:167(get_mouse_position)
       21    0.000    0.000    0.027    0.001 ui_text_box.py:310(parse_html_into_style_data)
     1857    0.003    0.000    0.025    0.000 sprite.py:121(__init__)
      246    0.003    0.000    0.024    0.000 ui_text_box.py:327(redraw_from_text_block)
      375    0.001    0.000    0.023    0.000 __init__.py:1521(handle)
   299658    0.022    0.000    0.022    0.000 {built-in method _operator.truth}
       52    0.000    0.000    0.022    0.000 game_handler.py:26(process_event)
     5491    0.016    0.000    0.022    0.000 ui_container.py:124(check_hover)
    10508    0.021    0.000    0.022    0.000 {built-in method _warnings.warn}
     1857    0.007    0.000    0.022    0.000 sprite.py:126(add)
   153032    0.022    0.000    0.022    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      375    0.001    0.000    0.021    0.000 __init__.py:1575(callHandlers)
      916    0.002    0.000    0.021    0.000 ui_appearance_theme.py:158(update_shape_cache)
       12    0.000    0.000    0.021    0.002 manager.py:286(update_camera_game_map)
      375    0.002    0.000    0.020    0.000 __init__.py:892(handle)
   145855    0.020    0.000    0.020    0.000 {method 'union' of 'pygame.Rect' objects}
      916    0.001    0.000    0.019    0.000 surface_cache.py:24(update)
     1687    0.003    0.000    0.018    0.000 ui_container.py:52(remove_element)
       21    0.000    0.000    0.018    0.001 text_block.py:16(__init__)
      375    0.001    0.000    0.018    0.000 __init__.py:1123(emit)
       21    0.004    0.000    0.018    0.001 text_block.py:40(redraw)
      375    0.001    0.000    0.017    0.000 __init__.py:1022(emit)
     1857    0.004    0.000    0.017    0.000 ui_element.py:104(change_layer)
   156682    0.017    0.000    0.017    0.000 {method 'colliderect' of 'pygame.Rect' objects}
     4838    0.010    0.000    0.017    0.000 world.py:55(get_tile)
       42    0.013    0.000    0.016    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
      375    0.001    0.000    0.015    0.000 __init__.py:1481(makeRecord)
   212072    0.014    0.000    0.014    0.000 {method 'reverse' of 'list' objects}
      375    0.005    0.000    0.014    0.000 __init__.py:293(__init__)
     1857    0.013    0.000    0.013    0.000 sprite.py:646(add_internal)
     1865    0.011    0.000    0.013    0.000 sprite.py:822(change_layer)
      916    0.007    0.000    0.012    0.000 ecs.py:265(process_pending_deletions)
      124    0.001    0.000    0.012    0.000 ui_text_box.py:462(set_active_effect)
     2929    0.010    0.000    0.012    0.000 typing.py:806(__new__)
     7348    0.010    0.000    0.011    0.000 drawable_shape.py:122(rebuild_images_and_text)
     2320    0.005    0.000    0.011    0.000 ui_font_dictionary.py:89(find_font)
       16    0.000    0.000    0.011    0.001 game_handler.py:81(process_end_turn)
       16    0.000    0.000    0.011    0.001 chrono.py:47(next_turn)
     2929    0.007    0.000    0.010    0.000 query.py:170(__init__)
    13734    0.009    0.000    0.009    0.000 ui_button.py:257(process_event)
      246    0.003    0.000    0.009    0.000 text_block.py:265(redraw_from_chunks)
     4576    0.007    0.000    0.009    0.000 ui_window.py:97(update)
       12    0.000    0.000    0.009    0.001 manager.py:275(update_cameras_tiles)
     1012    0.006    0.000    0.009    0.000 sprite.py:814(layers)
       12    0.003    0.000    0.009    0.001 camera.py:167(update_camera_tiles)
     1687    0.003    0.000    0.009    0.000 sprite.py:183(kill)
      375    0.001    0.000    0.009    0.000 __init__.py:869(format)
      375    0.002    0.000    0.008    0.000 __init__.py:606(format)
     7500    0.003    0.000    0.008    0.000 libtcodpy.py:3300(map_is_in_fov)
       21    0.000    0.000    0.008    0.000 parser.py:104(feed)
       21    0.001    0.000    0.008    0.000 parser.py:134(goahead)
     1847    0.002    0.000    0.007    0.000 drawable_shape.py:50(compute_aligned_text_rect)
      124    0.003    0.000    0.007    0.000 styled_chunk.py:8(__init__)
       60    0.000    0.000    0.007    0.000 __init__.py:1986(info)
       60    0.000    0.000    0.006    0.000 __init__.py:1373(info)
     1832    0.006    0.000    0.006    0.000 sprite.py:745(sprites)
      916    0.004    0.000    0.006    0.000 ui_manager.py:158(update_mouse_position)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      824    0.006    0.000    0.006    0.000 ui_manager.py:104(<listcomp>)
       20    0.001    0.000    0.006    0.000 chrono.py:24(rebuild_turn_queue)
     1687    0.003    0.000    0.006    0.000 sprite.py:728(remove_internal)
        2    0.000    0.000    0.006    0.003 entity.py:340(build_characteristic_sprites)
      375    0.001    0.000    0.005    0.000 __init__.py:1011(flush)
      391    0.005    0.000    0.005    0.000 {method 'size' of 'pygame.font.Font' objects}
       40    0.000    0.000    0.005    0.000 utility.py:13(get_image)
     4851    0.005    0.000    0.005    0.000 world.py:347(_is_tile_in_bounds)
       34    0.000    0.000    0.005    0.000 game_handler.py:42(process_change_game_state)
      380    0.001    0.000    0.005    0.000 ntpath.py:212(basename)
     1474    0.004    0.000    0.005    0.000 ecs.py:247(delete_entity_immediately)
        4    0.000    0.000    0.005    0.001 skill.py:139(_call_skill_func)
        4    0.000    0.000    0.005    0.001 interaction_handler.py:25(process_event)
      880    0.004    0.000    0.005    0.000 ui_vertical_scroll_bar.py:228(update)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
        2    0.000    0.000    0.005    0.002 entity_handler.py:133(_process_use_skill)
     1847    0.005    0.000    0.005    0.000 drawable_shape.py:11(__init__)
      380    0.003    0.000    0.005    0.000 ntpath.py:178(split)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
      375    0.002    0.000    0.005    0.000 __init__.py:1451(findCaller)
      915    0.002    0.000    0.004    0.000 skill_bar.py:45(update)
     7500    0.004    0.000    0.004    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       33    0.000    0.000    0.004    0.000 state.py:71(set_new)
     1853    0.003    0.000    0.004    0.000 ui_element.py:68(create_valid_ids)
     7348    0.004    0.000    0.004    0.000 surface_cache.py:109(find_surface_in_cache)
        4    0.000    0.000    0.004    0.001 interaction_handler.py:86(_process_entity_collision)
        2    0.000    0.000    0.004    0.002 skill.py:111(use)
        4    0.000    0.000    0.004    0.001 interaction_handler.py:121(_apply_effects_to_tiles)
       96    0.000    0.000    0.004    0.000 processors.py:57(process_intent)
      375    0.001    0.000    0.004    0.000 __init__.py:539(formatTime)
      124    0.001    0.000    0.004    0.000 parser.py:301(parse_starttag)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     4810    0.004    0.000    0.004    0.000 query.py:243(<listcomp>)
       12    0.000    0.000    0.004    0.000 entity.py:483(take_turn)
     2025    0.004    0.000    0.004    0.000 {built-in method builtins.sorted}
      375    0.004    0.000    0.004    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       81    0.001    0.000    0.004    0.000 processors.py:138(_process_player_turn_intents)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      915    0.002    0.000    0.003    0.000 message_log.py:36(update)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
      114    0.001    0.000    0.003    0.000 entity.py:42(get_player)
        4    0.000    0.000    0.003    0.001 skill.py:219(process_effect)
      246    0.001    0.000    0.003    0.000 html_parser.py:118(add_text)
     3076    0.002    0.000    0.003    0.000 ui_element.py:186(hover_point)
     3667    0.003    0.000    0.003    0.000 {method 'remove' of 'list' objects}
     2321    0.003    0.000    0.003    0.000 ui_font_dictionary.py:133(create_font_id)
      248    0.003    0.000    0.003    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      915    0.001    0.000    0.003    0.000 entity_info.py:45(update)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
     2929    0.003    0.000    0.003    0.000 query.py:50(__init__)
      246    0.002    0.000    0.003    0.000 html_parser.py:123(add_indexed_style)
      375    0.001    0.000    0.003    0.000 ntpath.py:201(splitext)
      217    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
     1876    0.002    0.000    0.002    0.000 state.py:45(get_current)
      124    0.001    0.000    0.002    0.000 html_parser.py:213(handle_starttag)
      376    0.002    0.000    0.002    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       15    0.000    0.000    0.002    0.000 god_handler.py:26(process_event)
        2    0.000    0.000    0.002    0.001 skill.py:261(_process_activate_skill)
     7388    0.002    0.000    0.002    0.000 {built-in method math.floor}
    19718    0.002    0.000    0.002    0.000 {method 'contains' of 'pygame.Rect' objects}
      916    0.002    0.000    0.002    0.000 {built-in method pygame.mouse.get_pos}
       37    0.002    0.000    0.002    0.000 {built-in method nt.stat}
        4    0.000    0.000    0.002    0.001 __init__.py:133(reload)
      375    0.002    0.000    0.002    0.000 {built-in method time.strftime}
      943    0.001    0.000    0.002    0.000 query.py:225(<listcomp>)
     6439    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
     4813    0.002    0.000    0.002    0.000 {method 'pop' of 'dict' objects}
        6    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
      760    0.001    0.000    0.002    0.000 ntpath.py:44(normcase)
        4    0.000    0.000    0.002    0.000 __init__.py:109(import_module)
      124    0.000    0.000    0.002    0.000 html_parser.py:283(handle_data)
      5/4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:994(_gcd_import)
      5/4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:978(_find_and_load)
        7    0.000    0.000    0.002    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
       21    0.000    0.000    0.002    0.000 html_parser.py:207(__init__)
        6    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:793(get_code)
     3955    0.002    0.000    0.002    0.000 {method 'get' of 'dict' objects}
     9700    0.002    0.000    0.002    0.000 world.py:48(get_game_map)
       21    0.000    0.000    0.002    0.000 html_parser.py:60(__init__)
      375    0.001    0.000    0.002    0.000 genericpath.py:117(_splitext)
     2930    0.002    0.000    0.002    0.000 {built-in method __new__ of type object at 0x00007FF84D989BA0}
      2/1    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
     1933    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:610(_exec)
      390    0.001    0.000    0.001    0.000 ntpath.py:122(splitdrive)
     6983    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
       15    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
    13/11    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
     1847    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
     7753    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     6406    0.001    0.000    0.001    0.000 sprite.py:168(update)
     3777    0.001    0.000    0.001    0.000 {built-in method builtins.min}
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
     3722    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     3782    0.001    0.000    0.001    0.000 {built-in method builtins.max}
        4    0.001    0.000    0.001    0.000 {built-in method builtins.print}
     7348    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
      375    0.000    0.000    0.001    0.000 __init__.py:590(formatMessage)
       96    0.001    0.000    0.001    0.000 action.py:12(convert_to_intent)
      329    0.001    0.000    0.001    0.000 entity.py:92(get_entitys_component)
     1891    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
        2    0.000    0.000    0.001    0.000 entity_handler.py:180(_process_die)
     4576    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
        5    0.000    0.000    0.001    0.000 combat_stats.py:270(sight_range)
       21    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
      375    0.001    0.000    0.001    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      375    0.000    0.000    0.001    0.000 __init__.py:584(usesTime)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
      918    0.001    0.000    0.001    0.000 {built-in method builtins.any}
       77    0.000    0.000    0.001    0.000 utility.py:188(value_to_member)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
      375    0.000    0.000    0.001    0.000 cp1252.py:18(encode)
     3723    0.001    0.000    0.001    0.000 ui_manager.py:44(get_sprite_group)
       45    0.000    0.000    0.001    0.000 entity.py:129(get_primary_stat)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
      750    0.000    0.000    0.001    0.000 __init__.py:849(acquire)
      107    0.000    0.000    0.001    0.000 entity.py:102(get_name)
       13    0.000    0.000    0.001    0.000 ui_text_box.py:102(kill)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
     1857    0.001    0.000    0.001    0.000 sprite.py:162(add_internal)
      375    0.001    0.000    0.001    0.000 __init__.py:432(format)
       12    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:914(get_data)
       78    0.001    0.000    0.001    0.000 surface_cache.py:80(split_rect)
       18    0.000    0.000    0.001    0.000 world.py:260(tile_has_tag)
     3076    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
        2    0.000    0.000    0.001    0.000 entity_handler.py:241(_process_created_timed_entity)
     3668    0.001    0.000    0.001    0.000 {method 'copy' of 'list' objects}
        7    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        5    0.000    0.000    0.001    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        8    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
       81    0.000    0.000    0.001    0.000 utility.py:94(get_class_members)
      353    0.001    0.000    0.001    0.000 ui_button.py:170(while_hovering)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
      107    0.000    0.000    0.000    0.000 entity.py:115(get_identity)
      750    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        2    0.000    0.000    0.000    0.000 entity.py:301(create_projectile)
      750    0.000    0.000    0.000    0.000 __init__.py:856(release)
       51    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
      375    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
      166    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        6    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
     1125    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      375    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
       20    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       12    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
     1841    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
      375    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
     1857    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      880    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        1    0.000    0.000    0.000    0.000 entity.py:199(create_god)
      508    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
       21    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      375    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
     1115    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
      252    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
      124    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
     1747    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
     1857    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
     1839    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       12    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      375    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        9    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       83    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
        1    0.000    0.000    0.000    0.000 basic_attack.py:8(use)
     1933    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        1    0.000    0.000    0.000    0.000 basic_attack.py:11(activate)
       81    0.000    0.000    0.000    0.000 event_core.py:38(publish)
      375    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        8    0.000    0.000    0.000    0.000 ai.py:72(act)
     1161    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        2    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
      444    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        2    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
        2    0.000    0.000    0.000    0.000 entity.py:187(delete)
      380    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
      752    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      246    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
      521    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
        9    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
     1112    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       42    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
      375    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      151    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        9    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
     2413    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       81    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
       42    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
     1687    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       16    0.000    0.000    0.000    0.000 entity_handler.py:233(_process_end_turn)
      375    0.000    0.000    0.000    0.000 threading.py:1052(name)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
       96    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
     1223    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
       42    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      267    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        5    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
      345    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
      228    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
      618    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        9    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       16    0.000    0.000    0.000    0.000 entity.py:378(spend_time)
        9    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        9    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        5    0.000    0.000    0.000    0.000 entity.py:172(create)
        9    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        2    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
        6    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
       96    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       81    0.000    0.000    0.000    0.000 event_core.py:12(notify)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        1    0.000    0.000    0.000    0.000 chrono.py:79(next_round)
      376    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
      454    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        2    0.000    0.000    0.000    0.000 entity.py:426(consider_intervening)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        5    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
      774    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
      329    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
       21    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        4    0.000    0.000    0.000    0.000 ai.py:45(act)
      375    0.000    0.000    0.000    0.000 {built-in method time.time}
       30    0.000    0.000    0.000    0.000 utility.py:107(lerp)
      375    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        7    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
      115    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
       34    0.000    0.000    0.000    0.000 event.py:106(__init__)
      228    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      611    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       42    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       81    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        4    0.000    0.000    0.000    0.000 entity.py:72(get_entities_and_components_in_area)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
      124    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
      752    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
      124    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       26    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       89    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
      250    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
        2    0.000    0.000    0.000    0.000 skill.py:247(_process_trigger_skill_effect)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       20    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
       81    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
       15    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       21    0.000    0.000    0.000    0.000 parser.py:96(reset)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        5    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        7    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
      336    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
       88    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       16    0.000    0.000    0.000    0.000 event.py:88(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
        5    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       18    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
       10    0.000    0.000    0.000    0.000 event.py:184(__init__)
        7    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       34    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        6    0.000    0.000    0.000    0.000 entity.py:333(add_component)
      141    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        9    0.000    0.000    0.000    0.000 event.py:63(__init__)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      130    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
       42    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
      162    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       24    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       83    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
      370    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       14    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
        5    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       21    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        6    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       14    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       83    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
       53    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        4    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
       81    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
      256    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
      132    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        2    0.000    0.000    0.000    0.000 random.py:344(choices)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        2    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        7    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       20    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
      124    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        5    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
        7    0.000    0.000    0.000    0.000 entity.py:122(get_combat_stats)
       42    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       57    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        2    0.000    0.000    0.000    0.000 manager.py:264(move_camera)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
        7    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
      125    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       47    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        4    0.000    0.000    0.000    0.000 event.py:136(__init__)
       14    0.000    0.000    0.000    0.000 {built-in method math.sin}
       54    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
       18    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
       47    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       25    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       47    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       42    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
       48    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
       12    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       21    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        2    0.000    0.000    0.000    0.000 camera.py:223(move_camera)
       36    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
       21    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        2    0.000    0.000    0.000    0.000 event.py:54(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       21    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
       16    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       54    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        2    0.000    0.000    0.000    0.000 event.py:29(__init__)
        7    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
       15    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        2    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       55    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        9    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        4    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       24    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
       36    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       30    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       12    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
       42    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
       16    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
       16    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
        3    0.000    0.000    0.000    0.000 component.py:39(__init__)
        2    0.000    0.000    0.000    0.000 event.py:77(__init__)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       52    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       17    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
       14    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        5    0.000    0.000    0.000    0.000 component.py:81(__init__)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        5    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
       42    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        2    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
        7    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        7    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
       12    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        4    0.000    0.000    0.000    0.000 component.py:55(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
       16    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 entity_handler.py:24(__init__)
        1    0.000    0.000    0.000    0.000 event.py:116(__init__)
        4    0.000    0.000    0.000    0.000 component.py:30(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        7    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        2    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        3    0.000    0.000    0.000    0.000 component.py:63(__init__)
        2    0.000    0.000    0.000    0.000 component.py:183(__init__)
        2    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        3    0.000    0.000    0.000    0.000 component.py:117(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        4    0.000    0.000    0.000    0.000 entity.py:83(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        3    0.000    0.000    0.000    0.000 component.py:132(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        2    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        2    0.000    0.000    0.000    0.000 component.py:72(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:91(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 component.py:109(__init__)
        1    0.000    0.000    0.000    0.000 component.py:175(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:69(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 chrono.py:95(increment_round)
        2    0.000    0.000    0.000    0.000 component.py:100(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


