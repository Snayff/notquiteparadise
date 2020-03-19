Thu Mar 19 12:05:15 2020    logs/profiling/profile.dump

         818232 function calls (739516 primitive calls) in 3.016 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.028    0.028    2.974    2.974 main.py:80(game_loop)
      150    1.624    0.011    1.624    0.011 {method 'tick' of 'Clock' objects}
       75    0.001    0.000    0.818    0.011 state.py:38(get_delta_time)
       75    0.000    0.000    0.807    0.011 state.py:63(update_clock)
       75    0.000    0.000    0.520    0.007 event_core.py:21(update)
        8    0.000    0.000    0.500    0.062 ui_handler.py:30(process_event)
        3    0.000    0.000    0.486    0.162 ui_handler.py:207(update_camera)
        3    0.000    0.000    0.478    0.159 manager.py:295(update_camera_grid)
        3    0.003    0.001    0.478    0.159 camera.py:106(update_grid)
      455    0.006    0.000    0.471    0.001 ui_button.py:30(__init__)
      455    0.025    0.000    0.443    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
       75    0.001    0.000    0.383    0.005 manager.py:73(draw)
       75    0.000    0.000    0.377    0.005 manager.py:54(update)
       75    0.021    0.000    0.377    0.005 ui_manager.py:122(update)
    13240    0.032    0.000    0.356    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
        2    0.000    0.000    0.325    0.163 ui_handler.py:48(process_entity_event)
91920/13240    0.303    0.000    0.321    0.000 ui_appearance_theme.py:322(get_next_id_node)
    24528    0.269    0.000    0.269    0.000 {method 'blit' of 'pygame.Surface' objects}
       75    0.012    0.000    0.236    0.003 sprite.py:453(update)
     6846    0.017    0.000    0.200    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
        6    0.000    0.000    0.174    0.029 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.169    0.169 ui_handler.py:111(init_game_ui)
       77    0.070    0.001    0.152    0.002 camera.py:79(update_game_map)
       75    0.001    0.000    0.147    0.002 ui_manager.py:173(draw_ui)
       74    0.000    0.000    0.147    0.002 camera.py:72(update)
       75    0.024    0.000    0.147    0.002 sprite.py:753(draw)
     4116    0.008    0.000    0.118    0.000 ui_appearance_theme.py:428(get_misc_data)
       79    0.111    0.001    0.111    0.001 {built-in method pygame.transform.scale}
    11692    0.051    0.000    0.090    0.000 ui_element.py:121(check_hover)
    11470    0.022    0.000    0.074    0.000 ui_button.py:197(update)
      455    0.003    0.000    0.055    0.000 ui_button.py:97(set_any_images_from_theme)
     1820    0.003    0.000    0.052    0.000 ui_appearance_theme.py:366(get_image)
    11470    0.010    0.000    0.048    0.000 drawable_shape.py:36(update)
     2278    0.015    0.000    0.047    0.000 rect_drawable_shape.py:118(redraw_state)
        1    0.000    0.000    0.042    0.042 main.py:184(initialise_game)
        2    0.000    0.000    0.038    0.019 entity.py:225(create_actor)
       75    0.036    0.000    0.036    0.000 {built-in method pygame.event.get}
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
      455    0.004    0.000    0.028    0.000 ui_button.py:537(rebuild_shape)
       75    0.027    0.000    0.027    0.000 {built-in method pygame.display.flip}
    11470    0.014    0.000    0.027    0.000 ui_button.py:138(hover_point)
      802    0.025    0.000    0.026    0.000 sprite.py:913(get_sprites_from_layer)
     6004    0.008    0.000    0.025    0.000 _internal.py:24(wrapper)
      458    0.002    0.000    0.025    0.000 rect_drawable_shape.py:22(__init__)
      458    0.007    0.000    0.022    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      468    0.005    0.000    0.022    0.000 ui_element.py:23(__init__)
      455    0.002    0.000    0.018    0.000 ui_appearance_theme.py:405(get_font)
        8    0.000    0.000    0.017    0.002 entity_handler.py:29(process_event)
    11554    0.017    0.000    0.017    0.000 camera.py:234(world_to_screen_position)
        2    0.000    0.000    0.016    0.008 entity_handler.py:57(_process_move)
        2    0.004    0.002    0.016    0.008 world.py:445(update_tile_visibility)
     2296    0.013    0.000    0.013    0.000 {method 'copy' of 'pygame.Surface' objects}
   188500    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
      458    0.002    0.000    0.013    0.000 drawable_shape.py:45(redraw_all_states)
    11470    0.011    0.000    0.013    0.000 rect_drawable_shape.py:84(collide_point)
     2278    0.013    0.000    0.013    0.000 surface_cache.py:119(build_cache_id)
     6005    0.012    0.000    0.012    0.000 {built-in method _warnings.warn}
     3458    0.007    0.000    0.011    0.000 world.py:55(get_tile)
       94    0.011    0.000    0.011    0.000 {method 'fill' of 'pygame.Surface' objects}
      468    0.001    0.000    0.010    0.000 ui_container.py:42(add_element)
    23755    0.008    0.000    0.010    0.000 sprite.py:208(alive)
   162890    0.008    0.000    0.008    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.007    0.002 ui_text_box.py:50(__init__)
        3    0.001    0.000    0.007    0.002 ui_container.py:116(clear)
        3    0.000    0.000    0.007    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
      769    0.007    0.000    0.007    0.000 ui_container.py:62(recalculate_container_layer_thickness)
        3    0.000    0.000    0.007    0.002 ui_text_box.py:110(rebuild)
      468    0.001    0.000    0.007    0.000 sprite.py:121(__init__)
        2    0.000    0.000    0.006    0.003 entity.py:332(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
      300    0.000    0.000    0.006    0.000 ui_button.py:130(kill)
      468    0.002    0.000    0.006    0.000 sprite.py:126(add)
        3    0.000    0.000    0.006    0.002 ui_text_box.py:310(parse_html_into_style_data)
      301    0.001    0.000    0.005    0.000 ui_element.py:114(kill)
        3    0.000    0.000    0.005    0.002 manager.py:286(update_camera_game_map)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       39    0.000    0.000    0.005    0.000 __init__.py:1496(_log)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
        3    0.000    0.000    0.005    0.002 text_block.py:16(__init__)
        3    0.000    0.000    0.005    0.002 text_block.py:40(redraw)
       35    0.000    0.000    0.005    0.000 __init__.py:1996(debug)
       35    0.000    0.000    0.005    0.000 __init__.py:1361(debug)
    11470    0.005    0.000    0.005    0.000 ui_button.py:154(can_hover)
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
      462    0.001    0.000    0.004    0.000 ui_font_dictionary.py:89(find_font)
      468    0.001    0.000    0.004    0.000 ui_element.py:104(change_layer)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     2278    0.003    0.000    0.004    0.000 drawable_shape.py:122(rebuild_images_and_text)
       16    0.000    0.000    0.004    0.000 manager.py:60(process_ui_events)
     3460    0.003    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
       16    0.001    0.000    0.004    0.000 ui_manager.py:86(process_events)
    52580    0.004    0.000    0.004    0.000 {method 'reverse' of 'list' objects}
      468    0.003    0.000    0.003    0.000 sprite.py:646(add_internal)
      476    0.003    0.000    0.003    0.000 sprite.py:822(change_layer)
      301    0.001    0.000    0.003    0.000 ui_container.py:52(remove_element)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       39    0.000    0.000    0.003    0.000 __init__.py:1521(handle)
       39    0.000    0.000    0.002    0.000 __init__.py:1575(callHandlers)
       39    0.000    0.000    0.002    0.000 __init__.py:892(handle)
     3000    0.001    0.000    0.002    0.000 libtcodpy.py:3300(map_is_in_fov)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        3    0.000    0.000    0.002    0.001 manager.py:275(update_cameras_tiles)
        3    0.001    0.000    0.002    0.001 camera.py:168(update_camera_tiles)
        6    0.000    0.000    0.002    0.000 game_handler.py:26(process_event)
    12285    0.002    0.000    0.002    0.000 ui_manager.py:167(get_mouse_position)
       39    0.000    0.000    0.002    0.000 __init__.py:1123(emit)
       39    0.000    0.000    0.002    0.000 __init__.py:1022(emit)
        1    0.000    0.000    0.002    0.002 message_log.py:49(add_message)
    12137    0.002    0.000    0.002    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
    23755    0.002    0.000    0.002    0.000 {built-in method _operator.truth}
       39    0.000    0.000    0.002    0.000 __init__.py:1481(makeRecord)
    11392    0.002    0.000    0.002    0.000 {method 'union' of 'pygame.Rect' objects}
      445    0.001    0.000    0.002    0.000 ui_container.py:124(check_hover)
       39    0.001    0.000    0.002    0.000 __init__.py:293(__init__)
      301    0.000    0.000    0.002    0.000 sprite.py:183(kill)
    12252    0.001    0.000    0.001    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       75    0.000    0.000    0.001    0.000 processors.py:16(process_all)
     2278    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
       75    0.000    0.000    0.001    0.000 ui_appearance_theme.py:158(update_shape_cache)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       27    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
      458    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
      148    0.001    0.000    0.001    0.000 ui_text_box.py:205(update)
       75    0.001    0.000    0.001    0.000 processors.py:23(_process_aesthetic_update)
      464    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
        2    0.000    0.000    0.001    0.001 styled_chunk.py:8(__init__)
       75    0.000    0.000    0.001    0.000 surface_cache.py:24(update)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.001    0.001    0.001    0.001 camera.py:24(__init__)
      301    0.001    0.000    0.001    0.000 sprite.py:728(remove_internal)
     6922    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       39    0.000    0.000    0.001    0.000 __init__.py:869(format)
       39    0.000    0.000    0.001    0.000 __init__.py:606(format)
        4    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
       91    0.001    0.000    0.001    0.000 sprite.py:814(layers)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
      371    0.001    0.000    0.001    0.000 ui_window.py:97(update)
       74    0.000    0.000    0.001    0.000 screen_message.py:34(update)
      458    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
        4    0.000    0.000    0.001    0.000 game_handler.py:42(process_change_game_state)
      463    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
       39    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
       41    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
        1    0.000    0.000    0.001    0.001 game_handler.py:81(process_end_turn)
     1832    0.001    0.000    0.001    0.000 {built-in method math.floor}
        1    0.000    0.000    0.001    0.001 chrono.py:50(next_turn)
      792    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
       41    0.000    0.000    0.001    0.000 ntpath.py:178(split)
       75    0.000    0.000    0.001    0.000 ui_manager.py:158(update_mouse_position)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       39    0.000    0.000    0.001    0.000 __init__.py:1451(findCaller)
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
      150    0.000    0.000    0.000    0.000 sprite.py:745(sprites)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
      775    0.000    0.000    0.000    0.000 ui_button.py:257(process_event)
        4    0.000    0.000    0.000    0.000 __init__.py:1986(info)
       39    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
        4    0.000    0.000    0.000    0.000 __init__.py:1373(info)
       39    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        3    0.000    0.000    0.000    0.000 state.py:71(set_new)
     3895    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
       61    0.000    0.000    0.000    0.000 ui_manager.py:104(<listcomp>)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       40    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
       74    0.000    0.000    0.000    0.000 skill_bar.py:45(update)
      481    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
      222    0.000    0.000    0.000    0.000 ui_element.py:186(hover_point)
      182    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        3    0.000    0.000    0.000    0.000 parser.py:104(feed)
     2278    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
      458    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
        3    0.000    0.000    0.000    0.000 parser.py:134(goahead)
       74    0.000    0.000    0.000    0.000 message_log.py:36(update)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        2    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
       11    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 chrono.py:23(rebuild_turn_queue)
     1449    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      944    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      935    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
       39    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      900    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      458    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       39    0.000    0.000    0.000    0.000 {built-in method time.strftime}
       74    0.000    0.000    0.000    0.000 entity_info.py:45(update)
       16    0.000    0.000    0.000    0.000 processors.py:57(process_intent)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
      850    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      157    0.000    0.000    0.000    0.000 state.py:45(get_current)
        3    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
        3    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       82    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
      945    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       45    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       75    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
        3    0.000    0.000    0.000    0.000 entity.py:166(create)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      468    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       39    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       34    0.000    0.000    0.000    0.000 entity.py:325(add_component)
        5    0.000    0.000    0.000    0.000 processors.py:138(_process_player_turn_intents)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      912    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      476    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       16    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
        2    0.000    0.000    0.000    0.000 {built-in method nt.stat}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
       39    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       34    0.000    0.000    0.000    0.000 esper.py:196(add_component)
        2    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        1    0.000    0.000    0.000    0.000 main.py:211(initialise_event_handlers)
       39    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
      468    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       39    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        8    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
      469    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
      468    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      519    0.000    0.000    0.000    0.000 sprite.py:168(update)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       75    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       39    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       78    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        4    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
        2    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
      371    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
      457    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
       39    0.000    0.000    0.000    0.000 __init__.py:432(format)
      455    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
       17    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       12    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        8    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      322    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        6    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
      222    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
       39    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        3    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
       78    0.000    0.000    0.000    0.000 __init__.py:856(release)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       39    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       39    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       16    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        2    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       39    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        3    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        2    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
      113    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       78    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        4    0.000    0.000    0.000    0.000 entity.py:96(get_name)
       39    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      117    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:38(publish)
        2    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
       16    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
      211    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
       39    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       34    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
      301    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      138    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       11    0.000    0.000    0.000    0.000 entity.py:37(get_player)
      131    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
      176    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       39    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       80    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        4    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
        4    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        2    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       12    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       41    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        8    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
       15    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
      147    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       50    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       39    0.000    0.000    0.000    0.000 threading.py:1052(name)
        2    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        1    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        8    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        2    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       36    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        5    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        3    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       10    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       39    0.000    0.000    0.000    0.000 {built-in method time.time}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       39    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        4    0.000    0.000    0.000    0.000 event.py:106(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       41    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 event.py:63(__init__)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       21    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       78    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       39    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        3    0.000    0.000    0.000    0.000 parser.py:96(reset)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       12    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       46    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        6    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       80    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        8    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
       14    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       21    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        5    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        1    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
        5    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
       17    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        6    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
       68    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
       10    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        6    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method math.sin}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 main.py:161(disable_profiling)
        1    0.000    0.000    0.000    0.000 entity.py:370(spend_time)
        3    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
       43    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       13    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        1    0.000    0.000    0.000    0.000 event.py:88(__init__)
       18    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        8    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
       34    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        3    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        3    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        3    0.000    0.000    0.000    0.000 component.py:87(__init__)
        5    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        7    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        2    0.000    0.000    0.000    0.000 component.py:189(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        3    0.000    0.000    0.000    0.000 chrono.py:135(get_time)
        2    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        3    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        5    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 chrono.py:158(set_turn_holder)
        6    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        3    0.000    0.000    0.000    0.000 component.py:69(__init__)
        3    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        6    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        4    0.000    0.000    0.000    0.000 chrono.py:114(get_turn_holder)
        2    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
       12    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        3    0.000    0.000    0.000    0.000 component.py:138(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 component.py:37(__init__)
        3    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        5    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        8    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 component.py:61(__init__)
        2    0.000    0.000    0.000    0.000 component.py:78(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:105(add_time)
        2    0.000    0.000    0.000    0.000 component.py:97(__init__)
        1    0.000    0.000    0.000    0.000 component.py:181(__init__)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 chrono.py:172(set_turn_queue)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:128(get_time_in_round)
        1    0.000    0.000    0.000    0.000 ai.py:68(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 chrono.py:121(get_turn_queue)
        2    0.000    0.000    0.000    0.000 component.py:106(__init__)
        2    0.000    0.000    0.000    0.000 component.py:115(__init__)
        1    0.000    0.000    0.000    0.000 component.py:123(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:179(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 chrono.py:165(set_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:142(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}


