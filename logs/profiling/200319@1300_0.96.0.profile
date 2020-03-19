Thu Mar 19 13:00:13 2020    logs/profiling/profile.dump

         4635524 function calls (4502976 primitive calls) in 48.701 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.410    0.410   48.659   48.659 main.py:78(game_loop)
     2186   24.579    0.011   24.579    0.011 {method 'tick' of 'Clock' objects}
     1093    0.005    0.000   12.474    0.011 state.py:63(update_clock)
     1093    0.007    0.000   12.118    0.011 state.py:38(get_delta_time)
     1093    0.002    0.000    9.168    0.008 event_core.py:21(update)
     1093    0.018    0.000    5.429    0.005 manager.py:73(draw)
     1093    0.005    0.000    5.301    0.005 manager.py:54(update)
     1093    0.343    0.000    5.296    0.005 ui_manager.py:122(update)
       37    0.000    0.000    4.250    0.115 entity_handler.py:29(process_event)
        1    4.211    4.211    4.219    4.219 entity_handler.py:57(_process_move)
       33    0.000    0.000    4.030    0.122 game_handler.py:26(process_event)
       10    0.000    0.000    4.023    0.402 game_handler.py:81(process_end_turn)
        1    4.018    4.018    4.019    4.019 chrono.py:44(next_turn)
   356086    3.821    0.000    3.821    0.000 {method 'blit' of 'pygame.Surface' objects}
        5    0.000    0.000    3.349    0.670 entity.py:475(take_turn)
        1    3.347    3.347    3.347    3.347 ai.py:71(act)
     1093    0.182    0.000    3.133    0.003 sprite.py:453(update)
     1097    1.130    0.001    2.307    0.002 camera.py:79(update_game_map)
     1092    0.007    0.000    2.300    0.002 camera.py:72(update)
     1093    0.009    0.000    2.091    0.002 ui_manager.py:173(draw_ui)
     1093    0.345    0.000    2.082    0.002 sprite.py:753(draw)
     1097    1.530    0.001    1.530    0.001 {built-in method pygame.transform.scale}
   175180    0.789    0.000    1.413    0.000 ui_element.py:121(check_hover)
       42    0.000    0.000    0.884    0.021 ui_handler.py:30(process_event)
        5    0.000    0.000    0.846    0.169 ui_handler.py:207(update_camera)
        5    0.000    0.000    0.822    0.164 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.822    0.164 camera.py:106(update_grid)
      761    0.010    0.000    0.807    0.001 ui_button.py:30(__init__)
      761    0.042    0.000    0.758    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        4    0.000    0.000    0.683    0.171 ui_handler.py:48(process_entity_event)
    22222    0.056    0.000    0.611    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
   171786    0.344    0.000    0.571    0.000 ui_button.py:197(update)
154734/22222    0.522    0.000    0.551    0.000 ui_appearance_theme.py:322(get_next_id_node)
   171786    0.223    0.000    0.430    0.000 ui_button.py:138(hover_point)
     1093    0.427    0.000    0.427    0.000 {built-in method pygame.display.flip}
    10719    0.347    0.000    0.366    0.000 sprite.py:913(get_sprites_from_layer)
    11486    0.030    0.000    0.345    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
     1093    0.324    0.000    0.324    0.000 {built-in method pygame.event.get}
   164556    0.250    0.000    0.250    0.000 camera.py:234(world_to_screen_position)
   171786    0.182    0.000    0.207    0.000 rect_drawable_shape.py:84(collide_point)
     6920    0.014    0.000    0.202    0.000 ui_appearance_theme.py:428(get_misc_data)
       33    0.000    0.000    0.178    0.005 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.172    0.172 ui_handler.py:111(init_game_ui)
   171786    0.092    0.000    0.159    0.000 drawable_shape.py:36(update)
     1630    0.159    0.000    0.159    0.000 {method 'fill' of 'pygame.Surface' objects}
   355821    0.129    0.000    0.155    0.000 sprite.py:208(alive)
      761    0.005    0.000    0.094    0.000 ui_button.py:97(set_any_images_from_theme)
     3044    0.006    0.000    0.089    0.000 ui_appearance_theme.py:366(get_image)
   171786    0.075    0.000    0.075    0.000 ui_button.py:154(can_hover)
     3807    0.024    0.000    0.072    0.000 rect_drawable_shape.py:118(redraw_state)
       89    0.000    0.000    0.061    0.001 manager.py:60(process_ui_events)
       89    0.023    0.000    0.061    0.001 ui_manager.py:86(process_events)
   670895    0.060    0.000    0.060    0.000 {method 'append' of 'list' objects}
      761    0.006    0.000    0.047    0.000 ui_button.py:537(rebuild_shape)
        1    0.000    0.000    0.043    0.043 main.py:183(initialise_game)
      772    0.003    0.000    0.042    0.000 rect_drawable_shape.py:22(__init__)
     1460    0.015    0.000    0.041    0.000 ui_text_box.py:205(update)
      368    0.002    0.000    0.041    0.000 screen_message.py:34(update)
        2    0.000    0.000    0.039    0.019 entity.py:225(create_actor)
      772    0.012    0.000    0.037    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      782    0.008    0.000    0.037    0.000 ui_element.py:23(__init__)
     9006    0.011    0.000    0.037    0.000 _internal.py:24(wrapper)
      246    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
   184035    0.035    0.000    0.035    0.000 ui_manager.py:167(get_mouse_position)
        2    0.008    0.004    0.032    0.016 world.py:26(create_fov_map)
        4    0.008    0.002    0.031    0.008 world.py:445(update_tile_visibility)
      761    0.004    0.000    0.030    0.000 ui_appearance_theme.py:405(get_font)
     6553    0.021    0.000    0.029    0.000 ui_container.py:124(check_hover)
   181733    0.028    0.000    0.028    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
        9    0.000    0.000    0.026    0.003 ui_text_box.py:50(__init__)
   355821    0.026    0.000    0.026    0.000 {built-in method _operator.truth}
        9    0.000    0.000    0.025    0.003 ui_text_box.py:492(rebuild_from_changed_theme_data)
   174569    0.025    0.000    0.025    0.000 {method 'union' of 'pygame.Rect' objects}
      246    0.003    0.000    0.024    0.000 ui_text_box.py:327(redraw_from_text_block)
   428349    0.024    0.000    0.024    0.000 {built-in method builtins.len}
        9    0.001    0.000    0.024    0.003 ui_text_box.py:110(rebuild)
      182    0.001    0.000    0.023    0.000 __init__.py:1496(_log)
      772    0.004    0.000    0.023    0.000 drawable_shape.py:45(redraw_all_states)
      151    0.000    0.000    0.022    0.000 __init__.py:1996(debug)
      151    0.001    0.000    0.021    0.000 __init__.py:1361(debug)
   186769    0.021    0.000    0.021    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        5    0.004    0.001    0.020    0.004 ui_container.py:116(clear)
     3807    0.020    0.000    0.020    0.000 surface_cache.py:119(build_cache_id)
     3847    0.020    0.000    0.020    0.000 {method 'copy' of 'pygame.Surface' objects}
        6    0.000    0.000    0.020    0.003 message_log.py:49(add_message)
     9007    0.018    0.000    0.019    0.000 {built-in method _warnings.warn}
     1093    0.005    0.000    0.018    0.000 processors.py:16(process_all)
        5    0.000    0.000    0.018    0.004 ui_handler.py:155(process_ui_event)
        5    0.000    0.000    0.018    0.004 ui_handler.py:238(process_message)
        5    0.000    0.000    0.018    0.004 manager.py:444(add_to_message_log)
      782    0.002    0.000    0.017    0.000 ui_container.py:42(add_element)
      603    0.001    0.000    0.016    0.000 ui_button.py:130(kill)
        5    0.000    0.000    0.016    0.003 manager.py:286(update_camera_game_map)
     1394    0.015    0.000    0.015    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     3766    0.009    0.000    0.015    0.000 world.py:55(get_tile)
      612    0.002    0.000    0.015    0.000 ui_element.py:114(kill)
     1093    0.013    0.000    0.014    0.000 processors.py:23(_process_aesthetic_update)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
     1182    0.008    0.000    0.012    0.000 sprite.py:814(layers)
       11    0.000    0.000    0.012    0.001 ui_text_box.py:310(parse_html_into_style_data)
      182    0.001    0.000    0.012    0.000 __init__.py:1521(handle)
     5461    0.010    0.000    0.012    0.000 ui_window.py:97(update)
      182    0.001    0.000    0.012    0.000 __init__.py:1575(callHandlers)
      782    0.001    0.000    0.011    0.000 sprite.py:121(__init__)
      182    0.001    0.000    0.011    0.000 __init__.py:892(handle)
      182    0.000    0.000    0.010    0.000 __init__.py:1123(emit)
      782    0.003    0.000    0.010    0.000 sprite.py:126(add)
      182    0.001    0.000    0.010    0.000 __init__.py:1022(emit)
      246    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
      612    0.002    0.000    0.009    0.000 ui_container.py:52(remove_element)
     1093    0.003    0.000    0.009    0.000 ui_appearance_theme.py:158(update_shape_cache)
       11    0.000    0.000    0.009    0.001 text_block.py:16(__init__)
       11    0.001    0.000    0.009    0.001 text_block.py:40(redraw)
        2    0.000    0.000    0.009    0.004 ui_vertical_scroll_bar.py:22(__init__)
    11423    0.009    0.000    0.009    0.000 ui_button.py:257(process_event)
     1093    0.006    0.000    0.008    0.000 ui_manager.py:158(update_mouse_position)
     2186    0.008    0.000    0.008    0.000 sprite.py:745(sprites)
        5    0.000    0.000    0.008    0.002 manager.py:275(update_cameras_tiles)
        5    0.003    0.001    0.008    0.002 camera.py:168(update_camera_tiles)
      182    0.001    0.000    0.008    0.000 __init__.py:1481(makeRecord)
      782    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
      182    0.002    0.000    0.007    0.000 __init__.py:293(__init__)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
     1092    0.003    0.000    0.006    0.000 skill_bar.py:45(update)
        2    0.000    0.000    0.006    0.003 entity.py:332(build_characteristic_sprites)
      895    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
      782    0.006    0.000    0.006    0.000 sprite.py:646(add_internal)
     3807    0.005    0.000    0.006    0.000 drawable_shape.py:122(rebuild_images_and_text)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
     1093    0.002    0.000    0.006    0.000 surface_cache.py:24(update)
      790    0.005    0.000    0.006    0.000 sprite.py:822(change_layer)
    88292    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
      706    0.005    0.000    0.005    0.000 ui_manager.py:104(<listcomp>)
     2367    0.005    0.000    0.005    0.000 {built-in method builtins.sorted}
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
     3770    0.005    0.000    0.005    0.000 world.py:347(_is_tile_in_bounds)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
      182    0.000    0.000    0.005    0.000 __init__.py:869(format)
     6000    0.003    0.000    0.005    0.000 libtcodpy.py:3300(map_is_in_fov)
      842    0.004    0.000    0.005    0.000 ui_vertical_scroll_bar.py:228(update)
      182    0.001    0.000    0.004    0.000 __init__.py:606(format)
     1092    0.002    0.000    0.004    0.000 message_log.py:36(update)
      612    0.001    0.000    0.004    0.000 sprite.py:183(kill)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     3394    0.003    0.000    0.004    0.000 ui_element.py:186(hover_point)
       31    0.000    0.000    0.003    0.000 __init__.py:1986(info)
       31    0.000    0.000    0.003    0.000 __init__.py:1373(info)
     2215    0.003    0.000    0.003    0.000 state.py:45(get_current)
       22    0.000    0.000    0.003    0.000 game_handler.py:42(process_change_game_state)
     1092    0.002    0.000    0.003    0.000 entity_info.py:45(update)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
      182    0.001    0.000    0.003    0.000 __init__.py:1011(flush)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
       21    0.000    0.000    0.003    0.000 state.py:71(set_new)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
      612    0.001    0.000    0.003    0.000 sprite.py:728(remove_internal)
     1093    0.003    0.000    0.003    0.000 {built-in method pygame.mouse.get_pos}
       20    0.002    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
      185    0.000    0.000    0.003    0.000 ntpath.py:212(basename)
       34    0.001    0.000    0.003    0.000 styled_chunk.py:8(__init__)
       11    0.000    0.000    0.002    0.000 parser.py:104(feed)
       11    0.000    0.000    0.002    0.000 parser.py:134(goahead)
      182    0.001    0.000    0.002    0.000 __init__.py:1451(findCaller)
      185    0.001    0.000    0.002    0.000 ntpath.py:178(split)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      182    0.002    0.000    0.002    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
     3807    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
      182    0.001    0.000    0.002    0.000 __init__.py:539(formatTime)
     6254    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
     6000    0.002    0.000    0.002    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
      772    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
      778    0.001    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
       68    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        3    0.000    0.000    0.002    0.001 pydevd_modify_bytecode.py:213(insert_code)
        3    0.000    0.000    0.002    0.001 pydevd_modify_bytecode.py:233(_insert_code)
       89    0.000    0.000    0.002    0.000 processors.py:57(process_intent)
       73    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.002    0.000 god_handler.py:26(process_event)
       18    0.000    0.000    0.002    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       19    0.002    0.000    0.002    0.000 {built-in method nt.stat}
     7645    0.001    0.000    0.001    0.000 sprite.py:168(update)
        3    0.001    0.000    0.001    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     1446    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
     7542    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
     1093    0.001    0.000    0.001    0.000 {built-in method builtins.any}
      183    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      896    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
      182    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
      772    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       71    0.001    0.000    0.001    0.000 processors.py:138(_process_player_turn_intents)
       34    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
      182    0.001    0.000    0.001    0.000 {built-in method time.strftime}
     5461    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
     3088    0.001    0.000    0.001    0.000 {built-in method math.floor}
       89    0.001    0.000    0.001    0.000 action.py:12(convert_to_intent)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.001    0.001    0.001    0.001 camera.py:24(__init__)
      370    0.001    0.000    0.001    0.000 ntpath.py:44(normcase)
       66    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
       11    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
     3394    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       11    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
      182    0.000    0.000    0.001    0.000 genericpath.py:117(_splitext)
      191    0.001    0.000    0.001    0.000 ntpath.py:122(splitdrive)
      861    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
     5229    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
       66    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
       34    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
     2960    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      772    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
      414    0.001    0.000    0.001    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
     3807    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
      182    0.000    0.000    0.001    0.000 __init__.py:590(formatMessage)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     1595    0.001    0.000    0.001    0.000 {built-in method builtins.min}
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
     1280    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
     1572    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
     1609    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      111    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       34    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
      811    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
      182    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
       46    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
      842    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
      345    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
      182    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
      182    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        1    0.000    0.000    0.000    0.000 chrono.py:23(rebuild_turn_queue)
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
       91    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
      364    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       46    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      182    0.000    0.000    0.000    0.000 __init__.py:432(format)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
     1573    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
       46    0.000    0.000    0.000    0.000 entity.py:96(get_name)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        3    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       46    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
      782    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      776    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
       90    0.000    0.000    0.000    0.000 entity.py:37(get_player)
        8    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      364    0.000    0.000    0.000    0.000 __init__.py:747(filter)
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
      364    0.000    0.000    0.000    0.000 __init__.py:856(release)
      381    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
     1528    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       46    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
      263    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
      182    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       32    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
      790    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       71    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      139    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
     2520    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        7    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      182    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
       11    0.000    0.000    0.000    0.000 chrono.py:152(_get_pretty_queue)
      182    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
       89    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       89    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
       36    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
       20    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        7    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
      182    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        3    0.000    0.000    0.000    0.000 entity.py:166(create)
      658    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      782    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      185    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       11    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
       42    0.000    0.000    0.000    0.000 event_core.py:38(publish)
      546    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        6    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
      527    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       34    0.000    0.000    0.000    0.000 entity.py:325(add_component)
      148    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
      782    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        4    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
      934    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       56    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       10    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
      570    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
      769    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
      182    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        8    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
        3    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      182    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      532    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      366    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        6    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        4    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      758    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      185    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       34    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       34    0.000    0.000    0.000    0.000 esper.py:196(add_component)
      230    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        3    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:52(_pydev_stop_at_break)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      500    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       10    0.000    0.000    0.000    0.000 entity.py:370(spend_time)
       72    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       71    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       24    0.000    0.000    0.000    0.000 utility.py:107(lerp)
       20    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      182    0.000    0.000    0.000    0.000 threading.py:1052(name)
      612    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       42    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       99    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       22    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
       22    0.000    0.000    0.000    0.000 event.py:106(__init__)
      188    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       12    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       85    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        9    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       10    0.000    0.000    0.000    0.000 event.py:88(__init__)
       84    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       11    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
      182    0.000    0.000    0.000    0.000 {built-in method time.time}
       77    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       66    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
      185    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
       17    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
      367    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
      182    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        4    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       20    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        4    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 main.py:210(initialise_event_handlers)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
      366    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
      668    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      337    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       42    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        4    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        6    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       11    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       91    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
       24    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
       11    0.000    0.000    0.000    0.000 chrono.py:160(_get_next_entity_in_queue)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        8    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        4    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
        5    0.000    0.000    0.000    0.000 event.py:184(__init__)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
       42    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        3    0.000    0.000    0.000    0.000 _collections_abc.py:657(get)
       34    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        4    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       34    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        4    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        4    0.000    0.000    0.000    0.000 event.py:63(__init__)
       20    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       70    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
      119    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        3    0.000    0.000    0.000    0.000 os.py:673(__getitem__)
       34    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       20    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       36    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
       60    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       40    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        2    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        9    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       29    0.000    0.000    0.000    0.000 chrono.py:110(get_turn_holder)
       46    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       11    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
      100    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        9    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       41    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       36    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        9    0.000    0.000    0.000    0.000 {built-in method math.sin}
       12    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        5    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
       42    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       12    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        6    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       16    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        6    0.000    0.000    0.000    0.000 _weakrefset.py:38(_remove)
       32    0.000    0.000    0.000    0.000 chrono.py:117(get_turn_queue)
       20    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
       76    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       34    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       10    0.000    0.000    0.000    0.000 chrono.py:101(add_time)
        3    0.000    0.000    0.000    0.000 os.py:743(encodekey)
       20    0.000    0.000    0.000    0.000 chrono.py:124(get_time_in_round)
       11    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       35    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
       11    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
       68    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        3    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:21(update_globals_dict)
        2    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
       10    0.000    0.000    0.000    0.000 chrono.py:138(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 main.py:160(disable_profiling)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
       12    0.000    0.000    0.000    0.000 chrono.py:131(get_time)
       25    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
       12    0.000    0.000    0.000    0.000 chrono.py:166(set_turn_holder)
        3    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
       10    0.000    0.000    0.000    0.000 chrono.py:187(set_time_of_last_turn)
       30    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       40    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 pydev_log.py:16(debug)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        4    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
       10    0.000    0.000    0.000    0.000 chrono.py:173(set_time_in_round)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        9    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        3    0.000    0.000    0.000    0.000 os.py:737(check_str)
        3    0.000    0.000    0.000    0.000 component.py:88(__init__)
        2    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        2    0.000    0.000    0.000    0.000 component.py:190(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        9    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        3    0.000    0.000    0.000    0.000 component.py:70(__init__)
        9    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        6    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 pydevd_constants.py:479(get_global_debugger)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        3    0.000    0.000    0.000    0.000 component.py:139(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        2    0.000    0.000    0.000    0.000 component.py:37(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF955F79BA0}
        2    0.000    0.000    0.000    0.000 component.py:79(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        3    0.000    0.000    0.000    0.000 {_pydevd_frame_eval.pydevd_frame_evaluator_win32_37_64.get_thread_info_py}
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        4    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 ai.py:68(__init__)
        2    0.000    0.000    0.000    0.000 component.py:62(__init__)
        1    0.000    0.000    0.000    0.000 component.py:182(__init__)
        2    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        5    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:98(__init__)
        2    0.000    0.000    0.000    0.000 component.py:116(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:180(set_turn_queue)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 component.py:124(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 component.py:107(__init__)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


