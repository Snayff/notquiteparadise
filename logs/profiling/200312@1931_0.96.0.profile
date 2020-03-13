Thu Mar 12 19:31:35 2020    logs/profiling/profile.dump

         1155154 function calls (1102538 primitive calls) in 8.091 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.086    0.086    8.037    8.037 main.py:77(game_loop)
      462    5.241    0.011    5.241    0.011 {method 'tick' of 'Clock' objects}
      231    0.001    0.000    2.643    0.011 state.py:61(update_clock)
      231    0.001    0.000    2.600    0.011 state.py:36(get_delta_time)
      231    0.003    0.000    1.096    0.005 manager.py:73(draw)
      231    0.001    0.000    1.068    0.005 manager.py:54(update)
      231    0.063    0.000    1.067    0.005 ui_manager.py:122(update)
    74923    0.785    0.000    0.785    0.000 {method 'blit' of 'pygame.Surface' objects}
      231    0.037    0.000    0.658    0.003 sprite.py:453(update)
      232    0.215    0.001    0.458    0.002 camera.py:79(update_game_map)
      230    0.001    0.000    0.456    0.002 camera.py:72(update)
      231    0.002    0.000    0.410    0.002 ui_manager.py:173(draw_ui)
      231    0.064    0.000    0.408    0.002 sprite.py:753(draw)
      231    0.000    0.000    0.352    0.002 event_core.py:21(update)
        7    0.000    0.000    0.346    0.049 ui_handler.py:30(process_event)
        2    0.000    0.000    0.330    0.165 ui_handler.py:205(update_camera)
        2    0.000    0.000    0.325    0.163 manager.py:295(update_camera_grid)
        2    0.002    0.001    0.325    0.163 camera.py:106(update_grid)
      305    0.004    0.000    0.323    0.001 ui_button.py:30(__init__)
      235    0.308    0.001    0.308    0.001 {built-in method pygame.transform.scale}
      305    0.017    0.000    0.303    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
    36293    0.152    0.000    0.268    0.000 ui_element.py:121(check_hover)
     8890    0.022    0.000    0.242    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
61470/8890    0.206    0.000    0.218    0.000 ui_appearance_theme.py:322(get_next_id_node)
        6    0.000    0.000    0.179    0.030 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.173    0.173 ui_handler.py:111(init_game_ui)
      231    0.168    0.001    0.168    0.001 {built-in method pygame.event.get}
        1    0.000    0.000    0.167    0.167 ui_handler.py:48(process_entity_event)
     4596    0.012    0.000    0.137    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    35650    0.071    0.000    0.133    0.000 ui_button.py:197(update)
      231    0.095    0.000    0.095    0.000 {built-in method pygame.display.flip}
    35650    0.043    0.000    0.081    0.000 ui_button.py:138(hover_point)
     2766    0.005    0.000    0.080    0.000 ui_appearance_theme.py:428(get_misc_data)
     2514    0.069    0.000    0.073    0.000 sprite.py:913(get_sprites_from_layer)
        1    0.000    0.000    0.054    0.054 main.py:182(initialise_game)
    34803    0.051    0.000    0.051    0.000 camera.py:234(world_to_screen_position)
        2    0.000    0.000    0.049    0.025 entity.py:216(create_actor)
    35650    0.020    0.000    0.047    0.000 drawable_shape.py:36(update)
    35650    0.033    0.000    0.038    0.000 rect_drawable_shape.py:84(collide_point)
      305    0.002    0.000    0.037    0.000 ui_button.py:97(set_any_images_from_theme)
     1220    0.002    0.000    0.035    0.000 ui_appearance_theme.py:366(get_image)
        2    0.009    0.004    0.034    0.017 world.py:28(create_fov_map)
      492    0.033    0.000    0.033    0.000 {method 'fill' of 'pygame.Surface' objects}
     1528    0.010    0.000    0.032    0.000 rect_drawable_shape.py:118(redraw_state)
    73737    0.025    0.000    0.030    0.000 sprite.py:208(alive)
      183    0.001    0.000    0.025    0.000 screen_message.py:34(update)
      121    0.001    0.000    0.021    0.000 ui_text_box.py:347(redraw_from_chunks)
      305    0.003    0.000    0.021    0.000 ui_button.py:537(rebuild_shape)
       41    0.000    0.000    0.019    0.000 manager.py:60(process_ui_events)
       41    0.007    0.000    0.019    0.000 ui_manager.py:86(process_events)
      308    0.001    0.000    0.019    0.000 rect_drawable_shape.py:22(__init__)
      413    0.003    0.000    0.018    0.000 ui_text_box.py:205(update)
      308    0.005    0.000    0.017    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
      318    0.003    0.000    0.015    0.000 ui_element.py:23(__init__)
   193226    0.015    0.000    0.015    0.000 {method 'append' of 'list' objects}
       40    0.000    0.000    0.015    0.000 utility.py:13(get_image)
        2    0.000    0.000    0.015    0.007 entity.py:278(build_characteristic_sprites)
      121    0.002    0.000    0.015    0.000 ui_text_box.py:327(redraw_from_text_block)
     3002    0.004    0.000    0.014    0.000 _internal.py:24(wrapper)
       12    0.000    0.000    0.014    0.001 utility.py:39(get_images)
    35650    0.014    0.000    0.014    0.000 ui_button.py:154(can_hover)
       41    0.013    0.000    0.013    0.000 {built-in method pygame.imageext.load_extended}
      305    0.001    0.000    0.012    0.000 ui_appearance_theme.py:405(get_font)
     3304    0.007    0.000    0.012    0.000 world.py:57(get_tile)
     1546    0.010    0.000    0.010    0.000 {method 'copy' of 'pygame.Surface' objects}
      308    0.002    0.000    0.010    0.000 drawable_shape.py:45(redraw_all_states)
        3    0.000    0.000    0.010    0.003 ui_text_box.py:50(__init__)
        3    0.000    0.000    0.009    0.003 ui_text_box.py:492(rebuild_from_changed_theme_data)
        3    0.000    0.000    0.009    0.003 ui_text_box.py:110(rebuild)
     1528    0.008    0.000    0.008    0.000 surface_cache.py:119(build_cache_id)
        3    0.000    0.000    0.008    0.003 ui_text_box.py:310(parse_html_into_style_data)
       61    0.000    0.000    0.008    0.000 ui_text_box.py:462(set_active_effect)
   137421    0.007    0.000    0.007    0.000 {built-in method builtins.len}
        3    0.000    0.000    0.007    0.002 text_block.py:16(__init__)
        3    0.000    0.000    0.007    0.002 text_block.py:40(redraw)
      318    0.001    0.000    0.007    0.000 ui_container.py:42(add_element)
     3003    0.006    0.000    0.007    0.000 {built-in method _warnings.warn}
    38087    0.006    0.000    0.006    0.000 ui_manager.py:167(get_mouse_position)
      121    0.002    0.000    0.006    0.000 text_block.py:265(redraw_from_chunks)
        1    0.000    0.000    0.006    0.006 manager.py:223(create_screen_message)
        1    0.000    0.000    0.006    0.006 screen_message.py:16(__init__)
    37674    0.005    0.000    0.005    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
    73737    0.005    0.000    0.005    0.000 {built-in method _operator.truth}
      312    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
       38    0.000    0.000    0.005    0.000 __init__.py:1996(debug)
     1381    0.004    0.000    0.005    0.000 ui_container.py:124(check_hover)
       38    0.000    0.000    0.005    0.000 __init__.py:1361(debug)
      318    0.001    0.000    0.005    0.000 sprite.py:121(__init__)
       39    0.000    0.000    0.005    0.000 __init__.py:1496(_log)
    36142    0.005    0.000    0.005    0.000 {method 'union' of 'pygame.Rect' objects}
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
      470    0.004    0.000    0.004    0.000 ui_container.py:62(recalculate_container_layer_thickness)
        1    0.000    0.000    0.004    0.004 skill_bar.py:14(__init__)
        1    0.000    0.000    0.004    0.004 manager.py:156(init_message_log)
        1    0.000    0.000    0.004    0.004 message_log.py:18(__init__)
      318    0.001    0.000    0.004    0.000 sprite.py:126(add)
    38718    0.004    0.000    0.004    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        1    0.000    0.000    0.004    0.004 world.py:21(create_game_map)
        1    0.002    0.002    0.004    0.004 game_map.py:12(__init__)
     3305    0.003    0.000    0.004    0.000 world.py:349(_is_tile_in_bounds)
        2    0.000    0.000    0.004    0.002 manager.py:286(update_camera_game_map)
        2    0.001    0.000    0.004    0.002 ui_container.py:116(clear)
      231    0.001    0.000    0.004    0.000 processors.py:15(process_all)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        1    0.003    0.003    0.003    0.003 ui_font_dictionary.py:155(preload_font)
        1    0.000    0.000    0.003    0.003 message_log.py:49(add_message)
      318    0.001    0.000    0.003    0.000 ui_element.py:104(change_layer)
     4030    0.003    0.000    0.003    0.000 ui_button.py:257(process_event)
      150    0.000    0.000    0.003    0.000 ui_button.py:130(kill)
      152    0.000    0.000    0.003    0.000 ui_element.py:114(kill)
      231    0.003    0.000    0.003    0.000 processors.py:22(_process_aesthetic_update)
     1151    0.002    0.000    0.003    0.000 ui_window.py:97(update)
      272    0.002    0.000    0.002    0.000 sprite.py:814(layers)
     1528    0.002    0.000    0.002    0.000 drawable_shape.py:122(rebuild_images_and_text)
      318    0.002    0.000    0.002    0.000 sprite.py:646(add_internal)
       39    0.000    0.000    0.002    0.000 __init__.py:1521(handle)
      326    0.002    0.000    0.002    0.000 sprite.py:822(change_layer)
        6    0.000    0.000    0.002    0.000 game_handler.py:26(process_event)
    35180    0.002    0.000    0.002    0.000 {method 'reverse' of 'list' objects}
      231    0.001    0.000    0.002    0.000 ui_appearance_theme.py:158(update_shape_cache)
       39    0.000    0.000    0.002    0.000 __init__.py:1575(callHandlers)
       39    0.000    0.000    0.002    0.000 __init__.py:892(handle)
        7    0.000    0.000    0.002    0.000 entity_handler.py:25(process_event)
     3000    0.002    0.000    0.002    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       39    0.000    0.000    0.002    0.000 __init__.py:1123(emit)
        4    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
       39    0.000    0.000    0.002    0.000 __init__.py:1022(emit)
      260    0.002    0.000    0.002    0.000 ui_manager.py:104(<listcomp>)
      462    0.002    0.000    0.002    0.000 sprite.py:745(sprites)
       39    0.000    0.000    0.002    0.000 __init__.py:1481(makeRecord)
      231    0.001    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
      152    0.000    0.000    0.002    0.000 ui_container.py:52(remove_element)
      231    0.000    0.000    0.002    0.000 surface_cache.py:24(update)
       39    0.001    0.000    0.001    0.000 __init__.py:293(__init__)
        2    0.000    0.000    0.001    0.001 manager.py:275(update_cameras_tiles)
        2    0.000    0.000    0.001    0.001 camera.py:168(update_camera_tiles)
       27    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
      230    0.001    0.000    0.001    0.000 skill_bar.py:44(update)
        2    0.000    0.000    0.001    0.001 styled_chunk.py:8(__init__)
      308    0.000    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     6611    0.001    0.000    0.001    0.000 world.py:50(get_game_map)
      545    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
       35    0.001    0.000    0.001    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
      230    0.001    0.000    0.001    0.000 message_log.py:36(update)
      643    0.001    0.000    0.001    0.000 ui_element.py:186(hover_point)
      230    0.000    0.000    0.001    0.000 entity_info.py:45(update)
      308    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
       39    0.000    0.000    0.001    0.000 __init__.py:869(format)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:213(insert_code)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
       39    0.000    0.000    0.001    0.000 __init__.py:606(format)
     1528    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
      152    0.000    0.000    0.001    0.000 sprite.py:183(kill)
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:128(_update_label_offsets)
      314    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
       11    0.001    0.000    0.001    0.000 {method 'size' of 'pygame.font.Font' objects}
        6    0.000    0.000    0.001    0.000 map_handler.py:23(process_event)
      469    0.001    0.000    0.001    0.000 state.py:43(get_current)
       39    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
        1    0.000    0.000    0.001    0.001 game_handler.py:81(process_end_turn)
       41    0.000    0.000    0.001    0.000 ntpath.py:212(basename)
       41    0.000    0.000    0.001    0.000 processors.py:56(process_intent)
        1    0.000    0.000    0.001    0.001 chrono.py:51(next_turn)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
        4    0.000    0.000    0.001    0.000 game_handler.py:42(process_change_game_state)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       41    0.000    0.000    0.001    0.000 ntpath.py:178(split)
      152    0.000    0.000    0.001    0.000 sprite.py:728(remove_internal)
      231    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
     1232    0.000    0.000    0.000    0.000 {built-in method math.floor}
     1481    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
       39    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
      313    0.000    0.000    0.000    0.000 ui_font_dictionary.py:133(create_font_id)
       39    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
     3744    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       39    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        5    0.000    0.000    0.000    0.000 {built-in method nt.stat}
       41    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
       26    0.000    0.000    0.000    0.000 processors.py:137(_process_player_turn_intents)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      259    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
       40    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        3    0.000    0.000    0.000    0.000 parser.py:104(feed)
        3    0.000    0.000    0.000    0.000 state.py:69(set_new)
      356    0.000    0.000    0.000    0.000 ui_window_stack.py:73(get_root_window)
        3    0.000    0.000    0.000    0.000 parser.py:134(goahead)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
      494    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        1    0.000    0.000    0.000    0.000 chrono.py:23(build_new_turn_queue)
     1611    0.000    0.000    0.000    0.000 sprite.py:168(update)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        1    0.000    0.000    0.000    0.000 entity.py:187(create_god)
       20    0.000    0.000    0.000    0.000 entity.py:117(get_primary_stat)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
       39    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
       61    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       60    0.000    0.000    0.000    0.000 text_effects.py:88(update)
     1528    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
      308    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
       39    0.000    0.000    0.000    0.000 {built-in method time.strftime}
        3    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
      231    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        3    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
     1151    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_hp)
     1000    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
      644    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
      626    0.000    0.000    0.000    0.000 {built-in method builtins.min}
      619    0.000    0.000    0.000    0.000 {built-in method builtins.max}
      323    0.000    0.000    0.000    0.000 drawable_shape.py:86(get_surface)
       82    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
       45    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      643    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       39    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        3    0.000    0.000    0.000    0.000 entity.py:160(create)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      110    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        1    0.000    0.000    0.000    0.000 __init__.py:1986(info)
        1    0.000    0.000    0.000    0.000 __init__.py:1373(info)
      645    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        1    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      320    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
       25    0.000    0.000    0.000    0.000 entity.py:271(add_component)
       29    0.000    0.000    0.000    0.000 esper.py:196(add_component)
      318    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        2    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
       39    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
      612    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        1    0.000    0.000    0.000    0.000 entity_handler.py:47(process_move)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
      126    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       39    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
      326    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       39    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
      106    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       39    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       30    0.000    0.000    0.000    0.000 entity.py:34(get_player)
       26    0.000    0.000    0.000    0.000 processors.py:70(_get_pressed_direction)
      145    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       41    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       78    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
      318    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       41    0.000    0.000    0.000    0.000 processors.py:117(_process_stateless_intents)
       39    0.000    0.000    0.000    0.000 __init__.py:432(format)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        1    0.000    0.000    0.000    0.000 main.py:209(initialise_event_handlers)
       37    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
      319    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      318    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        2    0.000    0.000    0.000    0.000 world.py:262(tile_has_tag)
      307    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        3    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
      197    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       78    0.000    0.000    0.000    0.000 __init__.py:856(release)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
       39    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        2    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
       26    0.000    0.000    0.000    0.000 processors.py:97(_get_pressed_skills_number)
      305    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       39    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        2    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       39    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       61    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        3    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
       39    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        2    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       29    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
       78    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
      171    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
       39    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       60    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       10    0.000    0.000    0.000    0.000 entity.py:80(get_entitys_component)
      121    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
      117    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
       39    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      175    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
      211    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      132    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
        8    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        7    0.000    0.000    0.000    0.000 event_core.py:38(publish)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        1    0.000    0.000    0.000    0.000 world.py:361(_is_tile_blocking_movement)
      138    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       40    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       39    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       80    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       15    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        8    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       41    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       50    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
       39    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       60    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       39    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        9    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        3    0.000    0.000    0.000    0.000 entity.py:90(get_name)
        3    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        7    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
      152    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
      108    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        4    0.000    0.000    0.000    0.000 event.py:92(__init__)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 event.py:53(__init__)
        1    0.000    0.000    0.000    0.000 world.py:397(_tile_has_other_entity)
       40    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        3    0.000    0.000    0.000    0.000 entity.py:103(get_identity)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        7    0.000    0.000    0.000    0.000 event_core.py:12(notify)
       39    0.000    0.000    0.000    0.000 {built-in method time.time}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        1    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
        3    0.000    0.000    0.000    0.000 parser.py:96(reset)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
       41    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       13    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       78    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        6    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       39    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        9    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
       80    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        1    0.000    0.000    0.000    0.000 entity_handler.py:203(process_end_turn)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        7    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       58    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        2    0.000    0.000    0.000    0.000 entity.py:110(get_combat_stats)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        6    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        3    0.000    0.000    0.000    0.000 component.py:41(__init__)
       10    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       13    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        3    0.000    0.000    0.000    0.000 {built-in method math.sin}
        2    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       10    0.000    0.000    0.000    0.000 esper.py:176(has_component)
       43    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 main.py:159(disable_profiling)
        1    0.000    0.000    0.000    0.000 entity.py:316(spend_time)
        5    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
       17    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        1    0.000    0.000    0.000    0.000 event.py:84(__init__)
       19    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        1    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        3    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
       31    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        1    0.000    0.000    0.000    0.000 event.py:74(__init__)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       10    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        5    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        4    0.000    0.000    0.000    0.000 library.py:205(get_secondary_stat_data)
        3    0.000    0.000    0.000    0.000 component.py:75(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        3    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        7    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
       13    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        6    0.000    0.000    0.000    0.000 state.py:15(get_previous)
        2    0.000    0.000    0.000    0.000 component.py:164(__init__)
        5    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        3    0.000    0.000    0.000    0.000 component.py:120(__init__)
        3    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        1    0.000    0.000    0.000    0.000 entity_handler.py:22(__init__)
        3    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        6    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        5    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:21(update_globals_dict)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 chrono.py:159(set_turn_holder)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        9    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        3    0.000    0.000    0.000    0.000 chrono.py:115(get_turn_holder)
        2    0.000    0.000    0.000    0.000 component.py:32(__init__)
        2    0.000    0.000    0.000    0.000 component.py:66(__init__)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        8    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        2    0.000    0.000    0.000    0.000 component.py:85(__init__)
        1    0.000    0.000    0.000    0.000 library.py:230(get_god_data)
        1    0.000    0.000    0.000    0.000 component.py:156(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        1    0.000    0.000    0.000    0.000 chrono.py:106(add_time)
        1    0.000    0.000    0.000    0.000 chrono.py:173(set_turn_queue)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:94(__init__)
        1    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 component.py:103(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:129(get_time_in_round)
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        1    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)
        2    0.000    0.000    0.000    0.000 chrono.py:122(get_turn_queue)
        1    0.000    0.000    0.000    0.000 chrono.py:143(get_time_of_last_turn)
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF8848F9BA0}
        1    0.000    0.000    0.000    0.000 chrono.py:136(get_time)
        1    0.000    0.000    0.000    0.000 chrono.py:166(set_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:180(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


