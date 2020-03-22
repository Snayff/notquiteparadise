Sun Mar 22 15:46:13 2020    logs/profiling/profile.dump

         7203701 function calls (6990583 primitive calls) in 58.040 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.621    0.621   57.998   57.998 main.py:103(game_loop)
     3422   39.077    0.011   39.077    0.011 {method 'tick' of 'Clock' objects}
     1711    0.006    0.000   19.801    0.012 state.py:63(update_clock)
     1711    0.009    0.000   19.291    0.011 state.py:38(get_delta_time)
     1711    0.024    0.000    8.244    0.005 manager.py:73(draw)
     1711    0.007    0.000    7.959    0.005 manager.py:54(update)
     1711    0.501    0.000    7.952    0.005 ui_manager.py:122(update)
   552056    5.884    0.000    5.884    0.000 {method 'blit' of 'pygame.Surface' objects}
     1711    0.267    0.000    4.779    0.003 sprite.py:453(update)
     1718    1.678    0.001    3.561    0.002 camera.py:79(update_game_map)
     1710    0.011    0.000    3.560    0.002 camera.py:72(update)
     1711    0.013    0.000    3.176    0.002 ui_manager.py:173(draw_ui)
     1711    0.492    0.000    3.163    0.002 sprite.py:753(draw)
     1715    2.328    0.001    2.328    0.001 {built-in method pygame.transform.scale}
   269232    1.181    0.000    2.076    0.000 ui_element.py:121(check_hover)
     1711    0.002    0.000    1.410    0.001 event_core.py:24(update)
       57    0.000    0.000    1.352    0.024 ui_handler.py:31(process_event)
        8    0.000    0.000    1.299    0.162 ui_handler.py:201(_update_camera)
        8    0.000    0.000    1.278    0.160 manager.py:295(update_camera_grid)
        8    0.008    0.001    1.278    0.160 camera.py:105(update_grid)
     1220    0.016    0.000    1.267    0.001 ui_button.py:30(__init__)
     1220    0.065    0.000    1.191    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        9    0.000    0.000    1.139    0.127 ui_handler.py:44(process_entity_event)
    35605    0.088    0.000    0.964    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
248685/35605    0.823    0.000    0.869    0.000 ui_appearance_theme.py:322(get_next_id_node)
   265347    0.516    0.000    0.863    0.000 ui_button.py:197(update)
     1711    0.632    0.000    0.632    0.000 {built-in method pygame.display.flip}
   265347    0.317    0.000    0.617    0.000 ui_button.py:138(hover_point)
    18404    0.047    0.000    0.544    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    16208    0.489    0.000    0.517    0.000 sprite.py:913(get_sprites_from_layer)
     1711    0.502    0.000    0.502    0.000 {built-in method pygame.event.get}
   257707    0.378    0.000    0.378    0.000 camera.py:233(world_to_screen_position)
    11084    0.021    0.000    0.318    0.000 ui_appearance_theme.py:428(get_misc_data)
   265347    0.264    0.000    0.300    0.000 rect_drawable_shape.py:84(collide_point)
     2282    0.253    0.000    0.253    0.000 {method 'fill' of 'pygame.Surface' objects}
   265347    0.139    0.000    0.246    0.000 drawable_shape.py:36(update)
   547015    0.188    0.000    0.227    0.000 sprite.py:208(alive)
       40    0.000    0.000    0.173    0.004 ui_handler.py:68(process_game_event)
        1    0.000    0.000    0.168    0.168 ui_handler.py:107(init_game_ui)
     1220    0.008    0.000    0.149    0.000 ui_button.py:97(set_any_images_from_theme)
     4880    0.009    0.000    0.141    0.000 ui_appearance_theme.py:366(get_image)
     6117    0.039    0.000    0.115    0.000 rect_drawable_shape.py:118(redraw_state)
   265347    0.110    0.000    0.110    0.000 ui_button.py:154(can_hover)
     1711    0.006    0.000    0.105    0.000 processors.py:18(process_all)
     1711    0.051    0.000    0.099    0.000 processors.py:25(_process_aesthetic_update)
  1042838    0.091    0.000    0.091    0.000 {method 'append' of 'list' objects}
     1220    0.009    0.000    0.071    0.000 ui_button.py:537(rebuild_shape)
     1237    0.004    0.000    0.062    0.000 rect_drawable_shape.py:22(__init__)
     1247    0.013    0.000    0.057    0.000 ui_element.py:23(__init__)
     1237    0.017    0.000    0.055    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
    12265    0.041    0.000    0.053    0.000 query.py:212(__iter__)
       80    0.000    0.000    0.050    0.001 manager.py:60(process_ui_events)
       80    0.018    0.000    0.050    0.001 ui_manager.py:86(process_events)
     1220    0.006    0.000    0.047    0.000 ui_appearance_theme.py:405(get_font)
   281668    0.046    0.000    0.046    0.000 ui_manager.py:167(get_mouse_position)
       12    0.000    0.000    0.046    0.004 ui_text_box.py:50(__init__)
       12    0.000    0.000    0.045    0.004 ui_text_box.py:492(rebuild_from_changed_theme_data)
       12    0.001    0.000    0.043    0.004 ui_text_box.py:110(rebuild)
    10261    0.032    0.000    0.043    0.000 ui_container.py:124(check_hover)
     2076    0.017    0.000    0.043    0.000 ui_text_box.py:205(update)
        1    0.000    0.000    0.042    0.042 main.py:211(initialise_game)
    10507    0.013    0.000    0.042    0.000 _internal.py:24(wrapper)
       49    0.000    0.000    0.041    0.001 entity_handler.py:26(process_event)
        9    0.000    0.000    0.041    0.005 message_log.py:49(add_message)
      366    0.002    0.000    0.041    0.000 screen_message.py:34(update)
        7    0.000    0.000    0.040    0.006 entity_handler.py:45(_process_move)
   279493    0.040    0.000    0.040    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
   268156    0.040    0.000    0.040    0.000 {method 'union' of 'pygame.Rect' objects}
   547015    0.040    0.000    0.040    0.000 {built-in method _operator.truth}
        8    0.000    0.000    0.039    0.005 ui_handler.py:151(process_ui_event)
        8    0.000    0.000    0.039    0.005 ui_handler.py:232(_process_message)
        8    0.000    0.000    0.039    0.005 manager.py:444(add_to_message_log)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
        5    0.010    0.002    0.038    0.008 world.py:447(update_tile_visibility)
   676874    0.037    0.000    0.037    0.000 {built-in method builtins.len}
      246    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
     6117    0.034    0.000    0.034    0.000 surface_cache.py:119(build_cache_id)
     1237    0.006    0.000    0.033    0.000 drawable_shape.py:45(redraw_all_states)
   287471    0.032    0.000    0.032    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
     6185    0.029    0.000    0.029    0.000 {method 'copy' of 'pygame.Surface' objects}
     1247    0.003    0.000    0.026    0.000 ui_container.py:42(add_element)
        8    0.005    0.001    0.025    0.003 ui_container.py:116(clear)
      246    0.003    0.000    0.024    0.000 ui_text_box.py:327(redraw_from_text_block)
        5    0.000    0.000    0.021    0.004 ui_vertical_scroll_bar.py:22(__init__)
     2324    0.021    0.000    0.021    0.000 ui_container.py:62(recalculate_container_layer_thickness)
    10508    0.020    0.000    0.021    0.000 {built-in method _warnings.warn}
     1062    0.001    0.000    0.020    0.000 ui_button.py:130(kill)
       17    0.000    0.000    0.019    0.001 ui_text_box.py:310(parse_html_into_style_data)
     5266    0.017    0.000    0.019    0.000 typing.py:806(__new__)
     1711    0.005    0.000    0.019    0.000 ui_appearance_theme.py:158(update_shape_cache)
     1077    0.002    0.000    0.019    0.000 ui_element.py:114(kill)
     8551    0.016    0.000    0.019    0.000 ui_window.py:97(update)
     5266    0.013    0.000    0.018    0.000 query.py:170(__init__)
     1247    0.002    0.000    0.017    0.000 sprite.py:121(__init__)
     1791    0.011    0.000    0.016    0.000 sprite.py:814(layers)
     1247    0.005    0.000    0.015    0.000 sprite.py:126(add)
        8    0.000    0.000    0.015    0.002 manager.py:286(update_camera_game_map)
     1711    0.002    0.000    0.014    0.000 surface_cache.py:24(update)
     4234    0.008    0.000    0.014    0.000 world.py:55(get_tile)
      108    0.001    0.000    0.014    0.000 __init__.py:1496(_log)
       40    0.000    0.000    0.014    0.000 game_handler.py:26(process_event)
       17    0.000    0.000    0.013    0.001 text_block.py:16(__init__)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
       17    0.003    0.000    0.013    0.001 text_block.py:40(redraw)
     1711    0.008    0.000    0.012    0.000 ui_manager.py:158(update_mouse_position)
     1247    0.003    0.000    0.011    0.000 ui_element.py:104(change_layer)
     1077    0.002    0.000    0.011    0.000 ui_container.py:52(remove_element)
     3422    0.011    0.000    0.011    0.000 sprite.py:745(sprites)
       34    0.008    0.000    0.011    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     6117    0.008    0.000    0.010    0.000 drawable_shape.py:122(rebuild_images_and_text)
      246    0.003    0.000    0.009    0.000 text_block.py:265(redraw_from_chunks)
       68    0.000    0.000    0.009    0.000 __init__.py:1996(debug)
       12    0.000    0.000    0.009    0.001 game_handler.py:79(_process_end_turn)
   141680    0.009    0.000    0.009    0.000 {method 'reverse' of 'list' objects}
       68    0.000    0.000    0.009    0.000 __init__.py:1361(debug)
       12    0.000    0.000    0.009    0.001 chrono.py:47(next_turn)
     1255    0.008    0.000    0.009    0.000 sprite.py:822(change_layer)
     1247    0.008    0.000    0.009    0.000 sprite.py:646(add_internal)
     1710    0.004    0.000    0.008    0.000 skill_bar.py:45(update)
     1546    0.003    0.000    0.008    0.000 ui_font_dictionary.py:89(find_font)
    10567    0.008    0.000    0.008    0.000 ui_button.py:257(process_event)
     1710    0.003    0.000    0.007    0.000 message_log.py:36(update)
      108    0.000    0.000    0.007    0.000 __init__.py:1521(handle)
      108    0.000    0.000    0.007    0.000 __init__.py:1575(callHandlers)
     3583    0.006    0.000    0.006    0.000 {built-in method builtins.sorted}
     8717    0.006    0.000    0.006    0.000 query.py:243(<listcomp>)
      108    0.000    0.000    0.006    0.000 __init__.py:892(handle)
        2    0.000    0.000    0.006    0.003 entity.py:340(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
        8    0.000    0.000    0.006    0.001 manager.py:275(update_cameras_tiles)
     1710    0.003    0.000    0.006    0.000 entity_info.py:47(update)
        8    0.002    0.000    0.006    0.001 camera.py:167(update_camera_tiles)
      108    0.000    0.000    0.006    0.000 __init__.py:1123(emit)
     7500    0.003    0.000    0.006    0.000 libtcodpy.py:3300(map_is_in_fov)
      108    0.000    0.000    0.005    0.000 __init__.py:1022(emit)
        2    0.000    0.000    0.005    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.005    0.003 screen_message.py:16(__init__)
     1077    0.002    0.000    0.005    0.000 sprite.py:183(kill)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       38    0.000    0.000    0.005    0.000 __init__.py:1986(info)
     5266    0.005    0.000    0.005    0.000 query.py:50(__init__)
       38    0.000    0.000    0.005    0.000 __init__.py:1373(info)
       17    0.000    0.000    0.005    0.000 parser.py:104(feed)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
       17    0.001    0.000    0.005    0.000 parser.py:134(goahead)
      634    0.005    0.000    0.005    0.000 ui_manager.py:104(<listcomp>)
     3885    0.004    0.000    0.005    0.000 ui_element.py:186(hover_point)
     1711    0.005    0.000    0.005    0.000 ecs.py:265(process_pending_deletions)
      108    0.000    0.000    0.005    0.000 __init__.py:1481(makeRecord)
       82    0.002    0.000    0.005    0.000 styled_chunk.py:8(__init__)
     4243    0.004    0.000    0.005    0.000 world.py:349(_is_tile_in_bounds)
      108    0.002    0.000    0.004    0.000 __init__.py:293(__init__)
       26    0.000    0.000    0.004    0.000 game_handler.py:39(_process_change_game_state)
     3456    0.004    0.000    0.004    0.000 state.py:45(get_current)
     1711    0.004    0.000    0.004    0.000 {built-in method pygame.mouse.get_pos}
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
       12    0.000    0.000    0.004    0.000 chrono.py:24(rebuild_turn_queue)
     1077    0.002    0.000    0.004    0.000 sprite.py:728(remove_internal)
     1728    0.003    0.000    0.004    0.000 query.py:225(<listcomp>)
       25    0.000    0.000    0.003    0.000 state.py:71(set_new)
     6117    0.003    0.000    0.003    0.000 surface_cache.py:109(find_surface_in_cache)
       80    0.000    0.000    0.003    0.000 processors.py:59(process_intent)
     1237    0.003    0.000    0.003    0.000 drawable_shape.py:11(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
     1243    0.002    0.000    0.003    0.000 ui_element.py:68(create_valid_ids)
     5685    0.003    0.000    0.003    0.000 {method 'get' of 'dict' objects}
       63    0.001    0.000    0.003    0.000 processors.py:140(_process_player_turn_intents)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
      108    0.000    0.000    0.003    0.000 __init__.py:869(format)
     9806    0.003    0.000    0.003    0.000 ui_window.py:107(get_container)
     5267    0.003    0.000    0.003    0.000 {built-in method __new__ of type object at 0x00007FF84D989BA0}
       28    0.000    0.000    0.003    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      108    0.001    0.000    0.003    0.000 __init__.py:606(format)
       29    0.003    0.000    0.003    0.000 {built-in method nt.stat}
       82    0.001    0.000    0.003    0.000 parser.py:301(parse_starttag)
       90    0.001    0.000    0.002    0.000 entity.py:43(get_player)
     7500    0.002    0.000    0.002    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        2    0.000    0.000    0.002    0.001 interaction_handler.py:27(process_event)
        2    0.000    0.000    0.002    0.001 interaction_handler.py:85(_process_entity_collision)
    11971    0.002    0.000    0.002    0.000 sprite.py:168(update)
     1547    0.002    0.000    0.002    0.000 ui_font_dictionary.py:133(create_font_id)
      157    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
      162    0.000    0.000    0.002    0.000 html_parser.py:118(add_text)
     2422    0.002    0.000    0.002    0.000 {method 'remove' of 'list' objects}
        6    0.000    0.000    0.002    0.000 entity.py:483(take_turn)
      164    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      108    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
     8551    0.002    0.000    0.002    0.000 ui_window.py:116(check_hover)
      162    0.001    0.000    0.002    0.000 html_parser.py:123(add_indexed_style)
      110    0.000    0.000    0.002    0.000 ntpath.py:212(basename)
     1237    0.001    0.000    0.002    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       82    0.000    0.000    0.002    0.000 html_parser.py:213(handle_starttag)
     4948    0.001    0.000    0.001    0.000 {built-in method math.floor}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
      108    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
     1711    0.001    0.000    0.001    0.000 {built-in method builtins.any}
      110    0.001    0.000    0.001    0.000 ntpath.py:178(split)
      108    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
        2    0.000    0.000    0.001    0.001 interaction_handler.py:135(_apply_effects_to_tiles)
       17    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
     8486    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      108    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
    10844    0.001    0.000    0.001    0.000 {method 'contains' of 'pygame.Rect' objects}
       17    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
       82    0.000    0.000    0.001    0.000 html_parser.py:283(handle_data)
        5    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
  267/265    0.001    0.000    0.001    0.000 entity.py:93(get_entitys_component)
     1311    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
     3885    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
     5579    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     6117    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        5    0.000    0.000    0.001    0.000 combat_stats.py:270(sight_range)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     1237    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
       80    0.001    0.000    0.001    0.000 action.py:12(convert_to_intent)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
     4059    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
     2543    0.001    0.000    0.001    0.000 {built-in method builtins.min}
     2502    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     1271    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
      109    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      108    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
       45    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
      367    0.001    0.000    0.001    0.000 ui_button.py:170(while_hovering)
     2409    0.001    0.000    0.001    0.000 {built-in method builtins.max}
      108    0.001    0.000    0.001    0.000 {built-in method time.strftime}
       63    0.001    0.000    0.001    0.000 surface_cache.py:80(split_rect)
     1880    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
       99    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:228(update)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
       57    0.000    0.000    0.001    0.000 utility.py:188(value_to_member)
      220    0.000    0.000    0.001    0.000 ntpath.py:44(normcase)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
      261    0.001    0.000    0.001    0.000 {method 'size' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
     2503    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       11    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
      114    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
      108    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       16    0.000    0.000    0.000    0.000 world.py:262(tile_has_tag)
        2    0.000    0.000    0.000    0.000 skill.py:218(process_effect)
       65    0.000    0.000    0.000    0.000 entity.py:104(get_name)
     1247    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        2    0.000    0.000    0.000    0.000 entity_handler.py:166(_process_want_to_use_skill)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
       49    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
     2452    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       59    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        5    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
     1235    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
     1255    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      108    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       65    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
       10    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      108    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      116    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        2    0.000    0.000    0.000    0.000 debug.py:28(log_component_not_found)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        4    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
      340    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       17    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      108    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        2    0.000    0.000    0.000    0.000 skill.py:76(can_afford_cost)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
     1247    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       10    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        2    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
        2    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
      108    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
      168    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
     1247    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
       82    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
      216    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      352    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
     1125    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
     1220    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
     1231    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        6    0.000    0.000    0.000    0.000 ai.py:68(act)
       12    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        9    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        7    0.000    0.000    0.000    0.000 world.py:361(_is_tile_blocking_movement)
      108    0.000    0.000    0.000    0.000 __init__.py:432(format)
       63    0.000    0.000    0.000    0.000 processors.py:73(_get_pressed_direction)
       59    0.000    0.000    0.000    0.000 event_core.py:41(publish)
       34    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
       80    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        5    0.000    0.000    0.000    0.000 world.py:440(recompute_fov)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       34    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
       34    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        7    0.000    0.000    0.000    0.000 world.py:397(_tile_has_other_entity)
        9    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        1    0.000    0.000    0.000    0.000 chrono.py:79(next_round)
     1601    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        9    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        9    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      162    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        9    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
      488    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       12    0.000    0.000    0.000    0.000 entity_handler.py:225(_process_end_turn)
       88    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
      108    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
     1077    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       80    0.000    0.000    0.000    0.000 processors.py:120(_process_stateless_intents)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      216    0.000    0.000    0.000    0.000 __init__.py:856(release)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      218    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
      179    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
      279    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
      108    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       30    0.000    0.000    0.000    0.000 utility.py:107(lerp)
      108    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
      216    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       12    0.000    0.000    0.000    0.000 entity.py:378(spend_time)
       63    0.000    0.000    0.000    0.000 processors.py:100(_get_pressed_skills_number)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
      108    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      339    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       21    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       59    0.000    0.000    0.000    0.000 event_core.py:15(notify)
      324    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      108    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       17    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        7    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       15    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
      108    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        3    0.000    0.000    0.000    0.000 entity.py:174(create)
      200    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      556    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      265    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
      108    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      460    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        3    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
      219    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
      477    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       26    0.000    0.000    0.000    0.000 event.py:88(__init__)
      218    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        5    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        2    0.000    0.000    0.000    0.000 skill.py:246(_process_trigger_skill_effect)
      110    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       34    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
      108    0.000    0.000    0.000    0.000 threading.py:1052(name)
       17    0.000    0.000    0.000    0.000 parser.py:96(reset)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
       59    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
       73    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
       82    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      166    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        5    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       32    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       12    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        7    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       82    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        1    0.000    0.000    0.000    0.000 main.py:238(initialise_event_handlers)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
       72    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        2    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       99    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        8    0.000    0.000    0.000    0.000 event.py:166(__init__)
      236    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 event.py:70(__init__)
      109    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        5    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
       34    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       43    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        7    0.000    0.000    0.000    0.000 event.py:53(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        9    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
      108    0.000    0.000    0.000    0.000 {built-in method time.time}
        5    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
      110    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       13    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      108    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
      216    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       14    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       68    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       88    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       99    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       17    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        2    0.000    0.000    0.000    0.000 world.py:77(get_direction)
      244    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
      219    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       15    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        7    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       12    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       87    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        7    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        2    0.000    0.000    0.000    0.000 world.py:301(tile_has_tags)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       90    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
      172    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       59    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
       12    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        4    0.000    0.000    0.000    0.000 entity.py:333(add_component)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       12    0.000    0.000    0.000    0.000 {built-in method math.sin}
       82    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       34    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       47    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
       35    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        2    0.000    0.000    0.000    0.000 world.py:107(get_tiles)
       47    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       47    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        7    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       24    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        3    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
        5    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       83    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       17    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       43    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        9    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        4    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        1    0.000    0.000    0.000    0.000 manager.py:264(move_camera)
       17    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        7    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       17    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       36    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        2    0.000    0.000    0.000    0.000 event.py:18(__init__)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
        2    0.000    0.000    0.000    0.000 event.py:118(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       12    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        8    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
       26    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
       13    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        9    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        5    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 camera.py:223(move_camera)
       42    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
       12    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
       45    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        7    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        5    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        5    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       26    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        7    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
       16    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 main.py:188(disable_profiling)
       13    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        1    0.000    0.000    0.000    0.000 event.py:80(__init__)
       12    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        9    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       12    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       12    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        5    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       36    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        3    0.000    0.000    0.000    0.000 component.py:82(__init__)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        2    0.000    0.000    0.000    0.000 component.py:31(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        4    0.000    0.000    0.000    0.000 world.py:312(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:28(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:56(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 component.py:118(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:95(increment_round)
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


