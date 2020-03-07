Fri Feb 28 20:03:20 2020    logs/profiling/profile.dump

         652518 function calls (634387 primitive calls) in 10.963 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.111    0.111   10.929   10.929 engine.py:67(game_loop)
      648    8.051    0.012    8.051    0.012 {method 'tick' of 'Clock' objects}
      324    0.001    0.000    5.091    0.016 game_manager.py:23(update)
      324    0.001    0.000    5.090    0.016 state_methods.py:66(update_clock)
      324    0.002    0.000    2.965    0.009 state_methods.py:50(get_delta_time)
      324    0.007    0.000    1.400    0.004 ui_manager.py:47(draw)
      324    0.001    0.000    0.912    0.003 ui_manager.py:24(update)
      324    0.054    0.000    0.910    0.003 ui_manager.py:122(update)
    40012    0.776    0.000    0.776    0.000 {method 'blit' of 'pygame.Surface' objects}
      324    0.031    0.000    0.607    0.002 sprite.py:453(update)
      329    0.521    0.002    0.521    0.002 {built-in method pygame.transform.scale}
      323    0.002    0.000    0.450    0.001 camera.py:52(update)
      325    0.327    0.001    0.450    0.001 camera.py:71(update_game_map)
      324    0.002    0.000    0.364    0.001 ui_manager.py:173(draw_ui)
      324    0.041    0.000    0.362    0.001 sprite.py:753(draw)
      324    0.192    0.001    0.192    0.001 {built-in method pygame.event.get}
    20255    0.102    0.000    0.175    0.000 ui_element.py:121(check_hover)
      324    0.000    0.000    0.158    0.000 event_hub.py:21(update)
       11    0.000    0.000    0.147    0.013 ui_handler.py:28(process_event)
      324    0.118    0.000    0.118    0.000 {built-in method pygame.display.flip}
      103    0.001    0.000    0.115    0.001 ui_button.py:30(__init__)
      103    0.006    0.000    0.108    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        2    0.000    0.000    0.107    0.053 ui_handler.py:202(update_camera)
        2    0.000    0.000    0.100    0.050 element_methods.py:226(update_camera_grid)
        2    0.001    0.000    0.100    0.050 camera.py:98(update_grid)
     3095    0.008    0.000    0.086    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
     5633    0.078    0.000    0.081    0.000 sprite.py:913(get_sprites_from_layer)
21025/3095    0.073    0.000    0.077    0.000 ui_appearance_theme.py:322(get_next_id_node)
        9    0.000    0.000    0.076    0.008 ui_handler.py:70(process_game_event)
      182    0.001    0.000    0.075    0.000 ui_manager.py:30(process_ui_events)
      182    0.027    0.000    0.074    0.000 ui_manager.py:86(process_events)
    17664    0.040    0.000    0.072    0.000 ui_button.py:197(update)
        1    0.000    0.000    0.071    0.071 ui_handler.py:108(init_game_ui)
        1    0.000    0.000    0.054    0.054 ui_handler.py:46(process_entity_event)
     1595    0.004    0.000    0.049    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    17422    0.024    0.000    0.047    0.000 ui_button.py:138(hover_point)
      734    0.045    0.000    0.045    0.000 {method 'fill' of 'pygame.Surface' objects}
        1    0.000    0.000    0.035    0.035 initialisers.py:15(initialise_game)
     1383    0.013    0.000    0.033    0.000 ui_text_box.py:205(update)
      977    0.002    0.000    0.029    0.000 ui_appearance_theme.py:428(get_misc_data)
        6    0.000    0.000    0.027    0.004 ui_text_box.py:50(__init__)
        6    0.000    0.000    0.026    0.004 ui_text_box.py:492(rebuild_from_changed_theme_data)
        6    0.000    0.000    0.025    0.004 ui_text_box.py:110(rebuild)
    14374    0.025    0.000    0.025    0.000 camera.py:196(world_to_screen_position)
    17664    0.011    0.000    0.025    0.000 drawable_shape.py:36(update)
    17596    0.020    0.000    0.023    0.000 rect_drawable_shape.py:84(collide_point)
      175    0.001    0.000    0.022    0.000 screen_message.py:36(update)
     4803    0.006    0.000    0.022    0.000 _internal.py:24(wrapper)
    41831    0.017    0.000    0.021    0.000 sprite.py:208(alive)
      121    0.000    0.000    0.018    0.000 ui_text_box.py:347(redraw_from_chunks)
      182    0.002    0.000    0.018    0.000 input_manager.py:21(update)
        1    0.000    0.000    0.018    0.018 ui_handler.py:149(process_ui_event)
        1    0.000    0.000    0.018    0.018 ui_handler.py:229(select_entity)
        1    0.000    0.000    0.018    0.018 element_methods.py:346(set_selected_entity)
        1    0.000    0.000    0.018    0.018 entity_info.py:60(show)
        1    0.004    0.004    0.017    0.017 fov_methods.py:20(create_player_fov_map)
        2    0.000    0.000    0.016    0.008 fov_methods.py:34(recompute_player_fov)
      523    0.005    0.000    0.016    0.000 rect_drawable_shape.py:118(redraw_state)
        2    0.004    0.002    0.016    0.008 fov_methods.py:68(update_tile_visibility)
        2    0.000    0.000    0.014    0.007 entity_methods.py:287(create_actor)
        8    0.000    0.000    0.014    0.002 ui_text_box.py:310(parse_html_into_style_data)
      103    0.001    0.000    0.013    0.000 ui_button.py:97(set_any_images_from_theme)
      121    0.002    0.000    0.013    0.000 ui_text_box.py:327(redraw_from_text_block)
      412    0.001    0.000    0.012    0.000 ui_appearance_theme.py:366(get_image)
     4804    0.011    0.000    0.012    0.000 {built-in method _warnings.warn}
        8    0.000    0.000    0.010    0.001 text_block.py:16(__init__)
        8    0.001    0.000    0.010    0.001 text_block.py:40(redraw)
      111    0.000    0.000    0.010    0.000 rect_drawable_shape.py:22(__init__)
        1    0.000    0.000    0.009    0.009 entity_info.py:176(create_secondary_stats_section)
   102053    0.009    0.000    0.009    0.000 {method 'append' of 'list' objects}
      111    0.002    0.000    0.009    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        1    0.000    0.000    0.009    0.009 element_methods.py:60(init_skill_bar)
      103    0.001    0.000    0.009    0.000 ui_button.py:537(rebuild_shape)
        1    0.000    0.000    0.009    0.009 skill_bar.py:12(__init__)
      182    0.003    0.000    0.009    0.000 control_methods.py:175(reset_intents)
        1    0.000    0.000    0.009    0.009 entity_handler.py:28(process_event)
        1    0.000    0.000    0.009    0.009 entity_handler.py:47(process_move)
        2    0.000    0.000    0.008    0.004 ui_vertical_scroll_bar.py:22(__init__)
    17664    0.008    0.000    0.008    0.000 ui_button.py:154(can_hover)
     1939    0.006    0.000    0.008    0.000 ui_container.py:124(check_hover)
     8802    0.007    0.000    0.007    0.000 ui_button.py:257(process_event)
     1960    0.007    0.000    0.007    0.000 ui_manager.py:104(<listcomp>)
        1    0.000    0.000    0.007    0.007 entity_info.py:140(create_primary_stats_section)
       61    0.000    0.000    0.007    0.000 ui_text_box.py:462(set_active_effect)
        1    0.000    0.000    0.007    0.007 element_methods.py:36(init_message_log)
        1    0.000    0.000    0.007    0.007 message_log.py:18(__init__)
      324    0.005    0.000    0.007    0.000 world_manager.py:33(update)
      324    0.001    0.000    0.006    0.000 ui_appearance_theme.py:158(update_shape_cache)
      590    0.004    0.000    0.006    0.000 ui_vertical_scroll_bar.py:228(update)
      170    0.002    0.000    0.006    0.000 control_methods.py:209(process_player_turn_intents)
     1599    0.004    0.000    0.006    0.000 map_methods.py:50(get_tile)
      122    0.002    0.000    0.006    0.000 ui_element.py:23(__init__)
        2    0.000    0.000    0.005    0.003 entity_methods.py:344(build_characteristic_sprites)
      571    0.005    0.000    0.005    0.000 {method 'copy' of 'pygame.Surface' objects}
       40    0.000    0.000    0.005    0.000 utilities.py:13(get_image)
      111    0.001    0.000    0.005    0.000 drawable_shape.py:45(redraw_all_states)
      324    0.001    0.000    0.005    0.000 surface_cache.py:24(update)
      188    0.004    0.000    0.005    0.000 dataclasses.py:994(fields)
      121    0.002    0.000    0.005    0.000 text_block.py:265(redraw_from_chunks)
        1    0.000    0.000    0.005    0.005 element_methods.py:388(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:18(__init__)
       12    0.000    0.000    0.005    0.000 utilities.py:39(get_images)
    23925    0.005    0.000    0.005    0.000 ui_manager.py:167(get_mouse_position)
      506    0.003    0.000    0.005    0.000 sprite.py:814(layers)
      103    0.001    0.000    0.005    0.000 ui_appearance_theme.py:405(get_font)
       41    0.004    0.000    0.004    0.000 {built-in method pygame.imageext.load_extended}
        1    0.000    0.000    0.004    0.004 message_log.py:48(add_message)
       24    0.003    0.000    0.004    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
    22221    0.004    0.000    0.004    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
        2    0.001    0.000    0.004    0.002 element_methods.py:194(update_cameras_tiles)
     1616    0.003    0.000    0.004    0.000 ui_window.py:97(update)
      242    0.000    0.000    0.004    0.000 ui_font_dictionary.py:89(find_font)
    41831    0.004    0.000    0.004    0.000 {built-in method _operator.truth}
      523    0.004    0.000    0.004    0.000 surface_cache.py:119(build_cache_id)
    53634    0.003    0.000    0.003    0.000 {built-in method builtins.len}
       35    0.001    0.000    0.003    0.000 styled_chunk.py:8(__init__)
        1    0.000    0.000    0.003    0.003 map_methods.py:33(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:15(__init__)
      324    0.002    0.000    0.003    0.000 ui_manager.py:158(update_mouse_position)
     2591    0.002    0.000    0.003    0.000 ui_element.py:186(hover_point)
      300    0.001    0.000    0.003    0.000 fov_methods.py:45(is_tile_in_fov)
       80    0.003    0.000    0.003    0.000 {method 'render' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.003    0.001 element_methods.py:217(update_camera_game_map)
     3300    0.001    0.000    0.003    0.000 libtcodpy.py:3300(map_is_in_fov)
    24037    0.003    0.000    0.003    0.000 {method 'colliderect' of 'pygame.Rect' objects}
    20211    0.003    0.000    0.003    0.000 {method 'union' of 'pygame.Rect' objects}
        8    0.000    0.000    0.002    0.000 parser.py:104(feed)
        8    0.000    0.000    0.002    0.000 parser.py:134(goahead)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
     1012    0.002    0.000    0.002    0.000 {built-in method builtins.sorted}
      523    0.001    0.000    0.002    0.000 drawable_shape.py:122(rebuild_images_and_text)
       70    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      122    0.000    0.000    0.002    0.000 ui_container.py:42(add_element)
      170    0.001    0.000    0.002    0.000 control_methods.py:104(get_pressed_direction)
      122    0.000    0.000    0.002    0.000 sprite.py:121(__init__)
     1600    0.002    0.000    0.002    0.000 map_methods.py:369(_is_tile_in_bounds)
      323    0.001    0.000    0.002    0.000 skill_bar.py:42(update)
      501    0.002    0.000    0.002    0.000 entity_methods.py:151(get_component)
        1    0.000    0.000    0.002    0.002 element_methods.py:72(init_camera)
        1    0.001    0.001    0.002    0.002 camera.py:18(__init__)
      432    0.001    0.000    0.002    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
      122    0.001    0.000    0.002    0.000 sprite.py:126(add)
3420/3255    0.001    0.000    0.002    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.002    0.002 entity_info.py:113(create_core_info_section)
     2924    0.001    0.000    0.002    0.000 control_methods.py:169(get_intent)
      648    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3254(map_set_properties)
        9    0.000    0.000    0.001    0.000 game_handler.py:26(process_event)
      170    0.001    0.000    0.001    0.000 control_methods.py:135(get_pressed_skills_number)
      122    0.000    0.000    0.001    0.000 ui_element.py:104(change_layer)
     4046    0.001    0.000    0.001    0.000 dataclasses.py:1009(<genexpr>)
      789    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
     3300    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
      323    0.001    0.000    0.001    0.000 message_log.py:36(update)
      182    0.001    0.000    0.001    0.000 control_methods.py:185(process_stateless_intents)
      122    0.001    0.000    0.001    0.000 ui_button.py:226(set_position)
       35    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
        3    0.000    0.000    0.001    0.000 __init__.py:1496(_log)
      323    0.001    0.000    0.001    0.000 entity_info.py:42(update)
      721    0.001    0.000    0.001    0.000 ui_text_box.py:379(process_event)
      130    0.001    0.000    0.001    0.000 sprite.py:822(change_layer)
       85    0.001    0.000    0.001    0.000 entity_methods.py:176(get_primary_stat)
        6    0.000    0.000    0.001    0.000 game_handler.py:48(process_change_game_state)
      290    0.001    0.000    0.001    0.000 ui_vertical_scroll_bar.py:195(process_event)
      175    0.000    0.000    0.001    0.000 entity_methods.py:41(get_player)
      122    0.001    0.000    0.001    0.000 sprite.py:646(add_internal)
      324    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
        1    0.000    0.000    0.001    0.001 __init__.py:1986(info)
     3824    0.001    0.000    0.001    0.000 {built-in method builtins.setattr}
        1    0.000    0.000    0.001    0.001 __init__.py:1373(info)
       69    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
      111    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
      327    0.001    0.000    0.001    0.000 entity_methods.py:157(get_components)
        7    0.001    0.000    0.001    0.000 {built-in method nt.stat}
        6    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
     1500    0.001    0.000    0.001    0.000 tile.py:22(__init__)
    11874    0.001    0.000    0.001    0.000 {method 'reverse' of 'list' objects}
        8    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
      122    0.001    0.000    0.001    0.000 ui_button.py:381(in_hold_range)
        2    0.000    0.000    0.001    0.000 ui_container.py:116(clear)
      114    0.001    0.000    0.001    0.000 {method 'size' of 'pygame.font.Font' objects}
        8    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        3    0.000    0.000    0.001    0.000 __init__.py:1521(handle)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       69    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
        3    0.000    0.000    0.001    0.000 __init__.py:1575(callHandlers)
     1749    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
       35    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
        3    0.000    0.000    0.001    0.000 __init__.py:892(handle)
        3    0.000    0.000    0.001    0.000 __init__.py:1123(emit)
      167    0.001    0.000    0.001    0.000 ui_container.py:62(recalculate_container_layer_thickness)
       45    0.000    0.000    0.001    0.000 ui_element.py:114(kill)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        5    0.000    0.000    0.001    0.000 ui_container.py:19(__init__)
      836    0.001    0.000    0.001    0.000 ui_window.py:55(process_event)
       43    0.000    0.000    0.001    0.000 ui_button.py:130(kill)
        3    0.000    0.000    0.001    0.000 __init__.py:1022(emit)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      841    0.000    0.000    0.000    0.000 state_methods.py:26(get_current)
     2591    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
       35    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
     2557    0.000    0.000    0.000    0.000 sprite.py:168(update)
     3201    0.000    0.000    0.000    0.000 map_methods.py:41(get_game_map)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
      324    0.000    0.000    0.000    0.000 {built-in method builtins.any}
      295    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
      122    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        7    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        3    0.000    0.000    0.000    0.000 combat_stats.py:288(sight_range)
       24    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
     4880    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
     1311    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
      523    0.000    0.000    0.000    0.000 surface_cache.py:109(find_surface_in_cache)
       46    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       17    0.000    0.000    0.000    0.000 combat_stats.py:19(vigour)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
      111    0.000    0.000    0.000    0.000 drawable_shape.py:11(__init__)
     1616    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        3    0.000    0.000    0.000    0.000 combat_stats.py:69(max_hp)
       45    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        2    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
        7    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        2    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
      243    0.000    0.000    0.000    0.000 ui_font_dictionary.py:133(create_font_id)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        1    0.000    0.000    0.000    0.000 element_methods.py:48(init_entity_info)
      118    0.000    0.000    0.000    0.000 ui_element.py:68(create_valid_ids)
        3    0.000    0.000    0.000    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.000    0.000 entity_info.py:16(__init__)
       17    0.000    0.000    0.000    0.000 combat_stats.py:29(clout)
       17    0.000    0.000    0.000    0.000 combat_stats.py:39(skullduggery)
        3    0.000    0.000    0.000    0.000 __init__.py:293(__init__)
        3    0.000    0.000    0.000    0.000 combat_stats.py:96(max_stamina)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       17    0.000    0.000    0.000    0.000 combat_stats.py:59(exactitude)
       17    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
      698    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
      324    0.000    0.000    0.000    0.000 display_methods.py:70(get_desired_resolution)
        1    0.000    0.000    0.000    0.000 entity_methods.py:253(create_god)
       46    0.000    0.000    0.000    0.000 __init__.py:1996(debug)
        4    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      122    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        3    0.000    0.000    0.000    0.000 __init__.py:1011(flush)
     1947    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
      369    0.000    0.000    0.000    0.000 {built-in method builtins.min}
       45    0.000    0.000    0.000    0.000 sprite.py:183(kill)
        6    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       61    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       45    0.000    0.000    0.000    0.000 ui_container.py:52(remove_element)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      411    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        3    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
      590    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
      115    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        3    0.000    0.000    0.000    0.000 __init__.py:869(format)
      324    0.000    0.000    0.000    0.000 display_methods.py:79(get_window)
      444    0.000    0.000    0.000    0.000 {built-in method math.floor}
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        6    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        3    0.000    0.000    0.000    0.000 __init__.py:606(format)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        1    0.000    0.000    0.000    0.000 map.py:66(__init__)
       60    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      182    0.000    0.000    0.000    0.000 ui_manager.py:36(handle_ui_events)
        8    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
      324    0.000    0.000    0.000    0.000 display_methods.py:61(get_main_surface)
        2    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      290    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        6    0.000    0.000    0.000    0.000 ntpath.py:212(basename)
       51    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       24    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       46    0.000    0.000    0.000    0.000 __init__.py:1361(debug)
       45    0.000    0.000    0.000    0.000 sprite.py:728(remove_internal)
      510    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       12    0.000    0.000    0.000    0.000 utilities.py:51(flatten_images)
        2    0.000    0.000    0.000    0.000 game_handler.py:83(process_end_turn)
      147    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        6    0.000    0.000    0.000    0.000 ntpath.py:178(split)
        9    0.000    0.000    0.000    0.000 map_handler.py:23(process_event)
      222    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.000    0.000 _internal.py:291(__init__)
      151    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
        1    0.000    0.000    0.000    0.000 _internal.py:274(_get_void_ptr)
        1    0.000    0.000    0.000    0.000 combat_stats.py:124(accuracy)
        3    0.000    0.000    0.000    0.000 entity_methods.py:223(create)
       35    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       72    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       27    0.000    0.000    0.000    0.000 esper.py:196(add_component)
      111    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      523    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
        1    0.000    0.000    0.000    0.000 combat_stats.py:151(resist_burn)
        1    0.000    0.000    0.000    0.000 combat_stats.py:207(resist_chemical)
        1    0.000    0.000    0.000    0.000 combat_stats.py:234(resist_astral)
        1    0.000    0.000    0.000    0.000 combat_stats.py:330(rush)
        1    0.000    0.000    0.000    0.000 combat_stats.py:179(resist_cold)
        1    0.000    0.000    0.000    0.000 combat_stats.py:261(resist_mundane)
       49    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      126    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 entity_info.py:92(create_entity_image_section)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        3    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
      252    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
        1    0.000    0.000    0.000    0.000 entity_methods.py:497(refresh_aesthetic_screen_position)
        2    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       24    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
       14    0.000    0.000    0.000    0.000 utilities.py:107(lerp)
      304    0.000    0.000    0.000    0.000 fov_methods.py:59(get_player_fov)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        3    0.000    0.000    0.000    0.000 esper.py:270(get_component)
      253    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       69    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
       12    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       12    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        8    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
      687    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       77    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
      198    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        2    0.000    0.000    0.000    0.000 map_methods.py:278(tile_has_tag)
      122    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       17    0.000    0.000    0.000    0.000 entity_methods.py:131(get_entitys_component)
        2    0.000    0.000    0.000    0.000 turn_manager.py:54(end_turn)
       15    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        3    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
       61    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        1    0.000    0.000    0.000    0.000 initialisers.py:43(initialise_event_handlers)
        7    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       11    0.000    0.000    0.000    0.000 event_hub.py:38(publish)
       12    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        3    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
      130    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 parser.py:96(reset)
      212    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        2    0.000    0.000    0.000    0.000 turn_manager.py:75(next_turn)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       24    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        3    0.000    0.000    0.000    0.000 {built-in method time.strftime}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
      121    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        1    0.000    0.000    0.000    0.000 map_methods.py:380(_is_tile_blocking_movement)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
      122    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       14    0.000    0.000    0.000    0.000 utilities.py:121(clamp)
        3    0.000    0.000    0.000    0.000 element_methods.py:330(world_to_screen_position)
        2    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)
       35    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
      117    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        3    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
      122    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        6    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       68    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
       27    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
       24    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       60    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 _asarray.py:16(asarray)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       71    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        5    0.000    0.000    0.000    0.000 state_methods.py:73(set)
        3    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
       90    0.000    0.000    0.000    0.000 library.py:148(get_people_data)
       51    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      153    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       11    0.000    0.000    0.000    0.000 event_hub.py:12(notify)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       90    0.000    0.000    0.000    0.000 library.py:164(get_homeland_data)
       90    0.000    0.000    0.000    0.000 library.py:132(get_savvy_data)
      104    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
      108    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       35    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
      119    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 control_methods.py:33(check_directions)
        3    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
        1    0.000    0.000    0.000    0.000 camera.py:59(handle_events)
        3    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        9    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
        3    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        6    0.000    0.000    0.000    0.000 game_events.py:32(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       60    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        1    0.000    0.000    0.000    0.000 entity_methods.py:97(get_entities_and_components_in_area)
       53    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        8    0.000    0.000    0.000    0.000 event_hub.py:50(subscribe)
        2    0.000    0.000    0.000    0.000 utilities.py:94(get_class_members)
        1    0.000    0.000    0.000    0.000 {built-in method _ctypes.pointer}
        3    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        2    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        5    0.000    0.000    0.000    0.000 ui_button.py:340(select)
       45    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      103    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 element_methods.py:276(should_camera_move)
        6    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 game_events.py:14(__init__)
       38    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
       15    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        6    0.000    0.000    0.000    0.000 {built-in method math.sin}
        1    0.000    0.000    0.000    0.000 god_handler.py:24(process_event)
        8    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        6    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        3    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
        5    0.000    0.000    0.000    0.000 entity_methods.py:163(get_combat_stats)
       11    0.000    0.000    0.000    0.000 event_hub.py:62(__init__)
        4    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
       42    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:432(format)
       24    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        3    0.000    0.000    0.000    0.000 control_methods.py:61(check_actions)
      104    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       25    0.000    0.000    0.000    0.000 {method 'get_rect' of 'pygame.Surface' objects}
        3    0.000    0.000    0.000    0.000 entity_methods.py:140(get_entitys_components)
        2    0.000    0.000    0.000    0.000 entity_methods.py:383(spend_time)
       39    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        6    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 _internal.py:262(__array_interface__)
       74    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 map_methods.py:428(_tile_has_other_entity)
        8    0.000    0.000    0.000    0.000 event_hub.py:15(subscribe)
       13    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        3    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       39    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       16    0.000    0.000    0.000    0.000 library.py:214(get_secondary_stat_data)
        1    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       14    0.000    0.000    0.000    0.000 element_methods.py:100(get_ui_element)
        6    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
       35    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       19    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        8    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       30    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        9    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       17    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        2    0.000    0.000    0.000    0.000 entity_methods.py:146(get_identity)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        6    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        7    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 debug_methods.py:88(disable_profiling)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
       45    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:489(cast)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        2    0.000    0.000    0.000    0.000 ui_button.py:348(unselect)
        3    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        6    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 entity_events.py:43(__init__)
        9    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        6    0.000    0.000    0.000    0.000 __init__.py:856(release)
        3    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
        8    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       15    0.000    0.000    0.000    0.000 {method 'title' of 'str' objects}
       36    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        3    0.000    0.000    0.000    0.000 esper.py:160(components_for_entity)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        3    0.000    0.000    0.000    0.000 components.py:38(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 element_methods.py:139(is_target_pos_in_camera_edge)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        4    0.000    0.000    0.000    0.000 element_methods.py:115(add_ui_element)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 ui_events.py:26(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       54    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 element_methods.py:236(set_player_tile)
        3    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 game_events.py:24(__init__)
        3    0.000    0.000    0.000    0.000 control_methods.py:86(check_dev_actions)
        1    0.000    0.000    0.000    0.000 {method 'capitalize' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'from_buffer' of '_ctypes.PyCArrayType' objects}
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
       27    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        5    0.000    0.000    0.000    0.000 combat_stats.py:16(__init__)
        6    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        5    0.000    0.000    0.000    0.000 event_hub.py:46(__init__)
        6    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        9    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        3    0.000    0.000    0.000    0.000 process.py:180(name)
        3    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        3    0.000    0.000    0.000    0.000 components.py:75(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       10    0.000    0.000    0.000    0.000 state_methods.py:32(get_previous)
        6    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        3    0.000    0.000    0.000    0.000 components.py:54(__init__)
        2    0.000    0.000    0.000    0.000 camera.py:160(set_tiles)
        1    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        3    0.000    0.000    0.000    0.000 {built-in method time.time}
       12    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)
        6    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        3    0.000    0.000    0.000    0.000 process.py:36(current_process)
        2    0.000    0.000    0.000    0.000 control_methods.py:162(set_intent)
        2    0.000    0.000    0.000    0.000 components.py:28(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:25(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:25(__init__)
        3    0.000    0.000    0.000    0.000 components.py:120(__init__)
       11    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.post}
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        2    0.000    0.000    0.000    0.000 components.py:65(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:21(__init__)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 components.py:85(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 entity_info.py:74(cleanse)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        1    0.000    0.000    0.000    0.000 library.py:239(get_god_data)
        2    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        2    0.000    0.000    0.000    0.000 components.py:103(__init__)
        1    0.000    0.000    0.000    0.000 components.py:156(__init__)
        1    0.000    0.000    0.000    0.000 _internal.py:259(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.Event}
        2    0.000    0.000    0.000    0.000 components.py:94(__init__)
        1    0.000    0.000    0.000    0.000 entity_info.py:54(set_entity)
        1    0.000    0.000    0.000    0.000 camera.py:169(set_player_tile)
        1    0.000    0.000    0.000    0.000 _internal.py:340(data)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 element_methods.py:109(get_ui_elements)
        1    0.000    0.000    0.000    0.000 entity_info.py:48(handle_events)
        1    0.000    0.000    0.000    0.000 message_log.py:42(handle_events)
        1    0.000    0.000    0.000    0.000 skill_bar.py:48(handle_events)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}


