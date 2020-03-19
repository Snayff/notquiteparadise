Thu Mar 19 13:11:17 2020    logs/profiling/profile.dump

         802367 function calls (723102 primitive calls) in 3.768 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.036    0.036    3.725    3.725 main.py:78(game_loop)
      194    2.323    0.012    2.323    0.012 {method 'tick' of 'Clock' objects}
       97    0.000    0.000    1.181    0.012 state.py:63(update_clock)
       97    0.001    0.000    1.143    0.012 state.py:38(get_delta_time)
       97    0.000    0.000    0.563    0.006 event_core.py:21(update)
       27    0.000    0.000    0.534    0.020 ui_handler.py:30(process_event)
        3    0.000    0.000    0.504    0.168 ui_handler.py:207(update_camera)
        3    0.000    0.000    0.496    0.165 manager.py:295(update_camera_grid)
        3    0.003    0.001    0.496    0.165 camera.py:106(update_grid)
      457    0.006    0.000    0.492    0.001 ui_button.py:30(__init__)
      457    0.026    0.000    0.462    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
       97    0.002    0.000    0.424    0.004 manager.py:73(draw)
    13365    0.034    0.000    0.371    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
       97    0.000    0.000    0.354    0.004 manager.py:54(update)
       97    0.022    0.000    0.353    0.004 ui_manager.py:122(update)
        2    0.000    0.000    0.341    0.171 ui_handler.py:48(process_entity_event)
92592/13365    0.316    0.000    0.334    0.000 ui_appearance_theme.py:322(get_next_id_node)
    20946    0.267    0.000    0.267    0.000 {method 'blit' of 'pygame.Surface' objects}
       97    0.011    0.000    0.216    0.002 sprite.py:453(update)
     6906    0.019    0.000    0.210    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
       22    0.000    0.000    0.184    0.008 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.170    0.170 ui_handler.py:111(init_game_ui)
      105    0.140    0.001    0.140    0.001 {built-in method pygame.transform.scale}
       65    0.062    0.001    0.134    0.002 camera.py:79(update_game_map)
       62    0.000    0.000    0.129    0.002 camera.py:72(update)
     4167    0.008    0.000    0.123    0.000 ui_appearance_theme.py:428(get_misc_data)
       97    0.001    0.000    0.121    0.001 ui_manager.py:173(draw_ui)
       97    0.019    0.000    0.120    0.001 sprite.py:753(draw)
    10028    0.048    0.000    0.085    0.000 ui_element.py:121(check_hover)
     9678    0.020    0.000    0.071    0.000 ui_button.py:197(update)
      457    0.003    0.000    0.057    0.000 ui_button.py:97(set_any_images_from_theme)
     1828    0.003    0.000    0.054    0.000 ui_appearance_theme.py:366(get_image)
     2293    0.015    0.000    0.047    0.000 rect_drawable_shape.py:118(redraw_state)
     9678    0.010    0.000    0.046    0.000 drawable_shape.py:36(update)
        1    0.000    0.000    0.043    0.043 main.py:183(initialise_game)
        2    0.000    0.000    0.039    0.020 entity.py:225(create_actor)
       97    0.035    0.000    0.035    0.000 {built-in method pygame.display.flip}
        2    0.008    0.004    0.032    0.016 world.py:26(create_fov_map)
      457    0.004    0.000    0.030    0.000 ui_button.py:537(rebuild_shape)
      465    0.002    0.000    0.027    0.000 rect_drawable_shape.py:22(__init__)
      923    0.025    0.000    0.026    0.000 sprite.py:913(get_sprites_from_layer)
     6004    0.008    0.000    0.025    0.000 _internal.py:24(wrapper)
     9678    0.013    0.000    0.025    0.000 ui_button.py:138(hover_point)
      465    0.008    0.000    0.024    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      477    0.005    0.000    0.023    0.000 ui_element.py:23(__init__)
       24    0.000    0.000    0.020    0.001 entity_handler.py:29(process_event)
      457    0.002    0.000    0.018    0.000 ui_appearance_theme.py:405(get_font)
        2    0.000    0.000    0.016    0.008 entity_handler.py:57(_process_move)
      124    0.001    0.000    0.016    0.000 __init__.py:1496(_log)
        2    0.004    0.002    0.016    0.008 world.py:445(update_tile_visibility)
     9754    0.015    0.000    0.015    0.000 camera.py:234(world_to_screen_position)
      104    0.000    0.000    0.015    0.000 __init__.py:1996(debug)
      465    0.002    0.000    0.014    0.000 drawable_shape.py:45(redraw_all_states)
      104    0.000    0.000    0.014    0.000 __init__.py:1361(debug)
      130    0.014    0.000    0.014    0.000 {method 'fill' of 'pygame.Surface' objects}
     2329    0.014    0.000    0.014    0.000 {method 'copy' of 'pygame.Surface' objects}
       97    0.013    0.000    0.013    0.000 {built-in method pygame.event.get}
   187200    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
     6010    0.012    0.000    0.013    0.000 {built-in method _warnings.warn}
     2293    0.013    0.000    0.013    0.000 surface_cache.py:119(build_cache_id)
        7    0.000    0.000    0.012    0.002 ui_text_box.py:50(__init__)
     9678    0.011    0.000    0.012    0.000 rect_drawable_shape.py:84(collide_point)
        7    0.000    0.000    0.012    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     3458    0.007    0.000    0.012    0.000 world.py:55(get_tile)
      8/7    0.002    0.000    0.011    0.002 ui_container.py:116(clear)
      477    0.001    0.000    0.011    0.000 ui_container.py:42(add_element)
        7    0.000    0.000    0.010    0.001 ui_text_box.py:110(rebuild)
    20435    0.008    0.000    0.009    0.000 sprite.py:208(alive)
      947    0.009    0.000    0.009    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      455    0.001    0.000    0.009    0.000 ui_button.py:130(kill)
       22    0.000    0.000    0.008    0.000 game_handler.py:26(process_event)
   163134    0.008    0.000    0.008    0.000 {built-in method builtins.len}
        7    0.000    0.000    0.008    0.001 ui_text_box.py:310(parse_html_into_style_data)
      470    0.001    0.000    0.008    0.000 ui_element.py:114(kill)
      124    0.000    0.000    0.008    0.000 __init__.py:1521(handle)
      124    0.000    0.000    0.008    0.000 __init__.py:1575(callHandlers)
      124    0.001    0.000    0.007    0.000 __init__.py:892(handle)
       24    0.000    0.000    0.007    0.000 manager.py:60(process_ui_events)
       24    0.003    0.000    0.007    0.000 ui_manager.py:86(process_events)
      477    0.001    0.000    0.007    0.000 sprite.py:121(__init__)
        4    0.000    0.000    0.007    0.002 message_log.py:49(add_message)
        7    0.000    0.000    0.007    0.001 text_block.py:16(__init__)
        7    0.001    0.000    0.007    0.001 text_block.py:40(redraw)
      124    0.000    0.000    0.006    0.000 __init__.py:1123(emit)
      124    0.000    0.000    0.006    0.000 __init__.py:1022(emit)
        2    0.000    0.000    0.006    0.003 entity.py:332(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
      477    0.002    0.000    0.006    0.000 sprite.py:126(add)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.005    0.003 screen_message.py:16(__init__)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
        3    0.000    0.000    0.005    0.002 manager.py:286(update_camera_game_map)
      124    0.000    0.000    0.005    0.000 __init__.py:1481(makeRecord)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
      470    0.001    0.000    0.005    0.000 ui_container.py:52(remove_element)
      124    0.002    0.000    0.005    0.000 __init__.py:293(__init__)
        3    0.000    0.000    0.005    0.002 ui_handler.py:155(process_ui_event)
        3    0.000    0.000    0.005    0.002 ui_handler.py:238(process_message)
        3    0.000    0.000    0.005    0.002 manager.py:444(add_to_message_log)
      486    0.001    0.000    0.005    0.000 ui_element.py:104(change_layer)
      503    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
     9678    0.004    0.000    0.004    0.000 ui_button.py:154(can_hover)
        1    0.000    0.000    0.004    0.004 ui_handler.py:129(close_game_ui)
        4    0.000    0.000    0.004    0.001 manager.py:97(kill_element)
        4    0.000    0.000    0.004    0.001 ui_window.py:146(kill)
     3460    0.003    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
     2293    0.003    0.000    0.004    0.000 drawable_shape.py:122(rebuild_images_and_text)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
      5/4    0.000    0.000    0.004    0.001 ui_container.py:108(kill)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
      506    0.003    0.000    0.004    0.000 sprite.py:822(change_layer)
        1    0.000    0.000    0.004    0.004 ui_handler.py:139(init_dev_ui)
        1    0.000    0.000    0.004    0.004 manager.py:210(init_skill_editor)
        1    0.000    0.000    0.004    0.004 data_editor.py:31(__init__)
       97    0.000    0.000    0.004    0.000 ui_appearance_theme.py:158(update_shape_cache)
    52950    0.004    0.000    0.004    0.000 {method 'reverse' of 'list' objects}
      477    0.003    0.000    0.004    0.000 sprite.py:646(add_internal)
        1    0.000    0.000    0.003    0.003 data_editor.py:257(_create_data_category_selector)
        6    0.000    0.000    0.003    0.001 game_handler.py:81(process_end_turn)
        1    0.000    0.000    0.003    0.003 ui_drop_down_menu.py:351(__init__)
       97    0.000    0.000    0.003    0.000 surface_cache.py:24(update)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        6    0.000    0.000    0.003    0.001 chrono.py:44(next_turn)
      124    0.000    0.000    0.003    0.000 __init__.py:869(format)
        1    0.000    0.000    0.003    0.003 ui_drop_down_menu.py:283(start)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      124    0.001    0.000    0.003    0.000 __init__.py:606(format)
       18    0.001    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
      470    0.001    0.000    0.002    0.000 sprite.py:183(kill)
       20    0.000    0.000    0.002    0.000 __init__.py:1986(info)
       15    0.000    0.000    0.002    0.000 game_handler.py:42(process_change_game_state)
       20    0.000    0.000    0.002    0.000 __init__.py:1373(info)
     3000    0.001    0.000    0.002    0.000 libtcodpy.py:3300(map_is_in_fov)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        3    0.000    0.000    0.002    0.001 manager.py:275(update_cameras_tiles)
        3    0.001    0.000    0.002    0.001 camera.py:168(update_camera_tiles)
    10723    0.002    0.000    0.002    0.000 ui_manager.py:167(get_mouse_position)
      192    0.001    0.000    0.002    0.000 screen_message.py:34(update)
      124    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
       14    0.000    0.000    0.002    0.000 state.py:71(set_new)
      126    0.000    0.000    0.002    0.000 ntpath.py:212(basename)
       97    0.000    0.000    0.002    0.000 processors.py:16(process_all)
      254    0.002    0.000    0.002    0.000 ui_text_box.py:205(update)
       12    0.000    0.000    0.002    0.000 styled_chunk.py:8(__init__)
      441    0.001    0.000    0.002    0.000 ui_container.py:124(check_hover)
    10469    0.002    0.000    0.002    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      126    0.001    0.000    0.002    0.000 ntpath.py:178(split)
        6    0.000    0.000    0.002    0.000 chrono.py:23(rebuild_turn_queue)
    20435    0.002    0.000    0.002    0.000 {built-in method _operator.truth}
      470    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
      124    0.001    0.000    0.002    0.000 __init__.py:1451(findCaller)
       47    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
      124    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
       97    0.001    0.000    0.001    0.000 processors.py:23(_process_aesthetic_update)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     2293    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
        3    0.000    0.000    0.001    0.000 entity.py:475(take_turn)
     9568    0.001    0.000    0.001    0.000 {method 'union' of 'pygame.Rect' objects}
      465    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
      124    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        7    0.000    0.000    0.001    0.000 parser.py:104(feed)
    10461    0.001    0.000    0.001    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        7    0.000    0.000    0.001    0.000 parser.py:134(goahead)
      121    0.001    0.000    0.001    0.000 sprite.py:814(layers)
      472    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
       24    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     6922    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        2    0.000    0.000    0.001    0.000 warnings.py:96(_showwarnmsg)
      126    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        2    0.000    0.000    0.001    0.000 warnings.py:20(_showwarnmsg_impl)
      379    0.001    0.000    0.001    0.000 ui_window.py:97(update)
      938    0.001    0.000    0.001    0.000 ui_button.py:257(process_event)
      124    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
     1008    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
      465    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       97    0.001    0.000    0.001    0.000 ui_manager.py:158(update_mouse_position)
      124    0.001    0.000    0.001    0.000 {built-in method time.strftime}
      504    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
        5    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     1860    0.001    0.000    0.001    0.000 {built-in method math.floor}
       98    0.001    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
      194    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
        2    0.000    0.000    0.001    0.000 warnings.py:117(_formatwarnmsg)
        2    0.000    0.000    0.001    0.000 warnings.py:35(_formatwarnmsg_impl)
      252    0.000    0.000    0.001    0.000 ntpath.py:44(normcase)
        2    0.000    0.000    0.001    0.000 linecache.py:15(getline)
        2    0.000    0.000    0.001    0.000 linecache.py:37(getlines)
        2    0.000    0.000    0.001    0.000 linecache.py:82(updatecache)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        7    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        5    0.000    0.000    0.001    0.000 ui_text_box.py:102(kill)
       12    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        7    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
     4492    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
      350    0.000    0.000    0.000    0.000 ui_element.py:186(hover_point)
      124    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
      242    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
      130    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
     1997    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
       62    0.000    0.000    0.000    0.000 skill_bar.py:45(update)
      494    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       43    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
      124    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        4    0.000    0.000    0.000    0.000 {built-in method nt.stat}
     2293    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
      465    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
       22    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
       24    0.000    0.000    0.000    0.000 processors.py:57(process_intent)
       12    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        2    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
      954    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      124    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       30    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
      124    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      983    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      985    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:257(rebuild)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      248    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
      214    0.000    0.000    0.000    0.000 state.py:45(get_current)
       12    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       22    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
       18    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        6    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       62    0.000    0.000    0.000    0.000 message_log.py:36(update)
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
       12    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      124    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
      468    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
       24    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:36(remove_window)
       20    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
       42    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
       97    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
      868    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
        2    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       62    0.000    0.000    0.000    0.000 entity_info.py:45(update)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
       34    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:420(update)
      124    0.000    0.000    0.000    0.000 __init__.py:432(format)
        2    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       12    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       51    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        3    0.000    0.000    0.000    0.000 entity.py:166(create)
       26    0.000    0.000    0.000    0.000 entity.py:96(get_name)
      970    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        6    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
       10    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
      477    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       34    0.000    0.000    0.000    0.000 entity.py:325(add_component)
        1    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:436(rebuild_from_changed_theme_data)
        3    0.000    0.000    0.000    0.000 ai.py:71(act)
        6    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        2    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      124    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
      248    0.000    0.000    0.000    0.000 __init__.py:856(release)
      921    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       26    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
        1    0.000    0.000    0.000    0.000 data_editor.py:493(_load_field_options)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      248    0.000    0.000    0.000    0.000 __init__.py:747(filter)
      762    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
      124    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       34    0.000    0.000    0.000    0.000 data_editor.py:81(update)
      506    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       24    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      124    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        4    0.000    0.000    0.000    0.000 processors.py:138(_process_player_turn_intents)
       34    0.000    0.000    0.000    0.000 esper.py:196(add_component)
       27    0.000    0.000    0.000    0.000 event_core.py:38(publish)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       62    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
       97    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        6    0.000    0.000    0.000    0.000 chrono.py:161(_get_pretty_queue)
      124    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      503    0.000    0.000    0.000    0.000 sprite.py:168(update)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      372    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        7    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      512    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
      124    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        2    0.000    0.000    0.000    0.000 {built-in method io.open}
      477    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
      636    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      124    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      386    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      124    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
      475    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
       62    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       34    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:327(update)
      250    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
      478    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        2    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      379    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
      464    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
      350    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
      126    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       26    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
      380    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
       13    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
        2    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
        2    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
      146    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      336    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       12    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      124    0.000    0.000    0.000    0.000 threading.py:1052(name)
      457    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       12    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       24    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        6    0.000    0.000    0.000    0.000 entity.py:370(spend_time)
       67    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        1    0.000    0.000    0.000    0.000 main.py:210(initialise_event_handlers)
      470    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       27    0.000    0.000    0.000    0.000 event_core.py:12(notify)
      151    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       13    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
       26    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       28    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       15    0.000    0.000    0.000    0.000 event.py:106(__init__)
        7    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
      124    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        6    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      124    0.000    0.000    0.000    0.000 {built-in method time.time}
       55    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       15    0.000    0.000    0.000    0.000 entity.py:37(get_player)
      248    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
      126    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      124    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       34    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
       52    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        2    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        2    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
      249    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
      250    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        7    0.000    0.000    0.000    0.000 parser.py:96(reset)
       12    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        3    0.000    0.000    0.000    0.000 event.py:184(__init__)
       29    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        6    0.000    0.000    0.000    0.000 event.py:88(__init__)
       27    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        6    0.000    0.000    0.000    0.000 chrono.py:169(_get_next_entity_in_queue)
        5    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       22    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        2    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        1    0.000    0.000    0.000    0.000 data_editor.py:674(_load_library_data)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
       18    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       68    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       51    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
       13    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        2    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
      241    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       22    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        5    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        2    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       34    0.000    0.000    0.000    0.000 ui_button.py:304(check_pressed)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       12    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       21    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       28    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       26    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        4    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       56    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       42    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        2    0.000    0.000    0.000    0.000 event.py:63(__init__)
       12    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       28    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       18    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       17    0.000    0.000    0.000    0.000 chrono.py:119(get_turn_holder)
        7    0.000    0.000    0.000    0.000 {built-in method math.sin}
        7    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        5    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       18    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
       23    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        1    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:20(__init__)
        2    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        6    0.000    0.000    0.000    0.000 chrono.py:191(set_turn_queue)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        7    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        4    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       13    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       34    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       20    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        2    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        8    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       12    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
       18    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        6    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
       68    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
       32    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 main.py:160(disable_profiling)
        7    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       14    0.000    0.000    0.000    0.000 chrono.py:140(get_time)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        6    0.000    0.000    0.000    0.000 chrono.py:110(add_time)
       12    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
       12    0.000    0.000    0.000    0.000 chrono.py:126(get_turn_queue)
       34    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        1    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:236(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
       14    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        7    0.000    0.000    0.000    0.000 chrono.py:177(set_turn_holder)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        5    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
       17    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
       25    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       12    0.000    0.000    0.000    0.000 chrono.py:133(get_time_in_round)
        4    0.000    0.000    0.000    0.000 processors.py:176(_process_dev_mode_intents)
        7    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        3    0.000    0.000    0.000    0.000 component.py:88(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:147(get_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        2    0.000    0.000    0.000    0.000 component.py:190(__init__)
        7    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        3    0.000    0.000    0.000    0.000 component.py:70(__init__)
        2    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        6    0.000    0.000    0.000    0.000 chrono.py:184(set_time_in_round)
        3    0.000    0.000    0.000    0.000 component.py:139(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.000    0.000 chrono.py:198(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        2    0.000    0.000    0.000    0.000 component.py:37(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        2    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 component.py:79(__init__)
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 component.py:62(__init__)
        2    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 data_editor.py:262(<listcomp>)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        2    0.000    0.000    0.000    0.000 component.py:98(__init__)
        1    0.000    0.000    0.000    0.000 component.py:124(__init__)
        1    0.000    0.000    0.000    0.000 data_editor.py:501(<listcomp>)
        1    0.000    0.000    0.000    0.000 ai.py:68(__init__)
        1    0.000    0.000    0.000    0.000 library.py:147(get_homelands_data)
        1    0.000    0.000    0.000    0.000 library.py:163(get_skills_data)
        1    0.000    0.000    0.000    0.000 library.py:199(get_primary_stats_data)
        1    0.000    0.000    0.000    0.000 component.py:182(__init__)
        1    0.000    0.000    0.000    0.000 data_editor.py:502(<listcomp>)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:107(__init__)
        2    0.000    0.000    0.000    0.000 component.py:116(__init__)
        1    0.000    0.000    0.000    0.000 library.py:60(get_aspects_data)
        1    0.000    0.000    0.000    0.000 library.py:87(get_afflictions_data)
        1    0.000    0.000    0.000    0.000 library.py:115(get_savvys_data)
        1    0.000    0.000    0.000    0.000 library.py:131(get_peoples_data)
        1    0.000    0.000    0.000    0.000 data_editor.py:507(<listcomp>)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 library.py:215(get_secondary_stats_data)
        1    0.000    0.000    0.000    0.000 library.py:222(get_gods_data)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


