Sun Mar 22 16:52:07 2020    logs/profiling/profile.dump

         2002399 function calls (1870582 primitive calls) in 11.318 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.112    0.112   11.276   11.276 main.py:103(game_loop)
      632    7.170    0.011    7.170    0.011 {method 'tick' of 'Clock' objects}
      316    0.002    0.000    3.601    0.011 state.py:38(get_delta_time)
      316    0.001    0.000    3.571    0.011 state.py:63(update_clock)
      316    0.001    0.000    1.490    0.005 manager.py:54(update)
      316    0.087    0.000    1.489    0.005 ui_manager.py:122(update)
      316    0.004    0.000    1.472    0.005 manager.py:73(draw)
   104421    1.076    0.000    1.076    0.000 {method 'blit' of 'pygame.Surface' objects}
      316    0.050    0.000    0.910    0.003 sprite.py:453(update)
      316    0.001    0.000    0.867    0.003 event_core.py:24(update)
       31    0.000    0.000    0.843    0.027 ui_handler.py:31(process_event)
        5    0.000    0.000    0.818    0.164 ui_handler.py:201(_update_camera)
        5    0.000    0.000    0.806    0.161 manager.py:295(update_camera_grid)
        5    0.005    0.001    0.806    0.161 camera.py:105(update_grid)
      758    0.009    0.000    0.794    0.001 ui_button.py:30(__init__)
      758    0.040    0.000    0.748    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        6    0.000    0.000    0.657    0.109 ui_handler.py:44(process_entity_event)
      320    0.292    0.001    0.627    0.002 camera.py:79(update_game_map)
      315    0.002    0.000    0.621    0.002 camera.py:72(update)
    22111    0.056    0.000    0.605    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
      316    0.002    0.000    0.569    0.002 ui_manager.py:173(draw_ui)
      316    0.088    0.000    0.567    0.002 sprite.py:753(draw)
153867/22111    0.516    0.000    0.545    0.000 ui_appearance_theme.py:322(get_next_id_node)
      320    0.409    0.001    0.409    0.001 {built-in method pygame.transform.scale}
    50965    0.213    0.000    0.377    0.000 ui_element.py:121(check_hover)
    11430    0.030    0.000    0.342    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
     6882    0.013    0.000    0.201    0.000 ui_appearance_theme.py:428(get_misc_data)
    49683    0.095    0.000    0.188    0.000 ui_button.py:197(update)
       21    0.000    0.000    0.176    0.008 ui_handler.py:68(process_game_event)
        1    0.000    0.000    0.170    0.170 ui_handler.py:107(init_game_ui)
      316    0.120    0.000    0.120    0.000 {built-in method pygame.event.get}
      316    0.115    0.000    0.115    0.000 {built-in method pygame.display.flip}
    49683    0.058    0.000    0.112    0.000 ui_button.py:138(hover_point)
     3212    0.098    0.000    0.103    0.000 sprite.py:913(get_sprites_from_layer)
      758    0.005    0.000    0.093    0.000 ui_button.py:97(set_any_images_from_theme)
     3032    0.006    0.000    0.088    0.000 ui_appearance_theme.py:366(get_image)
    49683    0.028    0.000    0.074    0.000 drawable_shape.py:36(update)
    48003    0.067    0.000    0.067    0.000 camera.py:233(world_to_screen_position)
     2899    0.019    0.000    0.059    0.000 rect_drawable_shape.py:118(redraw_state)
    49683    0.048    0.000    0.055    0.000 rect_drawable_shape.py:84(collide_point)
      847    0.048    0.000    0.048    0.000 {method 'fill' of 'pygame.Surface' objects}
      758    0.006    0.000    0.045    0.000 ui_button.py:537(rebuild_shape)
   103506    0.035    0.000    0.042    0.000 sprite.py:208(alive)
        1    0.000    0.000    0.042    0.042 main.py:211(initialise_game)
      366    0.002    0.000    0.041    0.000 screen_message.py:34(update)
      767    0.003    0.000    0.040    0.000 rect_drawable_shape.py:22(__init__)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      246    0.001    0.000    0.035    0.000 ui_text_box.py:347(redraw_from_chunks)
      777    0.008    0.000    0.035    0.000 ui_element.py:23(__init__)
      767    0.011    0.000    0.035    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
      681    0.006    0.000    0.030    0.000 ui_text_box.py:205(update)
      758    0.003    0.000    0.029    0.000 ui_appearance_theme.py:405(get_font)
   386057    0.028    0.000    0.028    0.000 {method 'append' of 'list' objects}
      246    0.003    0.000    0.025    0.000 ui_text_box.py:327(redraw_from_text_block)
      767    0.004    0.000    0.021    0.000 drawable_shape.py:45(redraw_all_states)
    49683    0.019    0.000    0.019    0.000 ui_button.py:154(can_hover)
        8    0.000    0.000    0.019    0.002 ui_text_box.py:50(__init__)
        8    0.000    0.000    0.018    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
      316    0.001    0.000    0.018    0.000 processors.py:18(process_all)
     4503    0.006    0.000    0.018    0.000 _internal.py:24(wrapper)
      316    0.009    0.000    0.017    0.000 processors.py:25(_process_aesthetic_update)
       29    0.000    0.000    0.017    0.001 manager.py:60(process_ui_events)
     2935    0.017    0.000    0.017    0.000 {method 'copy' of 'pygame.Surface' objects}
        8    0.000    0.000    0.017    0.002 ui_text_box.py:110(rebuild)
       29    0.006    0.000    0.017    0.001 ui_manager.py:86(process_events)
      777    0.002    0.000    0.017    0.000 ui_container.py:42(add_element)
     2899    0.016    0.000    0.016    0.000 surface_cache.py:119(build_cache_id)
   302120    0.016    0.000    0.016    0.000 {built-in method builtins.len}
        5    0.003    0.001    0.014    0.003 ui_container.py:116(clear)
     3762    0.008    0.000    0.013    0.000 world.py:55(get_tile)
        5    0.000    0.000    0.013    0.003 message_log.py:49(add_message)
      124    0.001    0.000    0.013    0.000 ui_text_box.py:462(set_active_effect)
     1384    0.013    0.000    0.013    0.000 ui_container.py:62(recalculate_container_layer_thickness)
       27    0.000    0.000    0.012    0.000 entity_handler.py:26(process_event)
      600    0.001    0.000    0.011    0.000 ui_button.py:130(kill)
        4    0.000    0.000    0.011    0.003 ui_handler.py:151(process_ui_event)
        4    0.000    0.000    0.011    0.003 ui_handler.py:232(_process_message)
        4    0.000    0.000    0.011    0.003 manager.py:444(add_to_message_log)
      607    0.001    0.000    0.011    0.000 ui_element.py:114(kill)
      777    0.001    0.000    0.010    0.000 sprite.py:121(__init__)
        9    0.000    0.000    0.010    0.001 ui_text_box.py:310(parse_html_into_style_data)
       76    0.001    0.000    0.010    0.000 __init__.py:1496(_log)
      246    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
     2338    0.007    0.000    0.009    0.000 query.py:212(__iter__)
     4504    0.009    0.000    0.009    0.000 {built-in method _warnings.warn}
      777    0.003    0.000    0.009    0.000 sprite.py:126(add)
    53823    0.009    0.000    0.009    0.000 ui_manager.py:167(get_mouse_position)
        5    0.000    0.000    0.009    0.002 manager.py:286(update_camera_game_map)
        3    0.000    0.000    0.008    0.003 entity_handler.py:45(_process_move)
        9    0.000    0.000    0.008    0.001 text_block.py:16(__init__)
        9    0.001    0.000    0.008    0.001 text_block.py:40(redraw)
   103506    0.008    0.000    0.008    0.000 {built-in method _operator.truth}
        1    0.002    0.002    0.007    0.007 world.py:433(update_tile_visibility)
       51    0.000    0.000    0.007    0.000 __init__.py:1996(debug)
    52856    0.007    0.000    0.007    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
       51    0.000    0.000    0.007    0.000 __init__.py:1361(debug)
      777    0.002    0.000    0.007    0.000 ui_element.py:104(change_layer)
     1891    0.005    0.000    0.007    0.000 ui_container.py:124(check_hover)
       21    0.000    0.000    0.007    0.000 game_handler.py:26(process_event)
    50359    0.006    0.000    0.006    0.000 {method 'union' of 'pygame.Rect' objects}
      607    0.001    0.000    0.006    0.000 ui_container.py:52(remove_element)
        2    0.000    0.000    0.006    0.003 entity.py:339(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
      844    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
    87896    0.006    0.000    0.006    0.000 {method 'reverse' of 'list' objects}
    53980    0.006    0.000    0.006    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        2    0.000    0.000    0.006    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.006    0.003 screen_message.py:16(__init__)
      785    0.005    0.000    0.006    0.000 sprite.py:822(change_layer)
      777    0.005    0.000    0.006    0.000 sprite.py:646(add_internal)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       76    0.000    0.000    0.005    0.000 __init__.py:1521(handle)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
     2899    0.004    0.000    0.005    0.000 drawable_shape.py:122(rebuild_images_and_text)
      316    0.001    0.000    0.005    0.000 ui_appearance_theme.py:158(update_shape_cache)
       76    0.000    0.000    0.005    0.000 __init__.py:1575(callHandlers)
     3774    0.004    0.000    0.005    0.000 world.py:347(_is_tile_in_bounds)
       76    0.000    0.000    0.005    0.000 __init__.py:892(handle)
        1    0.000    0.000    0.004    0.004 ui_vertical_scroll_bar.py:22(__init__)
        2    0.000    0.000    0.004    0.002 skill.py:138(_call_skill_func)
        6    0.000    0.000    0.004    0.001 game_handler.py:81(_process_end_turn)
        6    0.000    0.000    0.004    0.001 chrono.py:47(next_turn)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:27(process_event)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:85(_process_entity_collision)
       76    0.000    0.000    0.004    0.000 __init__.py:1123(emit)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
       76    0.000    0.000    0.004    0.000 __init__.py:1022(emit)
      316    0.001    0.000    0.004    0.000 surface_cache.py:24(update)
        5    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
        5    0.001    0.000    0.004    0.001 camera.py:167(update_camera_tiles)
        2    0.000    0.000    0.004    0.002 interaction_handler.py:135(_apply_effects_to_tiles)
     1004    0.003    0.000    0.003    0.000 typing.py:806(__new__)
      316    0.002    0.000    0.003    0.000 ecs.py:265(process_pending_deletions)
     1004    0.002    0.000    0.003    0.000 query.py:170(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
       76    0.000    0.000    0.003    0.000 __init__.py:1481(makeRecord)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
        1    0.000    0.000    0.003    0.003 entity_handler.py:119(_process_use_skill)
       18    0.002    0.000    0.003    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
       24    0.000    0.000    0.003    0.000 __init__.py:1986(info)
      607    0.001    0.000    0.003    0.000 sprite.py:183(kill)
       24    0.000    0.000    0.003    0.000 __init__.py:1373(info)
       76    0.001    0.000    0.003    0.000 __init__.py:293(__init__)
      345    0.002    0.000    0.003    0.000 sprite.py:814(layers)
     1576    0.002    0.000    0.003    0.000 ui_window.py:97(update)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        1    0.000    0.000    0.003    0.003 skill.py:113(use)
      3/2    0.000    0.000    0.003    0.001 skill.py:218(process_effect)
     3148    0.003    0.000    0.003    0.000 ui_button.py:257(process_event)
       22    0.001    0.000    0.002    0.000 styled_chunk.py:8(__init__)
       14    0.000    0.000    0.002    0.000 game_handler.py:39(_process_change_game_state)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        1    0.000    0.000    0.002    0.002 skill.py:259(_process_activate_skill)
      767    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
        7    0.000    0.000    0.002    0.000 chrono.py:24(rebuild_turn_queue)
      607    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
      316    0.001    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
      632    0.002    0.000    0.002    0.000 sprite.py:745(sprites)
       76    0.000    0.000    0.002    0.000 __init__.py:869(format)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
      773    0.001    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
       76    0.000    0.000    0.002    0.000 __init__.py:606(format)
        2    0.000    0.000    0.002    0.001 __init__.py:109(import_module)
        4    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:994(_gcd_import)
      3/2    0.000    0.000    0.002    0.001 <frozen importlib._bootstrap>:978(_find_and_load)
       57    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.002    0.000 entity.py:482(take_turn)
     2899    0.002    0.000    0.002    0.000 surface_cache.py:109(find_surface_in_cache)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
        9    0.000    0.000    0.002    0.000 parser.py:104(feed)
      9/7    0.000    0.000    0.002    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
        9    0.000    0.000    0.002    0.000 parser.py:134(goahead)
      193    0.002    0.000    0.002    0.000 ui_manager.py:104(<listcomp>)
       44    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      287    0.001    0.000    0.001    0.000 ecs.py:247(delete_entity_immediately)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:793(get_code)
      286    0.001    0.000    0.001    0.000 ui_vertical_scroll_bar.py:228(update)
      315    0.001    0.000    0.001    0.000 skill_bar.py:45(update)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     1282    0.001    0.000    0.001    0.000 ui_element.py:186(hover_point)
       76    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
        2    0.000    0.000    0.001    0.001 __init__.py:133(reload)
       21    0.001    0.000    0.001    0.000 {built-in method nt.stat}
     7542    0.001    0.000    0.001    0.000 world.py:48(get_game_map)
     1654    0.001    0.000    0.001    0.000 query.py:243(<listcomp>)
      691    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.001    0.001 basic_attack.py:18(activate)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
       29    0.000    0.000    0.001    0.000 processors.py:59(process_intent)
       81    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
      845    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
      315    0.001    0.000    0.001    0.000 message_log.py:36(update)
      767    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     1429    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:663(_load_unlocked)
        2    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:610(_exec)
       76    0.001    0.000    0.001    0.000 __init__.py:1451(findCaller)
       81    0.001    0.000    0.001    0.000 ntpath.py:178(split)
       19    0.000    0.000    0.001    0.000 processors.py:140(_process_player_turn_intents)
      315    0.000    0.000    0.001    0.000 entity_info.py:47(update)
     3068    0.001    0.000    0.001    0.000 {built-in method math.floor}
       32    0.000    0.000    0.001    0.000 entity.py:43(get_player)
       76    0.001    0.000    0.001    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       76    0.000    0.000    0.001    0.000 __init__.py:539(formatTime)
        1    0.000    0.000    0.001    0.001 skill.py:413(_process_damage_effect)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:882(_find_spec)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     1004    0.001    0.000    0.001    0.000 query.py:50(__init__)
      650    0.001    0.000    0.001    0.000 state.py:45(get_current)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
        6    0.001    0.000    0.001    0.000 {built-in method builtins.compile}
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       22    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
      316    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
        4    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
      325    0.000    0.000    0.001    0.000 query.py:225(<listcomp>)
  190/189    0.000    0.000    0.001    0.000 entity.py:93(get_entitys_component)
        9    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
        9    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
     4637    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     2365    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
       77    0.000    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      798    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
       15    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
        5    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
       36    0.000    0.000    0.001    0.000 entity.py:131(get_primary_stat)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
     1320    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
     1359    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
       42    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      767    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       76    0.000    0.000    0.001    0.000 ntpath.py:201(splitext)
     2563    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
        1    0.000    0.000    0.000    0.000 entity_handler.py:142(_process_die)
     1562    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
       76    0.000    0.000    0.000    0.000 {built-in method time.strftime}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
     1552    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
     1005    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF84D989BA0}
       42    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
     2899    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
     1503    0.000    0.000    0.000    0.000 {built-in method builtins.max}
       73    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
       22    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:914(get_data)
      778    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
      162    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 skill.py:536(_calculate_to_hit_score)
     2206    0.000    0.000    0.000    0.000 sprite.py:168(update)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 skill.py:484(_calculate_damage)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
       49    0.000    0.000    0.000    0.000 entity.py:104(get_name)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
       91    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
       29    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
       45    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
     1563    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
       32    0.000    0.000    0.000    0.000 utility.py:188(value_to_member)
       22    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       76    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
     1576    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
       30    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      318    0.000    0.000    0.000    0.000 {built-in method builtins.any}
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
     2034    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
      777    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        7    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
       49    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
     1282    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
     1520    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 entity_handler.py:162(_process_want_to_use_skill)
      773    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
       35    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
       76    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 entity.py:300(create_projectile)
       76    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      152    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
       76    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        8    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       18    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
  348/330    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       76    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        7    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        6    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      777    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
       76    0.000    0.000    0.000    0.000 __init__.py:432(format)
      777    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        1    0.000    0.000    0.000    0.000 debug.py:28(log_component_not_found)
        1    0.000    0.000    0.000    0.000 skill.py:76(can_afford_cost)
        3    0.000    0.000    0.000    0.000 ai.py:68(act)
        1    0.000    0.000    0.000    0.000 skill.py:95(pay_resource_cost)
        7    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
      159    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        9    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        6    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        1    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
        1    0.000    0.000    0.000    0.000 entity.py:189(delete)
        8    0.000    0.000    0.000    0.000 world.py:268(tile_has_tag)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
        1    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
      765    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      649    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        7    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        7    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
      286    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
        7    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        7    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        4    0.000    0.000    0.000    0.000 entity.py:174(create)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
      383    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       33    0.000    0.000    0.000    0.000 event_core.py:41(publish)
      100    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        1    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
       40    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      152    0.000    0.000    0.000    0.000 __init__.py:856(release)
        4    0.000    0.000    0.000    0.000 {method 'read' of '_io.FileIO' objects}
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        4    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
       76    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       18    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
       76    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
      195    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
        6    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:147(__enter__)
        3    0.000    0.000    0.000    0.000 entity.py:73(get_entities_and_components_in_area)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:403(cached)
       76    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
       16    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
      152    0.000    0.000    0.000    0.000 __init__.py:747(filter)
       22    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       76    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
      109    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
      458    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
      607    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       76    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       76    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        1    0.000    0.000    0.000    0.000 god_handler.py:70(process_interventions)
       48    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       29    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       19    0.000    0.000    0.000    0.000 processors.py:73(_get_pressed_direction)
      432    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        6    0.000    0.000    0.000    0.000 entity_handler.py:221(_process_end_turn)
      228    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
       81    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       51    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
      264    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
        3    0.000    0.000    0.000    0.000 world.py:366(_tile_has_any_entity)
      189    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
       48    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        1    0.000    0.000    0.000    0.000 entity.py:425(consider_intervening)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       29    0.000    0.000    0.000    0.000 processors.py:120(_process_stateless_intents)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
       76    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       18    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      120    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       33    0.000    0.000    0.000    0.000 event_core.py:15(notify)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
      295    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
      155    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        2    0.000    0.000    0.000    0.000 world.py:315(tile_has_tags)
       51    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        6    0.000    0.000    0.000    0.000 entity.py:377(spend_time)
        2    0.000    0.000    0.000    0.000 ai.py:42(act)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
       28    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        9    0.000    0.000    0.000    0.000 parser.py:87(__init__)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
      149    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        1    0.000    0.000    0.000    0.000 main.py:238(initialise_event_handlers)
       76    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        3    0.000    0.000    0.000    0.000 world.py:83(get_tiles)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       42    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
        1    0.000    0.000    0.000    0.000 world.py:426(recompute_fov)
       14    0.000    0.000    0.000    0.000 event.py:90(__init__)
       51    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       33    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
        1    0.000    0.000    0.000    0.000 skill.py:246(_process_trigger_skill_effect)
       18    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       23    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
       19    0.000    0.000    0.000    0.000 processors.py:100(_get_pressed_skills_number)
      433    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        9    0.000    0.000    0.000    0.000 parser.py:96(reset)
      131    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       58    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       77    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
        4    0.000    0.000    0.000    0.000 event.py:168(__init__)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        7    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
       18    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
      164    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       76    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       76    0.000    0.000    0.000    0.000 {built-in method time.time}
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
        6    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        6    0.000    0.000    0.000    0.000 event.py:72(__init__)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       27    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        5    0.000    0.000    0.000    0.000 entity.py:332(add_component)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
        5    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
       12    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
       12    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
       22    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
      155    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 world.py:381(_tile_has_specific_entity)
       46    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       26    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
        5    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        4    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       30    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       84    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 random.py:344(choices)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       12    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        3    0.000    0.000    0.000    0.000 event.py:55(__init__)
        2    0.000    0.000    0.000    0.000 event.py:120(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       38    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       40    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 random.py:218(randint)
        5    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       22    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        1    0.000    0.000    0.000    0.000 world.py:103(get_direction)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
       38    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       38    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
       35    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        8    0.000    0.000    0.000    0.000 {built-in method math.sin}
        6    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
       37    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       28    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        8    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
       19    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
        1    0.000    0.000    0.000    0.000 random.py:174(randrange)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
       20    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        9    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        1    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       64    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       30    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       15    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
        7    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       18    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       48    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       52    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
       16    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
        1    0.000    0.000    0.000    0.000 main.py:188(disable_profiling)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
        8    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
       22    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       18    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
       12    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        9    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        2    0.000    0.000    0.000    0.000 {built-in method builtins.all}
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
       15    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        5    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        9    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       15    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        1    0.000    0.000    0.000    0.000 event.py:19(__init__)
        7    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        3    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        1    0.000    0.000    0.000    0.000 event.py:46(__init__)
        1    0.000    0.000    0.000    0.000 event.py:82(__init__)
        8    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        8    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
        6    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
       45    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       20    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       23    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        1    0.000    0.000    0.000    0.000 event.py:33(__init__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
       22    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.format}
       25    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        4    0.000    0.000    0.000    0.000 component.py:82(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
        5    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
       24    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        5    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
        3    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        8    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        6    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
       24    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:45(process_judgements)
        6    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        3    0.000    0.000    0.000    0.000 component.py:31(__init__)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        4    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        6    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        6    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 ai.py:34(__init__)
        4    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        1    0.000    0.000    0.000    0.000 skill.py:204(_get_hit_type)
        1    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        1    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        2    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        1    0.000    0.000    0.000    0.000 ui_handler.py:28(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
        4    0.000    0.000    0.000    0.000 world.py:326(<genexpr>)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        2    0.000    0.000    0.000    0.000 component.py:118(__init__)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        4    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 component.py:199(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 basic_attack.py:14(use)
        1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}


