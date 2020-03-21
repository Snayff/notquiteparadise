Sat Mar 21 14:52:09 2020    logs/profiling/profile.dump

         918074 function calls (865368 primitive calls) in 5.592 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.056    0.056    5.550    5.550 main.py:85(game_loop)
      312    3.383    0.011    3.383    0.011 {method 'tick' of 'Clock' objects}
      156    0.001    0.000    1.720    0.011 state.py:38(get_delta_time)
      156    0.001    0.000    1.665    0.011 state.py:63(update_clock)
      156    0.001    0.000    0.832    0.005 manager.py:54(update)
      156    0.051    0.000    0.831    0.005 ui_manager.py:122(update)
      156    0.002    0.000    0.802    0.005 manager.py:73(draw)
    51028    0.578    0.000    0.578    0.000 {method 'blit' of 'pygame.Surface' objects}
      156    0.025    0.000    0.502    0.003 sprite.py:453(update)
      156    0.000    0.000    0.355    0.002 event_core.py:24(update)
      157    0.169    0.001    0.347    0.002 camera.py:79(update_game_map)
      155    0.001    0.000    0.344    0.002 camera.py:72(update)
       18    0.000    0.000    0.341    0.019 ui_handler.py:30(process_event)
        2    0.000    0.000    0.322    0.161 ui_handler.py:207(update_camera)
        2    0.000    0.000    0.317    0.158 manager.py:295(update_camera_grid)
        2    0.002    0.001    0.317    0.158 camera.py:105(update_grid)
      156    0.001    0.000    0.315    0.002 ui_manager.py:173(draw_ui)
      305    0.004    0.000    0.315    0.001 ui_button.py:30(__init__)
      156    0.048    0.000    0.313    0.002 sprite.py:753(draw)
      305    0.017    0.000    0.296    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
     8935    0.022    0.000    0.237    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
      160    0.235    0.001    0.235    0.001 {built-in method pygame.transform.scale}
61605/8935    0.202    0.000    0.213    0.000 ui_appearance_theme.py:322(get_next_id_node)
    24645    0.120    0.000    0.210    0.000 ui_element.py:121(check_hover)
       15    0.000    0.000    0.175    0.012 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.169    0.169 ui_handler.py:111(init_game_ui)
        1    0.000    0.000    0.161    0.161 ui_handler.py:48(process_entity_event)
     4617    0.012    0.000    0.135    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    24025    0.050    0.000    0.103    0.000 ui_button.py:197(update)
      156    0.103    0.001    0.103    0.001 {built-in method pygame.event.get}
     2787    0.005    0.000    0.078    0.000 ui_appearance_theme.py:428(get_misc_data)
     1603    0.058    0.000    0.062    0.000 sprite.py:913(get_sprites_from_layer)
    24025    0.032    0.000    0.061    0.000 ui_button.py:138(hover_point)
      156    0.056    0.000    0.056    0.000 {built-in method pygame.display.flip}
    24025    0.016    0.000    0.044    0.000 drawable_shape.py:36(update)
        1    0.000    0.000    0.042    0.042 main.py:193(initialise_game)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      305    0.002    0.000    0.036    0.000 ui_button.py:97(set_any_images_from_theme)
    23553    0.036    0.000    0.036    0.000 camera.py:233(world_to_screen_position)
     1220    0.002    0.000    0.035    0.000 ui_appearance_theme.py:366(get_image)
     1531    0.011    0.000    0.034    0.000 rect_drawable_shape.py:118(redraw_state)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
    24025    0.026    0.000    0.029    0.000 rect_drawable_shape.py:84(collide_point)
      446    0.026    0.000    0.026    0.000 {method 'fill' of 'pygame.Surface' objects}
      310    0.001    0.000    0.025    0.000 screen_message.py:34(update)
    50066    0.018    0.000    0.022    0.000 sprite.py:208(alive)
      134    0.001    0.000    0.021    0.000 ui_text_box.py:347(redraw_from_chunks)
      305    0.003    0.000    0.019    0.000 ui_button.py:537(rebuild_shape)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
      311    0.001    0.000    0.018    0.000 rect_drawable_shape.py:22(__init__)
      465    0.003    0.000    0.017    0.000 ui_text_box.py:205(update)
      311    0.005    0.000    0.016    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      321    0.003    0.000    0.015    0.000 ui_element.py:23(__init__)
      134    0.002    0.000    0.014    0.000 ui_text_box.py:327(redraw_from_text_block)
   164167    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
      305    0.001    0.000    0.012    0.000 ui_appearance_theme.py:405(get_font)
    24025    0.011    0.000    0.011    0.000 ui_button.py:154(can_hover)
     3304    0.007    0.000    0.011    0.000 world.py:55(get_tile)
        6    0.000    0.000    0.011    0.002 ui_text_box.py:50(__init__)
     1549    0.011    0.000    0.011    0.000 {method 'copy' of 'pygame.Surface' objects}
      156    0.001    0.000    0.011    0.000 processors.py:16(process_all)
        6    0.000    0.000    0.010    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
      156    0.005    0.000    0.010    0.000 processors.py:23(_process_aesthetic_update)
      311    0.001    0.000    0.009    0.000 drawable_shape.py:45(redraw_all_states)
     4504    0.009    0.000    0.009    0.000 {built-in method _warnings.warn}
        6    0.000    0.000    0.009    0.002 ui_text_box.py:110(rebuild)
     1531    0.009    0.000    0.009    0.000 surface_cache.py:119(build_cache_id)
       16    0.000    0.000    0.008    0.001 entity_handler.py:27(process_event)
        1    0.000    0.000    0.008    0.008 entity_handler.py:49(_process_move)
        1    0.002    0.002    0.008    0.008 world.py:446(update_tile_visibility)
       68    0.000    0.000    0.008    0.000 ui_text_box.py:462(set_active_effect)
       58    0.000    0.000    0.007    0.000 __init__.py:1496(_log)
        6    0.000    0.000    0.007    0.001 ui_text_box.py:310(parse_html_into_style_data)
      321    0.001    0.000    0.007    0.000 ui_container.py:42(add_element)
   126102    0.007    0.000    0.007    0.000 {built-in method builtins.len}
       45    0.000    0.000    0.006    0.000 __init__.py:1996(debug)
       45    0.000    0.000    0.006    0.000 __init__.py:1361(debug)
        6    0.000    0.000    0.006    0.001 text_block.py:16(__init__)
        6    0.000    0.000    0.006    0.001 text_block.py:40(redraw)
        2    0.000    0.000    0.006    0.003 entity.py:342(build_characteristic_sprites)
       16    0.000    0.000    0.006    0.000 manager.py:60(process_ui_events)
       16    0.002    0.000    0.006    0.000 ui_manager.py:86(process_events)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      134    0.002    0.000    0.006    0.000 text_block.py:265(redraw_from_chunks)
     1136    0.004    0.000    0.005    0.000 query.py:212(__iter__)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
    26041    0.005    0.000    0.005    0.000 ui_manager.py:167(get_mouse_position)
       15    0.000    0.000    0.005    0.000 game_handler.py:26(process_event)
        3    0.000    0.000    0.004    0.001 message_log.py:49(add_message)
      321    0.001    0.000    0.004    0.000 sprite.py:121(__init__)
      474    0.004    0.000    0.004    0.000 ui_container.py:62(recalculate_container_layer_thickness)
    25576    0.004    0.000    0.004    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      335    0.001    0.000    0.004    0.000 ui_font_dictionary.py:89(find_font)
    50066    0.004    0.000    0.004    0.000 {built-in method _operator.truth}
       58    0.000    0.000    0.004    0.000 __init__.py:1521(handle)
      931    0.003    0.000    0.004    0.000 ui_container.py:124(check_hover)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
      321    0.001    0.000    0.004    0.000 sprite.py:126(add)
        2    0.000    0.000    0.004    0.002 manager.py:286(update_camera_game_map)
       58    0.000    0.000    0.004    0.000 __init__.py:1575(callHandlers)
     3305    0.003    0.000    0.004    0.000 world.py:348(_is_tile_in_bounds)
        2    0.001    0.000    0.004    0.002 ui_container.py:116(clear)
       58    0.000    0.000    0.004    0.000 __init__.py:892(handle)
    24493    0.003    0.000    0.003    0.000 {method 'union' of 'pygame.Rect' objects}
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
       58    0.000    0.000    0.003    0.000 __init__.py:1123(emit)
    26244    0.003    0.000    0.003    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       58    0.000    0.000    0.003    0.000 __init__.py:1022(emit)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      321    0.001    0.000    0.003    0.000 ui_element.py:104(change_layer)
        4    0.000    0.000    0.003    0.001 game_handler.py:78(process_end_turn)
      150    0.000    0.000    0.003    0.000 ui_button.py:130(kill)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        4    0.000    0.000    0.003    0.001 chrono.py:47(next_turn)
      153    0.000    0.000    0.003    0.000 ui_element.py:114(kill)
     1531    0.002    0.000    0.003    0.000 drawable_shape.py:122(rebuild_images_and_text)
        2    0.000    0.000    0.003    0.001 ui_handler.py:155(process_ui_event)
        2    0.000    0.000    0.003    0.001 ui_handler.py:238(process_message)
        2    0.000    0.000    0.003    0.001 manager.py:444(add_to_message_log)
       58    0.000    0.000    0.002    0.000 __init__.py:1481(makeRecord)
      329    0.002    0.000    0.002    0.000 sprite.py:822(change_layer)
    35270    0.002    0.000    0.002    0.000 {method 'reverse' of 'list' objects}
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      321    0.002    0.000    0.002    0.000 sprite.py:646(add_internal)
       58    0.001    0.000    0.002    0.000 __init__.py:293(__init__)
      156    0.000    0.000    0.002    0.000 ui_appearance_theme.py:158(update_shape_cache)
       10    0.000    0.000    0.002    0.000 game_handler.py:39(process_change_game_state)
      487    0.002    0.000    0.002    0.000 typing.py:806(__new__)
      487    0.001    0.000    0.002    0.000 query.py:170(__init__)
       13    0.000    0.000    0.002    0.000 __init__.py:1986(info)
       13    0.000    0.000    0.002    0.000 __init__.py:1373(info)
      776    0.001    0.000    0.002    0.000 ui_window.py:97(update)
      172    0.001    0.000    0.002    0.000 sprite.py:814(layers)
      153    0.000    0.000    0.002    0.000 ui_container.py:52(remove_element)
        8    0.000    0.000    0.002    0.000 styled_chunk.py:8(__init__)
      156    0.000    0.000    0.002    0.000 surface_cache.py:24(update)
       58    0.000    0.000    0.001    0.000 __init__.py:869(format)
        9    0.000    0.000    0.001    0.000 state.py:71(set_new)
        2    0.000    0.000    0.001    0.001 manager.py:275(update_cameras_tiles)
        2    0.000    0.000    0.001    0.001 camera.py:167(update_camera_tiles)
       33    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
       58    0.000    0.000    0.001    0.000 __init__.py:606(format)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
        4    0.000    0.000    0.001    0.000 chrono.py:24(rebuild_turn_queue)
      156    0.001    0.000    0.001    0.000 ui_manager.py:158(update_mouse_position)
      312    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
       16    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        9    0.001    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
       58    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
      620    0.001    0.000    0.001    0.000 ui_element.py:186(hover_point)
     6612    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
       60    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
      155    0.000    0.000    0.001    0.000 skill_bar.py:45(update)
     1531    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
      311    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
        6    0.000    0.000    0.001    0.000 parser.py:104(feed)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        6    0.000    0.000    0.001    0.000 parser.py:134(goahead)
      620    0.001    0.000    0.001    0.000 ui_button.py:257(process_event)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
      153    0.000    0.000    0.001    0.000 sprite.py:183(kill)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       58    0.000    0.000    0.001    0.000 __init__.py:1451(findCaller)
       60    0.000    0.000    0.001    0.000 ntpath.py:178(split)
      317    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
       58    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
      806    0.001    0.000    0.001    0.000 query.py:243(<listcomp>)
       58    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
      344    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
      311    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
      487    0.001    0.000    0.001    0.000 query.py:50(__init__)
      155    0.000    0.000    0.001    0.000 message_log.py:36(update)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
        2    0.000    0.000    0.001    0.000 entity.py:485(take_turn)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
      156    0.001    0.000    0.001    0.000 ecs.py:265(process_pending_deletions)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
       52    0.000    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      153    0.000    0.000    0.001    0.000 sprite.py:728(remove_internal)
     3956    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       59    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      155    0.000    0.000    0.000    0.000 entity_info.py:45(update)
      336    0.000    0.000    0.000    0.000 ui_font_dictionary.py:133(create_font_id)
        6    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
      326    0.000    0.000    0.000    0.000 state.py:45(get_current)
        6    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
      156    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       25    0.000    0.000    0.000    0.000 entity.py:131(get_primary_stat)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
       58    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
     1244    0.000    0.000    0.000    0.000 {built-in method math.floor}
       16    0.000    0.000    0.000    0.000 processors.py:57(process_intent)
       58    0.000    0.000    0.000    0.000 {built-in method time.strftime}
      159    0.000    0.000    0.000    0.000 query.py:225(<listcomp>)
       10    0.000    0.000    0.000    0.000 entity.py:43(get_player)
        8    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
       29    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
      721    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
     1083    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
      499    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
     1108    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      120    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        3    0.000    0.000    0.000    0.000 processors.py:138(_process_player_turn_intents)
      107    0.000    0.000    0.000    0.000 entity.py:93(get_entitys_component)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      155    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
      332    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
      487    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF84F319BA0}
       68    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       19    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
       64    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       58    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
     1531    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        3    0.000    0.000    0.000    0.000 {built-in method nt.stat}
      311    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
     1086    0.000    0.000    0.000    0.000 sprite.py:168(update)
       14    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
      635    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      650    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      645    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       58    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       66    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      776    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
       16    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
      313    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       14    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        8    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
      156    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       19    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        2    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       58    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
       58    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
      620    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
      651    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        8    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       58    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      116    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
       58    0.000    0.000    0.000    0.000 __init__.py:432(format)
       17    0.000    0.000    0.000    0.000 entity.py:103(get_name)
        5    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      321    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      612    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        3    0.000    0.000    0.000    0.000 entity.py:174(create)
       18    0.000    0.000    0.000    0.000 event_core.py:41(publish)
      329    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        5    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        5    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        5    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        5    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       17    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
        3    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      139    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
      116    0.000    0.000    0.000    0.000 __init__.py:856(release)
        2    0.000    0.000    0.000    0.000 world.py:261(tile_has_tag)
       58    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       44    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
      321    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      305    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
       58    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
      320    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
       58    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        2    0.000    0.000    0.000    0.000 ai.py:72(act)
      194    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
      321    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
       20    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        3    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      116    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       58    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       58    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      310    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      174    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      196    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       58    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      184    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
      306    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      188    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        4    0.000    0.000    0.000    0.000 entity_handler.py:217(_process_end_turn)
        8    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       58    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        1    0.000    0.000    0.000    0.000 world.py:439(recompute_fov)
       16    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      109    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
       68    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        6    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      118    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       60    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       76    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       58    0.000    0.000    0.000    0.000 threading.py:1052(name)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
      205    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       10    0.000    0.000    0.000    0.000 event.py:106(__init__)
      134    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        4    0.000    0.000    0.000    0.000 entity.py:380(spend_time)
       16    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        1    0.000    0.000    0.000    0.000 world.py:396(_tile_has_other_entity)
       42    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
      153    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       18    0.000    0.000    0.000    0.000 event_core.py:15(notify)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      107    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       20    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        1    0.000    0.000    0.000    0.000 world.py:360(_is_tile_blocking_movement)
       66    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       32    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        6    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       58    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
      116    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        3    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
       60    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       58    0.000    0.000    0.000    0.000 {built-in method time.time}
       42    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       40    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       58    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        4    0.000    0.000    0.000    0.000 entity.py:335(add_component)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       18    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
       20    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       66    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       14    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        4    0.000    0.000    0.000    0.000 event.py:88(__init__)
        4    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        3    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
      118    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
      157    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       15    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        2    0.000    0.000    0.000    0.000 event.py:184(__init__)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       27    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        3    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        3    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        8    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       44    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       27    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        6    0.000    0.000    0.000    0.000 {built-in method math.sin}
       18    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       15    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        2    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       27    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       14    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        3    0.000    0.000    0.000    0.000 component.py:39(__init__)
        6    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       12    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       23    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       42    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 event.py:63(__init__)
        8    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        6    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       19    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        3    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
       14    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
       15    0.000    0.000    0.000    0.000 state.py:17(get_previous)
       11    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
        2    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        1    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        4    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        6    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       16    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       13    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       10    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        3    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        5    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:24(__init__)
       24    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       22    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        5    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        4    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        3    0.000    0.000    0.000    0.000 component.py:63(__init__)
        6    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       34    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        8    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        3    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
       12    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        3    0.000    0.000    0.000    0.000 component.py:81(__init__)
       15    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 component.py:183(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        6    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        2    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        8    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        9    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        3    0.000    0.000    0.000    0.000 component.py:132(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 component.py:30(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        4    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        4    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        4    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 component.py:72(__init__)
        4    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        2    0.000    0.000    0.000    0.000 component.py:55(__init__)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 component.py:175(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        1    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:91(__init__)
        2    0.000    0.000    0.000    0.000 component.py:109(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:69(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 component.py:117(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:100(__init__)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


