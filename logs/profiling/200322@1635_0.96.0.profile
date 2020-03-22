Sun Mar 22 16:35:54 2020    logs/profiling/profile.dump

         2142488 function calls (1956227 primitive calls) in 12.253 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.085    0.085   12.211   12.211 main.py:104(game_loop)
      472    5.176    0.011    5.176    0.011 {method 'tick' of 'Clock' objects}
      236    0.001    0.000    4.516    0.019 event_core.py:24(update)
       47    0.000    0.000    3.309    0.070 entity_handler.py:26(process_event)
        6    0.000    0.000    3.308    0.551 entity_handler.py:45(_process_move)
       13    0.000    0.000    3.266    0.251 world.py:268(tile_has_tag)
        1    3.265    3.265    3.265    3.265 world.py:365(_tile_has_any_entity)
      236    0.001    0.000    2.660    0.011 state.py:38(get_delta_time)
      236    0.001    0.000    2.518    0.011 state.py:63(update_clock)
       54    0.000    0.000    1.192    0.022 ui_handler.py:31(process_event)
      236    0.001    0.000    1.182    0.005 manager.py:54(update)
      236    0.065    0.000    1.181    0.005 ui_manager.py:122(update)
        7    0.000    0.000    1.146    0.164 ui_handler.py:201(_update_camera)
        7    0.000    0.000    1.128    0.161 manager.py:295(update_camera_grid)
        7    0.007    0.001    1.128    0.161 camera.py:105(update_grid)
     1067    0.014    0.000    1.118    0.001 ui_button.py:30(__init__)
      236    0.004    0.000    1.111    0.005 manager.py:73(draw)
     1067    0.058    0.000    1.051    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        7    0.000    0.000    0.986    0.141 ui_handler.py:44(process_entity_event)
    31144    0.078    0.000    0.851    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
    78651    0.823    0.000    0.823    0.000 {method 'blit' of 'pygame.Surface' objects}
217368/31144    0.724    0.000    0.766    0.000 ui_appearance_theme.py:322(get_next_id_node)
      236    0.038    0.000    0.748    0.003 sprite.py:453(update)
    16098    0.042    0.000    0.481    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
      242    0.215    0.001    0.473    0.002 camera.py:79(update_game_map)
      235    0.001    0.000    0.462    0.002 camera.py:72(update)
      236    0.002    0.000    0.430    0.002 ui_manager.py:173(draw_ui)
      236    0.067    0.000    0.429    0.002 sprite.py:753(draw)
      240    0.310    0.001    0.310    0.001 {built-in method pygame.transform.scale}
     9696    0.019    0.000    0.280    0.000 ui_appearance_theme.py:428(get_misc_data)
    37903    0.156    0.000    0.278    0.000 ui_element.py:121(check_hover)
    36905    0.073    0.000    0.199    0.000 ui_button.py:197(update)
       40    0.000    0.000    0.174    0.004 ui_handler.py:68(process_game_event)
        1    0.000    0.000    0.169    0.169 ui_handler.py:107(init_game_ui)
     1067    0.007    0.000    0.131    0.000 ui_button.py:97(set_any_images_from_theme)
     4268    0.008    0.000    0.124    0.000 ui_appearance_theme.py:366(get_image)
    36905    0.029    0.000    0.112    0.000 drawable_shape.py:36(update)
     5350    0.036    0.000    0.103    0.000 rect_drawable_shape.py:118(redraw_state)
      236    0.091    0.000    0.091    0.000 {built-in method pygame.event.get}
      236    0.085    0.000    0.085    0.000 {built-in method pygame.display.flip}
    36905    0.044    0.000    0.084    0.000 ui_button.py:138(hover_point)
     2653    0.079    0.000    0.083    0.000 sprite.py:913(get_sprites_from_layer)
     1067    0.009    0.000    0.063    0.000 ui_button.py:537(rebuild_shape)
     1082    0.004    0.000    0.055    0.000 rect_drawable_shape.py:22(__init__)
    36307    0.051    0.000    0.051    0.000 camera.py:233(world_to_screen_position)
     1092    0.011    0.000    0.050    0.000 ui_element.py:23(__init__)
     1082    0.015    0.000    0.049    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
    10507    0.013    0.000    0.043    0.000 _internal.py:24(wrapper)
        1    0.000    0.000    0.042    0.042 main.py:212(initialise_game)
     1067    0.005    0.000    0.042    0.000 ui_appearance_theme.py:405(get_font)
        5    0.010    0.002    0.041    0.008 world.py:432(update_tile_visibility)
      368    0.002    0.000    0.040    0.000 screen_message.py:34(update)
    36905    0.035    0.000    0.040    0.000 rect_drawable_shape.py:84(collide_point)
       11    0.000    0.000    0.039    0.004 ui_text_box.py:50(__init__)
       11    0.000    0.000    0.038    0.003 ui_text_box.py:492(rebuild_from_changed_theme_data)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      805    0.037    0.000    0.037    0.000 {method 'fill' of 'pygame.Surface' objects}
       11    0.001    0.000    0.036    0.003 ui_text_box.py:110(rebuild)
      250    0.001    0.000    0.034    0.000 ui_text_box.py:347(redraw_from_chunks)
        8    0.000    0.000    0.033    0.004 message_log.py:49(add_message)
   471412    0.033    0.000    0.033    0.000 {method 'append' of 'list' objects}
    76982    0.026    0.000    0.032    0.000 sprite.py:208(alive)
        7    0.000    0.000    0.032    0.005 ui_handler.py:151(process_ui_event)
        7    0.000    0.000    0.032    0.005 ui_handler.py:232(_process_message)
        2    0.008    0.004    0.032    0.016 world.py:26(create_fov_map)
        7    0.000    0.000    0.032    0.005 manager.py:444(add_to_message_log)
     5350    0.030    0.000    0.030    0.000 surface_cache.py:119(build_cache_id)
     1082    0.005    0.000    0.029    0.000 drawable_shape.py:45(redraw_all_states)
      603    0.005    0.000    0.029    0.000 ui_text_box.py:205(update)
       45    0.000    0.000    0.028    0.001 manager.py:60(process_ui_events)
       45    0.010    0.000    0.028    0.001 ui_manager.py:86(process_events)
     5410    0.026    0.000    0.026    0.000 {method 'copy' of 'pygame.Surface' objects}
      250    0.003    0.000    0.024    0.000 ui_text_box.py:327(redraw_from_text_block)
     1092    0.003    0.000    0.024    0.000 ui_container.py:42(add_element)
        7    0.004    0.001    0.021    0.003 ui_container.py:116(clear)
    10508    0.020    0.000    0.021    0.000 {built-in method _warnings.warn}
   396589    0.021    0.000    0.021    0.000 {built-in method builtins.len}
     2014    0.018    0.000    0.018    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      909    0.001    0.000    0.017    0.000 ui_button.py:130(kill)
       15    0.000    0.000    0.017    0.001 ui_text_box.py:310(parse_html_into_style_data)
        4    0.000    0.000    0.017    0.004 ui_vertical_scroll_bar.py:22(__init__)
      922    0.002    0.000    0.016    0.000 ui_element.py:114(kill)
     1092    0.002    0.000    0.015    0.000 sprite.py:121(__init__)
     4066    0.009    0.000    0.014    0.000 world.py:55(get_tile)
      236    0.001    0.000    0.014    0.000 processors.py:18(process_all)
    36905    0.014    0.000    0.014    0.000 ui_button.py:154(can_hover)
      236    0.007    0.000    0.013    0.000 processors.py:25(_process_aesthetic_update)
       40    0.000    0.000    0.013    0.000 game_handler.py:26(process_event)
     1092    0.004    0.000    0.013    0.000 sprite.py:126(add)
      104    0.001    0.000    0.013    0.000 __init__.py:1496(_log)
        7    0.000    0.000    0.013    0.002 manager.py:286(update_camera_game_map)
      126    0.001    0.000    0.012    0.000 ui_text_box.py:462(set_active_effect)
       15    0.000    0.000    0.012    0.001 text_block.py:16(__init__)
       15    0.002    0.000    0.011    0.001 text_block.py:40(redraw)
     1092    0.002    0.000    0.010    0.000 ui_element.py:104(change_layer)
      922    0.002    0.000    0.009    0.000 ui_container.py:52(remove_element)
      250    0.003    0.000    0.009    0.000 text_block.py:265(redraw_from_chunks)
       12    0.000    0.000    0.009    0.001 game_handler.py:81(_process_end_turn)
       12    0.000    0.000    0.009    0.001 chrono.py:47(next_turn)
      236    0.001    0.000    0.009    0.000 ui_appearance_theme.py:158(update_shape_cache)
       65    0.000    0.000    0.009    0.000 __init__.py:1996(debug)
     5350    0.008    0.000    0.009    0.000 drawable_shape.py:122(rebuild_images_and_text)
       65    0.000    0.000    0.008    0.000 __init__.py:1361(debug)
   123884    0.008    0.000    0.008    0.000 {method 'reverse' of 'list' objects}
      236    0.001    0.000    0.008    0.000 surface_cache.py:24(update)
     1092    0.007    0.000    0.008    0.000 sprite.py:646(add_internal)
     1100    0.007    0.000    0.008    0.000 sprite.py:822(change_layer)
     1844    0.006    0.000    0.008    0.000 query.py:212(__iter__)
       30    0.005    0.000    0.007    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     1321    0.003    0.000    0.007    0.000 ui_font_dictionary.py:89(find_font)
     7500    0.003    0.000    0.007    0.000 libtcodpy.py:3300(map_is_in_fov)
      104    0.000    0.000    0.007    0.000 __init__.py:1521(handle)
    40077    0.006    0.000    0.006    0.000 ui_manager.py:167(get_mouse_position)
      104    0.000    0.000    0.006    0.000 __init__.py:1575(callHandlers)
      104    0.000    0.000    0.006    0.000 __init__.py:892(handle)
    76982    0.006    0.000    0.006    0.000 {built-in method _operator.truth}
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 entity.py:339(build_characteristic_sprites)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      104    0.000    0.000    0.005    0.000 __init__.py:1123(emit)
       40    0.000    0.000    0.005    0.000 utility.py:13(get_image)
        7    0.000    0.000    0.005    0.001 manager.py:275(update_cameras_tiles)
        7    0.002    0.000    0.005    0.001 camera.py:167(update_camera_tiles)
       38    0.000    0.000    0.005    0.000 __init__.py:1986(info)
      104    0.000    0.000    0.005    0.000 __init__.py:1022(emit)
       38    0.000    0.000    0.005    0.000 __init__.py:1373(info)
    39314    0.005    0.000    0.005    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     1411    0.004    0.000    0.005    0.000 ui_container.py:124(check_hover)
     4080    0.004    0.000    0.005    0.000 world.py:346(_is_tile_in_bounds)
    36982    0.005    0.000    0.005    0.000 {method 'union' of 'pygame.Rect' objects}
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      922    0.001    0.000    0.005    0.000 sprite.py:183(kill)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
      104    0.000    0.000    0.004    0.000 __init__.py:1481(makeRecord)
       26    0.000    0.000    0.004    0.000 game_handler.py:39(_process_change_game_state)
       64    0.002    0.000    0.004    0.000 styled_chunk.py:8(__init__)
    39966    0.004    0.000    0.004    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       15    0.000    0.000    0.004    0.000 parser.py:104(feed)
      104    0.001    0.000    0.004    0.000 __init__.py:293(__init__)
       15    0.001    0.000    0.004    0.000 parser.py:134(goahead)
     5646    0.004    0.000    0.004    0.000 ui_button.py:257(process_event)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     7500    0.004    0.000    0.004    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       25    0.000    0.000    0.004    0.000 state.py:71(set_new)
       12    0.000    0.000    0.004    0.000 chrono.py:24(rebuild_turn_queue)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
      922    0.002    0.000    0.003    0.000 sprite.py:728(remove_internal)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
     5350    0.003    0.000    0.003    0.000 surface_cache.py:109(find_surface_in_cache)
     1082    0.003    0.000    0.003    0.000 drawable_shape.py:11(__init__)
      797    0.003    0.000    0.003    0.000 typing.py:806(__new__)
      353    0.003    0.000    0.003    0.000 ui_manager.py:104(<listcomp>)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
     1088    0.002    0.000    0.003    0.000 ui_element.py:68(create_valid_ids)
      797    0.002    0.000    0.003    0.000 query.py:170(__init__)
      104    0.000    0.000    0.003    0.000 __init__.py:869(format)
      104    0.001    0.000    0.002    0.000 __init__.py:606(format)
      281    0.002    0.000    0.002    0.000 sprite.py:814(layers)
     1176    0.002    0.000    0.002    0.000 ui_window.py:97(update)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       45    0.000    0.000    0.002    0.000 processors.py:59(process_intent)
       64    0.001    0.000    0.002    0.000 parser.py:301(parse_starttag)
        6    0.000    0.000    0.002    0.000 entity.py:482(take_turn)
      129    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
      128    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      104    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
       32    0.000    0.000    0.002    0.000 processors.py:140(_process_player_turn_intents)
     1322    0.002    0.000    0.002    0.000 ui_font_dictionary.py:133(create_font_id)
     2097    0.002    0.000    0.002    0.000 {method 'remove' of 'list' objects}
       57    0.001    0.000    0.002    0.000 entity.py:43(get_player)
      236    0.001    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
      126    0.000    0.000    0.002    0.000 html_parser.py:118(add_text)
      472    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
      107    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
     1082    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
      104    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
     4328    0.001    0.000    0.001    0.000 {built-in method math.floor}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
        1    0.000    0.000    0.001    0.001 interaction_handler.py:27(process_event)
        1    0.000    0.000    0.001    0.001 interaction_handler.py:85(_process_entity_collision)
      107    0.001    0.000    0.001    0.000 ntpath.py:178(split)
      126    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
      104    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
     8154    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      104    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       64    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
      998    0.001    0.000    0.001    0.000 ui_element.py:186(hover_point)
      235    0.001    0.000    0.001    0.000 skill_bar.py:45(update)
       15    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
       15    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        1    0.000    0.000    0.001    0.001 interaction_handler.py:135(_apply_effects_to_tiles)
      564    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
     1289    0.001    0.000    0.001    0.000 query.py:243(<listcomp>)
        4    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
        3    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
  255/254    0.001    0.000    0.001    0.000 entity.py:93(get_entitys_component)
        5    0.000    0.000    0.001    0.000 combat_stats.py:270(sight_range)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:233(_insert_code)
      235    0.000    0.000    0.001    0.000 message_log.py:36(update)
       64    0.000    0.000    0.001    0.000 html_parser.py:283(handle_data)
     5379    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     1123    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
      160    0.001    0.000    0.001    0.000 ui_vertical_scroll_bar.py:228(update)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     7490    0.001    0.000    0.001    0.000 {method 'contains' of 'pygame.Rect' objects}
     5350    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
     1082    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
      797    0.001    0.000    0.001    0.000 query.py:50(__init__)
      105    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
     3578    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
     2231    0.001    0.000    0.001    0.000 {built-in method builtins.min}
       45    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
      104    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
      235    0.000    0.000    0.001    0.000 entity_info.py:47(update)
     2192    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     2277    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
      104    0.001    0.000    0.001    0.000 {built-in method time.strftime}
     2128    0.001    0.000    0.001    0.000 {built-in method builtins.max}
      236    0.001    0.000    0.001    0.000 ecs.py:265(process_pending_deletions)
     1104    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
      505    0.001    0.000    0.001    0.000 state.py:45(get_current)
       58    0.000    0.000    0.001    0.000 utility.py:188(value_to_member)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
      236    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       45    0.000    0.000    0.001    0.000 action.py:12(convert_to_intent)
      244    0.000    0.000    0.001    0.000 query.py:225(<listcomp>)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      214    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
      205    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       53    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
     1192    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
     2193    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
     1092    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
      799    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF84D989BA0}
      104    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
      113    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       59    0.000    0.000    0.000    0.000 entity.py:104(get_name)
       10    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       48    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      202    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
       59    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
      126    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        5    0.000    0.000    0.000    0.000 {built-in method nt.stat}
     2144    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        4    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
      104    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
     1100    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       59    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
     1646    0.000    0.000    0.000    0.000 sprite.py:168(update)
      124    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      104    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        9    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      104    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
     1082    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       15    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        1    0.000    0.000    0.000    0.000 skill.py:218(process_effect)
        6    0.000    0.000    0.000    0.000 ai.py:68(act)
     1176    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
      104    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
      998    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
      168    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
       94    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
       12    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        9    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
      268    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 entity_handler.py:165(_process_want_to_use_skill)
     1092    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      208    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        9    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        3    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
        2    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
      971    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      104    0.000    0.000    0.000    0.000 __init__.py:432(format)
     1092    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      236    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       30    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        5    0.000    0.000    0.000    0.000 world.py:425(recompute_fov)
      132    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
     1077    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       55    0.000    0.000    0.000    0.000 event_core.py:41(publish)
       64    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
     1067    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        9    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        9    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        6    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       12    0.000    0.000    0.000    0.000 entity_handler.py:224(_process_end_turn)
        9    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        9    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       32    0.000    0.000    0.000    0.000 processors.py:73(_get_pressed_direction)
        1    0.000    0.000    0.000    0.000 debug.py:28(log_component_not_found)
        1    0.000    0.000    0.000    0.000 chrono.py:79(next_round)
      104    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       30    0.000    0.000    0.000    0.000 utility.py:107(lerp)
       30    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      214    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        1    0.000    0.000    0.000    0.000 skill.py:76(can_afford_cost)
        1    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
      208    0.000    0.000    0.000    0.000 __init__.py:856(release)
        1    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       30    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
      255    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        6    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       76    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
      104    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      266    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
       45    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
      104    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        3    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
      189    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
      335    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
      126    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
      122    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
      141    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       12    0.000    0.000    0.000    0.000 entity.py:377(spend_time)
      922    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      208    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        3    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      104    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       22    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       55    0.000    0.000    0.000    0.000 event_core.py:15(notify)
      105    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      312    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      104    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
     1252    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 entity.py:174(create)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      254    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       15    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
      544    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        6    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       15    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      335    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      182    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       45    0.000    0.000    0.000    0.000 processors.py:120(_process_stateless_intents)
       26    0.000    0.000    0.000    0.000 event.py:88(__init__)
        3    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
      412    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        5    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
      104    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       14    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
      261    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
      214    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      211    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
      160    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      478    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
      107    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       55    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
       32    0.000    0.000    0.000    0.000 utility.py:121(clamp)
      126    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
       32    0.000    0.000    0.000    0.000 processors.py:100(_get_pressed_skills_number)
        5    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        7    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
      104    0.000    0.000    0.000    0.000 threading.py:1052(name)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       15    0.000    0.000    0.000    0.000 parser.py:96(reset)
      250    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
       12    0.000    0.000    0.000    0.000 event.py:70(__init__)
       30    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        6    0.000    0.000    0.000    0.000 event.py:53(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
      124    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
      130    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       12    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        1    0.000    0.000    0.000    0.000 main.py:239(initialise_event_handlers)
       64    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        8    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        7    0.000    0.000    0.000    0.000 event.py:166(__init__)
        5    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        6    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
      107    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
      104    0.000    0.000    0.000    0.000 {built-in method time.time}
       64    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
      104    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        1    0.000    0.000    0.000    0.000 skill.py:246(_process_trigger_skill_effect)
      107    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      193    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:52(_pydev_stop_at_break)
      209    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       30    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       39    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        4    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       60    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       12    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
      124    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       38    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
      211    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       70    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        1    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        6    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        7    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       88    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
      190    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       11    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       15    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       59    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       71    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       72    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        4    0.000    0.000    0.000    0.000 entity.py:332(add_component)
       47    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       11    0.000    0.000    0.000    0.000 {built-in method math.sin}
       35    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
      136    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       12    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 world.py:314(tile_has_tags)
       30    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       64    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 world.py:83(get_tiles)
       47    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       15    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       47    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        7    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        3    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       43    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        1    0.000    0.000    0.000    0.000 world.py:103(get_direction)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       15    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        1    0.000    0.000    0.000    0.000 manager.py:264(move_camera)
        4    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        7    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
       18    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       65    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        6    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        7    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
       12    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
       22    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
       36    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
       26    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
        8    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       15    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        1    0.000    0.000    0.000    0.000 _collections_abc.py:657(get)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        7    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
       24    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        9    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
       12    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
       13    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        6    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        1    0.000    0.000    0.000    0.000 os.py:673(__getitem__)
       42    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 camera.py:223(move_camera)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 event.py:118(__init__)
        1    0.000    0.000    0.000    0.000 event.py:80(__init__)
       26    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       40    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        5    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        1    0.000    0.000    0.000    0.000 main.py:189(disable_profiling)
        4    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        7    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 _weakrefset.py:38(_remove)
        1    0.000    0.000    0.000    0.000 event.py:18(__init__)
       12    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       38    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
       13    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
       12    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       12    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
       11    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        6    0.000    0.000    0.000    0.000 world.py:358(_is_tile_blocking_movement)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 os.py:743(encodekey)
        3    0.000    0.000    0.000    0.000 component.py:82(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        6    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        6    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        1    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        2    0.000    0.000    0.000    0.000 component.py:31(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:21(update_globals_dict)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        4    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 ui_handler.py:28(__init__)
        6    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:56(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 pydev_log.py:16(debug)
        1    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        6    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 os.py:737(check_str)
        1    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 world.py:325(<genexpr>)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 pydevd_constants.py:479(get_global_debugger)
        1    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        1    0.000    0.000    0.000    0.000 chrono.py:95(increment_round)
        1    0.000    0.000    0.000    0.000 component.py:118(__init__)
        1    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        1    0.000    0.000    0.000    0.000 {_pydevd_frame_eval.pydevd_frame_evaluator_win32_37_64.get_thread_info_py}
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        3    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


