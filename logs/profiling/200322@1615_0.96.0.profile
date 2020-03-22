Sun Mar 22 16:15:37 2020    logs/profiling/profile.dump

         9626370 function calls (8266987 primitive calls) in 15.046 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.077    0.077   15.003   15.003 main.py:103(game_loop)
      202    0.001    0.000    8.413    0.042 event_core.py:24(update)
       62    0.000    0.000    8.402    0.136 ui_handler.py:31(process_event)
       52    0.001    0.000    8.368    0.161 ui_handler.py:201(_update_camera)
       52    0.000    0.000    8.244    0.159 manager.py:295(update_camera_grid)
       52    0.051    0.001    8.243    0.159 camera.py:105(update_grid)
       51    0.000    0.000    8.207    0.161 ui_handler.py:44(process_entity_event)
     7811    0.097    0.000    8.027    0.001 ui_button.py:30(__init__)
     7811    0.421    0.000    7.552    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
   226657    0.558    0.000    6.104    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
1585839/226657    5.209    0.000    5.503    0.000 ui_appearance_theme.py:322(get_next_id_node)
      404    4.087    0.010    4.087    0.010 {method 'tick' of 'Clock' objects}
   117229    0.300    0.000    3.449    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
      202    0.001    0.000    2.196    0.011 state.py:38(get_delta_time)
    70363    0.134    0.000    2.010    0.000 ui_appearance_theme.py:428(get_misc_data)
      202    0.001    0.000    1.893    0.009 state.py:63(update_clock)
      202    0.001    0.000    1.081    0.005 manager.py:54(update)
      202    0.058    0.000    1.080    0.005 ui_manager.py:122(update)
      202    0.003    0.000    1.039    0.005 manager.py:73(draw)
     7811    0.048    0.000    0.948    0.000 ui_button.py:97(set_any_images_from_theme)
    31244    0.057    0.000    0.900    0.000 ui_appearance_theme.py:366(get_image)
    74297    0.796    0.000    0.796    0.000 {method 'blit' of 'pygame.Surface' objects}
      202    0.034    0.000    0.690    0.003 sprite.py:453(update)
      253    0.215    0.001    0.485    0.002 camera.py:79(update_game_map)
     7811    0.061    0.000    0.430    0.000 ui_button.py:537(rebuild_shape)
      201    0.001    0.000    0.405    0.002 camera.py:72(update)
      202    0.002    0.000    0.403    0.002 ui_manager.py:173(draw_ui)
      202    0.059    0.000    0.402    0.002 sprite.py:753(draw)
     7821    0.024    0.000    0.366    0.000 rect_drawable_shape.py:22(__init__)
     7832    0.076    0.000    0.351    0.000 ui_element.py:23(__init__)
     7821    0.099    0.000    0.321    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
     7811    0.035    0.000    0.297    0.000 ui_appearance_theme.py:405(get_font)
      207    0.295    0.001    0.295    0.001 {built-in method pygame.transform.scale}
    13115    0.088    0.000    0.251    0.000 rect_drawable_shape.py:118(redraw_state)
    32355    0.140    0.000    0.248    0.000 ui_element.py:121(check_hover)
    31371    0.063    0.000    0.201    0.000 ui_button.py:197(update)
     7821    0.036    0.000    0.200    0.000 drawable_shape.py:45(redraw_all_states)
        9    0.000    0.000    0.177    0.020 ui_handler.py:68(process_game_event)
  2862878    0.176    0.000    0.176    0.000 {method 'append' of 'list' objects}
       52    0.028    0.001    0.172    0.003 ui_container.py:116(clear)
        1    0.000    0.000    0.170    0.170 ui_handler.py:107(init_game_ui)
     7832    0.020    0.000    0.167    0.000 ui_container.py:42(add_element)
      177    0.001    0.000    0.146    0.001 manager.py:60(process_ui_events)
      177    0.052    0.000    0.145    0.001 ui_manager.py:86(process_events)
     7650    0.009    0.000    0.142    0.000 ui_button.py:130(kill)
    15486    0.141    0.000    0.141    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      202    0.135    0.001    0.135    0.001 {built-in method pygame.event.get}
     7654    0.016    0.000    0.133    0.000 ui_element.py:114(kill)
     3782    0.124    0.000    0.131    0.000 sprite.py:913(get_sprites_from_layer)
  2582491    0.126    0.000    0.126    0.000 {built-in method builtins.len}
    31371    0.028    0.000    0.125    0.000 drawable_shape.py:36(update)
     7832    0.013    0.000    0.103    0.000 sprite.py:121(__init__)
     7832    0.029    0.000    0.090    0.000 sprite.py:126(add)
       52    0.000    0.000    0.081    0.002 manager.py:286(update_camera_game_map)
     7654    0.015    0.000    0.081    0.000 ui_container.py:52(remove_element)
      202    0.079    0.000    0.079    0.000 {built-in method pygame.display.flip}
    13115    0.075    0.000    0.075    0.000 surface_cache.py:119(build_cache_id)
    31368    0.039    0.000    0.074    0.000 ui_button.py:138(hover_point)
     7832    0.015    0.000    0.070    0.000 ui_element.py:104(change_layer)
    13163    0.058    0.000    0.058    0.000 {method 'copy' of 'pygame.Surface' objects}
   906062    0.057    0.000    0.057    0.000 {method 'reverse' of 'list' objects}
     7832    0.052    0.000    0.055    0.000 sprite.py:646(add_internal)
     7840    0.047    0.000    0.055    0.000 sprite.py:822(change_layer)
    37952    0.054    0.000    0.054    0.000 camera.py:233(world_to_screen_position)
      366    0.002    0.000    0.044    0.000 screen_message.py:34(update)
        1    0.000    0.000    0.043    0.043 main.py:211(initialise_game)
       52    0.000    0.000    0.041    0.001 manager.py:275(update_cameras_tiles)
       52    0.013    0.000    0.040    0.001 camera.py:167(update_camera_tiles)
        2    0.000    0.000    0.040    0.020 entity.py:232(create_actor)
    10903    0.023    0.000    0.039    0.000 world.py:55(get_tile)
      246    0.001    0.000    0.038    0.000 ui_text_box.py:347(redraw_from_chunks)
     7654    0.011    0.000    0.036    0.000 sprite.py:183(kill)
    31411    0.031    0.000    0.035    0.000 rect_drawable_shape.py:84(collide_point)
      742    0.033    0.000    0.033    0.000 {method 'fill' of 'pygame.Surface' objects}
        2    0.008    0.004    0.033    0.016 world.py:26(create_fov_map)
     7961    0.017    0.000    0.031    0.000 ui_font_dictionary.py:89(find_font)
      675    0.005    0.000    0.031    0.000 ui_text_box.py:205(update)
    65680    0.023    0.000    0.028    0.000 sprite.py:208(alive)
      246    0.003    0.000    0.027    0.000 ui_text_box.py:327(redraw_from_text_block)
        8    0.000    0.000    0.026    0.003 ui_text_box.py:50(__init__)
        8    0.000    0.000    0.026    0.003 ui_text_box.py:492(rebuild_from_changed_theme_data)
     7654    0.012    0.000    0.024    0.000 sprite.py:728(remove_internal)
        8    0.000    0.000    0.024    0.003 ui_text_box.py:110(rebuild)
     7821    0.021    0.000    0.021    0.000 drawable_shape.py:11(__init__)
    13115    0.019    0.000    0.020    0.000 drawable_shape.py:122(rebuild_images_and_text)
     7828    0.015    0.000    0.020    0.000 ui_element.py:68(create_valid_ids)
    25462    0.020    0.000    0.020    0.000 ui_button.py:257(process_event)
        2    0.000    0.000    0.019    0.009 ui_handler.py:151(process_ui_event)
        1    0.000    0.000    0.017    0.017 ui_handler.py:225(_select_entity)
        1    0.000    0.000    0.017    0.017 manager.py:414(set_selected_entity)
        1    0.000    0.000    0.017    0.017 entity_info.py:65(show)
      124    0.001    0.000    0.014    0.000 ui_text_box.py:462(set_active_effect)
       10    0.000    0.000    0.014    0.001 ui_text_box.py:310(parse_html_into_style_data)
    10954    0.012    0.000    0.013    0.000 world.py:351(_is_tile_in_bounds)
     3002    0.004    0.000    0.013    0.000 _internal.py:24(wrapper)
    31371    0.013    0.000    0.013    0.000 ui_button.py:154(can_hover)
    15543    0.012    0.000    0.012    0.000 {method 'remove' of 'list' objects}
      202    0.001    0.000    0.011    0.000 processors.py:18(process_all)
     7962    0.011    0.000    0.011    0.000 ui_font_dictionary.py:133(create_font_id)
       10    0.000    0.000    0.010    0.001 text_block.py:16(__init__)
      202    0.005    0.000    0.010    0.000 processors.py:25(_process_aesthetic_update)
       10    0.001    0.000    0.010    0.001 text_block.py:40(redraw)
      246    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
     1717    0.010    0.000    0.010    0.000 ui_manager.py:104(<listcomp>)
     2472    0.007    0.000    0.009    0.000 query.py:212(__iter__)
    13115    0.009    0.000    0.009    0.000 surface_cache.py:109(find_surface_in_cache)
        1    0.000    0.000    0.009    0.009 entity_info.py:179(create_secondary_stats_section)
    31284    0.009    0.000    0.009    0.000 {built-in method math.floor}
      177    0.001    0.000    0.008    0.000 processors.py:59(process_intent)
        2    0.000    0.000    0.008    0.004 ui_vertical_scroll_bar.py:22(__init__)
     7821    0.007    0.000    0.008    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     3003    0.006    0.000    0.008    0.000 {built-in method _warnings.warn}
      163    0.001    0.000    0.007    0.000 processors.py:140(_process_player_turn_intents)
       60    0.000    0.000    0.007    0.000 entity_handler.py:26(process_event)
        1    0.000    0.000    0.007    0.007 entity_info.py:148(create_primary_stats_section)
       51    0.001    0.000    0.007    0.000 entity_handler.py:45(_process_move)
        2    0.000    0.000    0.007    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.007    0.003 screen_message.py:16(__init__)
        2    0.000    0.000    0.006    0.003 entity.py:339(build_characteristic_sprites)
    34306    0.006    0.000    0.006    0.000 ui_manager.py:167(get_mouse_position)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
     7999    0.005    0.000    0.006    0.000 ui_window_stack.py:73(get_root_window)
      217    0.002    0.000    0.006    0.000 entity.py:43(get_player)
      202    0.001    0.000    0.005    0.000 ui_appearance_theme.py:158(update_shape_cache)
     7821    0.005    0.000    0.005    0.000 drawable_shape.py:46(<listcomp>)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
    65680    0.005    0.000    0.005    0.000 {built-in method _operator.truth}
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
    33632    0.005    0.000    0.005    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      202    0.000    0.000    0.005    0.000 surface_cache.py:24(update)
     7869    0.005    0.000    0.005    0.000 drawable_shape.py:86(get_surface)
    15672    0.004    0.000    0.004    0.000 {method 'insert' of 'list' objects}
     1207    0.003    0.000    0.004    0.000 ui_container.py:124(check_hover)
    15646    0.004    0.000    0.004    0.000 {built-in method builtins.min}
    29502    0.004    0.000    0.004    0.000 {method 'union' of 'pygame.Rect' objects}
    23478    0.004    0.000    0.004    0.000 {built-in method builtins.hasattr}
       24    0.003    0.000    0.004    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
       26    0.000    0.000    0.004    0.000 __init__.py:1496(_log)
    14419    0.004    0.000    0.004    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
    31986    0.004    0.000    0.004    0.000 {method 'colliderect' of 'pygame.Rect' objects}
     1082    0.003    0.000    0.004    0.000 typing.py:806(__new__)
        2    0.000    0.000    0.003    0.002 message_log.py:49(add_message)
    21859    0.003    0.000    0.003    0.000 world.py:48(get_game_map)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
    15673    0.003    0.000    0.003    0.000 ui_manager.py:44(get_sprite_group)
     1082    0.002    0.000    0.003    0.000 query.py:170(__init__)
      379    0.002    0.000    0.003    0.000 sprite.py:814(layers)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      102    0.000    0.000    0.003    0.000 world.py:268(tile_has_tag)
       38    0.001    0.000    0.003    0.000 styled_chunk.py:8(__init__)
       17    0.000    0.000    0.003    0.000 __init__.py:1996(debug)
     7832    0.003    0.000    0.003    0.000 sprite.py:162(add_internal)
       17    0.000    0.000    0.003    0.000 __init__.py:1361(debug)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
        9    0.000    0.000    0.003    0.000 game_handler.py:26(process_event)
       10    0.000    0.000    0.002    0.000 parser.py:104(feed)
       10    0.000    0.000    0.002    0.000 parser.py:134(goahead)
    15628    0.002    0.000    0.002    0.000 {method 'copy' of 'list' objects}
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
       83    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
       26    0.000    0.000    0.002    0.000 __init__.py:1521(handle)
     7840    0.002    0.000    0.002    0.000 {method 'pop' of 'dict' objects}
     1006    0.002    0.000    0.002    0.000 ui_window.py:97(update)
       26    0.000    0.000    0.002    0.000 __init__.py:1575(callHandlers)
     8849    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
    13115    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
       26    0.000    0.000    0.002    0.000 __init__.py:892(handle)
      177    0.001    0.000    0.002    0.000 action.py:12(convert_to_intent)
       76    0.002    0.000    0.002    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     7826    0.002    0.000    0.002    0.000 ui_manager.py:51(get_window_stack)
       26    0.000    0.000    0.002    0.000 __init__.py:1123(emit)
       51    0.001    0.000    0.002    0.000 world.py:401(_tile_has_entity_blocking_movement)
       26    0.000    0.000    0.002    0.000 __init__.py:1022(emit)
     7832    0.002    0.000    0.002    0.000 ui_manager.py:37(get_theme)
     7832    0.001    0.000    0.001    0.000 {method '__contains__' of 'dict' objects}
        1    0.000    0.000    0.001    0.001 ui_handler.py:232(_process_message)
        1    0.000    0.000    0.001    0.001 manager.py:444(add_to_message_log)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.001    0.001 warnings.py:20(_showwarnmsg_impl)
        2    0.000    0.000    0.001    0.001 game_handler.py:81(_process_end_turn)
      202    0.001    0.000    0.001    0.000 ui_manager.py:158(update_mouse_position)
        2    0.000    0.000    0.001    0.001 chrono.py:47(next_turn)
        1    0.000    0.000    0.001    0.001 entity_info.py:119(create_core_info_section)
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
       27    0.001    0.000    0.001    0.000 {method 'write' of '_io.TextIOWrapper' objects}
       26    0.000    0.000    0.001    0.000 __init__.py:1481(makeRecord)
     7818    0.001    0.000    0.001    0.000 {method 'copy' of 'pygame.Rect' objects}
  800/635    0.000    0.000    0.001    0.000 {built-in method builtins.getattr}
       38    0.000    0.000    0.001    0.000 parser.py:301(parse_starttag)
      984    0.001    0.000    0.001    0.000 ui_element.py:186(hover_point)
    11531    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
      394    0.001    0.000    0.001    0.000 entity.py:93(get_entitys_component)
        6    0.000    0.000    0.001    0.000 game_handler.py:39(_process_change_game_state)
       26    0.000    0.000    0.001    0.000 __init__.py:293(__init__)
       52    0.001    0.000    0.001    0.000 entity.py:73(get_entities_and_components_in_area)
       75    0.001    0.000    0.001    0.000 entity.py:131(get_primary_stat)
     7728    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
      758    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
      404    0.001    0.000    0.001    0.000 sprite.py:745(sprites)
     1643    0.001    0.000    0.001    0.000 query.py:243(<listcomp>)
        7    0.000    0.000    0.001    0.000 __init__.py:1986(info)
        7    0.000    0.000    0.001    0.000 __init__.py:1373(info)
      201    0.000    0.000    0.001    0.000 skill_bar.py:45(update)
     7654    0.001    0.000    0.001    0.000 {method 'clear' of 'dict' objects}
        1    0.000    0.000    0.001    0.001 entity.py:482(take_turn)
       74    0.000    0.000    0.001    0.000 html_parser.py:118(add_text)
       63    0.000    0.000    0.001    0.000 utility.py:188(value_to_member)
       51    0.000    0.000    0.001    0.000 world.py:385(_tile_has_specific_entity)
      568    0.001    0.000    0.001    0.000 ui_text_box.py:379(process_event)
     1082    0.001    0.000    0.001    0.000 query.py:50(__init__)
        5    0.000    0.000    0.001    0.000 state.py:71(set_new)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
       51    0.000    0.000    0.001    0.000 manager.py:345(should_camera_move)
      201    0.000    0.000    0.001    0.000 message_log.py:36(update)
       26    0.000    0.000    0.001    0.000 __init__.py:869(format)
       26    0.000    0.000    0.001    0.000 __init__.py:606(format)
       10    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
       74    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
       38    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
       10    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
      202    0.001    0.000    0.001    0.000 ecs.py:265(process_pending_deletions)
      356    0.000    0.000    0.001    0.000 query.py:225(<listcomp>)
      413    0.001    0.000    0.001    0.000 state.py:45(get_current)
      201    0.000    0.000    0.001    0.000 entity_info.py:47(update)
        2    0.000    0.000    0.001    0.000 chrono.py:24(rebuild_turn_queue)
       59    0.000    0.000    0.001    0.000 entity.py:104(get_name)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       65    0.000    0.000    0.001    0.000 utility.py:94(get_class_members)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
       26    0.000    0.000    0.001    0.000 __init__.py:1011(flush)
      827    0.001    0.000    0.001    0.000 ui_window.py:55(process_event)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
       38    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
      202    0.000    0.000    0.000    0.000 {built-in method pygame.mouse.get_pos}
     1407    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       59    0.000    0.000    0.000    0.000 entity.py:117(get_identity)
       28    0.000    0.000    0.000    0.000 ntpath.py:212(basename)
     1082    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF84D989BA0}
      163    0.000    0.000    0.000    0.000 processors.py:73(_get_pressed_direction)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       26    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
     4880    0.000    0.000    0.000    0.000 {method 'contains' of 'pygame.Rect' objects}
      123    0.000    0.000    0.000    0.000 {method 'size' of 'pygame.font.Font' objects}
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       28    0.000    0.000    0.000    0.000 ntpath.py:178(split)
       26    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
       26    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
      177    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
     1205    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       46    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       15    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
        3    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
        2    0.000    0.000    0.000    0.000 __init__.py:1971(warning)
       72    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:228(update)
       45    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        2    0.000    0.000    0.000    0.000 __init__.py:1385(warning)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
      104    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        4    0.000    0.000    0.000    0.000 {built-in method nt.stat}
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      102    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        3    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
      163    0.000    0.000    0.000    0.000 processors.py:100(_get_pressed_skills_number)
        3    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       15    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
       15    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
       24    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
     1444    0.000    0.000    0.000    0.000 sprite.py:168(update)
       15    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
       15    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
      177    0.000    0.000    0.000    0.000 processors.py:120(_process_stateless_intents)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
     1006    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
      394    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
       26    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
       51    0.000    0.000    0.000    0.000 event.py:53(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       62    0.000    0.000    0.000    0.000 event_core.py:41(publish)
       51    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
       26    0.000    0.000    0.000    0.000 {built-in method time.strftime}
      984    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        2    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
        7    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
      563    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
       58    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
      202    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       56    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
      364    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       87    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
       10    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        7    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      164    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
        2    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
      394    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
      761    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
       32    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        1    0.000    0.000    0.000    0.000 ai.py:68(act)
        1    0.000    0.000    0.000    0.000 combat_stats.py:220(resist_astral)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       26    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
        1    0.000    0.000    0.000    0.000 entity_info.py:97(create_entity_image_section)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       24    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
       38    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       27    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
       80    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      126    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      125    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       62    0.000    0.000    0.000    0.000 event_core.py:15(notify)
        1    0.000    0.000    0.000    0.000 combat_stats.py:118(accuracy)
        1    0.000    0.000    0.000    0.000 combat_stats.py:195(resist_chemical)
       26    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
        4    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
        3    0.000    0.000    0.000    0.000 entity.py:174(create)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       26    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 combat_stats.py:143(resist_burn)
        1    0.000    0.000    0.000    0.000 combat_stats.py:169(resist_cold)
      741    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 combat_stats.py:245(resist_mundane)
        1    0.000    0.000    0.000    0.000 combat_stats.py:310(rush)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       24    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        3    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
       26    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
       26    0.000    0.000    0.000    0.000 cp1252.py:18(encode)
       74    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
       52    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
       52    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
       62    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
       84    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       51    0.000    0.000    0.000    0.000 god_handler.py:26(process_event)
       26    0.000    0.000    0.000    0.000 __init__.py:432(format)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
       17    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
       10    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       26    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      209    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
        1    0.000    0.000    0.000    0.000 main.py:238(initialise_event_handlers)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       26    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       42    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
       65    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:153(_get_pretty_queue)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
       26    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
       52    0.000    0.000    0.000    0.000 __init__.py:856(release)
       51    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
       74    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
       24    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       26    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
       10    0.000    0.000    0.000    0.000 parser.py:96(reset)
       52    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
      107    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      104    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
       78    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
       38    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
       52    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       26    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
      146    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       78    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       26    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       42    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
        2    0.000    0.000    0.000    0.000 entity_handler.py:225(_process_end_turn)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       55    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       77    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       38    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
       24    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       26    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       28    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       72    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
       77    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       77    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        1    0.000    0.000    0.000    0.000 event.py:166(__init__)
      120    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        6    0.000    0.000    0.000    0.000 event.py:88(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        2    0.000    0.000    0.000    0.000 entity.py:377(spend_time)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       51    0.000    0.000    0.000    0.000 world.py:363(_is_tile_blocking_movement)
        4    0.000    0.000    0.000    0.000 entity.py:332(add_component)
        1    0.000    0.000    0.000    0.000 camera.py:58(handle_events)
       26    0.000    0.000    0.000    0.000 threading.py:1052(name)
       44    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       53    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 event.py:70(__init__)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       10    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        3    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
      112    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        2    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        4    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
        8    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        3    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       46    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
       26    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       24    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       26    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       52    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       28    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       26    0.000    0.000    0.000    0.000 {built-in method time.time}
       64    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        4    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
        8    0.000    0.000    0.000    0.000 {built-in method math.sin}
       84    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       43    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        3    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       38    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
       55    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
       15    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
        1    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       14    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
       39    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       42    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       10    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       15    0.000    0.000    0.000    0.000 {method 'title' of 'str' objects}
       10    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        2    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
        1    0.000    0.000    0.000    0.000 event.py:80(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        1    0.000    0.000    0.000    0.000 main.py:188(disable_profiling)
        1    0.000    0.000    0.000    0.000 event.py:156(__init__)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
        1    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        1    0.000    0.000    0.000    0.000 ui_button.py:340(select)
       30    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        5    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        3    0.000    0.000    0.000    0.000 component.py:82(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:23(__init__)
        8    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        4    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        2    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
       34    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        3    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        6    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        8    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        1    0.000    0.000    0.000    0.000 ui_button.py:348(unselect)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        1    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
        9    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        2    0.000    0.000    0.000    0.000 component.py:56(__init__)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:24(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        4    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
        2    0.000    0.000    0.000    0.000 component.py:31(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:28(__init__)
        4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.post}
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        2    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 entity_info.py:79(cleanse)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'capitalize' of 'str' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 component.py:118(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        2    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        2    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.Event}
        2    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        1    0.000    0.000    0.000    0.000 entity_info.py:59(set_entity)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 skill_bar.py:51(handle_events)
        1    0.000    0.000    0.000    0.000 entity_info.py:53(handle_events)
        1    0.000    0.000    0.000    0.000 message_log.py:42(handle_events)
        1    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)


