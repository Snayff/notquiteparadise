Sat Mar 21 14:51:19 2020    logs/profiling/profile.dump

         106374562 function calls (106242764 primitive calls) in 1046.316 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1   11.338   11.338 1046.273 1046.273 main.py:85(game_loop)
    62430  713.548    0.011  713.548    0.011 {method 'tick' of 'Clock' objects}
    31215    0.128    0.000  365.992    0.012 state.py:63(update_clock)
    31215    0.179    0.000  347.863    0.011 state.py:38(get_delta_time)
    31215    0.496    0.000  153.998    0.005 manager.py:73(draw)
    31215    0.127    0.000  146.765    0.005 manager.py:54(update)
    31215    9.550    0.000  146.638    0.005 ui_manager.py:122(update)
 10153984  107.917    0.000  107.917    0.000 {method 'blit' of 'pygame.Surface' objects}
    31215    5.096    0.000   86.698    0.003 sprite.py:453(update)
    31214    0.193    0.000   65.372    0.002 camera.py:72(update)
    31219   31.068    0.001   65.124    0.002 camera.py:79(update_game_map)
    31215    0.234    0.000   59.444    0.002 ui_manager.py:173(draw_ui)
    31215    9.375    0.000   59.211    0.002 sprite.py:753(draw)
    31219   44.567    0.001   44.567    0.001 {built-in method pygame.transform.scale}
  5025738   22.458    0.000   39.563    0.000 ui_element.py:121(check_hover)
  4931752    9.735    0.000   14.506    0.000 ui_button.py:197(update)
    31215    0.033    0.000   13.118    0.000 event_core.py:24(update)
        2    0.000    0.000   12.213    6.107 interaction_handler.py:26(process_event)
        2    0.000    0.000   12.213    6.107 interaction_handler.py:88(_process_entity_collision)
        2    0.001    0.000   12.212    6.106 interaction_handler.py:126(_apply_effects_to_tiles)
        2    1.179    0.589   12.212    6.106 skill.py:139(_call_skill_func)
      3/2    0.978    0.326   12.211    6.106 skill.py:219(process_effect)
        1    0.001    0.001   12.210   12.210 skill.py:261(_process_activate_skill)
  4925583    6.092    0.000   11.724    0.000 ui_button.py:138(hover_point)
    31215   11.474    0.000   11.474    0.000 {built-in method pygame.display.flip}
        1    4.220    4.220   11.029   11.029 basic_attack.py:17(activate)
   282203    8.799    0.000    9.299    0.000 sprite.py:913(get_sprites_from_layer)
  4682853    7.000    0.000    7.000    0.000 camera.py:233(world_to_screen_position)
        1    5.829    5.829    5.830    5.830 skill.py:415(_process_damage_effect)
  4929272    4.962    0.000    5.639    0.000 rect_drawable_shape.py:84(collide_point)
    31215    4.799    0.000    4.799    0.000 {built-in method pygame.event.get}
    35421    4.556    0.000    4.556    0.000 {method 'fill' of 'pygame.Surface' objects}
 10207547    3.688    0.000    4.443    0.000 sprite.py:208(alive)
  4931752    2.438    0.000    2.815    0.000 drawable_shape.py:36(update)
  4931752    2.061    0.000    2.061    0.000 ui_button.py:154(can_hover)
    31215    0.115    0.000    1.874    0.000 processors.py:16(process_all)
    31215    0.918    0.000    1.759    0.000 processors.py:23(_process_aesthetic_update)
 11372298    1.174    0.000    1.174    0.000 {method 'append' of 'list' objects}
   218831    0.742    0.000    0.957    0.000 query.py:212(__iter__)
  5269626    0.883    0.000    0.883    0.000 ui_manager.py:167(get_mouse_position)
    31578    0.467    0.000    0.877    0.000 ui_text_box.py:205(update)
       31    0.000    0.000    0.851    0.027 ui_handler.py:30(process_event)
        5    0.000    0.000    0.822    0.164 ui_handler.py:207(update_camera)
        5    0.000    0.000    0.809    0.162 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.809    0.162 camera.py:105(update_grid)
   187285    0.578    0.000    0.801    0.000 ui_container.py:124(check_hover)
      758    0.010    0.000    0.796    0.001 ui_button.py:30(__init__)
 10207547    0.755    0.000    0.755    0.000 {built-in method _operator.truth}
  5214206    0.752    0.000    0.752    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      758    0.042    0.000    0.748    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
  5025132    0.668    0.000    0.668    0.000 {method 'union' of 'pygame.Rect' objects}
        6    0.000    0.000    0.655    0.109 ui_handler.py:48(process_entity_event)
    22111    0.056    0.000    0.604    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
  5368642    0.582    0.000    0.582    0.000 {method 'colliderect' of 'pygame.Rect' objects}
153867/22111    0.515    0.000    0.544    0.000 ui_appearance_theme.py:322(get_next_id_node)
    93799    0.304    0.000    0.347    0.000 typing.py:806(__new__)
  5184853    0.346    0.000    0.346    0.000 {built-in method builtins.len}
    31215    0.197    0.000    0.344    0.000 ecs.py:265(process_pending_deletions)
    11430    0.030    0.000    0.340    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   156071    0.280    0.000    0.337    0.000 ui_window.py:97(update)
    93799    0.227    0.000    0.320    0.000 query.py:170(__init__)
    31346    0.200    0.000    0.292    0.000 sprite.py:814(layers)
    31194    0.186    0.000    0.279    0.000 ui_vertical_scroll_bar.py:228(update)
    31215    0.135    0.000    0.206    0.000 ui_manager.py:158(update_mouse_position)
     6882    0.014    0.000    0.200    0.000 ui_appearance_theme.py:428(get_misc_data)
    62430    0.187    0.000    0.187    0.000 sprite.py:745(sprites)
       21    0.000    0.000    0.181    0.009 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.175    0.175 ui_handler.py:111(init_game_ui)
    31214    0.081    0.000    0.160    0.000 skill_bar.py:45(update)
    31215    0.081    0.000    0.148    0.000 ui_appearance_theme.py:158(update_shape_cache)
    31195    0.109    0.000    0.147    0.000 ecs.py:247(delete_entity_immediately)
    31214    0.058    0.000    0.133    0.000 message_log.py:36(update)
    62695    0.121    0.000    0.121    0.000 {built-in method builtins.sorted}
   156251    0.120    0.000    0.120    0.000 query.py:243(<listcomp>)
      758    0.005    0.000    0.093    0.000 ui_button.py:97(set_any_images_from_theme)
    93799    0.092    0.000    0.092    0.000 query.py:50(__init__)
    31214    0.042    0.000    0.092    0.000 entity_info.py:45(update)
    93986    0.076    0.000    0.092    0.000 ui_element.py:186(hover_point)
      131    0.001    0.000    0.089    0.001 manager.py:60(process_ui_events)
     3032    0.006    0.000    0.088    0.000 ui_appearance_theme.py:366(get_image)
      131    0.032    0.000    0.088    0.001 ui_manager.py:86(process_events)
    62449    0.087    0.000    0.087    0.000 state.py:45(get_current)
    31215    0.071    0.000    0.071    0.000 {built-in method pygame.mouse.get_pos}
    31227    0.049    0.000    0.070    0.000 query.py:225(<listcomp>)
    31215    0.039    0.000    0.068    0.000 surface_cache.py:24(update)
     2899    0.020    0.000    0.060    0.000 rect_drawable_shape.py:118(redraw_state)
   156860    0.057    0.000    0.057    0.000 ui_window.py:107(get_container)
    24823    0.048    0.000    0.048    0.000 ui_button.py:170(while_hovering)
    94192    0.046    0.000    0.046    0.000 {method 'get' of 'dict' objects}
      758    0.006    0.000    0.045    0.000 ui_button.py:537(rebuild_shape)
      508    0.002    0.000    0.044    0.000 ui_appearance_theme.py:138(check_need_to_reload)
    93804    0.043    0.000    0.043    0.000 {built-in method __new__ of type object at 0x00007FF84F319BA0}
        1    0.000    0.000    0.042    0.042 main.py:193(initialise_game)
      524    0.042    0.000    0.042    0.000 {built-in method nt.stat}
      364    0.002    0.000    0.042    0.000 screen_message.py:34(update)
      767    0.003    0.000    0.040    0.000 rect_drawable_shape.py:22(__init__)
        2    0.000    0.000    0.039    0.019 entity.py:232(create_actor)
    63175    0.038    0.000    0.038    0.000 {method 'pop' of 'dict' objects}
   218499    0.038    0.000    0.038    0.000 sprite.py:168(update)
     3684    0.016    0.000    0.036    0.000 ui_button.py:226(set_position)
      777    0.008    0.000    0.036    0.000 ui_element.py:23(__init__)
      767    0.011    0.000    0.036    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      242    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
   156071    0.031    0.000    0.031    0.000 ui_window.py:116(check_hover)
      758    0.003    0.000    0.030    0.000 ui_appearance_theme.py:405(get_font)
     3683    0.022    0.000    0.030    0.000 ui_button.py:381(in_hold_range)
    31217    0.026    0.000    0.026    0.000 {built-in method builtins.any}
      242    0.003    0.000    0.025    0.000 ui_text_box.py:327(redraw_from_text_block)
      767    0.004    0.000    0.022    0.000 drawable_shape.py:45(redraw_all_states)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
        8    0.000    0.000    0.019    0.002 ui_text_box.py:50(__init__)
    93986    0.018    0.000    0.018    0.000 ui_element.py:204(can_hover)
        8    0.000    0.000    0.018    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     2935    0.017    0.000    0.017    0.000 {method 'copy' of 'pygame.Surface' objects}
      777    0.002    0.000    0.017    0.000 ui_container.py:42(add_element)
        8    0.000    0.000    0.017    0.002 ui_text_box.py:110(rebuild)
     2899    0.016    0.000    0.016    0.000 surface_cache.py:119(build_cache_id)
        5    0.003    0.001    0.015    0.003 ui_container.py:116(clear)
    31194    0.015    0.000    0.015    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
      109    0.001    0.000    0.014    0.000 __init__.py:1496(_log)
       27    0.000    0.000    0.013    0.000 entity_handler.py:27(process_event)
     1384    0.013    0.000    0.013    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      122    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
     3765    0.008    0.000    0.013    0.000 world.py:55(get_tile)
    18465    0.013    0.000    0.013    0.000 ui_button.py:257(process_event)
        5    0.000    0.000    0.013    0.003 message_log.py:49(add_message)
      600    0.001    0.000    0.012    0.000 ui_button.py:130(kill)
       86    0.000    0.000    0.012    0.000 __init__.py:1996(debug)
       86    0.000    0.000    0.012    0.000 __init__.py:1361(debug)
      607    0.001    0.000    0.012    0.000 ui_element.py:114(kill)
     3684    0.011    0.000    0.011    0.000 ui_element.py:160(set_position)
        4    0.000    0.000    0.011    0.003 ui_handler.py:155(process_ui_event)
        4    0.000    0.000    0.011    0.003 ui_handler.py:238(process_message)
        4    0.000    0.000    0.011    0.003 manager.py:444(add_to_message_log)
      777    0.001    0.000    0.011    0.000 sprite.py:121(__init__)
    31487    0.010    0.000    0.010    0.000 {method 'values' of 'dict' objects}
        9    0.000    0.000    0.010    0.001 ui_text_box.py:310(parse_html_into_style_data)
      242    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
     4504    0.009    0.000    0.010    0.000 {built-in method _warnings.warn}
        5    0.000    0.000    0.009    0.002 manager.py:286(update_camera_game_map)
      777    0.003    0.000    0.009    0.000 sprite.py:126(add)
        3    0.000    0.000    0.009    0.003 entity_handler.py:49(_process_move)
     1094    0.009    0.000    0.009    0.000 ui_manager.py:104(<listcomp>)
        1    0.002    0.002    0.008    0.008 world.py:446(update_tile_visibility)
     3684    0.008    0.000    0.008    0.000 rect_drawable_shape.py:107(set_position)
        9    0.000    0.000    0.008    0.001 text_block.py:16(__init__)
        9    0.001    0.000    0.008    0.001 text_block.py:40(redraw)
      777    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
      109    0.000    0.000    0.007    0.000 __init__.py:1521(handle)
      607    0.001    0.000    0.007    0.000 ui_container.py:52(remove_element)
      109    0.000    0.000    0.007    0.000 __init__.py:1575(callHandlers)
       21    0.000    0.000    0.006    0.000 game_handler.py:26(process_event)
      109    0.000    0.000    0.006    0.000 __init__.py:892(handle)
        2    0.000    0.000    0.006    0.003 entity.py:342(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
      131    0.001    0.000    0.006    0.000 processors.py:57(process_intent)
      844    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
    87896    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      109    0.000    0.000    0.006    0.000 __init__.py:1123(emit)
      785    0.005    0.000    0.006    0.000 sprite.py:822(change_layer)
      777    0.005    0.000    0.006    0.000 sprite.py:646(add_internal)
      109    0.000    0.000    0.005    0.000 __init__.py:1022(emit)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      114    0.001    0.000    0.005    0.000 processors.py:138(_process_player_turn_intents)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
     5206    0.005    0.000    0.005    0.000 {built-in method builtins.max}
     2899    0.004    0.000    0.005    0.000 drawable_shape.py:122(rebuild_images_and_text)
      109    0.000    0.000    0.005    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.004    0.004 ui_vertical_scroll_bar.py:22(__init__)
     3771    0.004    0.000    0.004    0.000 world.py:348(_is_tile_in_bounds)
      109    0.002    0.000    0.004    0.000 __init__.py:293(__init__)
        6    0.000    0.000    0.004    0.001 game_handler.py:78(process_end_turn)
      126    0.002    0.000    0.004    0.000 entity.py:43(get_player)
        6    0.000    0.000    0.004    0.001 chrono.py:47(next_turn)
        5    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
        5    0.001    0.000    0.004    0.001 camera.py:167(update_camera_tiles)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
      607    0.001    0.000    0.003    0.000 sprite.py:183(kill)
        1    0.000    0.000    0.003    0.003 entity_handler.py:127(_process_use_skill)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
        1    0.000    0.000    0.003    0.003 skill.py:111(use)
      109    0.000    0.000    0.003    0.000 __init__.py:869(format)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       23    0.000    0.000    0.003    0.000 __init__.py:1986(info)
       18    0.002    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
       23    0.000    0.000    0.003    0.000 __init__.py:1373(info)
      109    0.001    0.000    0.003    0.000 __init__.py:606(format)
     5236    0.003    0.000    0.003    0.000 {built-in method builtins.min}
        8    0.000    0.000    0.002    0.000 chrono.py:24(rebuild_turn_queue)
       14    0.000    0.000    0.002    0.000 game_handler.py:39(process_change_game_state)
        4    0.000    0.000    0.002    0.001 pydevd_modify_bytecode.py:213(insert_code)
        3    0.000    0.000    0.002    0.001 pydevd_modify_bytecode.py:233(_insert_code)
      607    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       22    0.001    0.000    0.002    0.000 styled_chunk.py:8(__init__)
        3    0.001    0.000    0.002    0.001 pydevd_modify_bytecode.py:128(_update_label_offsets)
      767    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
      773    0.001    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
        4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
        2    0.000    0.000    0.002    0.001 __init__.py:109(import_module)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:994(_gcd_import)
      109    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
     2899    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
       57    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
        9    0.000    0.000    0.002    0.000 parser.py:104(feed)
      9/7    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        9    0.000    0.000    0.002    0.000 parser.py:134(goahead)
      115    0.000    0.000    0.002    0.000 ntpath.py:212(basename)
        5    0.000    0.000    0.001    0.000 entity.py:485(take_turn)
      131    0.001    0.000    0.001    0.000 action.py:12(convert_to_intent)
      109    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
        2    0.000    0.000    0.001    0.001 __init__.py:133(reload)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
      115    0.001    0.000    0.001    0.000 ntpath.py:178(split)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
       44    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
      109    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
     1429    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
     7542    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      109    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
      845    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
      767    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
        6    0.000    0.000    0.001    0.000 god_handler.py:26(process_event)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:610(_exec)
        1    0.001    0.001    0.001    0.001 camera.py:24(__init__)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
     3068    0.001    0.000    0.001    0.000 {built-in method math.floor}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
      582    0.001    0.000    0.001    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        8    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
       22    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
      900    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
      110    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      109    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
      109    0.001    0.000    0.001    0.000 {built-in method time.strftime}
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        9    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
     4834    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
        9    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
       15    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        6    0.000    0.000    0.001    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.001    0.001 entity_handler.py:164(_process_die)
      230    0.000    0.000    0.001    0.000 ntpath.py:44(normcase)
      767    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
     2695    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
       42    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      156    0.000    0.000    0.000    0.000 entity.py:93(get_entitys_component)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      127    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
      803    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       42    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
     1562    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      109    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
      122    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
      108    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
     2899    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
      114    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
       22    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
       45    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       26    0.000    0.000    0.000    0.000 entity.py:131(get_primary_stat)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
       73    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
       12    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
      597    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
       49    0.000    0.000    0.000    0.000 entity.py:103(get_name)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       30    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
      109    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       22    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
      120    0.000    0.000    0.000    0.000 text_effects.py:88(update)
     1563    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        3    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        1    0.000    0.000    0.000    0.000 entity_handler.py:225(_process_created_timed_entity)
      109    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        7    0.000    0.000    0.000    0.000 world.py:261(tile_has_tag)
       12    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      109    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
      131    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
      777    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      139    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       49    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
        1    0.000    0.000    0.000    0.000 skill.py:532(_calculate_to_hit_score)
      109    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
     1520    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
      833    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        6    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      218    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
       32    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
       30    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
       12    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
     2034    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        6    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
      131    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      109    0.000    0.000    0.000    0.000 __init__.py:432(format)
        1    0.000    0.000    0.000    0.000 entity.py:303(create_projectile)
      225    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       18    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      114    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        4    0.000    0.000    0.000    0.000 entity.py:174(create)
      777    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        7    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      773    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        8    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
      247    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 world.py:396(_tile_has_other_entity)
      777    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
      109    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
      649    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      218    0.000    0.000    0.000    0.000 __init__.py:856(release)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        4    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        1    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
        4    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        1    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
        1    0.000    0.000    0.000    0.000 entity.py:189(delete)
        6    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
      765    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
      109    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       33    0.000    0.000    0.000    0.000 event_core.py:41(publish)
      109    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
      129    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
      100    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       40    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
      218    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        3    0.000    0.000    0.000    0.000 world.py:360(_is_tile_blocking_movement)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        3    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
      109    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      327    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      111    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        4    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
      605    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      128    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        3    0.000    0.000    0.000    0.000 ai.py:72(act)
      372    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
      122    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
        1    0.000    0.000    0.000    0.000 world.py:300(tile_has_tags)
       22    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      109    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        5    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       18    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      109    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      161    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
      363    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        5    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        5    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        5    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      220    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
      458    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      607    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
      157    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       48    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
      115    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        6    0.000    0.000    0.000    0.000 entity_handler.py:217(_process_end_turn)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:52(_pydev_stop_at_break)
        1    0.000    0.000    0.000    0.000 entity.py:428(consider_intervening)
       51    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
        9    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        2    0.000    0.000    0.000    0.000 ai.py:45(act)
      109    0.000    0.000    0.000    0.000 threading.py:1052(name)
       33    0.000    0.000    0.000    0.000 event_core.py:15(notify)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
        9    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      313    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       18    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
      242    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       16    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
      155    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        6    0.000    0.000    0.000    0.000 entity.py:380(spend_time)
       51    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      108    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
       14    0.000    0.000    0.000    0.000 event.py:106(__init__)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
      120    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
      114    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        1    0.000    0.000    0.000    0.000 skill.py:247(_process_trigger_skill_effect)
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        1    0.000    0.000    0.000    0.000 world.py:439(recompute_fov)
        9    0.000    0.000    0.000    0.000 parser.py:96(reset)
       51    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
      165    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       16    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
      232    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
      109    0.000    0.000    0.000    0.000 {built-in method time.time}
       42    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       12    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       33    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
      109    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        8    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
      433    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        3    0.000    0.000    0.000    0.000 event.py:63(__init__)
      120    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
      220    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        3    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        5    0.000    0.000    0.000    0.000 entity.py:335(add_component)
       18    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        3    0.000    0.000    0.000    0.000 component.py:39(__init__)
       44    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        4    0.000    0.000    0.000    0.000 event.py:184(__init__)
       28    0.000    0.000    0.000    0.000 _weakrefset.py:38(_remove)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        5    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        2    0.000    0.000    0.000    0.000 _collections_abc.py:657(get)
       18    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       67    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        6    0.000    0.000    0.000    0.000 event.py:88(__init__)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        1    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       86    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       22    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       12    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       46    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
        4    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       30    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        1    0.000    0.000    0.000    0.000 random.py:218(randint)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       22    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        1    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 os.py:673(__getitem__)
        5    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
       39    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        2    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        8    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       21    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       32    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        8    0.000    0.000    0.000    0.000 {built-in method math.sin}
       28    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
       20    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        2    0.000    0.000    0.000    0.000 event.py:136(__init__)
        9    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       27    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        8    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
       27    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       10    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
       48    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       27    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       30    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       18    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       64    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        3    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
       52    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       17    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        9    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
        2    0.000    0.000    0.000    0.000 ui_button.py:340(select)
        2    0.000    0.000    0.000    0.000 os.py:743(encodekey)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
       22    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       15    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        5    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        1    0.000    0.000    0.000    0.000 event.py:29(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        9    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        9    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
       49    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       20    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 event.py:54(__init__)
        3    0.000    0.000    0.000    0.000 <string>:1(__new__)
        6    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
       25    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       34    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
       23    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        5    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        8    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
       18    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:21(update_globals_dict)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
       12    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        9    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        4    0.000    0.000    0.000    0.000 component.py:81(__init__)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        2    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
       25    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       24    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        4    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 entity_handler.py:24(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        1    0.000    0.000    0.000    0.000 event.py:77(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 component.py:30(__init__)
        8    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:183(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        2    0.000    0.000    0.000    0.000 pydev_log.py:16(debug)
        3    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        3    0.000    0.000    0.000    0.000 component.py:63(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
        2    0.000    0.000    0.000    0.000 os.py:737(check_str)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        9    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        6    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
        3    0.000    0.000    0.000    0.000 component.py:132(__init__)
        9    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        6    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        3    0.000    0.000    0.000    0.000 component.py:55(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        6    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_constants.py:479(get_global_debugger)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 component.py:72(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        2    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        2    0.000    0.000    0.000    0.000 component.py:117(__init__)
        2    0.000    0.000    0.000    0.000 component.py:109(__init__)
        1    0.000    0.000    0.000    0.000 component.py:175(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:69(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        4    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {_pydevd_frame_eval.pydevd_frame_evaluator_win32_37_64.get_thread_info_py}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        2    0.000    0.000    0.000    0.000 component.py:91(__init__)
        2    0.000    0.000    0.000    0.000 component.py:100(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 world.py:311(<genexpr>)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        1    0.000    0.000    0.000    0.000 ui_element.py:220(select)
        1    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 ui_element.py:226(unselect)
        1    0.000    0.000    0.000    0.000 basic_attack.py:13(use)
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


