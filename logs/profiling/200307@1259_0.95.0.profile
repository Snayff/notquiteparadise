Sat Mar  7 12:59:16 2020    logs/profiling/profile.dump

         1287481 function calls (1130435 primitive calls) in 3.098 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.021    0.021    3.057    3.057 main.py:77(game_loop)
      126    1.336    0.011    1.336    0.011 {method 'tick' of 'Clock' objects}
       63    0.000    0.000    1.021    0.016 event_core.py:21(update)
       12    0.000    0.000    1.020    0.085 ui_handler.py:30(process_event)
        6    0.000    0.000    1.006    0.168 ui_handler.py:205(update_camera)
        6    0.000    0.000    0.990    0.165 manager.py:295(update_camera_grid)
        6    0.006    0.001    0.990    0.165 camera.py:106(update_grid)
      905    0.012    0.000    0.970    0.001 ui_button.py:30(__init__)
      905    0.050    0.000    0.913    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
        5    0.000    0.000    0.846    0.169 ui_handler.py:48(process_entity_event)
    26305    0.068    0.000    0.737    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
       63    0.000    0.000    0.728    0.012 state.py:36(get_delta_time)
183315/26305    0.630    0.000    0.665    0.000 ui_appearance_theme.py:322(get_next_id_node)
       63    0.000    0.000    0.608    0.010 state.py:61(update_clock)
    13603    0.036    0.000    0.417    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
       63    0.000    0.000    0.336    0.005 manager.py:54(update)
       63    0.016    0.000    0.336    0.005 ui_manager.py:122(update)
       63    0.001    0.000    0.277    0.004 manager.py:73(draw)
     8173    0.016    0.000    0.244    0.000 ui_appearance_theme.py:428(get_misc_data)
       63    0.011    0.000    0.230    0.004 sprite.py:453(update)
    21124    0.202    0.000    0.202    0.000 {method 'blit' of 'pygame.Surface' objects}
        6    0.000    0.000    0.172    0.029 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.167    0.167 ui_handler.py:111(init_game_ui)
       68    0.051    0.001    0.120    0.002 camera.py:79(update_game_map)
      905    0.006    0.000    0.114    0.000 ui_button.py:97(set_any_images_from_theme)
       62    0.000    0.000    0.110    0.002 camera.py:72(update)
     3620    0.007    0.000    0.108    0.000 ui_appearance_theme.py:366(get_image)
     9610    0.020    0.000    0.108    0.000 ui_button.py:197(update)
       63    0.000    0.000    0.104    0.002 ui_manager.py:173(draw_ui)
       63    0.017    0.000    0.104    0.002 sprite.py:753(draw)
     4529    0.030    0.000    0.088    0.000 rect_drawable_shape.py:118(redraw_state)
     9610    0.014    0.000    0.084    0.000 drawable_shape.py:36(update)
       67    0.077    0.001    0.077    0.001 {built-in method pygame.transform.scale}
     9796    0.038    0.000    0.069    0.000 ui_element.py:121(check_hover)
       63    0.054    0.001    0.054    0.001 {built-in method pygame.event.get}
      905    0.007    0.000    0.053    0.000 ui_button.py:537(rebuild_shape)
      909    0.003    0.000    0.047    0.000 rect_drawable_shape.py:22(__init__)
      919    0.009    0.000    0.043    0.000 ui_element.py:23(__init__)
        1    0.000    0.000    0.041    0.041 main.py:182(initialise_game)
      909    0.013    0.000    0.041    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        2    0.000    0.000    0.038    0.019 entity.py:216(create_actor)
      905    0.004    0.000    0.035    0.000 ui_appearance_theme.py:405(get_font)
        2    0.008    0.004    0.031    0.016 world.py:28(create_fov_map)
     4529    0.026    0.000    0.026    0.000 surface_cache.py:119(build_cache_id)
      909    0.004    0.000    0.025    0.000 drawable_shape.py:45(redraw_all_states)
       63    0.022    0.000    0.022    0.000 {built-in method pygame.display.flip}
   344639    0.022    0.000    0.022    0.000 {method 'append' of 'list' objects}
     4547    0.021    0.000    0.021    0.000 {method 'copy' of 'pygame.Surface' objects}
     9610    0.011    0.000    0.021    0.000 ui_button.py:138(hover_point)
      919    0.002    0.000    0.021    0.000 ui_container.py:42(add_element)
      746    0.019    0.000    0.020    0.000 sprite.py:913(get_sprites_from_layer)
        6    0.004    0.001    0.018    0.003 ui_container.py:116(clear)
   311020    0.016    0.000    0.016    0.000 {built-in method builtins.len}
     1671    0.016    0.000    0.016    0.000 ui_container.py:62(recalculate_container_layer_thickness)
    10206    0.015    0.000    0.015    0.000 camera.py:234(world_to_screen_position)
      750    0.001    0.000    0.014    0.000 ui_button.py:130(kill)
     3920    0.008    0.000    0.013    0.000 world.py:57(get_tile)
      752    0.002    0.000    0.013    0.000 ui_element.py:114(kill)
     3002    0.004    0.000    0.013    0.000 _internal.py:24(wrapper)
      919    0.002    0.000    0.013    0.000 sprite.py:121(__init__)
      919    0.004    0.000    0.011    0.000 sprite.py:126(add)
        6    0.000    0.000    0.011    0.002 manager.py:286(update_camera_game_map)
     9610    0.009    0.000    0.010    0.000 rect_drawable_shape.py:84(collide_point)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:50(__init__)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
      919    0.002    0.000    0.009    0.000 ui_element.py:104(change_layer)
       26    0.000    0.000    0.009    0.000 manager.py:60(process_ui_events)
       26    0.003    0.000    0.008    0.000 ui_manager.py:86(process_events)
    19903    0.007    0.000    0.008    0.000 sprite.py:208(alive)
       83    0.008    0.000    0.008    0.000 {method 'fill' of 'pygame.Surface' objects}
      752    0.001    0.000    0.008    0.000 ui_container.py:52(remove_element)
        4    0.000    0.000    0.008    0.002 ui_text_box.py:110(rebuild)
     4529    0.007    0.000    0.008    0.000 drawable_shape.py:122(rebuild_images_and_text)
   104810    0.007    0.000    0.007    0.000 {method 'reverse' of 'list' objects}
      919    0.006    0.000    0.007    0.000 sprite.py:646(add_internal)
      927    0.006    0.000    0.007    0.000 sprite.py:822(change_layer)
     3003    0.006    0.000    0.007    0.000 {built-in method _warnings.warn}
        4    0.000    0.000    0.007    0.002 ui_text_box.py:310(parse_html_into_style_data)
      920    0.002    0.000    0.006    0.000 ui_font_dictionary.py:89(find_font)
        2    0.000    0.000    0.006    0.003 entity.py:278(build_characteristic_sprites)
        4    0.000    0.000    0.006    0.001 text_block.py:16(__init__)
        4    0.000    0.000    0.006    0.001 text_block.py:40(redraw)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
        6    0.000    0.000    0.004    0.001 manager.py:275(update_cameras_tiles)
        6    0.001    0.000    0.004    0.001 camera.py:168(update_camera_tiles)
     3925    0.004    0.000    0.004    0.000 world.py:349(_is_tile_in_bounds)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:14(__init__)
      752    0.001    0.000    0.004    0.000 sprite.py:183(kill)
     9610    0.004    0.000    0.004    0.000 ui_button.py:154(can_hover)
        2    0.000    0.000    0.003    0.002 message_log.py:49(add_message)
        1    0.000    0.000    0.003    0.003 world.py:21(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
     4529    0.003    0.000    0.003    0.000 surface_cache.py:109(find_surface_in_cache)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
      752    0.001    0.000    0.003    0.000 sprite.py:728(remove_internal)
      909    0.002    0.000    0.002    0.000 drawable_shape.py:11(__init__)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      915    0.002    0.000    0.002    0.000 ui_element.py:68(create_valid_ids)
    10293    0.002    0.000    0.002    0.000 ui_manager.py:167(get_mouse_position)
       29    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
    19903    0.001    0.000    0.001    0.000 {built-in method _operator.truth}
        1    0.000    0.000    0.001    0.001 ui_handler.py:155(process_ui_event)
        1    0.000    0.000    0.001    0.001 ui_handler.py:236(process_message)
        1    0.000    0.000    0.001    0.001 manager.py:444(add_to_message_log)
        4    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
    10169    0.001    0.000    0.001    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     1695    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
      921    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
      373    0.001    0.000    0.001    0.000 ui_container.py:124(check_hover)
     7847    0.001    0.000    0.001    0.000 world.py:50(get_game_map)
     9045    0.001    0.000    0.001    0.000 {method 'union' of 'pygame.Rect' objects}
      909    0.001    0.000    0.001    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       63    0.000    0.000    0.001    0.000 ui_appearance_theme.py:158(update_shape_cache)
       63    0.000    0.000    0.001    0.000 processors.py:15(process_all)
        8    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     1705    0.001    0.000    0.001    0.000 ui_button.py:257(process_event)
     3636    0.001    0.000    0.001    0.000 {built-in method math.floor}
     9773    0.001    0.000    0.001    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       63    0.000    0.000    0.001    0.000 surface_cache.py:24(update)
       63    0.001    0.000    0.001    0.000 processors.py:22(_process_aesthetic_update)
      124    0.001    0.000    0.001    0.000 ui_text_box.py:205(update)
      125    0.001    0.000    0.001    0.000 ui_manager.py:104(<listcomp>)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
        9    0.000    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
      941    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
       89    0.000    0.000    0.001    0.000 sprite.py:814(layers)
     4529    0.001    0.000    0.001    0.000 {method 'popleft' of 'collections.deque' objects}
      909    0.001    0.000    0.001    0.000 drawable_shape.py:46(<listcomp>)
      311    0.001    0.000    0.001    0.000 ui_window.py:97(update)
       62    0.000    0.000    0.001    0.000 screen_message.py:34(update)
        6    0.000    0.000    0.001    0.000 game_handler.py:26(process_event)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     1855    0.001    0.000    0.001    0.000 {built-in method builtins.min}
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
       11    0.000    0.000    0.001    0.000 entity_handler.py:25(process_event)
     1846    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
      915    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
        4    0.000    0.000    0.001    0.000 parser.py:104(feed)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        4    0.000    0.000    0.001    0.000 parser.py:134(goahead)
     1699    0.000    0.000    0.000    0.000 {built-in method builtins.max}
     2650    0.000    0.000    0.000    0.000 {built-in method builtins.hasattr}
     4187    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
       26    0.000    0.000    0.000    0.000 processors.py:56(process_intent)
       63    0.000    0.000    0.000    0.000 ui_manager.py:158(update_mouse_position)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        5    0.000    0.000    0.000    0.000 entity_handler.py:47(process_move)
      126    0.000    0.000    0.000    0.000 sprite.py:745(sprites)
     1847    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
        4    0.000    0.000    0.000    0.000 game_handler.py:42(process_change_game_state)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
     1241    0.000    0.000    0.000    0.000 ui_window.py:107(get_container)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       62    0.000    0.000    0.000    0.000 skill_bar.py:44(update)
      919    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       17    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
        4    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
       11    0.000    0.000    0.000    0.000 processors.py:137(_process_player_turn_intents)
     1812    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1986(info)
      178    0.000    0.000    0.000    0.000 {built-in method builtins.sorted}
        1    0.000    0.000    0.000    0.000 __init__.py:1373(info)
      186    0.000    0.000    0.000    0.000 ui_element.py:186(hover_point)
       20    0.000    0.000    0.000    0.000 entity.py:117(get_primary_stat)
       62    0.000    0.000    0.000    0.000 message_log.py:36(update)
        1    0.000    0.000    0.000    0.000 entity.py:187(create_god)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:1496(_log)
      927    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
       26    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
       51    0.000    0.000    0.000    0.000 __init__.py:1996(debug)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_hp)
       62    0.000    0.000    0.000    0.000 entity_info.py:45(update)
      919    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
        4    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        2    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      919    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
      919    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        2    0.000    0.000    0.000    0.000 {built-in method nt.stat}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        1    0.000    0.000    0.000    0.000 __init__.py:1521(handle)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
      908    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1575(callHandlers)
       10    0.000    0.000    0.000    0.000 world.py:262(tile_has_tag)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      905    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        3    0.000    0.000    0.000    0.000 entity.py:160(create)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      133    0.000    0.000    0.000    0.000 state.py:43(get_current)
        1    0.000    0.000    0.000    0.000 __init__.py:892(handle)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       63    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
        1    0.000    0.000    0.000    0.000 __init__.py:1123(emit)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        1    0.000    0.000    0.000    0.000 __init__.py:1022(emit)
      776    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        1    0.000    0.000    0.000    0.000 game_handler.py:81(process_end_turn)
       25    0.000    0.000    0.000    0.000 entity.py:271(add_component)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       51    0.000    0.000    0.000    0.000 __init__.py:1361(debug)
       29    0.000    0.000    0.000    0.000 esper.py:196(add_component)
        7    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
        1    0.000    0.000    0.000    0.000 chrono.py:51(next_turn)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      752    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       24    0.000    0.000    0.000    0.000 utility.py:107(lerp)
       25    0.000    0.000    0.000    0.000 entity.py:80(get_entitys_component)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        4    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        7    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        1    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      435    0.000    0.000    0.000    0.000 sprite.py:168(update)
       62    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        5    0.000    0.000    0.000    0.000 event.py:53(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        1    0.000    0.000    0.000    0.000 __init__.py:1011(flush)
        4    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        1    0.000    0.000    0.000    0.000 chrono.py:23(build_new_turn_queue)
        1    0.000    0.000    0.000    0.000 __init__.py:1481(makeRecord)
        5    0.000    0.000    0.000    0.000 world.py:361(_is_tile_blocking_movement)
        1    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
        5    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       12    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        1    0.000    0.000    0.000    0.000 __init__.py:293(__init__)
       26    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
       63    0.000    0.000    0.000    0.000 {built-in method builtins.any}
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      311    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       52    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        1    0.000    0.000    0.000    0.000 main.py:209(initialise_event_handlers)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        3    0.000    0.000    0.000    0.000 ntpath.py:212(basename)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       12    0.000    0.000    0.000    0.000 event_core.py:38(publish)
       26    0.000    0.000    0.000    0.000 processors.py:117(_process_stateless_intents)
       22    0.000    0.000    0.000    0.000 entity.py:34(get_player)
      186    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        1    0.000    0.000    0.000    0.000 __init__.py:869(format)
        5    0.000    0.000    0.000    0.000 world.py:397(_tile_has_other_entity)
        6    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        3    0.000    0.000    0.000    0.000 ntpath.py:178(split)
        2    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
       70    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       24    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:606(format)
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       12    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        5    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        6    0.000    0.000    0.000    0.000 map_handler.py:23(process_event)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       29    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
      121    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       22    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       11    0.000    0.000    0.000    0.000 processors.py:70(_get_pressed_direction)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        4    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        7    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       12    0.000    0.000    0.000    0.000 event_core.py:12(notify)
       92    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       10    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        4    0.000    0.000    0.000    0.000 parser.py:87(__init__)
       11    0.000    0.000    0.000    0.000 processors.py:97(_get_pressed_skills_number)
        6    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        1    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        1    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
        3    0.000    0.000    0.000    0.000 entity.py:90(get_name)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        3    0.000    0.000    0.000    0.000 state.py:69(set_new)
        9    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       25    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
       10    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       45    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        5    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.000    0.000 parser.py:96(reset)
      102    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
       21    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        3    0.000    0.000    0.000    0.000 entity.py:103(get_identity)
      105    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 event.py:92(__init__)
        6    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       12    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       66    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       13    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       20    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       11    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
        9    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
       25    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        5    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        7    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       12    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        1    0.000    0.000    0.000    0.000 {built-in method time.strftime}
       14    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       84    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 entity_handler.py:203(process_end_turn)
        4    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        4    0.000    0.000    0.000    0.000 {built-in method math.sin}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 main.py:159(disable_profiling)
       26    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
       22    0.000    0.000    0.000    0.000 library.py:124(get_savvy_data)
       22    0.000    0.000    0.000    0.000 library.py:140(get_people_data)
        6    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
       58    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        1    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        2    0.000    0.000    0.000    0.000 entity.py:110(get_combat_stats)
        1    0.000    0.000    0.000    0.000 event.py:148(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       22    0.000    0.000    0.000    0.000 library.py:156(get_homeland_data)
       10    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        3    0.000    0.000    0.000    0.000 component.py:41(__init__)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
       17    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 event.py:84(__init__)
        9    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        1    0.000    0.000    0.000    0.000 entity.py:316(spend_time)
        4    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       17    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
        4    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
       21    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        1    0.000    0.000    0.000    0.000 event.py:74(__init__)
        4    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        9    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        4    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       29    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        8    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        7    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        1    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        3    0.000    0.000    0.000    0.000 component.py:75(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        5    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
        4    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:432(format)
        6    0.000    0.000    0.000    0.000 chrono.py:115(get_turn_holder)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        3    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        4    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
       11    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        4    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        2    0.000    0.000    0.000    0.000 component.py:164(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:22(__init__)
       12    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 component.py:120(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:159(set_turn_holder)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:32(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
       12    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        2    0.000    0.000    0.000    0.000 __init__.py:856(release)
        6    0.000    0.000    0.000    0.000 state.py:15(get_previous)
        5    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        3    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        9    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 component.py:66(__init__)
        1    0.000    0.000    0.000    0.000 library.py:170(get_skill_data)
        1    0.000    0.000    0.000    0.000 component.py:156(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:1052(name)
        1    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:85(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 chrono.py:129(get_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:143(get_time_of_last_turn)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:94(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:106(add_time)
        1    0.000    0.000    0.000    0.000 chrono.py:173(set_turn_queue)
        4    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:122(get_turn_queue)
        1    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        1    0.000    0.000    0.000    0.000 {built-in method time.time}
        2    0.000    0.000    0.000    0.000 component.py:103(__init__)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        1    0.000    0.000    0.000    0.000 chrono.py:166(set_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:180(set_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)
        2    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 chrono.py:136(get_time)


