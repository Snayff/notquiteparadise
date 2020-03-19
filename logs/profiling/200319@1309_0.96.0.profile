Thu Mar 19 13:09:50 2020    logs/profiling/profile.dump

         3549553 function calls (3470717 primitive calls) in 30.421 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.338    0.338   30.379   30.379 main.py:78(game_loop)
     1798   20.585    0.011   20.585    0.011 {method 'tick' of 'Clock' objects}
      899    0.004    0.000   10.582    0.012 state.py:63(update_clock)
      899    0.006    0.000   10.012    0.011 state.py:38(get_delta_time)
      899    0.016    0.000    4.426    0.005 manager.py:73(draw)
      899    0.004    0.000    4.164    0.005 manager.py:54(update)
      899    0.264    0.000    4.160    0.005 ui_manager.py:122(update)
   290081    3.116    0.000    3.116    0.000 {method 'blit' of 'pygame.Surface' objects}
      899    0.144    0.000    2.484    0.003 sprite.py:453(update)
      898    0.005    0.000    1.820    0.002 camera.py:72(update)
      901    0.872    0.001    1.819    0.002 camera.py:79(update_game_map)
      899    0.008    0.000    1.705    0.002 ui_manager.py:173(draw_ui)
      899    0.277    0.000    1.697    0.002 sprite.py:753(draw)
      903    1.258    0.001    1.258    0.001 {built-in method pygame.transform.scale}
   141354    0.622    0.000    1.097    0.000 ui_element.py:121(check_hover)
      899    0.001    0.000    0.560    0.001 event_core.py:21(update)
       26    0.000    0.000    0.530    0.020 ui_handler.py:30(process_event)
        3    0.000    0.000    0.508    0.169 ui_handler.py:207(update_camera)
        3    0.000    0.000    0.500    0.167 manager.py:295(update_camera_grid)
        3    0.004    0.001    0.500    0.167 camera.py:106(update_grid)
      455    0.006    0.000    0.492    0.001 ui_button.py:30(__init__)
      455    0.025    0.000    0.462    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
   139190    0.276    0.000    0.452    0.000 ui_button.py:197(update)
    13300    0.034    0.000    0.371    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
        2    0.000    0.000    0.341    0.170 ui_handler.py:48(process_entity_event)
      899    0.336    0.000    0.336    0.000 {built-in method pygame.display.flip}
92100/13300    0.317    0.000    0.335    0.000 ui_appearance_theme.py:322(get_next_id_node)
   139190    0.170    0.000    0.328    0.000 ui_button.py:138(hover_point)
     8739    0.268    0.000    0.283    0.000 sprite.py:913(get_sprites_from_layer)
      899    0.236    0.000    0.236    0.000 {built-in method pygame.event.get}
     6874    0.018    0.000    0.210    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   135154    0.199    0.000    0.199    0.000 camera.py:234(world_to_screen_position)
       21    0.000    0.000    0.181    0.009 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.176    0.176 ui_handler.py:111(init_game_ui)
   139190    0.139    0.000    0.158    0.000 rect_drawable_shape.py:84(collide_point)
     1414    0.129    0.000    0.129    0.000 {method 'fill' of 'pygame.Surface' objects}
     4144    0.008    0.000    0.123    0.000 ui_appearance_theme.py:428(get_misc_data)
   139190    0.074    0.000    0.122    0.000 drawable_shape.py:36(update)
   287199    0.102    0.000    0.122    0.000 sprite.py:208(alive)
   139190    0.057    0.000    0.057    0.000 ui_button.py:154(can_hover)
      455    0.003    0.000    0.057    0.000 ui_button.py:97(set_any_images_from_theme)
     1820    0.003    0.000    0.054    0.000 ui_appearance_theme.py:366(get_image)
     2282    0.017    0.000    0.051    0.000 rect_drawable_shape.py:118(redraw_state)
   482829    0.045    0.000    0.045    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.042    0.042 main.py:183(initialise_game)
      368    0.002    0.000    0.041    0.000 screen_message.py:34(update)
       59    0.000    0.000    0.040    0.001 manager.py:60(process_ui_events)
       59    0.014    0.000    0.039    0.001 ui_manager.py:86(process_events)
        2    0.000    0.000    0.038    0.019 entity.py:225(create_actor)
     1266    0.010    0.000    0.035    0.000 ui_text_box.py:205(update)
      246    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
      455    0.004    0.000    0.030    0.000 ui_button.py:537(rebuild_shape)
      462    0.002    0.000    0.027    0.000 rect_drawable_shape.py:22(__init__)
     6004    0.008    0.000    0.025    0.000 _internal.py:24(wrapper)
      246    0.003    0.000    0.024    0.000 ui_text_box.py:327(redraw_from_text_block)
   148009    0.024    0.000    0.024    0.000 ui_manager.py:167(get_mouse_position)
      462    0.008    0.000    0.024    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      472    0.005    0.000    0.023    0.000 ui_element.py:23(__init__)
     5389    0.016    0.000    0.022    0.000 ui_container.py:124(check_hover)
   146743    0.021    0.000    0.021    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
   141049    0.021    0.000    0.021    0.000 {method 'union' of 'pygame.Rect' objects}
       23    0.000    0.000    0.021    0.001 entity_handler.py:29(process_event)
   287199    0.020    0.000    0.020    0.000 {built-in method _operator.truth}
      455    0.002    0.000    0.018    0.000 ui_appearance_theme.py:405(get_font)
   150973    0.018    0.000    0.018    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        2    0.000    0.000    0.017    0.009 entity_handler.py:57(_process_move)
        2    0.004    0.002    0.017    0.008 world.py:445(update_tile_visibility)
   291689    0.017    0.000    0.017    0.000 {built-in method builtins.len}
      899    0.003    0.000    0.015    0.000 processors.py:16(process_all)
      120    0.001    0.000    0.015    0.000 __init__.py:1496(_log)
     2300    0.015    0.000    0.015    0.000 {method 'copy' of 'pygame.Surface' objects}
      462    0.002    0.000    0.014    0.000 drawable_shape.py:45(redraw_all_states)
     2282    0.014    0.000    0.014    0.000 surface_cache.py:119(build_cache_id)
      101    0.000    0.000    0.014    0.000 __init__.py:1996(debug)
      101    0.000    0.000    0.013    0.000 __init__.py:1361(debug)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
        7    0.000    0.000    0.013    0.002 ui_text_box.py:50(__init__)
     6005    0.012    0.000    0.012    0.000 {built-in method _warnings.warn}
        7    0.000    0.000    0.012    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     3458    0.007    0.000    0.012    0.000 world.py:55(get_tile)
      899    0.012    0.000    0.012    0.000 processors.py:23(_process_aesthetic_update)
        7    0.000    0.000    0.011    0.002 ui_text_box.py:110(rebuild)
      472    0.001    0.000    0.011    0.000 ui_container.py:42(add_element)
      958    0.007    0.000    0.010    0.000 sprite.py:814(layers)
      246    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
     4491    0.008    0.000    0.009    0.000 ui_window.py:97(update)
        7    0.000    0.000    0.009    0.001 ui_text_box.py:310(parse_html_into_style_data)
       21    0.000    0.000    0.008    0.000 game_handler.py:26(process_event)
      120    0.000    0.000    0.008    0.000 __init__.py:1521(handle)
     1798    0.007    0.000    0.007    0.000 sprite.py:745(sprites)
        3    0.001    0.000    0.007    0.002 ui_container.py:116(clear)
      778    0.007    0.000    0.007    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      899    0.005    0.000    0.007    0.000 ui_manager.py:158(update_mouse_position)
      120    0.000    0.000    0.007    0.000 __init__.py:1575(callHandlers)
        7    0.000    0.000    0.007    0.001 text_block.py:16(__init__)
        7    0.001    0.000    0.007    0.001 text_block.py:40(redraw)
      472    0.001    0.000    0.007    0.000 sprite.py:121(__init__)
      120    0.001    0.000    0.007    0.000 __init__.py:892(handle)
        4    0.000    0.000    0.006    0.002 message_log.py:49(add_message)
      120    0.000    0.000    0.006    0.000 __init__.py:1123(emit)
        2    0.000    0.000    0.006    0.003 entity.py:332(build_characteristic_sprites)
      472    0.002    0.000    0.006    0.000 sprite.py:126(add)
      899    0.003    0.000    0.006    0.000 ui_appearance_theme.py:158(update_shape_cache)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
      120    0.000    0.000    0.006    0.000 __init__.py:1022(emit)
      300    0.000    0.000    0.006    0.000 ui_button.py:130(kill)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
        3    0.000    0.000    0.006    0.002 manager.py:286(update_camera_game_map)
     7440    0.006    0.000    0.006    0.000 ui_button.py:257(process_event)
      306    0.001    0.000    0.005    0.000 ui_element.py:114(kill)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      898    0.003    0.000    0.005    0.000 skill_bar.py:45(update)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
      120    0.000    0.000    0.005    0.000 __init__.py:1481(makeRecord)
      501    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
      120    0.002    0.000    0.005    0.000 __init__.py:293(__init__)
      472    0.001    0.000    0.004    0.000 ui_element.py:104(change_layer)
        3    0.000    0.000    0.004    0.001 ui_handler.py:155(process_ui_event)
        3    0.000    0.000    0.004    0.001 ui_handler.py:238(process_message)
        3    0.000    0.000    0.004    0.001 manager.py:444(add_to_message_log)
     1916    0.004    0.000    0.004    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
     2282    0.003    0.000    0.004    0.000 drawable_shape.py:122(rebuild_images_and_text)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
     3460    0.003    0.000    0.004    0.000 world.py:347(_is_tile_in_bounds)
      898    0.002    0.000    0.004    0.000 message_log.py:36(update)
      472    0.003    0.000    0.004    0.000 sprite.py:646(add_internal)
      472    0.003    0.000    0.004    0.000 ui_manager.py:104(<listcomp>)
      480    0.003    0.000    0.004    0.000 sprite.py:822(change_layer)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
    52700    0.003    0.000    0.003    0.000 {method 'reverse' of 'list' objects}
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
      306    0.001    0.000    0.003    0.000 ui_container.py:52(remove_element)
        6    0.000    0.000    0.003    0.001 game_handler.py:81(process_end_turn)
      899    0.001    0.000    0.003    0.000 surface_cache.py:24(update)
        6    0.000    0.000    0.003    0.001 chrono.py:44(next_turn)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3300(map_is_in_fov)
      120    0.000    0.000    0.003    0.000 __init__.py:869(format)
      898    0.001    0.000    0.003    0.000 entity_info.py:45(update)
     2164    0.002    0.000    0.003    0.000 ui_element.py:186(hover_point)
      120    0.001    0.000    0.003    0.000 __init__.py:606(format)
     1817    0.003    0.000    0.003    0.000 state.py:45(get_current)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        3    0.000    0.000    0.002    0.001 manager.py:275(update_cameras_tiles)
        3    0.001    0.000    0.002    0.001 camera.py:168(update_camera_tiles)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       19    0.000    0.000    0.002    0.000 __init__.py:1986(info)
      899    0.002    0.000    0.002    0.000 {built-in method pygame.mouse.get_pos}
       14    0.000    0.000    0.002    0.000 game_handler.py:42(process_change_game_state)
       19    0.000    0.000    0.002    0.000 __init__.py:1373(info)
      120    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
     4975    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
       12    0.000    0.000    0.002    0.000 styled_chunk.py:8(__init__)
      122    0.000    0.000    0.002    0.000 ntpath.py:212(basename)
        6    0.000    0.000    0.002    0.000 chrono.py:23(rebuild_turn_queue)
      306    0.000    0.000    0.002    0.000 sprite.py:183(kill)
      122    0.001    0.000    0.002    0.000 ntpath.py:178(split)
       24    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      120    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       37    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
       15    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       16    0.001    0.000    0.001    0.000 {built-in method nt.stat}
     2282    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
      462    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
      120    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
      120    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
      468    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     6287    0.001    0.000    0.001    0.000 sprite.py:168(update)
       59    0.000    0.000    0.001    0.000 processors.py:57(process_intent)
        7    0.000    0.000    0.001    0.000 parser.py:104(feed)
        7    0.000    0.000    0.001    0.000 parser.py:134(goahead)
     6922    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      306    0.001    0.000    0.001    0.000 sprite.py:728(remove_internal)
      899    0.001    0.000    0.001    0.000 {built-in method builtins.any}
     4491    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.001    0.001    0.001    0.001 camera.py:24(__init__)
      120    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
      121    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        3    0.000    0.000    0.001    0.000 entity.py:475(take_turn)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
      462    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       47    0.000    0.000    0.001    0.000 processors.py:138(_process_player_turn_intents)
      502    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
       59    0.000    0.000    0.001    0.000 action.py:12(convert_to_intent)
      120    0.001    0.000    0.001    0.000 {built-in method time.strftime}
     1848    0.001    0.000    0.001    0.000 {built-in method math.floor}
      806    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        7    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        7    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     2164    0.001    0.000    0.001    0.000 ui_element.py:204(can_hover)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
      244    0.000    0.000    0.001    0.000 ntpath.py:44(normcase)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
     4461    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
       12    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
      525    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
      120    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
      126    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
     2282    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
     1023    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 entity.py:194(create_god)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
      462    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
     1786    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        2    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
      948    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      981    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      120    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      952    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      493    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
       22    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       41    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       28    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
      120    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      120    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
      120    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
       12    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       22    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
      240    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
      120    0.000    0.000    0.000    0.000 __init__.py:432(format)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      953    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       12    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       51    0.000    0.000    0.000    0.000 entity.py:86(get_entitys_component)
       28    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      472    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        3    0.000    0.000    0.000    0.000 entity.py:166(create)
       58    0.000    0.000    0.000    0.000 entity.py:37(get_player)
       26    0.000    0.000    0.000    0.000 entity.py:96(get_name)
      106    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
      251    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
      912    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
      240    0.000    0.000    0.000    0.000 __init__.py:856(release)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
       47    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
      120    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       34    0.000    0.000    0.000    0.000 entity.py:325(add_component)
       59    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        6    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      480    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 main.py:210(initialise_event_handlers)
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
      120    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       59    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      240    0.000    0.000    0.000    0.000 __init__.py:747(filter)
      120    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       26    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        6    0.000    0.000    0.000    0.000 chrono.py:161(_get_pretty_queue)
       34    0.000    0.000    0.000    0.000 esper.py:196(add_component)
      472    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        7    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
      120    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      120    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      360    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      470    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       26    0.000    0.000    0.000    0.000 event_core.py:38(publish)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
      616    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
      347    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
      120    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      374    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      120    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      461    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        3    0.000    0.000    0.000    0.000 ai.py:71(act)
      472    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
       60    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      242    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        6    0.000    0.000    0.000    0.000 entity_handler.py:236(_process_end_turn)
      342    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        4    0.000    0.000    0.000    0.000 world.py:260(tile_has_tag)
      122    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       26    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        2    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
      371    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       47    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
      142    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      455    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       51    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
      328    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        6    0.000    0.000    0.000    0.000 entity.py:370(spend_time)
       67    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
       12    0.000    0.000    0.000    0.000 utility.py:107(lerp)
      120    0.000    0.000    0.000    0.000 threading.py:1052(name)
       12    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       57    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
       26    0.000    0.000    0.000    0.000 event_core.py:12(notify)
       15    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       16    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
       56    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        7    0.000    0.000    0.000    0.000 parser.py:87(__init__)
       14    0.000    0.000    0.000    0.000 event.py:106(__init__)
       28    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      120    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
        6    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
      120    0.000    0.000    0.000    0.000 {built-in method time.time}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
      122    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      240    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
      120    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
      306    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       55    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        2    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
      233    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       34    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        4    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      242    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        7    0.000    0.000    0.000    0.000 parser.py:96(reset)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        2    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       29    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       12    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       26    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:169(_get_next_entity_in_queue)
       22    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        2    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
        6    0.000    0.000    0.000    0.000 event.py:88(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       51    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        2    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        8    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
      236    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 event.py:184(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       24    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       12    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        7    0.000    0.000    0.000    0.000 {built-in method math.sin}
       12    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        2    0.000    0.000    0.000    0.000 event.py:63(__init__)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       26    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       56    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        8    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
       12    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        7    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       17    0.000    0.000    0.000    0.000 chrono.py:119(get_turn_holder)
       28    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       27    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       18    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        6    0.000    0.000    0.000    0.000 chrono.py:191(set_turn_queue)
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        7    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       12    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       20    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       17    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       34    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        6    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 main.py:160(disable_profiling)
       68    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
       14    0.000    0.000    0.000    0.000 chrono.py:140(get_time)
        7    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       32    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        7    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        6    0.000    0.000    0.000    0.000 chrono.py:110(add_time)
        7    0.000    0.000    0.000    0.000 chrono.py:177(set_turn_holder)
        3    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       12    0.000    0.000    0.000    0.000 chrono.py:133(get_time_in_round)
        1    0.000    0.000    0.000    0.000 entity_handler.py:26(__init__)
       12    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       12    0.000    0.000    0.000    0.000 chrono.py:126(get_turn_queue)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 component.py:190(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
       34    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 component.py:88(__init__)
       13    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        6    0.000    0.000    0.000    0.000 chrono.py:147(get_time_of_last_turn)
       17    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        3    0.000    0.000    0.000    0.000 component.py:70(__init__)
        7    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:184(set_time_in_round)
        3    0.000    0.000    0.000    0.000 component.py:139(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:198(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 component.py:37(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        2    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 component.py:62(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        2    0.000    0.000    0.000    0.000 component.py:79(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:68(__init__)
        2    0.000    0.000    0.000    0.000 component.py:98(__init__)
        2    0.000    0.000    0.000    0.000 component.py:107(__init__)
        1    0.000    0.000    0.000    0.000 component.py:124(__init__)
        1    0.000    0.000    0.000    0.000 component.py:182(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:116(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        2    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        1    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)
        1    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


