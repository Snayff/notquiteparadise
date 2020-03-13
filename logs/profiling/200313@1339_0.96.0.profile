Fri Mar 13 13:39:20 2020    logs/profiling/profile.dump

         1168734 function calls (1037818 primitive calls) in 3.413 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.025    0.025    3.373    3.373 main.py:77(game_loop)
      158    1.728    0.011    1.728    0.011 {method 'tick' of 'Clock' objects}
       79    0.000    0.000    0.887    0.011 state.py:36(get_delta_time)
       79    0.000    0.000    0.844    0.011 event_core.py:21(update)
       79    0.000    0.000    0.842    0.011 state.py:61(update_clock)
       10    0.000    0.000    0.839    0.084 ui_handler.py:30(process_event)
        5    0.000    0.000    0.825    0.165 ui_handler.py:205(update_camera)
        5    0.000    0.000    0.812    0.162 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.812    0.162 camera.py:106(update_grid)
      755    0.010    0.000    0.796    0.001 ui_button.py:30(__init__)
      755    0.042    0.000    0.749    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        4    0.000    0.000    0.658    0.164 ui_handler.py:48(process_entity_event)
    21940    0.055    0.000    0.602    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
152820/21940    0.514    0.000    0.542    0.000 ui_appearance_theme.py:322(get_next_id_node)
       79    0.000    0.000    0.381    0.005 manager.py:54(update)
       79    0.020    0.000    0.381    0.005 ui_manager.py:122(update)
       79    0.001    0.000    0.376    0.005 manager.py:73(draw)
    11346    0.030    0.000    0.342    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    26120    0.268    0.000    0.268    0.000 {method 'blit' of 'pygame.Surface' objects}
       79    0.012    0.000    0.252    0.003 sprite.py:453(update)
     6816    0.014    0.000    0.198    0.000 ui_appearance_theme.py:428(get_misc_data)
        6    0.000    0.000    0.180    0.030 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.175    0.175 ui_handler.py:111(init_game_ui)
       83    0.066    0.001    0.149    0.002 camera.py:79(update_game_map)
       79    0.001    0.000    0.148    0.002 ui_manager.py:173(draw_ui)
       79    0.023    0.000    0.147    0.002 sprite.py:753(draw)
       78    0.000    0.000    0.140    0.002 camera.py:72(update)
       83    0.105    0.001    0.105    0.001 {built-in method pygame.transform.scale}
    12090    0.023    0.000    0.097    0.000 ui_button.py:197(update)
      755    0.005    0.000    0.093    0.000 ui_button.py:97(set_any_images_from_theme)
     3020    0.006    0.000    0.088    0.000 ui_appearance_theme.py:366(get_image)
    12324    0.046    0.000    0.082    0.000 ui_element.py:121(check_hover)
     3778    0.024    0.000    0.072    0.000 rect_drawable_shape.py:118(redraw_state)
    12090    0.013    0.000    0.069    0.000 drawable_shape.py:36(update)
      755    0.006    0.000    0.045    0.000 ui_button.py:537(rebuild_shape)
        1    0.000    0.000    0.040    0.040 main.py:182(initialise_game)
      758    0.003    0.000    0.039    0.000 rect_drawable_shape.py:22(__init__)
        2    0.000    0.000    0.037    0.018 entity.py:216(create_actor)
      768    0.008    0.000    0.036    0.000 ui_element.py:23(__init__)
      758    0.011    0.000    0.035    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        2    0.008    0.004    0.031    0.015 world.py:28(create_fov_map)
      755    0.003    0.000    0.029    0.000 ui_appearance_theme.py:405(get_font)
       79    0.028    0.000    0.028    0.000 {built-in method pygame.display.flip}
      882    0.024    0.000    0.025    0.000 sprite.py:913(get_sprites_from_layer)
    12090    0.013    0.000    0.025    0.000 ui_button.py:138(hover_point)
      758    0.004    0.000    0.021    0.000 drawable_shape.py:45(redraw_all_states)
     3778    0.021    0.000    0.021    0.000 surface_cache.py:119(build_cache_id)
   296697    0.019    0.000    0.019    0.000 {method 'append' of 'list' objects}
     3796    0.019    0.000    0.019    0.000 {method 'copy' of 'pygame.Surface' objects}
    12456    0.018    0.000    0.018    0.000 camera.py:234(world_to_screen_position)
      768    0.002    0.000    0.017    0.000 ui_container.py:42(add_element)
        5    0.003    0.001    0.014    0.003 ui_container.py:116(clear)
   263443    0.013    0.000    0.013    0.000 {built-in method builtins.len}
     3002    0.004    0.000    0.013    0.000 _internal.py:24(wrapper)
     1369    0.012    0.000    0.012    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     3766    0.008    0.000    0.012    0.000 world.py:57(get_tile)
    12090    0.010    0.000    0.012    0.000 rect_drawable_shape.py:84(collide_point)
       98    0.011    0.000    0.011    0.000 {method 'fill' of 'pygame.Surface' objects}
      600    0.001    0.000    0.011    0.000 ui_button.py:130(kill)
      768    0.001    0.000    0.011    0.000 sprite.py:121(__init__)
      601    0.001    0.000    0.010    0.000 ui_element.py:114(kill)
    25039    0.008    0.000    0.010    0.000 sprite.py:208(alive)
      768    0.003    0.000    0.009    0.000 sprite.py:126(add)
        5    0.000    0.000    0.009    0.002 manager.py:286(update_camera_game_map)
       79    0.008    0.000    0.008    0.000 {built-in method pygame.event.get}
        3    0.000    0.000    0.007    0.002 ui_text_box.py:50(__init__)
      768    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
        3    0.000    0.000    0.007    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
       20    0.000    0.000    0.007    0.000 manager.py:60(process_ui_events)
       20    0.003    0.000    0.007    0.000 ui_manager.py:86(process_events)
        3    0.000    0.000    0.007    0.002 ui_text_box.py:110(rebuild)
     3003    0.006    0.000    0.006    0.000 {built-in method _warnings.warn}
      601    0.001    0.000    0.006    0.000 ui_container.py:52(remove_element)
       47    0.000    0.000    0.006    0.000 __init__.py:1996(debug)
       47    0.000    0.000    0.006    0.000 __init__.py:1361(debug)
    87380    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
     3778    0.005    0.000    0.006    0.000 drawable_shape.py:122(rebuild_images_and_text)
       48    0.000    0.000    0.006    0.000 __init__.py:1496(_log)
      776    0.005    0.000    0.006    0.000 sprite.py:822(change_layer)
        3    0.000    0.000    0.006    0.002 ui_text_box.py:310(parse_html_into_style_data)
      762    0.002    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
      768    0.005    0.000    0.005    0.000 sprite.py:646(add_internal)
        2    0.000    0.000    0.005    0.003 entity.py:294(build_characteristic_sprites)
       40    0.000    0.000    0.005    0.000 utility.py:13(get_image)
        3    0.000    0.000    0.005    0.002 text_block.py:16(__init__)
        3    0.000    0.000    0.005    0.002 text_block.py:40(redraw)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
       41    0.004    0.000    0.004    0.000 {built-in method pygame.imageext.load_extended}
    12090    0.004    0.000    0.004    0.000 ui_button.py:154(can_hover)
     3770    0.003    0.000    0.004    0.000 world.py:349(_is_tile_in_bounds)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:14(__init__)
        5    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
        5    0.001    0.000    0.004    0.001 camera.py:168(update_camera_tiles)
        1    0.000    0.000    0.003    0.003 world.py:21(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
       48    0.000    0.000    0.003    0.000 __init__.py:1521(handle)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      601    0.001    0.000    0.003    0.000 sprite.py:183(kill)
       48    0.000    0.000    0.003    0.000 __init__.py:1575(callHandlers)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
       48    0.000    0.000    0.003    0.000 __init__.py:892(handle)
       48    0.000    0.000    0.002    0.000 __init__.py:1123(emit)
       48    0.000    0.000    0.002    0.000 __init__.py:1022(emit)
        6    0.000    0.000    0.002    0.000 game_handler.py:26(process_event)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
     3778    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
      764    0.002    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
      601    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
      758    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
        1    0.000    0.000    0.002    0.002 message_log.py:49(add_message)
       48    0.000    0.000    0.002    0.000 __init__.py:1481(makeRecord)
    12949    0.002    0.000    0.002    0.000 ui_manager.py:167(get_mouse_position)
       10    0.000    0.000    0.002    0.000 entity_handler.py:26(process_event)
       48    0.001    0.000    0.002    0.000 __init__.py:293(__init__)
    11724    0.002    0.000    0.002    0.000 {method 'union' of 'pygame.Rect' objects}
    25039    0.002    0.000    0.002    0.000 {built-in method _operator.truth}
      469    0.001    0.000    0.002    0.000 ui_container.py:124(check_hover)
    12793    0.002    0.000    0.002    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
       79    0.000    0.000    0.001    0.000 processors.py:15(process_all)
    12628    0.001    0.000    0.001    0.000 {method 'colliderect' of 'pygame.Rect' objects}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       79    0.000    0.000    0.001    0.000 ui_appearance_theme.py:158(update_shape_cache)
       48    0.000    0.000    0.001    0.000 __init__.py:869(format)
       27    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
       79    0.001    0.000    0.001    0.000 processors.py:22(_process_aesthetic_update)
       48    0.000    0.000    0.001    0.000 __init__.py:606(format)
      156    0.001    0.000    0.001    0.000 ui_text_box.py:205(update)
      763    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
        2    0.000    0.000    0.001    0.001 styled_chunk.py:8(__init__)
     1392    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
     7538    0.001    0.000    0.001    0.000 world.py:50(get_game_map)
       79    0.000    0.000    0.001    0.000 surface_cache.py:24(update)
      758    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     3032    0.001    0.000    0.001    0.000 {built-in method math.floor}
     1395    0.001    0.000    0.001    0.000 ui_button.py:257(process_event)
        4    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      391    0.001    0.000    0.001    0.000 ui_window.py:97(update)
       99    0.001    0.000    0.001    0.000 sprite.py:814(layers)
       78    0.000    0.000    0.001    0.000 screen_message.py:34(update)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
       48    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
       50    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
        6    0.000    0.000    0.001    0.000 map_handler.py:23(process_event)
      101    0.001    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
       48    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
       50    0.000    0.000    0.001    0.000 ntpath.py:178(split)
      758    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
       48    0.000    0.000    0.001    0.000 __init__.py:1451(findCaller)
        1    0.000    0.000    0.001    0.001 game_handler.py:81(process_end_turn)
      785    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        1    0.000    0.000    0.001    0.001 chrono.py:51(next_turn)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
      158    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
     3778    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
       79    0.000    0.000    0.001    0.000 ui_manager.py:158(update_mouse_position)
        4    0.000    0.000    0.001    0.000 game_handler.py:42(process_change_game_state)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        4    0.000    0.000    0.001    0.000 god_handler.py:26(process_event)
     1553    0.001    0.000    0.001    0.000 {built-in method builtins.min}
       48    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
     1544    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
       78    0.000    0.000    0.000    0.000 skill_bar.py:44(update)
     2385    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
     4262    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
     1471    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      758    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       49    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        3    0.000    0.000    0.000    0.000 parser.py:104(feed)
        3    0.000    0.000    0.000    0.000 parser.py:134(goahead)
     1170    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
       20    0.000    0.000    0.000    0.000 processors.py:56(process_intent)
      198    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        3    0.000    0.000    0.000    0.000 state.py:69(set_new)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
       78    0.000    0.000    0.000    0.000 message_log.py:36(update)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
       48    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
      234    0.000    0.000    0.000    0.000 ui_element.py:186(hover_point)
        2    0.000    0.000    0.000    0.000 {built-in method nt.stat}
     1545    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        4    0.000    0.000    0.000    0.000 entity_handler.py:48(process_move)
        1    0.000    0.000    0.000    0.000 chrono.py:23(build_new_turn_queue)
      768    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       20    0.000    0.000    0.000    0.000 entity.py:117(get_primary_stat)
       11    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       48    0.000    0.000    0.000    0.000 {built-in method time.strftime}
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        1    0.000    0.000    0.000    0.000 entity.py:187(create_god)
       78    0.000    0.000    0.000    0.000 entity_info.py:45(update)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        9    0.000    0.000    0.000    0.000 processors.py:137(_process_player_turn_intents)
        1    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
     1512    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
      100    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        3    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
      165    0.000    0.000    0.000    0.000 state.py:43(get_current)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        3    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
      776    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       54    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       48    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       20    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
      768    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       79    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
        3    0.000    0.000    0.000    0.000 entity.py:160(create)
      769    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        1    0.000    0.000    0.000    0.000 __init__.py:1986(info)
       48    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 __init__.py:1373(info)
      768    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      757    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       25    0.000    0.000    0.000    0.000 entity.py:287(add_component)
        8    0.000    0.000    0.000    0.000 world.py:262(tile_has_tag)
        2    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       48    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       29    0.000    0.000    0.000    0.000 esper.py:196(add_component)
       48    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      624    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
       24    0.000    0.000    0.000    0.000 utility.py:107(lerp)
      547    0.000    0.000    0.000    0.000 sprite.py:168(update)
      755    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       48    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       96    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       22    0.000    0.000    0.000    0.000 entity.py:80(get_entitys_component)
       48    0.000    0.000    0.000    0.000 __init__.py:432(format)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       79    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      601    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
      391    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
       12    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        4    0.000    0.000    0.000    0.000 event.py:53(__init__)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       48    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        4    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
       96    0.000    0.000    0.000    0.000 __init__.py:856(release)
        4    0.000    0.000    0.000    0.000 world.py:361(_is_tile_blocking_movement)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       20    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        1    0.000    0.000    0.000    0.000 main.py:209(initialise_event_handlers)
       48    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
      234    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        3    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
       48    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
       48    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       19    0.000    0.000    0.000    0.000 entity.py:34(get_player)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        2    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        6    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       20    0.000    0.000    0.000    0.000 processors.py:117(_process_stateless_intents)
       96    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      144    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
       24    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        3    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
       48    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       48    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       10    0.000    0.000    0.000    0.000 event_core.py:38(publish)
      125    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
      158    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       48    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
      256    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       15    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       29    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        4    0.000    0.000    0.000    0.000 world.py:397(_tile_has_other_entity)
      194    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
       98    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
       56    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       50    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
      156    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       18    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
       59    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       48    0.000    0.000    0.000    0.000 threading.py:1052(name)
        8    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        9    0.000    0.000    0.000    0.000 processors.py:70(_get_pressed_direction)
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        2    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       10    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        8    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        3    0.000    0.000    0.000    0.000 entity.py:90(get_name)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        9    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        1    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       74    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        9    0.000    0.000    0.000    0.000 processors.py:97(_get_pressed_skills_number)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       48    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
      102    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        4    0.000    0.000    0.000    0.000 event.py:92(__init__)
       22    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        3    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       50    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       48    0.000    0.000    0.000    0.000 {built-in method time.time}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        3    0.000    0.000    0.000    0.000 entity.py:103(get_identity)
        4    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       96    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       37    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       48    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       98    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       13    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       16    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
       10    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        6    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        3    0.000    0.000    0.000    0.000 parser.py:96(reset)
        9    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        1    0.000    0.000    0.000    0.000 entity_handler.py:204(process_end_turn)
       12    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        5    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       22    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 entity.py:332(spend_time)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 entity.py:110(get_combat_stats)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       15    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       58    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       10    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        6    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.000    0.000 main.py:159(disable_profiling)
        3    0.000    0.000    0.000    0.000 component.py:43(__init__)
       43    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {built-in method math.sin}
        1    0.000    0.000    0.000    0.000 event.py:84(__init__)
        3    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        5    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        2    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       18    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        3    0.000    0.000    0.000    0.000 component.py:58(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 event.py:74(__init__)
       29    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        6    0.000    0.000    0.000    0.000 chrono.py:115(get_turn_holder)
        7    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 library.py:205(get_secondary_stat_data)
        3    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        3    0.000    0.000    0.000    0.000 component.py:77(__init__)
        5    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        2    0.000    0.000    0.000    0.000 component.py:166(__init__)
        2    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        4    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        6    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        6    0.000    0.000    0.000    0.000 state.py:15(get_previous)
        3    0.000    0.000    0.000    0.000 component.py:122(__init__)
        3    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        5    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        2    0.000    0.000    0.000    0.000 chrono.py:159(set_turn_holder)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
       12    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 component.py:34(__init__)
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        2    0.000    0.000    0.000    0.000 component.py:68(__init__)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        9    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 component.py:158(__init__)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        8    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 chrono.py:106(add_time)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:87(__init__)
        1    0.000    0.000    0.000    0.000 library.py:230(get_god_data)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        3    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:96(__init__)
        2    0.000    0.000    0.000    0.000 component.py:105(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:143(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:122(get_turn_queue)
        1    0.000    0.000    0.000    0.000 chrono.py:173(set_turn_queue)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        2    0.000    0.000    0.000    0.000 chrono.py:129(get_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:166(set_time_in_round)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 chrono.py:136(get_time)
        1    0.000    0.000    0.000    0.000 chrono.py:180(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


