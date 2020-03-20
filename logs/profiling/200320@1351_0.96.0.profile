Fri Mar 20 13:51:59 2020    logs/profiling/profile.dump

         7344348 function calls (6272951 primitive calls) in 9.178 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.031    0.031    9.137    9.137 main.py:83(game_loop)
       85    0.001    0.000    6.668    0.078 event_core.py:21(update)
       66    0.000    0.000    6.617    0.100 ui_handler.py:30(process_event)
       41    0.000    0.000    6.583    0.161 ui_handler.py:207(update_camera)
       41    0.000    0.000    6.487    0.158 manager.py:295(update_camera_grid)
       41    0.039    0.001    6.487    0.158 camera.py:105(update_grid)
       44    0.000    0.000    6.420    0.146 ui_handler.py:48(process_entity_event)
     6158    0.076    0.000    6.309    0.001 ui_button.py:30(__init__)
     6158    0.329    0.000    5.936    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
   178711    0.435    0.000    4.798    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
1250067/178711    4.092    0.000    4.328    0.000 ui_appearance_theme.py:322(get_next_id_node)
    92430    0.238    0.000    2.715    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    55482    0.106    0.000    1.586    0.000 ui_appearance_theme.py:428(get_misc_data)
      170    1.422    0.008    1.422    0.008 {method 'tick' of 'Clock' objects}
       85    0.001    0.000    0.954    0.011 state.py:38(get_delta_time)
     6158    0.037    0.000    0.737    0.000 ui_button.py:97(set_any_images_from_theme)
    24632    0.044    0.000    0.700    0.000 ui_appearance_theme.py:366(get_image)
       85    0.000    0.000    0.553    0.007 manager.py:54(update)
       85    0.027    0.000    0.553    0.007 ui_manager.py:122(update)
       85    0.000    0.000    0.469    0.006 state.py:63(update_clock)
       85    0.001    0.000    0.411    0.005 manager.py:73(draw)
       85    0.015    0.000    0.368    0.004 sprite.py:453(update)
     6158    0.048    0.000    0.338    0.000 ui_button.py:537(rebuild_shape)
    33812    0.326    0.000    0.326    0.000 {method 'blit' of 'pygame.Surface' objects}
     6167    0.020    0.000    0.289    0.000 rect_drawable_shape.py:22(__init__)
     6177    0.058    0.000    0.276    0.000 ui_element.py:23(__init__)
     6167    0.080    0.000    0.253    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
    13099    0.087    0.000    0.246    0.000 rect_drawable_shape.py:118(redraw_state)
     6158    0.028    0.000    0.233    0.000 ui_appearance_theme.py:405(get_font)
      125    0.090    0.001    0.229    0.002 camera.py:79(update_game_map)
    13131    0.028    0.000    0.182    0.000 ui_button.py:197(update)
       18    0.000    0.000    0.178    0.010 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.172    0.172 ui_handler.py:111(init_game_ui)
       84    0.001    0.000    0.166    0.002 camera.py:72(update)
     6167    0.028    0.000    0.156    0.000 drawable_shape.py:45(redraw_all_states)
       85    0.001    0.000    0.154    0.002 ui_manager.py:173(draw_ui)
       85    0.021    0.000    0.153    0.002 sprite.py:753(draw)
    13131    0.023    0.000    0.148    0.000 drawable_shape.py:36(update)
       41    0.024    0.001    0.143    0.003 ui_container.py:116(clear)
  2215138    0.137    0.000    0.137    0.000 {method 'append' of 'list' objects}
     6177    0.017    0.000    0.132    0.000 ui_container.py:42(add_element)
       89    0.125    0.001    0.125    0.001 {built-in method pygame.transform.scale}
     6000    0.007    0.000    0.117    0.000 ui_button.py:130(kill)
    13504    0.066    0.000    0.117    0.000 ui_element.py:121(check_hover)
    12182    0.113    0.000    0.113    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     6005    0.012    0.000    0.110    0.000 ui_element.py:114(kill)
  2030884    0.100    0.000    0.100    0.000 {built-in method builtins.len}
     6177    0.010    0.000    0.082    0.000 sprite.py:121(__init__)
    13099    0.073    0.000    0.073    0.000 surface_cache.py:119(build_cache_id)
     6177    0.023    0.000    0.072    0.000 sprite.py:126(add)
     6005    0.012    0.000    0.067    0.000 ui_container.py:52(remove_element)
       41    0.000    0.000    0.064    0.002 manager.py:286(update_camera_game_map)
    13135    0.057    0.000    0.057    0.000 {method 'copy' of 'pygame.Surface' objects}
     6177    0.012    0.000    0.055    0.000 ui_element.py:104(change_layer)
   714296    0.047    0.000    0.047    0.000 {method 'reverse' of 'list' objects}
      327    0.002    0.000    0.045    0.000 __init__.py:1496(_log)
     6177    0.040    0.000    0.044    0.000 sprite.py:646(add_internal)
     6185    0.037    0.000    0.043    0.000 sprite.py:822(change_layer)
      270    0.001    0.000    0.042    0.000 __init__.py:1996(debug)
        1    0.000    0.000    0.041    0.041 main.py:188(initialise_game)
     1053    0.039    0.000    0.041    0.000 sprite.py:913(get_sprites_from_layer)
      270    0.002    0.000    0.041    0.000 __init__.py:1361(debug)
        2    0.000    0.000    0.038    0.019 entity.py:230(create_actor)
       62    0.001    0.000    0.035    0.001 entity_handler.py:29(process_event)
    13131    0.018    0.000    0.034    0.000 ui_button.py:138(hover_point)
       41    0.000    0.000    0.032    0.001 manager.py:275(update_cameras_tiles)
       41    0.010    0.000    0.032    0.001 camera.py:167(update_camera_tiles)
     6005    0.009    0.000    0.031    0.000 sprite.py:183(kill)
     9166    0.018    0.000    0.031    0.000 world.py:55(get_tile)
        2    0.008    0.004    0.031    0.015 world.py:26(create_fov_map)
       85    0.030    0.000    0.030    0.000 {built-in method pygame.display.flip}
    18753    0.028    0.000    0.028    0.000 camera.py:233(world_to_screen_position)
     6244    0.013    0.000    0.024    0.000 ui_font_dictionary.py:89(find_font)
      327    0.001    0.000    0.023    0.000 __init__.py:1521(handle)
      327    0.001    0.000    0.022    0.000 __init__.py:1575(callHandlers)
     6005    0.011    0.000    0.021    0.000 sprite.py:728(remove_internal)
      327    0.001    0.000    0.021    0.000 __init__.py:892(handle)
    13099    0.019    0.000    0.020    0.000 drawable_shape.py:122(rebuild_images_and_text)
        8    0.000    0.000    0.020    0.002 ui_text_box.py:50(__init__)
        8    0.000    0.000    0.019    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
      327    0.001    0.000    0.018    0.000 __init__.py:1123(emit)
      327    0.001    0.000    0.018    0.000 __init__.py:1022(emit)
        8    0.000    0.000    0.018    0.002 ui_text_box.py:110(rebuild)
       32    0.000    0.000    0.017    0.001 manager.py:60(process_ui_events)
       32    0.006    0.000    0.017    0.001 ui_manager.py:86(process_events)
    13131    0.014    0.000    0.016    0.000 rect_drawable_shape.py:84(collide_point)
     6173    0.012    0.000    0.015    0.000 ui_element.py:68(create_valid_ids)
      327    0.001    0.000    0.015    0.000 __init__.py:1481(makeRecord)
     6167    0.015    0.000    0.015    0.000 drawable_shape.py:11(__init__)
       40    0.001    0.000    0.015    0.000 entity.py:481(take_turn)
      327    0.005    0.000    0.014    0.000 __init__.py:293(__init__)
    27429    0.011    0.000    0.013    0.000 sprite.py:208(alive)
        5    0.000    0.000    0.013    0.003 message_log.py:49(add_message)
       85    0.013    0.000    0.013    0.000 {built-in method pygame.event.get}
      124    0.012    0.000    0.012    0.000 {method 'fill' of 'pygame.Surface' objects}
        4    0.000    0.000    0.011    0.003 ui_handler.py:155(process_ui_event)
        4    0.000    0.000    0.011    0.003 ui_handler.py:238(process_message)
        4    0.000    0.000    0.011    0.003 manager.py:444(add_to_message_log)
        9    0.000    0.000    0.011    0.001 ui_text_box.py:310(parse_html_into_style_data)
        2    0.000    0.000    0.010    0.005 entity_handler.py:135(_process_use_skill)
     9171    0.009    0.000    0.010    0.000 world.py:347(_is_tile_in_bounds)
    12225    0.010    0.000    0.010    0.000 {method 'remove' of 'list' objects}
        2    0.000    0.000    0.010    0.005 skill.py:111(use)
     4504    0.009    0.000    0.009    0.000 {built-in method _warnings.warn}
      327    0.001    0.000    0.009    0.000 __init__.py:869(format)
        2    0.000    0.000    0.009    0.004 skill.py:152(_call_skill_func)
    13099    0.009    0.000    0.009    0.000 surface_cache.py:109(find_surface_in_cache)
      327    0.002    0.000    0.008    0.000 __init__.py:606(format)
        9    0.000    0.000    0.008    0.001 text_block.py:16(__init__)
        9    0.001    0.000    0.008    0.001 text_block.py:40(redraw)
        3    0.000    0.000    0.008    0.003 entity_handler.py:57(_process_move)
     6245    0.008    0.000    0.008    0.000 ui_font_dictionary.py:133(create_font_id)
        1    0.002    0.002    0.008    0.008 world.py:445(update_tile_visibility)
       18    0.000    0.000    0.007    0.000 game_handler.py:26(process_event)
        2    0.000    0.000    0.007    0.004 __init__.py:109(import_module)
      3/2    0.000    0.000    0.007    0.004 <frozen importlib._bootstrap>:994(_gcd_import)
      3/2    0.000    0.000    0.007    0.004 <frozen importlib._bootstrap>:978(_find_and_load)
      2/1    0.000    0.000    0.007    0.007 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
       57    0.000    0.000    0.007    0.000 __init__.py:1986(info)
    24668    0.007    0.000    0.007    0.000 {built-in method math.floor}
        4    0.000    0.000    0.007    0.002 <frozen importlib._bootstrap_external>:722(exec_module)
       57    0.000    0.000    0.007    0.000 __init__.py:1373(info)
        4    0.000    0.000    0.007    0.002 <frozen importlib._bootstrap_external>:793(get_code)
        2    0.000    0.000    0.006    0.003 <frozen importlib._bootstrap>:663(_load_unlocked)
    13131    0.006    0.000    0.006    0.000 ui_button.py:154(can_hover)
        2    0.000    0.000    0.006    0.003 entity.py:338(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
       85    0.000    0.000    0.006    0.000 processors.py:16(process_all)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        8    0.001    0.000    0.006    0.001 <frozen importlib._bootstrap_external>:914(get_data)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
     6167    0.005    0.000    0.006    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       37    0.000    0.000    0.006    0.000 entity_handler.py:182(_process_die)
      327    0.001    0.000    0.006    0.000 __init__.py:1011(flush)
       44    0.000    0.000    0.006    0.000 god_handler.py:26(process_event)
       85    0.003    0.000    0.006    0.000 processors.py:23(_process_aesthetic_update)
       37    0.000    0.000    0.005    0.000 entity.py:187(delete)
      332    0.001    0.000    0.005    0.000 ntpath.py:212(basename)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
        4    0.005    0.001    0.005    0.001 {method 'read' of '_io.FileIO' objects}
      327    0.002    0.000    0.005    0.000 __init__.py:1451(findCaller)
      332    0.003    0.000    0.005    0.000 ntpath.py:178(split)
        1    0.000    0.000    0.004    0.004 ui_vertical_scroll_bar.py:22(__init__)
     6201    0.004    0.000    0.004    0.000 ui_window_stack.py:73(get_root_window)
      327    0.001    0.000    0.004    0.000 __init__.py:539(formatTime)
     6167    0.004    0.000    0.004    0.000 drawable_shape.py:46(<listcomp>)
      327    0.004    0.000    0.004    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
    12362    0.004    0.000    0.004    0.000 {method 'insert' of 'list' objects}
      797    0.003    0.000    0.004    0.000 query.py:212(__iter__)
    19741    0.004    0.000    0.004    0.000 {built-in method builtins.hasattr}
    12352    0.004    0.000    0.004    0.000 {built-in method builtins.min}
       85    0.000    0.000    0.003    0.000 ui_appearance_theme.py:158(update_shape_cache)
        5    0.000    0.000    0.003    0.001 game_handler.py:81(process_end_turn)
        5    0.000    0.000    0.003    0.001 chrono.py:44(next_turn)
    11634    0.003    0.000    0.003    0.000 {built-in method builtins.max}
     6197    0.003    0.000    0.003    0.000 drawable_shape.py:86(get_surface)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
       85    0.000    0.000    0.003    0.000 surface_cache.py:24(update)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
    18342    0.003    0.000    0.003    0.000 world.py:48(get_game_map)
    14298    0.003    0.000    0.003    0.000 ui_manager.py:167(get_mouse_position)
       18    0.002    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
      327    0.001    0.000    0.002    0.000 ntpath.py:201(splitext)
       22    0.001    0.000    0.002    0.000 styled_chunk.py:8(__init__)
    12363    0.002    0.000    0.002    0.000 ui_manager.py:44(get_sprite_group)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
    27429    0.002    0.000    0.002    0.000 {built-in method _operator.truth}
     3145    0.002    0.000    0.002    0.000 ui_button.py:257(process_event)
    14009    0.002    0.000    0.002    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     6177    0.002    0.000    0.002    0.000 sprite.py:162(add_internal)
      327    0.002    0.000    0.002    0.000 {built-in method time.strftime}
      505    0.002    0.000    0.002    0.000 ui_container.py:124(check_hover)
      328    0.001    0.000    0.002    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      252    0.002    0.000    0.002    0.000 ui_text_box.py:205(update)
        7    0.000    0.000    0.002    0.000 chrono.py:23(rebuild_turn_queue)
    13099    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
    12320    0.002    0.000    0.002    0.000 {method 'copy' of 'list' objects}
       12    0.000    0.000    0.002    0.000 game_handler.py:42(process_change_game_state)
      664    0.001    0.000    0.002    0.000 ntpath.py:44(normcase)
       57    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.002    0.001 interaction_handler.py:25(process_event)
        9    0.000    0.000    0.002    0.000 parser.py:104(feed)
       44    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        9    0.000    0.000    0.002    0.000 parser.py:134(goahead)
      9/7    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
     6186    0.002    0.000    0.002    0.000 {method 'pop' of 'dict' objects}
      168    0.001    0.000    0.002    0.000 screen_message.py:34(update)
      212    0.001    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
      327    0.001    0.000    0.001    0.000 genericpath.py:117(_splitext)
       11    0.000    0.000    0.001    0.000 state.py:71(set_new)
      342    0.001    0.000    0.001    0.000 ntpath.py:122(splitdrive)
      366    0.001    0.000    0.001    0.000 typing.py:806(__new__)
        2    0.000    0.000    0.001    0.001 interaction_handler.py:86(_process_entity_collision)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
        2    0.000    0.000    0.001    0.001 interaction_handler.py:121(_apply_effects_to_tiles)
    11483    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     6609    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
      117    0.000    0.000    0.001    0.000 entity.py:102(get_name)
      366    0.001    0.000    0.001    0.000 query.py:170(__init__)
     6177    0.001    0.000    0.001    0.000 {method '__contains__' of 'dict' objects}
     6173    0.001    0.000    0.001    0.000 ui_manager.py:51(get_window_stack)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
     6084    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
      246    0.001    0.000    0.001    0.000 entity.py:92(get_entitys_component)
      117    0.001    0.000    0.001    0.000 sprite.py:814(layers)
     8580    0.001    0.000    0.001    0.000 {method 'colliderect' of 'pygame.Rect' objects}
     6165    0.001    0.000    0.001    0.000 {method 'copy' of 'pygame.Rect' objects}
     7500    0.001    0.000    0.001    0.000 {method 'union' of 'pygame.Rect' objects}
      327    0.000    0.000    0.001    0.000 __init__.py:590(formatMessage)
        2    0.000    0.000    0.001    0.001 __init__.py:133(reload)
       38    0.001    0.000    0.001    0.000 ai.py:41(act)
     6177    0.001    0.000    0.001    0.000 ui_manager.py:37(get_theme)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
      327    0.001    0.000    0.001    0.000 {built-in method time.gmtime}
      327    0.000    0.000    0.001    0.000 __init__.py:584(usesTime)
      117    0.000    0.000    0.001    0.000 entity.py:115(get_identity)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
      421    0.001    0.000    0.001    0.000 ui_window.py:97(update)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
       22    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
      327    0.000    0.000    0.001    0.000 cp1252.py:18(encode)
        9    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        9    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
     6005    0.001    0.000    0.001    0.000 {method 'clear' of 'dict' objects}
       17    0.001    0.000    0.001    0.000 {built-in method nt.stat}
      654    0.000    0.000    0.001    0.000 __init__.py:849(acquire)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:610(_exec)
      327    0.001    0.000    0.001    0.000 __init__.py:432(format)
        2    0.001    0.000    0.001    0.000 {built-in method builtins.print}
       85    0.000    0.000    0.001    0.000 ui_manager.py:158(update_mouse_position)
      373    0.000    0.000    0.001    0.000 ui_element.py:186(hover_point)
       15    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
        2    0.000    0.000    0.001    0.000 entity_handler.py:244(_process_created_timed_entity)
       42    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
        1    0.000    0.000    0.001    0.001 entity.py:199(create_god)
     1500    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
      170    0.000    0.000    0.000    0.000 sprite.py:745(sprites)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
      327    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       42    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        2    0.000    0.000    0.000    0.000 skill.py:232(process_effect)
      654    0.000    0.000    0.000    0.000 __init__.py:856(release)
       22    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
      556    0.000    0.000    0.000    0.000 query.py:243(<listcomp>)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
       84    0.000    0.000    0.000    0.000 skill_bar.py:45(update)
      235    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
      327    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        2    0.000    0.000    0.000    0.000 entity.py:301(create_projectile)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       73    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
      654    0.000    0.000    0.000    0.000 __init__.py:747(filter)
      327    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      327    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      366    0.000    0.000    0.000    0.000 query.py:50(__init__)
     1225    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       68    0.000    0.000    0.000    0.000 event_core.py:38(publish)
       84    0.000    0.000    0.000    0.000 message_log.py:36(update)
       22    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
      327    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       32    0.000    0.000    0.000    0.000 processors.py:57(process_intent)
      981    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       45    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
       13    0.000    0.000    0.000    0.000 entity.py:42(get_player)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       20    0.000    0.000    0.000    0.000 entity.py:129(get_primary_stat)
       32    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
     1687    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      327    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
      133    0.000    0.000    0.000    0.000 query.py:225(<listcomp>)
       27    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
     1017    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        2    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
       30    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
        2    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
      186    0.000    0.000    0.000    0.000 state.py:45(get_current)
      656    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
      327    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       84    0.000    0.000    0.000    0.000 entity_info.py:45(update)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        1    0.000    0.000    0.000    0.000 basic_attack.py:8(use)
      332    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
      252    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       85    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
     2034    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
      327    0.000    0.000    0.000    0.000 threading.py:1052(name)
       37    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:228(update)
      371    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        3    0.000    0.000    0.000    0.000 processors.py:138(_process_player_turn_intents)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       29    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        6    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
      798    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       37    0.000    0.000    0.000    0.000 event.py:54(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       18    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      367    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF84CEC9BA0}
       68    0.000    0.000    0.000    0.000 event_core.py:12(notify)
      120    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
        2    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
        7    0.000    0.000    0.000    0.000 chrono.py:150(_get_pretty_queue)
        6    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      328    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        5    0.000    0.000    0.000    0.000 entity.py:172(create)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
      327    0.000    0.000    0.000    0.000 {built-in method time.time}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      246    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
        2    0.000    0.000    0.000    0.000 entity.py:424(consider_intervening)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
      589    0.000    0.000    0.000    0.000 sprite.py:168(update)
       30    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
      382    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        6    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        5    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
        9    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      327    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
      666    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
       40    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      100    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
        5    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      142    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        9    0.000    0.000    0.000    0.000 parser.py:96(reset)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        3    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        2    0.000    0.000    0.000    0.000 ai.py:71(act)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
      373    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
       60    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      421    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
      656    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       87    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
       18    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       22    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
        2    0.000    0.000    0.000    0.000 skill.py:258(_process_trigger_skill_effect)
       90    0.000    0.000    0.000    0.000 chrono.py:108(get_turn_holder)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
       68    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
       48    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       32    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        3    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      112    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       15    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
       68    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
       50    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        1    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       37    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
       18    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        5    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
      280    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       32    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
       41    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
      152    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
      156    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        2    0.000    0.000    0.000    0.000 entity.py:72(get_entities_and_components_in_area)
        1    0.000    0.000    0.000    0.000 main.py:215(initialise_event_handlers)
       42    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      308    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
       51    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        1    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
        5    0.000    0.000    0.000    0.000 entity.py:376(spend_time)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       51    0.000    0.000    0.000    0.000 chrono.py:115(get_turn_queue)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
      433    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 event.py:106(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       30    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        2    0.000    0.000    0.000    0.000 random.py:344(choices)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        2    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        7    0.000    0.000    0.000    0.000 chrono.py:158(_get_next_entity_in_queue)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
       18    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        8    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        4    0.000    0.000    0.000    0.000 event.py:184(__init__)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       26    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       22    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        5    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       18    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       46    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        5    0.000    0.000    0.000    0.000 event.py:88(__init__)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        8    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       58    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 entity.py:331(add_component)
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        3    0.000    0.000    0.000    0.000 event.py:63(__init__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       84    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        2    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        6    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       87    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       37    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
       22    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       40    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       25    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       37    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        8    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       28    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        3    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        4    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
       19    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        8    0.000    0.000    0.000    0.000 {built-in method math.sin}
        9    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        3    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       29    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        1    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        2    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
       54    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 event.py:29(__init__)
       64    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        2    0.000    0.000    0.000    0.000 event.py:136(__init__)
       18    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       30    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        5    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
       18    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        4    0.000    0.000    0.000    0.000 <string>:1(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        4    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       52    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 component.py:39(__init__)
        7    0.000    0.000    0.000    0.000 chrono.py:180(set_turn_queue)
        9    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        2    0.000    0.000    0.000    0.000 entity.py:122(get_combat_stats)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        3    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
       22    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
       15    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        2    0.000    0.000    0.000    0.000 event.py:77(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        9    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       14    0.000    0.000    0.000    0.000 chrono.py:129(get_time)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        8    0.000    0.000    0.000    0.000 chrono.py:166(set_turn_holder)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       15    0.000    0.000    0.000    0.000 chrono.py:122(get_time_in_round)
        5    0.000    0.000    0.000    0.000 component.py:81(__init__)
        2    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
       20    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       23    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       21    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        1    0.000    0.000    0.000    0.000 main.py:165(disable_profiling)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        8    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        2    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        2    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        5    0.000    0.000    0.000    0.000 chrono.py:99(add_time)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       25    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       24    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        4    0.000    0.000    0.000    0.000 component.py:30(__init__)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        5    0.000    0.000    0.000    0.000 chrono.py:143(get_round)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 component.py:55(__init__)
        1    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        2    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        2    0.000    0.000    0.000    0.000 component.py:183(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        3    0.000    0.000    0.000    0.000 component.py:63(__init__)
        3    0.000    0.000    0.000    0.000 component.py:117(__init__)
        3    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        2    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 component.py:132(__init__)
        5    0.000    0.000    0.000    0.000 chrono.py:136(get_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        5    0.000    0.000    0.000    0.000 chrono.py:173(set_time_in_round)
        2    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        5    0.000    0.000    0.000    0.000 chrono.py:187(set_time_of_last_turn)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        2    0.000    0.000    0.000    0.000 component.py:72(__init__)
        2    0.000    0.000    0.000    0.000 entity.py:83(<listcomp>)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        1    0.000    0.000    0.000    0.000 ai.py:68(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 component.py:91(__init__)
        2    0.000    0.000    0.000    0.000 component.py:109(__init__)
        1    0.000    0.000    0.000    0.000 component.py:175(__init__)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        3    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:100(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        1    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


