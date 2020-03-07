Sat Feb 29 15:40:43 2020    logs/profiling/profile.dump

         996002 function calls (895506 primitive calls) in 14.119 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.057    0.057   14.084   14.084 engine.py:67(game_loop)
      173    0.001    0.000    8.426    0.049 event_hub.py:21(update)
       30    0.000    0.000    7.710    0.257 game_handler.py:25(process_event)
        9    0.000    0.000    7.709    0.857 game_handler.py:77(process_end_turn)
        9    5.657    0.629    7.708    0.856 turn_methods.py:63(next_turn)
      346    4.257    0.012    4.257    0.012 {method 'tick' of 'Clock' objects}
      173    0.001    0.000    2.770    0.016 game_manager.py:23(update)
      173    0.001    0.000    2.769    0.016 state_methods.py:66(update_clock)
       65    2.051    0.032    2.051    0.032 entity_methods.py:122(get_entitys_component)
      173    0.001    0.000    1.490    0.009 state_methods.py:50(get_delta_time)
      173    0.003    0.000    0.718    0.004 ui_manager.py:47(draw)
       40    0.000    0.000    0.646    0.016 ui_handler.py:28(process_event)
       10    0.000    0.000    0.630    0.063 ui_handler.py:205(update_camera)
       10    0.000    0.000    0.605    0.060 element_methods.py:197(update_camera_grid)
       10    0.004    0.000    0.605    0.060 camera.py:101(update_grid)
      580    0.007    0.000    0.595    0.001 ui_button.py:30(__init__)
        9    0.000    0.000    0.582    0.065 ui_handler.py:46(process_entity_event)
      580    0.031    0.000    0.563    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
      173    0.001    0.000    0.508    0.003 ui_manager.py:24(update)
      173    0.027    0.000    0.508    0.003 ui_manager.py:122(update)
    16880    0.041    0.000    0.454    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
    22647    0.414    0.000    0.414    0.000 {method 'blit' of 'pygame.Surface' objects}
117340/16880    0.388    0.000    0.410    0.000 ui_appearance_theme.py:322(get_next_id_node)
      173    0.015    0.000    0.358    0.002 sprite.py:453(update)
     8728    0.022    0.000    0.256    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
      182    0.172    0.001    0.256    0.001 camera.py:74(update_game_map)
      177    0.255    0.001    0.255    0.001 {built-in method pygame.transform.scale}
      172    0.001    0.000    0.246    0.001 camera.py:67(update)
      173    0.001    0.000    0.191    0.001 ui_manager.py:173(draw_ui)
      173    0.020    0.000    0.190    0.001 sprite.py:753(draw)
     5248    0.010    0.000    0.150    0.000 ui_appearance_theme.py:428(get_misc_data)
      173    0.091    0.001    0.091    0.001 {built-in method pygame.event.get}
     9981    0.023    0.000    0.090    0.000 ui_button.py:197(update)
    10326    0.051    0.000    0.090    0.000 ui_element.py:121(check_hover)
        9    0.000    0.000    0.075    0.008 fov_methods.py:33(recompute_player_fov)
        9    0.018    0.002    0.075    0.008 fov_methods.py:67(update_tile_visibility)
    16510    0.020    0.000    0.071    0.000 _internal.py:24(wrapper)
      580    0.004    0.000    0.070    0.000 ui_button.py:97(set_any_images_from_theme)
       39    0.000    0.000    0.069    0.002 entity_handler.py:28(process_event)
        9    0.000    0.000    0.069    0.008 entity_handler.py:50(process_move)
     2320    0.004    0.000    0.067    0.000 ui_appearance_theme.py:366(get_image)
     9981    0.012    0.000    0.063    0.000 drawable_shape.py:36(update)
      173    0.062    0.000    0.062    0.000 {built-in method pygame.display.flip}
       30    0.000    0.000    0.062    0.002 ui_handler.py:70(process_game_event)
     2904    0.021    0.000    0.062    0.000 rect_drawable_shape.py:118(redraw_state)
        1    0.000    0.000    0.056    0.056 ui_handler.py:108(init_game_ui)
    16511    0.037    0.000    0.038    0.000 {built-in method _warnings.warn}
        1    0.000    0.000    0.035    0.035 initialisers.py:16(initialise_game)
      580    0.005    0.000    0.034    0.000 ui_button.py:537(rebuild_shape)
      584    0.002    0.000    0.030    0.000 rect_drawable_shape.py:22(__init__)
     9981    0.014    0.000    0.027    0.000 ui_button.py:138(hover_point)
     1813    0.024    0.000    0.026    0.000 sprite.py:913(get_sprites_from_layer)
      584    0.008    0.000    0.026    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      195    0.024    0.000    0.024    0.000 {method 'fill' of 'pygame.Surface' objects}
      594    0.006    0.000    0.024    0.000 ui_element.py:23(__init__)
      580    0.003    0.000    0.022    0.000 ui_appearance_theme.py:405(get_font)
     2904    0.018    0.000    0.018    0.000 surface_cache.py:119(build_cache_id)
        1    0.004    0.004    0.017    0.017 fov_methods.py:19(create_player_fov_map)
     9706    0.016    0.000    0.016    0.000 camera.py:232(world_to_screen_position)
      584    0.003    0.000    0.016    0.000 drawable_shape.py:45(redraw_all_states)
   234517    0.016    0.000    0.016    0.000 {method 'append' of 'list' objects}
     2922    0.015    0.000    0.015    0.000 {method 'copy' of 'pygame.Surface' objects}
        2    0.000    0.000    0.015    0.007 entity_methods.py:272(create_actor)
       10    0.000    0.000    0.014    0.001 element_methods.py:177(update_cameras_tiles)
       10    0.002    0.000    0.014    0.001 camera.py:163(update_camera_tiles)
     9981    0.012    0.000    0.013    0.000 rect_drawable_shape.py:84(collide_point)
    15000    0.007    0.000    0.012    0.000 libtcodpy.py:3300(map_is_in_fov)
       39    0.000    0.000    0.012    0.000 ui_manager.py:30(process_ui_events)
       39    0.005    0.000    0.012    0.000 ui_manager.py:86(process_events)
       10    0.000    0.000    0.011    0.001 element_methods.py:188(update_camera_game_map)
    21513    0.009    0.000    0.010    0.000 sprite.py:208(alive)
   203542    0.010    0.000    0.010    0.000 {built-in method builtins.len}
        4    0.000    0.000    0.010    0.002 ui_text_box.py:50(__init__)
      594    0.002    0.000    0.010    0.000 ui_container.py:42(add_element)
        4    0.000    0.000    0.010    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
     1500    0.003    0.000    0.009    0.000 fov_methods.py:44(is_tile_in_fov)
       10    0.002    0.000    0.009    0.001 ui_container.py:116(clear)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:110(rebuild)
     2120    0.005    0.000    0.008    0.000 map_methods.py:49(get_tile)
      594    0.001    0.000    0.008    0.000 sprite.py:121(__init__)
        4    0.000    0.000    0.008    0.002 ui_text_box.py:310(parse_html_into_style_data)
      594    0.002    0.000    0.007    0.000 sprite.py:126(add)
        4    0.000    0.000    0.007    0.002 text_block.py:16(__init__)
        4    0.000    0.000    0.007    0.002 text_block.py:40(redraw)
      503    0.001    0.000    0.006    0.000 ui_button.py:130(kill)
      173    0.001    0.000    0.006    0.000 world_manager.py:32(update)
      506    0.001    0.000    0.006    0.000 ui_element.py:114(kill)
    15000    0.006    0.000    0.006    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
      595    0.001    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
        1    0.000    0.000    0.006    0.006 element_methods.py:356(create_screen_message)
        1    0.000    0.000    0.006    0.006 screen_message.py:18(__init__)
        2    0.000    0.000    0.006    0.003 entity_methods.py:329(build_characteristic_sprites)
     2904    0.005    0.000    0.005    0.000 drawable_shape.py:122(rebuild_images_and_text)
       40    0.000    0.000    0.005    0.000 utilities.py:13(get_image)
      594    0.001    0.000    0.005    0.000 ui_element.py:104(change_layer)
      173    0.004    0.000    0.005    0.000 entity_methods.py:478(process_aesthetic_update)
     1033    0.004    0.000    0.005    0.000 ui_container.py:124(check_hover)
       12    0.000    0.000    0.005    0.000 utilities.py:39(get_images)
     1100    0.005    0.000    0.005    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     9981    0.005    0.000    0.005    0.000 ui_button.py:154(can_hover)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
      602    0.003    0.000    0.004    0.000 sprite.py:822(change_layer)
    67110    0.004    0.000    0.004    0.000 {method 'reverse' of 'list' objects}
      594    0.004    0.000    0.004    0.000 sprite.py:646(add_internal)
        1    0.000    0.000    0.004    0.004 element_methods.py:61(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:12(__init__)
       39    0.000    0.000    0.004    0.000 input_manager.py:28(update)
        2    0.000    0.000    0.003    0.002 message_log.py:48(add_message)
        1    0.000    0.000    0.003    0.003 map_methods.py:32(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:15(__init__)
        1    0.000    0.000    0.003    0.003 element_methods.py:37(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
        1    0.003    0.003    0.003    0.003 ui_font_dictionary.py:155(preload_font)
      506    0.001    0.000    0.003    0.000 ui_container.py:52(remove_element)
     2129    0.002    0.000    0.003    0.000 map_methods.py:368(_is_tile_in_bounds)
      173    0.001    0.000    0.002    0.000 ui_appearance_theme.py:158(update_shape_cache)
      506    0.001    0.000    0.002    0.000 sprite.py:183(kill)
    11532    0.002    0.000    0.002    0.000 ui_manager.py:167(get_mouse_position)
    11359    0.002    0.000    0.002    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      212    0.001    0.000    0.002    0.000 sprite.py:814(layers)
      861    0.002    0.000    0.002    0.000 ui_window.py:97(update)
    21513    0.002    0.000    0.002    0.000 {built-in method _operator.truth}
       39    0.001    0.000    0.002    0.000 control_methods.py:176(reset_intents)
     2904    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
      173    0.002    0.000    0.002    0.000 ui_text_box.py:205(update)
      173    0.000    0.000    0.002    0.000 surface_cache.py:24(update)
     1500    0.001    0.000    0.002    0.000 libtcodpy.py:3254(map_set_properties)
      173    0.001    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
        1    0.000    0.000    0.002    0.002 ui_handler.py:152(process_ui_event)
        1    0.000    0.000    0.002    0.002 ui_handler.py:238(process_message)
        1    0.000    0.000    0.002    0.002 element_methods.py:345(add_to_message_log)
      584    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
       29    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
     1634    0.001    0.000    0.001    0.000 ui_button.py:257(process_event)
        4    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
     9821    0.001    0.000    0.001    0.000 {method 'union' of 'pygame.Rect' objects}
      506    0.001    0.000    0.001    0.000 sprite.py:728(remove_internal)
      590    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
    11759    0.001    0.000    0.001    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        8    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
        9    0.000    0.000    0.001    0.000 combat_stats.py:288(sight_range)
       45    0.001    0.000    0.001    0.000 dataclasses.py:994(fields)
      263    0.001    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
       28    0.000    0.000    0.001    0.000 control_methods.py:210(process_player_turn_intents)
     2033    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.001    0.001 element_methods.py:73(init_camera)
      172    0.000    0.000    0.001    0.000 skill_bar.py:42(update)
        1    0.001    0.001    0.001    0.001 camera.py:19(__init__)
      425    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
      279    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       65    0.001    0.000    0.001    0.000 entity_methods.py:167(get_primary_stat)
      596    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
      584    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     1500    0.001    0.000    0.001    0.000 tile.py:22(__init__)
      210    0.001    0.000    0.001    0.000 entity_methods.py:142(get_component)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      172    0.000    0.000    0.001    0.000 message_log.py:36(update)
      346    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
      191    0.000    0.000    0.001    0.000 __init__.py:1996(debug)
     2336    0.001    0.000    0.001    0.000 {built-in method math.floor}
       20    0.000    0.000    0.001    0.000 game_handler.py:41(process_change_game_state)
     4258    0.001    0.000    0.001    0.000 map_methods.py:40(get_game_map)
      172    0.000    0.000    0.001    0.000 entity_info.py:42(update)
      122    0.000    0.000    0.001    0.000 utilities.py:107(lerp)
     1125    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.001    0.001 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:35(_formatwarnmsg_impl)
        4    0.000    0.000    0.001    0.000 parser.py:104(feed)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     1363    0.001    0.000    0.001    0.000 {built-in method builtins.min}
      173    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        4    0.000    0.000    0.001    0.000 parser.py:134(goahead)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      192    0.000    0.000    0.000    0.000 entity_methods.py:148(get_components)
     1467    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
        2    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:213(insert_code)
      629    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
     2904    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:233(_insert_code)
        5    0.000    0.000    0.000    0.000 {built-in method nt.stat}
      345    0.000    0.000    0.000    0.000 ui_element.py:186(hover_point)
      584    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
       28    0.000    0.000    0.000    0.000 control_methods.py:105(get_pressed_direction)
       61    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
     1240    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     2954    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.000    0.000 __init__.py:1986(info)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 __init__.py:1373(info)
       30    0.000    0.000    0.000    0.000 map_handler.py:23(process_event)
        4    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
     1196    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      191    0.000    0.000    0.000    0.000 __init__.py:1361(debug)
        1    0.000    0.000    0.000    0.000 __init__.py:1496(_log)
       13    0.000    0.000    0.000    0.000 combat_stats.py:19(vigour)
        4    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      478    0.000    0.000    0.000    0.000 control_methods.py:170(get_intent)
       17    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
      584    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       18    0.000    0.000    0.000    0.000 map_methods.py:277(tile_has_tag)
      900    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
      124    0.000    0.000    0.000    0.000 utilities.py:121(clamp)
       39    0.000    0.000    0.000    0.000 control_methods.py:186(process_stateless_intents)
       28    0.000    0.000    0.000    0.000 control_methods.py:136(get_pressed_skills_number)
     1518    0.000    0.000    0.000    0.000 fov_methods.py:58(get_player_fov)
        2    0.000    0.000    0.000    0.000 combat_stats.py:69(max_hp)
        1    0.000    0.000    0.000    0.000 entity_methods.py:238(create_god)
      173    0.000    0.000    0.000    0.000 display_methods.py:70(get_desired_resolution)
     1197    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       13    0.000    0.000    0.000    0.000 combat_stats.py:29(clout)
     1205    0.000    0.000    0.000    0.000 sprite.py:168(update)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
       13    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
       13    0.000    0.000    0.000    0.000 combat_stats.py:39(skullduggery)
      173    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       13    0.000    0.000    0.000    0.000 combat_stats.py:59(exactitude)
        9    0.000    0.000    0.000    0.000 entity_events.py:47(__init__)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      416    0.000    0.000    0.000    0.000 state_methods.py:26(get_current)
        1    0.000    0.000    0.000    0.000 __init__.py:1521(handle)
        1    0.000    0.000    0.000    0.000 screen_message.py:36(update)
        1    0.000    0.000    0.000    0.000 __init__.py:1575(callHandlers)
        1    0.000    0.000    0.000    0.000 __init__.py:892(handle)
      594    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        4    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
      861    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        1    0.000    0.000    0.000    0.000 __init__.py:1123(emit)
        1    0.000    0.000    0.000    0.000 __init__.py:1022(emit)
        2    0.000    0.000    0.000    0.000 combat_stats.py:96(max_stamina)
     1162    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        2    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        6    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        1    0.000    0.000    0.000    0.000 ui_text_box.py:462(set_active_effect)
      829    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
      602    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        1    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 element_methods.py:49(init_entity_info)
        1    0.000    0.000    0.000    0.000 ui_text_box.py:347(redraw_from_chunks)
      557    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        9    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)
        1    0.000    0.000    0.000    0.000 entity_info.py:16(__init__)
      760    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       40    0.000    0.000    0.000    0.000 event_hub.py:38(publish)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        6    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       98    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        9    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
      267    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       12    0.000    0.000    0.000    0.000 utilities.py:51(flatten_images)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      594    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      594    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        9    0.000    0.000    0.000    0.000 element_methods.py:247(should_camera_move)
        9    0.000    0.000    0.000    0.000 map_methods.py:379(_is_tile_blocking_movement)
      390    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
      173    0.000    0.000    0.000    0.000 display_methods.py:64(get_main_surface)
        3    0.000    0.000    0.000    0.000 entity_methods.py:207(create)
        7    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
      594    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
      151    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      345    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        9    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       27    0.000    0.000    0.000    0.000 esper.py:196(add_component)
       19    0.000    0.000    0.000    0.000 state_methods.py:73(set)
      192    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      173    0.000    0.000    0.000    0.000 display_methods.py:76(get_window)
        9    0.000    0.000    0.000    0.000 god_handler.py:24(process_event)
      583    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 _internal.py:291(__init__)
        9    0.000    0.000    0.000    0.000 map_methods.py:427(_tile_has_other_entity)
        1    0.000    0.000    0.000    0.000 _internal.py:274(_get_void_ptr)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        4    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       27    0.000    0.000    0.000    0.000 entity_methods.py:38(get_player)
        7    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
      580    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 __init__.py:1011(flush)
        1    0.000    0.000    0.000    0.000 __init__.py:869(format)
        1    0.000    0.000    0.000    0.000 __init__.py:606(format)
        1    0.000    0.000    0.000    0.000 ui_text_box.py:327(redraw_from_text_block)
        1    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1481(makeRecord)
        4    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       40    0.000    0.000    0.000    0.000 event_hub.py:12(notify)
        1    0.000    0.000    0.000    0.000 __init__.py:293(__init__)
        1    0.000    0.000    0.000    0.000 turn_methods.py:37(build_new_turn_queue)
       10    0.000    0.000    0.000    0.000 element_methods.py:301(world_to_screen_position)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        9    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       10    0.000    0.000    0.000    0.000 control_methods.py:34(check_directions)
      207    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
        4    0.000    0.000    0.000    0.000 ntpath.py:212(basename)
        1    0.000    0.000    0.000    0.000 text_block.py:265(redraw_from_chunks)
        3    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
      506    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       28    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       20    0.000    0.000    0.000    0.000 game_events.py:34(__init__)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
       61    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        4    0.000    0.000    0.000    0.000 ntpath.py:178(split)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       52    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
        1    0.000    0.000    0.000    0.000 initialisers.py:46(initialise_event_handlers)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        9    0.000    0.000    0.000    0.000 entity_handler.py:189(process_end_turn)
       65    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       18    0.000    0.000    0.000    0.000 element_methods.py:133(is_target_pos_in_camera_edge)
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       12    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        9    0.000    0.000    0.000    0.000 game_events.py:16(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       10    0.000    0.000    0.000    0.000 control_methods.py:62(check_actions)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        9    0.000    0.000    0.000    0.000 element_methods.py:207(set_player_tile)
       10    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       40    0.000    0.000    0.000    0.000 event_hub.py:62(__init__)
       78    0.000    0.000    0.000    0.000 element_methods.py:101(get_ui_element)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        9    0.000    0.000    0.000    0.000 entity_methods.py:131(get_entitys_components)
       27    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        4    0.000    0.000    0.000    0.000 parser.py:87(__init__)
       10    0.000    0.000    0.000    0.000 entity_methods.py:154(get_combat_stats)
       74    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
      136    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       76    0.000    0.000    0.000    0.000 library.py:148(get_people_data)
      140    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
       39    0.000    0.000    0.000    0.000 ui_manager.py:36(handle_ui_events)
        1    0.000    0.000    0.000    0.000 _asarray.py:16(asarray)
       76    0.000    0.000    0.000    0.000 library.py:164(get_homeland_data)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       76    0.000    0.000    0.000    0.000 library.py:132(get_savvy_data)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        9    0.000    0.000    0.000    0.000 entity_methods.py:368(spend_time)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        1    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        1    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
       10    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        4    0.000    0.000    0.000    0.000 parser.py:96(reset)
        8    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        9    0.000    0.000    0.000    0.000 event_hub.py:50(subscribe)
       10    0.000    0.000    0.000    0.000 control_methods.py:87(check_dev_actions)
        1    0.000    0.000    0.000    0.000 {built-in method _ctypes.pointer}
        9    0.000    0.000    0.000    0.000 esper.py:160(components_for_entity)
        3    0.000    0.000    0.000    0.000 entity_methods.py:137(get_identity)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       13    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
        1    0.000    0.000    0.000    0.000 element_methods.py:166(move_camera)
       70    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        7    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        9    0.000    0.000    0.000    0.000 camera.py:193(set_player_tile)
        6    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       13    0.000    0.000    0.000    0.000 library.py:214(get_secondary_stat_data)
       11    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        9    0.000    0.000    0.000    0.000 event_hub.py:15(subscribe)
        1    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
       12    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method time.strftime}
        6    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       18    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        1    0.000    0.000    0.000    0.000 _internal.py:262(__array_interface__)
        1    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       10    0.000    0.000    0.000    0.000 camera.py:184(set_tiles)
       38    0.000    0.000    0.000    0.000 state_methods.py:32(get_previous)
       25    0.000    0.000    0.000    0.000 {method 'get_rect' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 {built-in method math.sin}
       10    0.000    0.000    0.000    0.000 control_methods.py:163(set_intent)
       24    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        4    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        1    0.000    0.000    0.000    0.000 camera.py:222(move_camera)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       25    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        7    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       10    0.000    0.000    0.000    0.000 combat_stats.py:16(__init__)
       84    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       17    0.000    0.000    0.000    0.000 turn_methods.py:116(get_turn_holder)
        1    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       26    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 ui_events.py:36(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:489(cast)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        3    0.000    0.000    0.000    0.000 components.py:42(__init__)
        1    0.000    0.000    0.000    0.000 debug_methods.py:90(disable_profiling)
        1    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        9    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       54    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
       29    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        4    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        4    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       11    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        1    0.000    0.000    0.000    0.000 game_events.py:26(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        7    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
       11    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 {method 'from_buffer' of '_ctypes.PyCArrayType' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        4    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        5    0.000    0.000    0.000    0.000 event_hub.py:46(__init__)
        4    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        8    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       29    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        4    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        1    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        1    0.000    0.000    0.000    0.000 game_handler.py:22(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:432(format)
        3    0.000    0.000    0.000    0.000 components.py:79(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        4    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        3    0.000    0.000    0.000    0.000 components.py:58(__init__)
        4    0.000    0.000    0.000    0.000 element_methods.py:116(add_ui_element)
        1    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        2    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        4    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       13    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       12    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        4    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        3    0.000    0.000    0.000    0.000 components.py:124(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 components.py:69(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:25(__init__)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:1052(name)
        2    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 god_handler.py:21(__init__)
        3    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:856(release)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        9    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        1    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        2    0.000    0.000    0.000    0.000 components.py:32(__init__)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        4    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 ui_handler.py:25(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        1    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        1    0.000    0.000    0.000    0.000 library.py:178(get_skill_data)
        1    0.000    0.000    0.000    0.000 library.py:239(get_god_data)
        1    0.000    0.000    0.000    0.000 _internal.py:259(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 components.py:89(__init__)
        1    0.000    0.000    0.000    0.000 components.py:160(__init__)
        1    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        1    0.000    0.000    0.000    0.000 control_methods.py:27(set_player_id)
        2    0.000    0.000    0.000    0.000 components.py:107(__init__)
        1    0.000    0.000    0.000    0.000 turn_methods.py:130(set_turn_holder)
        4    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 components.py:98(__init__)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 process.py:36(current_process)
        1    0.000    0.000    0.000    0.000 process.py:180(name)
        1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FFA3A5C9BA0}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        1    0.000    0.000    0.000    0.000 _internal.py:340(data)
        2    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        1    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}


