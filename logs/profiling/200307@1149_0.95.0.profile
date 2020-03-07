Sat Mar  7 11:49:26 2020    logs/profiling/profile.dump

         3468452 function calls (3076506 primitive calls) in 10.521 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.080    0.080   10.480   10.480 main.py:77(game_loop)
      498    5.498    0.011    5.498    0.011 {method 'tick' of 'Clock' objects}
      249    0.001    0.000    2.833    0.011 state.py:36(get_delta_time)
      249    0.001    0.000    2.667    0.011 state.py:61(update_clock)
      249    0.000    0.000    2.450    0.010 event_core.py:21(update)
       21    0.000    0.000    2.447    0.117 ui_handler.py:30(process_event)
       15    0.000    0.000    2.433    0.162 ui_handler.py:205(update_camera)
       15    0.000    0.000    2.394    0.160 manager.py:295(update_camera_grid)
       15    0.015    0.001    2.394    0.160 camera.py:106(update_grid)
     2255    0.028    0.000    2.331    0.001 ui_button.py:30(__init__)
       14    0.000    0.000    2.273    0.162 ui_handler.py:48(process_entity_event)
     2255    0.122    0.000    2.192    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
    65455    0.163    0.000    1.770    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
457365/65455    1.510    0.000    1.595    0.000 ui_appearance_theme.py:322(get_next_id_node)
      249    0.001    0.000    1.203    0.005 manager.py:54(update)
      249    0.066    0.000    1.202    0.005 ui_manager.py:122(update)
      249    0.003    0.000    1.137    0.005 manager.py:73(draw)
    33853    0.087    0.000    1.003    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
      249    0.039    0.000    0.803    0.003 sprite.py:453(update)
    82695    0.801    0.000    0.801    0.000 {method 'blit' of 'pygame.Surface' objects}
    20323    0.039    0.000    0.584    0.000 ui_appearance_theme.py:428(get_misc_data)
      263    0.226    0.001    0.483    0.002 camera.py:79(update_game_map)
      248    0.001    0.000    0.457    0.002 camera.py:72(update)
      249    0.002    0.000    0.407    0.002 ui_manager.py:173(draw_ui)
      249    0.061    0.000    0.405    0.002 sprite.py:753(draw)
      253    0.359    0.001    0.359    0.001 {built-in method pygame.transform.scale}
    38440    0.073    0.000    0.280    0.000 ui_button.py:197(update)
     2255    0.014    0.000    0.272    0.000 ui_button.py:97(set_any_images_from_theme)
    39121    0.147    0.000    0.261    0.000 ui_element.py:121(check_hover)
     9020    0.016    0.000    0.259    0.000 ui_appearance_theme.py:366(get_image)
    11129    0.069    0.000    0.196    0.000 rect_drawable_shape.py:118(redraw_state)
    38440    0.039    0.000    0.193    0.000 drawable_shape.py:36(update)
        6    0.000    0.000    0.173    0.029 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.168    0.168 ui_handler.py:111(init_game_ui)
     2255    0.018    0.000    0.127    0.000 ui_button.py:537(rebuild_shape)
     2259    0.007    0.000    0.108    0.000 rect_drawable_shape.py:22(__init__)
     2269    0.022    0.000    0.104    0.000 ui_element.py:23(__init__)
     2259    0.029    0.000    0.095    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
     2255    0.010    0.000    0.086    0.000 ui_appearance_theme.py:405(get_font)
      249    0.084    0.000    0.084    0.000 {built-in method pygame.display.flip}
      249    0.082    0.000    0.082    0.000 {built-in method pygame.event.get}
    38440    0.040    0.000    0.079    0.000 ui_button.py:138(hover_point)
     2714    0.065    0.000    0.069    0.000 sprite.py:913(get_sprites_from_layer)
     2259    0.011    0.000    0.059    0.000 drawable_shape.py:45(redraw_all_states)
   890370    0.058    0.000    0.058    0.000 {method 'append' of 'list' objects}
    11129    0.057    0.000    0.057    0.000 surface_cache.py:119(build_cache_id)
    39465    0.052    0.000    0.052    0.000 camera.py:234(world_to_screen_position)
     2269    0.006    0.000    0.050    0.000 ui_container.py:42(add_element)
       15    0.010    0.001    0.050    0.003 ui_container.py:116(clear)
    11147    0.047    0.000    0.047    0.000 {method 'copy' of 'pygame.Surface' objects}
     4372    0.042    0.000    0.042    0.000 ui_container.py:62(recalculate_container_layer_thickness)
        1    0.000    0.000    0.041    0.041 main.py:182(initialise_game)
     2100    0.002    0.000    0.040    0.000 ui_button.py:130(kill)
   789154    0.039    0.000    0.039    0.000 {built-in method builtins.len}
    38440    0.034    0.000    0.038    0.000 rect_drawable_shape.py:84(collide_point)
     2103    0.004    0.000    0.037    0.000 ui_element.py:114(kill)
        2    0.000    0.000    0.037    0.019 entity.py:216(create_actor)
      519    0.033    0.000    0.033    0.000 {method 'fill' of 'pygame.Surface' objects}
        2    0.008    0.004    0.031    0.015 world.py:28(create_fov_map)
    79483    0.025    0.000    0.030    0.000 sprite.py:208(alive)
     2269    0.004    0.000    0.030    0.000 sprite.py:121(__init__)
       15    0.000    0.000    0.028    0.002 manager.py:286(update_camera_game_map)
     2269    0.009    0.000    0.026    0.000 sprite.py:126(add)
     2103    0.004    0.000    0.023    0.000 ui_container.py:52(remove_element)
       44    0.000    0.000    0.022    0.000 manager.py:60(process_ui_events)
       44    0.008    0.000    0.022    0.000 ui_manager.py:86(process_events)
      185    0.001    0.000    0.021    0.000 screen_message.py:34(update)
     2269    0.005    0.000    0.021    0.000 ui_element.py:104(change_layer)
      125    0.000    0.000    0.018    0.000 ui_text_box.py:347(redraw_from_chunks)
     5306    0.011    0.000    0.018    0.000 world.py:57(get_tile)
    11129    0.015    0.000    0.016    0.000 drawable_shape.py:122(rebuild_images_and_text)
     2277    0.014    0.000    0.016    0.000 sprite.py:822(change_layer)
   261410    0.016    0.000    0.016    0.000 {method 'reverse' of 'list' objects}
     2269    0.015    0.000    0.016    0.000 sprite.py:646(add_internal)
      433    0.003    0.000    0.016    0.000 ui_text_box.py:205(update)
    38440    0.013    0.000    0.013    0.000 ui_button.py:154(can_hover)
     3002    0.004    0.000    0.013    0.000 _internal.py:24(wrapper)
      125    0.001    0.000    0.012    0.000 ui_text_box.py:327(redraw_from_text_block)
       15    0.000    0.000    0.011    0.001 manager.py:275(update_cameras_tiles)
       15    0.003    0.000    0.011    0.001 camera.py:168(update_camera_tiles)
     2270    0.005    0.000    0.011    0.000 ui_font_dictionary.py:89(find_font)
     2103    0.003    0.000    0.010    0.000 sprite.py:183(kill)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:50(__init__)
        4    0.000    0.000    0.009    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
        4    0.000    0.000    0.008    0.002 ui_text_box.py:110(rebuild)
     2103    0.004    0.000    0.007    0.000 sprite.py:728(remove_internal)
        4    0.000    0.000    0.007    0.002 ui_text_box.py:310(parse_html_into_style_data)
       63    0.000    0.000    0.006    0.000 ui_text_box.py:462(set_active_effect)
     3003    0.006    0.000    0.006    0.000 {built-in method _warnings.warn}
    11129    0.006    0.000    0.006    0.000 surface_cache.py:109(find_surface_in_cache)
        2    0.000    0.000    0.006    0.003 entity.py:278(build_characteristic_sprites)
     5320    0.005    0.000    0.006    0.000 world.py:349(_is_tile_in_bounds)
    41043    0.006    0.000    0.006    0.000 ui_manager.py:167(get_mouse_position)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
     2259    0.006    0.000    0.006    0.000 drawable_shape.py:11(__init__)
        4    0.000    0.000    0.006    0.001 text_block.py:16(__init__)
        4    0.000    0.000    0.006    0.001 text_block.py:40(redraw)
     2265    0.004    0.000    0.005    0.000 ui_element.py:68(create_valid_ids)
    79483    0.005    0.000    0.005    0.000 {built-in method _operator.truth}
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      125    0.002    0.000    0.005    0.000 text_block.py:265(redraw_from_chunks)
    40610    0.005    0.000    0.005    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
     1489    0.004    0.000    0.005    0.000 ui_container.py:124(check_hover)
      249    0.001    0.000    0.005    0.000 processors.py:15(process_all)
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
    37019    0.005    0.000    0.005    0.000 {method 'union' of 'pygame.Rect' objects}
      249    0.003    0.000    0.004    0.000 processors.py:22(_process_aesthetic_update)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:14(__init__)
    39793    0.004    0.000    0.004    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        2    0.000    0.000    0.003    0.002 message_log.py:49(add_message)
     4397    0.003    0.000    0.003    0.000 {method 'remove' of 'list' objects}
        1    0.000    0.000    0.003    0.003 world.py:21(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
     2271    0.003    0.000    0.003    0.000 ui_font_dictionary.py:133(create_font_id)
     4495    0.003    0.000    0.003    0.000 ui_button.py:257(process_event)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
     9036    0.003    0.000    0.003    0.000 {built-in method math.floor}
      293    0.002    0.000    0.003    0.000 sprite.py:814(layers)
      249    0.001    0.000    0.002    0.000 ui_appearance_theme.py:158(update_shape_cache)
     2259    0.002    0.000    0.002    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     1241    0.002    0.000    0.002    0.000 ui_window.py:97(update)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      296    0.002    0.000    0.002    0.000 ui_manager.py:104(<listcomp>)
      249    0.000    0.000    0.002    0.000 surface_cache.py:24(update)
     2309    0.001    0.000    0.002    0.000 ui_window_stack.py:73(get_root_window)
     2259    0.002    0.000    0.002    0.000 drawable_shape.py:46(<listcomp>)
    10628    0.002    0.000    0.002    0.000 world.py:50(get_game_map)
      249    0.001    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
    11129    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
       29    0.001    0.000    0.001    0.000 {method 'render' of 'pygame.font.Font' objects}
      498    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
        4    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
        1    0.000    0.000    0.001    0.001 ui_handler.py:155(process_ui_event)
        1    0.000    0.000    0.001    0.001 ui_handler.py:236(process_message)
        1    0.000    0.000    0.001    0.001 manager.py:444(add_to_message_log)
     4650    0.001    0.000    0.001    0.000 {built-in method builtins.min}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       20    0.000    0.000    0.001    0.000 entity_handler.py:25(process_event)
     4546    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     2274    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
      248    0.001    0.000    0.001    0.000 skill_bar.py:44(update)
     6701    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
        9    0.001    0.000    0.001    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
        8    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     4238    0.001    0.000    0.001    0.000 {built-in method builtins.max}
      586    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
       44    0.000    0.000    0.001    0.000 processors.py:56(process_intent)
       14    0.000    0.000    0.001    0.000 entity_handler.py:47(process_move)
     3522    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
      681    0.001    0.000    0.001    0.000 ui_element.py:186(hover_point)
      248    0.000    0.000    0.001    0.000 message_log.py:36(update)
     4547    0.001    0.000    0.001    0.000 ui_manager.py:44(get_sprite_group)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
     2269    0.001    0.000    0.001    0.000 sprite.py:162(add_internal)
       29    0.000    0.000    0.001    0.000 processors.py:137(_process_player_turn_intents)
      248    0.000    0.000    0.001    0.000 entity_info.py:45(update)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.001    0.001    0.001    0.001 camera.py:24(__init__)
     4512    0.001    0.000    0.001    0.000 {method 'copy' of 'list' objects}
      505    0.001    0.000    0.001    0.000 state.py:43(get_current)
        6    0.000    0.000    0.001    0.000 game_handler.py:26(process_event)
     2277    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
     5609    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        4    0.000    0.000    0.000    0.000 parser.py:104(feed)
      249    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
        4    0.000    0.000    0.000    0.000 parser.py:134(goahead)
     2269    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
     2269    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
       44    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 game_handler.py:42(process_change_game_state)
     2269    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
     2258    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       28    0.000    0.000    0.000    0.000 world.py:262(tile_has_tag)
       86    0.000    0.000    0.000    0.000 utility.py:107(lerp)
       78    0.000    0.000    0.000    0.000 __init__.py:1996(debug)
     2135    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        5    0.000    0.000    0.000    0.000 {built-in method nt.stat}
     2105    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 __init__.py:1986(info)
        1    0.000    0.000    0.000    0.000 __init__.py:1373(info)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
       44    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        1    0.000    0.000    0.000    0.000 __init__.py:1496(_log)
      248    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        4    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
       17    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
     1737    0.000    0.000    0.000    0.000 sprite.py:168(update)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        4    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       20    0.000    0.000    0.000    0.000 entity.py:117(get_primary_stat)
        1    0.000    0.000    0.000    0.000 entity.py:187(create_god)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
      249    0.000    0.000    0.000    0.000 {built-in method builtins.any}
     2103    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       61    0.000    0.000    0.000    0.000 entity.py:80(get_entitys_component)
       14    0.000    0.000    0.000    0.000 event.py:53(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       43    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
     1241    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
       62    0.000    0.000    0.000    0.000 text_effects.py:88(update)
       63    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_hp)
        1    0.000    0.000    0.000    0.000 __init__.py:1521(handle)
        1    0.000    0.000    0.000    0.000 __init__.py:1575(callHandlers)
        1    0.000    0.000    0.000    0.000 __init__.py:892(handle)
        4    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        9    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
        1    0.000    0.000    0.000    0.000 __init__.py:1123(emit)
        2    0.000    0.000    0.000    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1022(emit)
       14    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
      681    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
       78    0.000    0.000    0.000    0.000 __init__.py:1361(debug)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
       14    0.000    0.000    0.000    0.000 world.py:361(_is_tile_blocking_movement)
        3    0.000    0.000    0.000    0.000 entity.py:160(create)
       88    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        1    0.000    0.000    0.000    0.000 manager.py:264(move_camera)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       44    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
        1    0.000    0.000    0.000    0.000 camera.py:224(move_camera)
        1    0.000    0.000    0.000    0.000 game_handler.py:81(process_end_turn)
       25    0.000    0.000    0.000    0.000 entity.py:271(add_component)
        5    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
       29    0.000    0.000    0.000    0.000 esper.py:196(add_component)
      343    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       58    0.000    0.000    0.000    0.000 entity.py:34(get_player)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        1    0.000    0.000    0.000    0.000 __init__.py:1011(flush)
        7    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
       14    0.000    0.000    0.000    0.000 world.py:397(_tile_has_other_entity)
       14    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
        1    0.000    0.000    0.000    0.000 chrono.py:51(next_turn)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
       15    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        5    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       14    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
      160    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       21    0.000    0.000    0.000    0.000 event_core.py:38(publish)
       29    0.000    0.000    0.000    0.000 processors.py:70(_get_pressed_direction)
        7    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      130    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        4    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       49    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       28    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        4    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
        1    0.000    0.000    0.000    0.000 chrono.py:23(build_new_turn_queue)
        1    0.000    0.000    0.000    0.000 __init__.py:1481(makeRecord)
       44    0.000    0.000    0.000    0.000 processors.py:117(_process_stateless_intents)
        3    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        1    0.000    0.000    0.000    0.000 __init__.py:293(__init__)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      218    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       29    0.000    0.000    0.000    0.000 processors.py:97(_get_pressed_skills_number)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
       79    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        3    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
       15    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       21    0.000    0.000    0.000    0.000 event_core.py:12(notify)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        1    0.000    0.000    0.000    0.000 main.py:209(initialise_event_handlers)
        3    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        3    0.000    0.000    0.000    0.000 ntpath.py:212(basename)
       14    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       61    0.000    0.000    0.000    0.000 esper.py:176(has_component)
      118    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        1    0.000    0.000    0.000    0.000 __init__.py:869(format)
        1    0.000    0.000    0.000    0.000 __init__.py:606(format)
       63    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
       12    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
        3    0.000    0.000    0.000    0.000 ntpath.py:178(split)
        6    0.000    0.000    0.000    0.000 map_handler.py:23(process_event)
        4    0.000    0.000    0.000    0.000 esper.py:270(get_component)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        9    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       29    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       62    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
       43    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        9    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
      125    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
      346    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
        4    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        7    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
       21    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        4    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
        4    0.000    0.000    0.000    0.000 parser.py:87(__init__)
       61    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        1    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
       30    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
      114    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
        9    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        3    0.000    0.000    0.000    0.000 state.py:69(set_new)
        3    0.000    0.000    0.000    0.000 entity.py:90(get_name)
       10    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
       62    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        9    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        4    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
      102    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        4    0.000    0.000    0.000    0.000 event.py:92(__init__)
       29    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
       15    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        3    0.000    0.000    0.000    0.000 entity.py:103(get_identity)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        6    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       13    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       15    0.000    0.000    0.000    0.000 chrono.py:115(get_turn_holder)
       66    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       11    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        9    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
        1    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        7    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method time.strftime}
        9    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        9    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       84    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
       14    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        4    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        1    0.000    0.000    0.000    0.000 entity_handler.py:203(process_end_turn)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        4    0.000    0.000    0.000    0.000 {built-in method math.sin}
       26    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 component.py:41(__init__)
       22    0.000    0.000    0.000    0.000 library.py:140(get_people_data)
       14    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
       22    0.000    0.000    0.000    0.000 library.py:124(get_savvy_data)
        1    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       22    0.000    0.000    0.000    0.000 library.py:156(get_homeland_data)
        3    0.000    0.000    0.000    0.000 <string>:1(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
       10    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 entity.py:110(get_combat_stats)
        1    0.000    0.000    0.000    0.000 main.py:159(disable_profiling)
        1    0.000    0.000    0.000    0.000 event.py:148(__init__)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       58    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        1    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       17    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        9    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        1    0.000    0.000    0.000    0.000 event.py:84(__init__)
        1    0.000    0.000    0.000    0.000 entity.py:316(spend_time)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        6    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
       17    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        4    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        1    0.000    0.000    0.000    0.000 event.py:74(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        4    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
       21    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        9    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        9    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       29    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 component.py:56(__init__)
        3    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        4    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        7    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        1    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        3    0.000    0.000    0.000    0.000 component.py:75(__init__)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        8    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        1    0.000    0.000    0.000    0.000 __init__.py:432(format)
       11    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
        2    0.000    0.000    0.000    0.000 component.py:164(__init__)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        4    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        3    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        2    0.000    0.000    0.000    0.000 component.py:32(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:159(set_turn_holder)
       20    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        1    0.000    0.000    0.000    0.000 entity_handler.py:22(__init__)
       12    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 component.py:120(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        6    0.000    0.000    0.000    0.000 state.py:15(get_previous)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
       12    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        4    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        5    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 component.py:66(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        9    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        1    0.000    0.000    0.000    0.000 component.py:156(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        1    0.000    0.000    0.000    0.000 threading.py:1052(name)
        2    0.000    0.000    0.000    0.000 __init__.py:856(release)
        3    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        1    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        1    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
        2    0.000    0.000    0.000    0.000 component.py:85(__init__)
        1    0.000    0.000    0.000    0.000 library.py:170(get_skill_data)
        1    0.000    0.000    0.000    0.000 chrono.py:106(add_time)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 component.py:94(__init__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        3    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        2    0.000    0.000    0.000    0.000 component.py:103(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:122(get_turn_queue)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        4    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:129(get_time_in_round)
        1    0.000    0.000    0.000    0.000 chrono.py:173(set_turn_queue)
        4    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        1    0.000    0.000    0.000    0.000 {built-in method time.time}
        1    0.000    0.000    0.000    0.000 chrono.py:143(get_time_of_last_turn)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        1    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        1    0.000    0.000    0.000    0.000 chrono.py:180(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 chrono.py:136(get_time)
        1    0.000    0.000    0.000    0.000 chrono.py:166(set_time_in_round)
        1    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)


