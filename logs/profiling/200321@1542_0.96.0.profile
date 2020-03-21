Sat Mar 21 15:42:00 2020    logs/profiling/profile.dump

         8269122 function calls (8136550 primitive calls) in 72.490 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.797    0.797   72.449   72.449 main.py:85(game_loop)
     4336   49.621    0.011   49.621    0.011 {method 'tick' of 'Clock' objects}
     2168    0.008    0.000   25.505    0.012 state.py:63(update_clock)
     2168    0.012    0.000   24.136    0.011 state.py:38(get_delta_time)
     2168    0.031    0.000   10.723    0.005 manager.py:73(draw)
     2168    0.009    0.000    9.791    0.005 manager.py:54(update)
     2168    0.634    0.000    9.782    0.005 ui_manager.py:122(update)
   706234    7.575    0.000    7.575    0.000 {method 'blit' of 'pygame.Surface' objects}
     2168    0.349    0.000    5.577    0.003 sprite.py:453(update)
     2168    0.016    0.000    4.181    0.002 ui_manager.py:173(draw_ui)
     2168    0.668    0.000    4.165    0.002 sprite.py:753(draw)
     2167    0.013    0.000    4.052    0.002 camera.py:72(update)
     2172    1.638    0.001    4.043    0.002 camera.py:79(update_game_map)
     2172    3.033    0.001    3.033    0.001 {built-in method pygame.transform.scale}
   349037    1.548    0.000    2.764    0.000 ui_element.py:121(check_hover)
   342224    0.676    0.000    1.057    0.000 ui_button.py:197(update)
     2168    0.002    0.000    0.883    0.000 event_core.py:24(update)
       31    0.000    0.000    0.857    0.028 ui_handler.py:30(process_event)
   342224    0.433    0.000    0.834    0.000 ui_button.py:138(hover_point)
        5    0.000    0.000    0.825    0.165 ui_handler.py:202(update_camera)
        5    0.000    0.000    0.813    0.163 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.813    0.163 camera.py:105(update_grid)
     2168    0.806    0.000    0.806    0.000 {built-in method pygame.display.flip}
      761    0.010    0.000    0.804    0.001 ui_button.py:30(__init__)
      761    0.041    0.000    0.755    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
    20162    0.673    0.000    0.710    0.000 sprite.py:913(get_sprites_from_layer)
        5    0.000    0.000    0.659    0.132 ui_handler.py:43(process_entity_event)
    22222    0.056    0.000    0.610    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
154734/22222    0.520    0.000    0.550    0.000 ui_appearance_theme.py:322(get_next_id_node)
   325803    0.504    0.000    0.504    0.000 camera.py:233(world_to_screen_position)
     2168    0.405    0.000    0.405    0.000 {built-in method pygame.event.get}
   342224    0.354    0.000    0.400    0.000 rect_drawable_shape.py:84(collide_point)
    11486    0.031    0.000    0.346    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
     2699    0.325    0.000    0.325    0.000 {method 'fill' of 'pygame.Surface' objects}
   708910    0.258    0.000    0.311    0.000 sprite.py:208(alive)
   342224    0.176    0.000    0.243    0.000 drawable_shape.py:36(update)
     6920    0.014    0.000    0.202    0.000 ui_appearance_theme.py:428(get_misc_data)
       21    0.000    0.000    0.180    0.009 ui_handler.py:67(process_game_event)
        1    0.000    0.000    0.174    0.174 ui_handler.py:106(init_game_ui)
   342224    0.152    0.000    0.152    0.000 ui_button.py:154(can_hover)
     2168    0.008    0.000    0.134    0.000 processors.py:16(process_all)
     2168    0.067    0.000    0.127    0.000 processors.py:23(_process_aesthetic_update)
  1049785    0.103    0.000    0.103    0.000 {method 'append' of 'list' objects}
      761    0.005    0.000    0.094    0.000 ui_button.py:97(set_any_images_from_theme)
     3044    0.006    0.000    0.089    0.000 ui_appearance_theme.py:366(get_image)
    15364    0.052    0.000    0.067    0.000 query.py:212(__iter__)
   366686    0.066    0.000    0.066    0.000 ui_manager.py:167(get_mouse_position)
     2910    0.020    0.000    0.059    0.000 rect_drawable_shape.py:118(redraw_state)
    13003    0.040    0.000    0.055    0.000 ui_container.py:124(check_hover)
     2533    0.028    0.000    0.054    0.000 ui_text_box.py:205(update)
   708910    0.053    0.000    0.053    0.000 {built-in method _operator.truth}
   362040    0.052    0.000    0.052    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
   348426    0.051    0.000    0.051    0.000 {method 'union' of 'pygame.Rect' objects}
      761    0.006    0.000    0.044    0.000 ui_button.py:537(rebuild_shape)
   372470    0.041    0.000    0.041    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        1    0.000    0.000    0.041    0.041 main.py:193(initialise_game)
      366    0.002    0.000    0.041    0.000 screen_message.py:34(update)
      772    0.003    0.000    0.039    0.000 rect_drawable_shape.py:22(__init__)
       57    0.000    0.000    0.039    0.001 manager.py:60(process_ui_events)
       57    0.014    0.000    0.038    0.001 ui_manager.py:86(process_events)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      782    0.008    0.000    0.037    0.000 ui_element.py:23(__init__)
   596404    0.037    0.000    0.037    0.000 {built-in method builtins.len}
      242    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
      772    0.011    0.000    0.035    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
      761    0.003    0.000    0.030    0.000 ui_appearance_theme.py:405(get_font)
        9    0.000    0.000    0.026    0.003 ui_text_box.py:50(__init__)
        9    0.000    0.000    0.026    0.003 ui_text_box.py:492(rebuild_from_changed_theme_data)
     2168    0.015    0.000    0.025    0.000 ecs.py:265(process_pending_deletions)
      242    0.003    0.000    0.025    0.000 ui_text_box.py:327(redraw_from_text_block)
     6590    0.021    0.000    0.024    0.000 typing.py:806(__new__)
        9    0.000    0.000    0.024    0.003 ui_text_box.py:110(rebuild)
     6590    0.016    0.000    0.022    0.000 query.py:170(__init__)
    10836    0.018    0.000    0.022    0.000 ui_window.py:97(update)
      772    0.004    0.000    0.021    0.000 drawable_shape.py:45(redraw_all_states)
        6    0.000    0.000    0.020    0.003 message_log.py:49(add_message)
     2225    0.014    0.000    0.020    0.000 sprite.py:814(layers)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
        5    0.000    0.000    0.018    0.004 ui_handler.py:150(process_ui_event)
        5    0.000    0.000    0.018    0.004 ui_handler.py:233(process_message)
        5    0.000    0.000    0.018    0.004 manager.py:444(add_to_message_log)
      782    0.002    0.000    0.018    0.000 ui_container.py:42(add_element)
     2952    0.016    0.000    0.016    0.000 {method 'copy' of 'pygame.Surface' objects}
     2910    0.016    0.000    0.016    0.000 surface_cache.py:119(build_cache_id)
     2168    0.010    0.000    0.015    0.000 ui_manager.py:158(update_mouse_position)
        5    0.003    0.001    0.015    0.003 ui_container.py:116(clear)
     2168    0.006    0.000    0.014    0.000 ui_appearance_theme.py:158(update_shape_cache)
     1394    0.014    0.000    0.014    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     4336    0.013    0.000    0.013    0.000 sprite.py:745(sprites)
      122    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
       26    0.000    0.000    0.013    0.000 entity_handler.py:26(process_event)
       11    0.000    0.000    0.013    0.001 ui_text_box.py:310(parse_html_into_style_data)
     3765    0.007    0.000    0.013    0.000 world.py:55(get_tile)
      603    0.001    0.000    0.012    0.000 ui_button.py:130(kill)
     2113    0.010    0.000    0.011    0.000 ui_vertical_scroll_bar.py:228(update)
      612    0.001    0.000    0.011    0.000 ui_element.py:114(kill)
     2167    0.005    0.000    0.011    0.000 skill_bar.py:45(update)
      782    0.001    0.000    0.011    0.000 sprite.py:121(__init__)
     2112    0.008    0.000    0.010    0.000 ecs.py:247(delete_entity_immediately)
       74    0.000    0.000    0.010    0.000 __init__.py:1496(_log)
      242    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
      782    0.003    0.000    0.009    0.000 sprite.py:126(add)
       11    0.000    0.000    0.009    0.001 text_block.py:16(__init__)
        3    0.000    0.000    0.009    0.003 entity_handler.py:45(_process_move)
       11    0.001    0.000    0.009    0.001 text_block.py:40(redraw)
        2    0.000    0.000    0.009    0.004 ui_vertical_scroll_bar.py:22(__init__)
     2168    0.003    0.000    0.009    0.000 surface_cache.py:24(update)
    10946    0.008    0.000    0.008    0.000 query.py:243(<listcomp>)
        1    0.002    0.002    0.008    0.008 world.py:446(update_tile_visibility)
        5    0.000    0.000    0.008    0.002 manager.py:286(update_camera_game_map)
     4451    0.008    0.000    0.008    0.000 {built-in method builtins.sorted}
     2167    0.004    0.000    0.008    0.000 message_log.py:36(update)
      782    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
       21    0.000    0.000    0.007    0.000 game_handler.py:26(process_event)
      612    0.001    0.000    0.007    0.000 ui_container.py:52(remove_element)
       50    0.000    0.000    0.007    0.000 __init__.py:1996(debug)
       50    0.000    0.000    0.007    0.000 __init__.py:1361(debug)
     6813    0.005    0.000    0.007    0.000 ui_element.py:186(hover_point)
     2167    0.003    0.000    0.006    0.000 entity_info.py:45(update)
     6590    0.006    0.000    0.006    0.000 query.py:50(__init__)
      895    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
    88292    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
      790    0.005    0.000    0.006    0.000 sprite.py:822(change_layer)
     4355    0.006    0.000    0.006    0.000 state.py:45(get_current)
      782    0.005    0.000    0.006    0.000 sprite.py:646(add_internal)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
        2    0.000    0.000    0.005    0.003 entity.py:342(build_characteristic_sprites)
     2168    0.005    0.000    0.005    0.000 {built-in method pygame.mouse.get_pos}
     7572    0.005    0.000    0.005    0.000 ui_button.py:257(process_event)
       40    0.000    0.000    0.005    0.000 utility.py:13(get_image)
       74    0.000    0.000    0.005    0.000 __init__.py:1521(handle)
     2910    0.004    0.000    0.005    0.000 drawable_shape.py:122(rebuild_images_and_text)
       74    0.000    0.000    0.005    0.000 __init__.py:1575(callHandlers)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
     2180    0.003    0.000    0.005    0.000 query.py:225(<listcomp>)
        6    0.000    0.000    0.005    0.001 game_handler.py:78(process_end_turn)
       74    0.000    0.000    0.004    0.000 __init__.py:892(handle)
        6    0.000    0.000    0.004    0.001 chrono.py:47(next_turn)
       41    0.004    0.000    0.004    0.000 {built-in method pygame.imageext.load_extended}
        2    0.000    0.000    0.004    0.002 skill.py:136(_call_skill_func)
     3771    0.004    0.000    0.004    0.000 world.py:348(_is_tile_in_bounds)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:27(process_event)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:85(_process_entity_collision)
       74    0.000    0.000    0.004    0.000 __init__.py:1123(emit)
       74    0.000    0.000    0.004    0.000 __init__.py:1022(emit)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
    11629    0.004    0.000    0.004    0.000 ui_window.py:107(get_container)
        5    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
        5    0.001    0.000    0.004    0.001 camera.py:167(update_camera_tiles)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:135(_apply_effects_to_tiles)
      475    0.003    0.000    0.004    0.000 ui_manager.py:104(<listcomp>)
       21    0.002    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     6913    0.003    0.000    0.003    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
       51    0.003    0.000    0.003    0.000 {built-in method nt.stat}
       24    0.000    0.000    0.003    0.000 __init__.py:1986(info)
       24    0.000    0.000    0.003    0.000 __init__.py:1373(info)
     6591    0.003    0.000    0.003    0.000 {built-in method __new__ of type object at 0x00007FF84F319BA0}
       74    0.000    0.000    0.003    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.003    0.003 entity_handler.py:123(_process_use_skill)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
      612    0.001    0.000    0.003    0.000 sprite.py:183(kill)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
       34    0.001    0.000    0.003    0.000 styled_chunk.py:8(__init__)
       74    0.001    0.000    0.003    0.000 __init__.py:293(__init__)
       35    0.000    0.000    0.003    0.000 ui_appearance_theme.py:138(check_need_to_reload)
     5014    0.003    0.000    0.003    0.000 {method 'pop' of 'dict' objects}
      3/2    0.000    0.000    0.003    0.001 skill.py:216(process_effect)
        1    0.000    0.000    0.003    0.003 skill.py:111(use)
    15170    0.003    0.000    0.003    0.000 sprite.py:168(update)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       14    0.000    0.000    0.003    0.000 game_handler.py:39(process_change_game_state)
       11    0.000    0.000    0.003    0.000 parser.py:104(feed)
       11    0.000    0.000    0.002    0.000 parser.py:134(goahead)
       57    0.000    0.000    0.002    0.000 processors.py:57(process_intent)
        1    0.000    0.000    0.002    0.002 skill.py:258(_process_activate_skill)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        7    0.000    0.000    0.002    0.000 chrono.py:24(rebuild_turn_queue)
    10836    0.002    0.000    0.002    0.000 ui_window.py:116(check_hover)
       47    0.000    0.000    0.002    0.000 processors.py:138(_process_player_turn_intents)
      612    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
      772    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
       74    0.000    0.000    0.002    0.000 __init__.py:869(format)
     2170    0.002    0.000    0.002    0.000 {built-in method builtins.any}
      778    0.001    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
       75    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
       74    0.000    0.000    0.002    0.000 __init__.py:606(format)
       59    0.001    0.000    0.002    0.000 entity.py:43(get_player)
        2    0.000    0.000    0.002    0.001 __init__.py:109(import_module)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:994(_gcd_import)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
     2910    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
        4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
       68    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
     1500    0.001    0.000    0.002    0.000 libtcodpy.py:3300(map_is_in_fov)
      9/7    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        5    0.000    0.000    0.001    0.000 entity.py:485(take_turn)
     6813    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
        2    0.000    0.000    0.001    0.001 __init__.py:133(reload)
       74    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       34    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
        1    0.000    0.000    0.001    0.001 basic_attack.py:17(activate)
     7542    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      896    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
       79    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
     1448    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
      772    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       74    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
       79    0.001    0.000    0.001    0.000 ntpath.py:178(split)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:610(_exec)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
       66    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
        1    0.000    0.000    0.001    0.001 skill.py:412(_process_damage_effect)
     2113    0.001    0.000    0.001    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
       74    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
     3088    0.001    0.000    0.001    0.000 {built-in method math.floor}
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       74    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
       11    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
       11    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
       34    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
       66    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
        6    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
     2290    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}
       75    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
      829    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
     4625    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
       57    0.000    0.000    0.001    0.000 action.py:12(convert_to_intent)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
       15    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
      772    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
       36    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
     2570    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
      189    0.000    0.000    0.001    0.000 entity.py:93(get_entitys_component)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
       74    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       34    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        1    0.000    0.000    0.000    0.000 entity_handler.py:160(_process_die)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
      801    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       74    0.000    0.000    0.000    0.000 {built-in method time.strftime}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
     1564    0.000    0.000    0.000    0.000 {built-in method builtins.min}
     2910    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
     1503    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     1572    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      111    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 skill.py:529(_calculate_to_hit_score)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
      158    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
      122    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        1    0.000    0.000    0.000    0.000 skill.py:477(_calculate_damage)
       46    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       89    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
     2944    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       48    0.000    0.000    0.000    0.000 entity.py:103(get_name)
       74    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       30    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
     1573    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      120    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      782    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
       34    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        8    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       48    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
     1528    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       74    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
       33    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        7    0.000    0.000    0.000    0.000 world.py:261(tile_has_tag)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        1    0.000    0.000    0.000    0.000 entity.py:303(create_projectile)
       74    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
       74    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      116    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
        7    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
  336/318    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        8    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       11    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
       74    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       21    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      148    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
       44    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
      776    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
      782    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      249    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        7    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       56    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
       74    0.000    0.000    0.000    0.000 __init__.py:432(format)
       47    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
      148    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
      155    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        1    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
        7    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        1    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
      782    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
      247    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
      649    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 entity.py:189(delete)
       57    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      769    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
       57    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
        3    0.000    0.000    0.000    0.000 ai.py:68(act)
        7    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       34    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        7    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        7    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        7    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       33    0.000    0.000    0.000    0.000 event_core.py:41(publish)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
       72    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        4    0.000    0.000    0.000    0.000 entity.py:174(create)
        1    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
       66    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
       74    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      148    0.000    0.000    0.000    0.000 __init__.py:856(release)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
        4    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        3    0.000    0.000    0.000    0.000 world.py:360(_is_tile_blocking_movement)
      345    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        4    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       74    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        4    0.000    0.000    0.000    0.000 world.py:396(_tile_has_other_entity)
        5    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
       21    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        3    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
      194    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       47    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
       74    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
       59    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
       74    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      148    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
        1    0.000    0.000    0.000    0.000 god_handler.py:71(process_interventions)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
       51    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
       74    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
      222    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        6    0.000    0.000    0.000    0.000 entity_handler.py:213(_process_end_turn)
      422    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      612    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       21    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
      458    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 entity.py:428(consider_intervening)
      258    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
      122    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
       77    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       74    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      188    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       11    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      130    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
      315    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
      242    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        6    0.000    0.000    0.000    0.000 event.py:80(__init__)
       74    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       33    0.000    0.000    0.000    0.000 event_core.py:15(notify)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      150    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       51    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      668    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        2    0.000    0.000    0.000    0.000 ai.py:42(act)
       79    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        6    0.000    0.000    0.000    0.000 entity.py:380(spend_time)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
       55    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
       14    0.000    0.000    0.000    0.000 event.py:98(__init__)
      120    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 skill.py:244(_process_trigger_skill_effect)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
       14    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        1    0.000    0.000    0.000    0.000 world.py:439(recompute_fov)
       15    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       74    0.000    0.000    0.000    0.000 threading.py:1052(name)
       11    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
        1    0.000    0.000    0.000    0.000 world.py:300(tile_has_tags)
       33    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       54    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
       75    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       34    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        5    0.000    0.000    0.000    0.000 event.py:176(__init__)
      120    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
      160    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
      129    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       21    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       70    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        7    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       74    0.000    0.000    0.000    0.000 {built-in method time.time}
       74    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
       34    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        3    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        5    0.000    0.000    0.000    0.000 entity.py:335(add_component)
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
      116    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
      150    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       70    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       21    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       44    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       31    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        2    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
       40    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        3    0.000    0.000    0.000    0.000 event.py:63(__init__)
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        4    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
       49    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
        1    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        9    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        5    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
       11    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       40    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 random.py:218(randint)
       38    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        5    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
      100    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        9    0.000    0.000    0.000    0.000 {built-in method math.sin}
       38    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       38    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       33    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       42    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       20    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       76    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 event.py:128(__init__)
       20    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        7    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       34    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       48    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       11    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       10    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       21    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       35    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       11    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
        1    0.000    0.000    0.000    0.000 event.py:29(__init__)
        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
       15    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
       15    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        2    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        5    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        7    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
       20    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 event.py:54(__init__)
        1    0.000    0.000    0.000    0.000 event.py:90(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
       18    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
       22    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        8    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        8    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
       45    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.format}
       30    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 component.py:82(__init__)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        5    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        2    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        1    0.000    0.000    0.000    0.000 skill.py:202(_get_hit_type)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        6    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 component.py:31(__init__)
        3    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        6    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:46(process_judgements)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        6    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        6    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        4    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        2    0.000    0.000    0.000    0.000 component.py:118(__init__)
        2    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 component.py:199(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        6    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 world.py:311(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 basic_attack.py:13(use)
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}


