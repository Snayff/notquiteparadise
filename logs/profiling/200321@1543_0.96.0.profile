Sat Mar 21 15:43:33 2020    logs/profiling/profile.dump

         4169776 function calls (3956617 primitive calls) in 27.586 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.282    0.282   27.544   27.544 main.py:85(game_loop)
     1582   17.994    0.011   17.994    0.011 {method 'tick' of 'Clock' objects}
      791    0.003    0.000    9.084    0.011 state.py:63(update_clock)
      791    0.004    0.000    8.917    0.011 state.py:38(get_delta_time)
      791    0.011    0.000    3.808    0.005 manager.py:73(draw)
      791    0.003    0.000    3.704    0.005 manager.py:54(update)
      791    0.222    0.000    3.701    0.005 ui_manager.py:122(update)
   259260    2.695    0.000    2.695    0.000 {method 'blit' of 'pygame.Surface' objects}
      791    0.128    0.000    2.231    0.003 sprite.py:453(update)
      798    0.746    0.001    1.606    0.002 camera.py:79(update_game_map)
      790    0.005    0.000    1.599    0.002 camera.py:72(update)
      791    0.006    0.000    1.461    0.002 ui_manager.py:173(draw_ui)
      791    0.236    0.000    1.456    0.002 sprite.py:753(draw)
      791    0.001    0.000    1.368    0.002 event_core.py:24(update)
       44    0.000    0.000    1.336    0.030 ui_handler.py:30(process_event)
        8    0.000    0.000    1.278    0.160 ui_handler.py:202(update_camera)
        8    0.000    0.000    1.258    0.157 manager.py:295(update_camera_grid)
        8    0.008    0.001    1.258    0.157 camera.py:105(update_grid)
     1220    0.015    0.000    1.250    0.001 ui_button.py:30(__init__)
     1220    0.065    0.000    1.175    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        9    0.000    0.000    1.118    0.124 ui_handler.py:43(process_entity_event)
      795    1.098    0.001    1.098    0.001 {built-in method pygame.transform.scale}
   127346    0.542    0.000    0.968    0.000 ui_element.py:121(check_hover)
    35605    0.086    0.000    0.949    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
248685/35605    0.810    0.000    0.857    0.000 ui_appearance_theme.py:322(get_next_id_node)
    18404    0.047    0.000    0.537    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   124664    0.248    0.000    0.436    0.000 ui_button.py:197(update)
    11084    0.021    0.000    0.315    0.000 ui_appearance_theme.py:428(get_misc_data)
      791    0.295    0.000    0.295    0.000 {built-in method pygame.display.flip}
   124664    0.156    0.000    0.294    0.000 ui_button.py:138(hover_point)
      791    0.278    0.000    0.278    0.000 {built-in method pygame.event.get}
     7805    0.234    0.000    0.247    0.000 sprite.py:913(get_sprites_from_layer)
       27    0.000    0.000    0.174    0.006 ui_handler.py:67(process_game_event)
   119703    0.172    0.000    0.172    0.000 camera.py:233(world_to_screen_position)
        1    0.000    0.000    0.169    0.169 ui_handler.py:106(init_game_ui)
     1220    0.007    0.000    0.145    0.000 ui_button.py:97(set_any_images_from_theme)
   124664    0.069    0.000    0.140    0.000 drawable_shape.py:36(update)
   124664    0.122    0.000    0.138    0.000 rect_drawable_shape.py:84(collide_point)
     4880    0.009    0.000    0.138    0.000 ui_appearance_theme.py:366(get_image)
     1346    0.116    0.000    0.116    0.000 {method 'fill' of 'pygame.Surface' objects}
   258643    0.091    0.000    0.110    0.000 sprite.py:208(alive)
     4296    0.030    0.000    0.087    0.000 rect_drawable_shape.py:118(redraw_state)
     1220    0.010    0.000    0.070    0.000 ui_button.py:537(rebuild_shape)
     1237    0.004    0.000    0.062    0.000 rect_drawable_shape.py:22(__init__)
     1247    0.013    0.000    0.057    0.000 ui_element.py:23(__init__)
   726388    0.056    0.000    0.056    0.000 {method 'append' of 'list' objects}
     1237    0.017    0.000    0.054    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
   124664    0.052    0.000    0.052    0.000 ui_button.py:154(can_hover)
       12    0.000    0.000    0.051    0.004 ui_text_box.py:50(__init__)
       12    0.000    0.000    0.050    0.004 ui_text_box.py:492(rebuild_from_changed_theme_data)
       12    0.001    0.000    0.048    0.004 ui_text_box.py:110(rebuild)
     1220    0.005    0.000    0.046    0.000 ui_appearance_theme.py:405(get_font)
      791    0.003    0.000    0.045    0.000 processors.py:16(process_all)
        9    0.000    0.000    0.045    0.005 message_log.py:49(add_message)
        8    0.000    0.000    0.043    0.005 ui_handler.py:150(process_ui_event)
        8    0.000    0.000    0.043    0.005 ui_handler.py:233(process_message)
        8    0.000    0.000    0.043    0.005 manager.py:444(add_to_message_log)
      791    0.022    0.000    0.043    0.000 processors.py:23(_process_aesthetic_update)
        1    0.000    0.000    0.042    0.042 main.py:193(initialise_game)
      364    0.002    0.000    0.041    0.000 screen_message.py:34(update)
       67    0.000    0.000    0.039    0.001 manager.py:60(process_ui_events)
       67    0.015    0.000    0.039    0.001 ui_manager.py:86(process_events)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
     1154    0.011    0.000    0.037    0.000 ui_text_box.py:205(update)
      242    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
     1237    0.006    0.000    0.033    0.000 drawable_shape.py:45(redraw_all_states)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
   532683    0.028    0.000    0.028    0.000 {built-in method builtins.len}
     1247    0.003    0.000    0.027    0.000 ui_container.py:42(add_element)
      242    0.003    0.000    0.025    0.000 ui_text_box.py:327(redraw_from_text_block)
        8    0.005    0.001    0.025    0.003 ui_container.py:116(clear)
     4296    0.024    0.000    0.024    0.000 surface_cache.py:119(build_cache_id)
     5791    0.019    0.000    0.024    0.000 query.py:212(__iter__)
     4356    0.023    0.000    0.023    0.000 {method 'copy' of 'pygame.Surface' objects}
        5    0.000    0.000    0.023    0.005 ui_vertical_scroll_bar.py:22(__init__)
       17    0.000    0.000    0.022    0.001 ui_text_box.py:310(parse_html_into_style_data)
   133979    0.022    0.000    0.022    0.000 ui_manager.py:167(get_mouse_position)
     2324    0.021    0.000    0.021    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     1062    0.001    0.000    0.020    0.000 ui_button.py:130(kill)
   258643    0.019    0.000    0.019    0.000 {built-in method _operator.truth}
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
     1077    0.002    0.000    0.019    0.000 ui_element.py:114(kill)
     4741    0.013    0.000    0.019    0.000 ui_container.py:124(check_hover)
   132087    0.018    0.000    0.018    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
   126270    0.017    0.000    0.017    0.000 {method 'union' of 'pygame.Rect' objects}
     1247    0.002    0.000    0.017    0.000 sprite.py:121(__init__)
       36    0.000    0.000    0.015    0.000 entity_handler.py:26(process_event)
     1247    0.005    0.000    0.015    0.000 sprite.py:126(add)
      109    0.001    0.000    0.014    0.000 __init__.py:1496(_log)
   135371    0.014    0.000    0.014    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       17    0.000    0.000    0.014    0.001 text_block.py:16(__init__)
     4226    0.008    0.000    0.014    0.000 world.py:55(get_tile)
       17    0.003    0.000    0.014    0.001 text_block.py:40(redraw)
        8    0.000    0.000    0.014    0.002 manager.py:286(update_camera_game_map)
      122    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
      791    0.002    0.000    0.013    0.000 ui_appearance_theme.py:158(update_shape_cache)
     1247    0.003    0.000    0.011    0.000 ui_element.py:104(change_layer)
     1077    0.002    0.000    0.011    0.000 ui_container.py:52(remove_element)
      791    0.006    0.000    0.011    0.000 ecs.py:265(process_pending_deletions)
       74    0.000    0.000    0.011    0.000 __init__.py:1996(debug)
       74    0.000    0.000    0.011    0.000 __init__.py:1361(debug)
      791    0.001    0.000    0.010    0.000 surface_cache.py:24(update)
      242    0.003    0.000    0.009    0.000 text_block.py:265(redraw_from_chunks)
     4504    0.009    0.000    0.009    0.000 {built-in method _warnings.warn}
   141680    0.009    0.000    0.009    0.000 {method 'reverse' of 'list' objects}
       27    0.000    0.000    0.009    0.000 game_handler.py:26(process_event)
     1255    0.008    0.000    0.009    0.000 sprite.py:822(change_layer)
        5    0.000    0.000    0.009    0.002 entity_handler.py:45(_process_move)
     2487    0.008    0.000    0.009    0.000 typing.py:806(__new__)
     1247    0.008    0.000    0.009    0.000 sprite.py:646(add_internal)
       30    0.006    0.000    0.008    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     2487    0.006    0.000    0.008    0.000 query.py:170(__init__)
     1546    0.003    0.000    0.008    0.000 ui_font_dictionary.py:89(find_font)
     3951    0.007    0.000    0.008    0.000 ui_window.py:97(update)
        1    0.002    0.002    0.008    0.008 world.py:446(update_tile_visibility)
      109    0.000    0.000    0.008    0.000 __init__.py:1521(handle)
      858    0.005    0.000    0.007    0.000 sprite.py:814(layers)
     4296    0.006    0.000    0.007    0.000 drawable_shape.py:122(rebuild_images_and_text)
        4    0.000    0.000    0.007    0.002 interaction_handler.py:27(process_event)
        4    0.000    0.000    0.007    0.002 interaction_handler.py:85(_process_entity_collision)
      109    0.000    0.000    0.007    0.000 __init__.py:1575(callHandlers)
        4    0.000    0.000    0.007    0.002 skill.py:136(_call_skill_func)
      109    0.000    0.000    0.007    0.000 __init__.py:892(handle)
        4    0.000    0.000    0.006    0.002 interaction_handler.py:135(_apply_effects_to_tiles)
        2    0.000    0.000    0.006    0.003 entity.py:342(build_characteristic_sprites)
      109    0.000    0.000    0.006    0.000 __init__.py:1123(emit)
        8    0.000    0.000    0.006    0.001 game_handler.py:78(process_end_turn)
        8    0.000    0.000    0.006    0.001 manager.py:275(update_cameras_tiles)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
        8    0.002    0.000    0.006    0.001 camera.py:167(update_camera_tiles)
      109    0.000    0.000    0.006    0.000 __init__.py:1022(emit)
        8    0.000    0.000    0.006    0.001 chrono.py:47(next_turn)
       17    0.000    0.000    0.006    0.000 parser.py:104(feed)
     8520    0.006    0.000    0.006    0.000 ui_button.py:257(process_event)
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
       17    0.001    0.000    0.006    0.000 parser.py:134(goahead)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
     1077    0.002    0.000    0.005    0.000 sprite.py:183(kill)
     1582    0.005    0.000    0.005    0.000 sprite.py:745(sprites)
       82    0.002    0.000    0.005    0.000 styled_chunk.py:8(__init__)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      6/4    0.000    0.000    0.005    0.001 skill.py:216(process_effect)
      791    0.003    0.000    0.005    0.000 ui_manager.py:158(update_mouse_position)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
     1302    0.004    0.000    0.005    0.000 ecs.py:247(delete_entity_immediately)
      109    0.000    0.000    0.005    0.000 __init__.py:1481(makeRecord)
     4237    0.004    0.000    0.005    0.000 world.py:348(_is_tile_in_bounds)
        2    0.000    0.000    0.005    0.002 entity_handler.py:123(_process_use_skill)
       35    0.000    0.000    0.005    0.000 __init__.py:1986(info)
       35    0.000    0.000    0.005    0.000 __init__.py:1373(info)
        2    0.000    0.000    0.004    0.002 skill.py:258(_process_activate_skill)
      109    0.002    0.000    0.004    0.000 __init__.py:293(__init__)
        2    0.000    0.000    0.004    0.002 skill.py:111(use)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
      790    0.002    0.000    0.004    0.000 skill_bar.py:45(update)
      738    0.003    0.000    0.004    0.000 ui_vertical_scroll_bar.py:228(update)
      512    0.004    0.000    0.004    0.000 ui_manager.py:104(<listcomp>)
     1077    0.002    0.000    0.004    0.000 sprite.py:728(remove_internal)
     1237    0.003    0.000    0.003    0.000 drawable_shape.py:11(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
       18    0.000    0.000    0.003    0.000 game_handler.py:39(process_change_game_state)
       10    0.000    0.000    0.003    0.000 chrono.py:24(rebuild_turn_queue)
     1717    0.003    0.000    0.003    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
     4102    0.003    0.000    0.003    0.000 query.py:243(<listcomp>)
     1243    0.002    0.000    0.003    0.000 ui_element.py:68(create_valid_ids)
        4    0.000    0.000    0.003    0.001 __init__.py:133(reload)
       82    0.001    0.000    0.003    0.000 parser.py:301(parse_starttag)
      109    0.000    0.000    0.003    0.000 __init__.py:869(format)
      790    0.001    0.000    0.003    0.000 message_log.py:36(update)
     2682    0.002    0.000    0.003    0.000 ui_element.py:186(hover_point)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        6    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
     4296    0.003    0.000    0.003    0.000 surface_cache.py:109(find_surface_in_cache)
      109    0.001    0.000    0.003    0.000 __init__.py:606(format)
        8    0.000    0.000    0.003    0.000 entity.py:485(take_turn)
       17    0.000    0.000    0.003    0.000 state.py:71(set_new)
       67    0.000    0.000    0.003    0.000 processors.py:57(process_intent)
        6    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:793(get_code)
      162    0.000    0.000    0.002    0.000 html_parser.py:118(add_text)
      790    0.001    0.000    0.002    0.000 entity_info.py:45(update)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
     1606    0.002    0.000    0.002    0.000 state.py:45(get_current)
     2487    0.002    0.000    0.002    0.000 query.py:50(__init__)
      164    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
       52    0.000    0.000    0.002    0.000 processors.py:138(_process_player_turn_intents)
      143    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:610(_exec)
    13/11    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
      109    0.000    0.000    0.002    0.000 __init__.py:1011(flush)
     1547    0.002    0.000    0.002    0.000 ui_font_dictionary.py:133(create_font_id)
     2414    0.002    0.000    0.002    0.000 {method 'remove' of 'list' objects}
       69    0.001    0.000    0.002    0.000 entity.py:43(get_player)
      162    0.001    0.000    0.002    0.000 html_parser.py:123(add_indexed_style)
        4    0.000    0.000    0.002    0.000 __init__.py:109(import_module)
      5/4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:994(_gcd_import)
       35    0.002    0.000    0.002    0.000 {built-in method nt.stat}
      5/4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:978(_find_and_load)
        2    0.000    0.000    0.002    0.001 skill.py:412(_process_damage_effect)
      791    0.002    0.000    0.002    0.000 {built-in method pygame.mouse.get_pos}
       82    0.000    0.000    0.002    0.000 html_parser.py:213(handle_starttag)
     3859    0.002    0.000    0.002    0.000 {method 'pop' of 'dict' objects}
      114    0.000    0.000    0.002    0.000 ntpath.py:212(basename)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
      812    0.001    0.000    0.002    0.000 query.py:225(<listcomp>)
      109    0.001    0.000    0.002    0.000 __init__.py:1451(findCaller)
     1237    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     5206    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
     4948    0.001    0.000    0.001    0.000 {built-in method math.floor}
      114    0.001    0.000    0.001    0.000 ntpath.py:178(split)
     8472    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
      109    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
      109    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
       17    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        5    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
       82    0.000    0.000    0.001    0.000 html_parser.py:283(handle_data)
        8    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
       17    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
     2936    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
     2488    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FF84F319BA0}
        2    0.000    0.000    0.001    0.001 entity_handler.py:160(_process_die)
        1    0.000    0.000    0.001    0.001 basic_attack.py:17(activate)
        6    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
     1298    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
     5531    0.001    0.000    0.001    0.000 sprite.py:168(update)
       13    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:663(_load_unlocked)
     8554    0.001    0.000    0.001    0.000 {method 'contains' of 'pygame.Rect' objects}
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
     1237    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
       21    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
     4129    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
     3951    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
        2    0.000    0.000    0.001    0.000 skill.py:529(_calculate_to_hit_score)
      271    0.001    0.000    0.001    0.000 entity.py:93(get_entitys_component)
      109    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
     5369    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
      110    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
       47    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
     2503    0.001    0.000    0.001    0.000 {built-in method builtins.min}
     1277    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
        2    0.000    0.000    0.001    0.000 skill.py:477(_calculate_damage)
       12    0.001    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:914(get_data)
      109    0.001    0.000    0.001    0.000 {built-in method time.strftime}
     2502    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
      793    0.001    0.000    0.001    0.000 {built-in method builtins.any}
     4296    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
     2382    0.001    0.000    0.001    0.000 {built-in method builtins.max}
       67    0.000    0.000    0.001    0.000 action.py:12(convert_to_intent)
      228    0.000    0.000    0.001    0.000 ntpath.py:44(normcase)
       11    0.000    0.000    0.001    0.000 ui_text_box.py:102(kill)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
       79    0.000    0.000    0.001    0.000 entity.py:103(get_name)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
      261    0.001    0.000    0.001    0.000 {method 'size' of 'pygame.font.Font' objects}
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     2682    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
     2503    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
      124    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       55    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
     1247    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
      109    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       41    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
        2    0.000    0.000    0.000    0.000 entity.py:303(create_projectile)
        5    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
       12    0.000    0.000    0.000    0.000 world.py:261(tile_has_tag)
       49    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       79    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        7    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
     2452    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
      122    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        4    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
      207    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
      109    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       47    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      116    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
  449/413    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       10    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      738    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
      109    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      340    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      120    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      109    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       17    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
     1247    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      934    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
      168    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       10    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
        2    0.000    0.000    0.000    0.000 skill.py:74(can_afford_cost)
      218    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        2    0.000    0.000    0.000    0.000 entity.py:189(delete)
     1235    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        2    0.000    0.000    0.000    0.000 skill.py:93(pay_resource_cost)
       82    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
      109    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       11    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      109    0.000    0.000    0.000    0.000 __init__.py:432(format)
     1114    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
     1247    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        7    0.000    0.000    0.000    0.000 world.py:396(_tile_has_other_entity)
        6    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
       30    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
       50    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
       10    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
     1231    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
      162    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        9    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
       48    0.000    0.000    0.000    0.000 event_core.py:41(publish)
      218    0.000    0.000    0.000    0.000 __init__.py:856(release)
      109    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        5    0.000    0.000    0.000    0.000 world.py:360(_is_tile_blocking_movement)
       52    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        9    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        6    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
      283    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
        9    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      109    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        9    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        4    0.000    0.000    0.000    0.000 ai.py:68(act)
       30    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
      247    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        9    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       67    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
        2    0.000    0.000    0.000    0.000 god_handler.py:71(process_interventions)
       30    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
      155    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        4    0.000    0.000    0.000    0.000 ai.py:42(act)
      179    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
     1601    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       67    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
        5    0.000    0.000    0.000    0.000 entity.py:174(create)
     1077    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
      279    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        2    0.000    0.000    0.000    0.000 entity.py:428(consider_intervening)
      109    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
       80    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      603    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        5    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
      109    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
      218    0.000    0.000    0.000    0.000 __init__.py:747(filter)
      327    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
      109    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
      391    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      213    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      504    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
       24    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      363    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      269    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       17    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        8    0.000    0.000    0.000    0.000 entity_handler.py:213(_process_end_turn)
        2    0.000    0.000    0.000    0.000 skill.py:244(_process_trigger_skill_effect)
      611    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      109    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      109    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
       48    0.000    0.000    0.000    0.000 event_core.py:15(notify)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      220    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       60    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
      114    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       52    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
       16    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
      166    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
      109    0.000    0.000    0.000    0.000 threading.py:1052(name)
        2    0.000    0.000    0.000    0.000 world.py:300(tile_has_tags)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       82    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        8    0.000    0.000    0.000    0.000 entity.py:380(spend_time)
      122    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       30    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       37    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       60    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       17    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
      242    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       18    0.000    0.000    0.000    0.000 event.py:98(__init__)
       82    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       64    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
      120    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
      188    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
      236    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
      110    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       48    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
        5    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        6    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
        8    0.000    0.000    0.000    0.000 event.py:176(__init__)
      242    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        3    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        1    0.000    0.000    0.000    0.000 world.py:439(recompute_fov)
       24    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
      109    0.000    0.000    0.000    0.000 {built-in method time.time}
       31    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
      109    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       10    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
      122    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       63    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       30    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       88    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
        4    0.000    0.000    0.000    0.000 event.py:128(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
      244    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       29    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       17    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       99    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        5    0.000    0.000    0.000    0.000 event.py:63(__init__)
        6    0.000    0.000    0.000    0.000 entity.py:335(add_component)
      120    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
      220    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       47    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        2    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        2    0.000    0.000    0.000    0.000 random.py:218(randint)
        2    0.000    0.000    0.000    0.000 random.py:344(choices)
        8    0.000    0.000    0.000    0.000 event.py:80(__init__)
       12    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
       90    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
      172    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       82    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       49    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        7    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        2    0.000    0.000    0.000    0.000 random.py:174(randrange)
       12    0.000    0.000    0.000    0.000 {built-in method math.sin}
        5    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       50    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       47    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       54    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        6    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        5    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
       49    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
       18    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
       49    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        2    0.000    0.000    0.000    0.000 event.py:54(__init__)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       23    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       83    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       30    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       17    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        3    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       29    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
       10    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        6    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       17    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       54    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
        2    0.000    0.000    0.000    0.000 event.py:29(__init__)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        2    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        2    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
       22    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
       18    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        8    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        4    0.000    0.000    0.000    0.000 {built-in method builtins.format}
       30    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
        5    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
       20    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        4    0.000    0.000    0.000    0.000 <string>:1(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        9    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
       12    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       45    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       42    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
       24    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
       42    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
       11    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
       54    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        9    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        8    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       16    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
       12    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
       28    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 component.py:82(__init__)
        1    0.000    0.000    0.000    0.000 event.py:90(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 god_handler.py:46(process_judgements)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        6    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        8    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        7    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        8    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        6    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        4    0.000    0.000    0.000    0.000 component.py:31(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 skill.py:202(_get_hit_type)
        2    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
       12    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        8    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        4    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        4    0.000    0.000    0.000    0.000 component.py:56(__init__)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        3    0.000    0.000    0.000    0.000 component.py:118(__init__)
        8    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        2    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        3    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        2    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        5    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        2    0.000    0.000    0.000    0.000 component.py:199(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        2    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        4    0.000    0.000    0.000    0.000 world.py:311(<genexpr>)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        1    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        1    0.000    0.000    0.000    0.000 basic_attack.py:13(use)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        1    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)


