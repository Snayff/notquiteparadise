Tue Mar 17 15:57:43 2020    logs/profiling/profile.dump

         5411286 function calls (5016256 primitive calls) in 53.684 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.263    0.263   53.642   53.642 main.py:78(game_loop)
      783    0.001    0.000   27.898    0.036 event_core.py:21(update)
     1566   17.877    0.011   17.877    0.011 {method 'tick' of 'Clock' objects}
       56    0.000    0.000   14.191    0.253 entity_handler.py:28(process_event)
       56    0.000    0.000   11.168    0.199 interaction_handler.py:25(process_event)
       21    0.000    0.000   11.161    0.531 interaction_handler.py:157(_apply_effects_to_tiles)
        7    0.000    0.000   11.161    1.594 interaction_handler.py:122(_process_entity_collision)
        7    0.000    0.000   11.159    1.594 skill.py:201(process_effect)
        1   11.157   11.157   11.157   11.157 skill.py:227(_process_trigger_skill_effect)
        7    0.000    0.000    9.107    1.301 entity_handler.py:128(process_skill)
        1    9.102    9.102    9.102    9.102 skill.py:110(use)
      783    0.005    0.000    8.943    0.011 state.py:38(get_delta_time)
      783    0.003    0.000    8.941    0.011 state.py:63(update_clock)
        2    5.017    2.508    5.025    2.513 entity_handler.py:50(process_move)
      783    0.011    0.000    3.653    0.005 manager.py:73(draw)
      783    0.003    0.000    3.598    0.005 manager.py:54(update)
      783    0.209    0.000    3.595    0.005 ui_manager.py:122(update)
   255910    2.533    0.000    2.533    0.000 {method 'blit' of 'pygame.Surface' objects}
       63    0.000    0.000    2.525    0.040 ui_handler.py:30(process_event)
       15    0.000    0.000    2.466    0.164 ui_handler.py:207(update_camera)
       15    0.000    0.000    2.426    0.162 manager.py:295(update_camera_grid)
       15    0.015    0.001    2.426    0.162 camera.py:106(update_grid)
     2267    0.029    0.000    2.384    0.001 ui_button.py:30(__init__)
       28    0.000    0.000    2.303    0.082 ui_handler.py:48(process_entity_event)
      783    0.120    0.000    2.248    0.003 sprite.py:453(update)
     2267    0.123    0.000    2.242    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
    65929    0.162    0.000    1.808    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
460923/65929    1.546    0.000    1.634    0.000 ui_appearance_theme.py:322(get_next_id_node)
      797    0.768    0.001    1.563    0.002 camera.py:79(update_game_map)
      782    0.004    0.000    1.541    0.002 camera.py:72(update)
      783    0.006    0.000    1.342    0.002 ui_manager.py:173(draw_ui)
      783    0.212    0.000    1.336    0.002 sprite.py:753(draw)
      787    1.109    0.001    1.109    0.001 {built-in method pygame.transform.scale}
    34091    0.089    0.000    1.023    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
   124498    0.496    0.000    0.882    0.000 ui_element.py:121(check_hover)
    20489    0.040    0.000    0.597    0.000 ui_appearance_theme.py:428(get_misc_data)
   122365    0.234    0.000    0.533    0.000 ui_button.py:197(update)
     2267    0.014    0.000    0.278    0.000 ui_button.py:97(set_any_images_from_theme)
      783    0.274    0.000    0.274    0.000 {built-in method pygame.display.flip}
     9108    0.259    0.000    0.272    0.000 sprite.py:913(get_sprites_from_layer)
     9068    0.017    0.000    0.264    0.000 ui_appearance_theme.py:366(get_image)
   122339    0.137    0.000    0.264    0.000 ui_button.py:138(hover_point)
   122365    0.081    0.000    0.253    0.000 drawable_shape.py:36(update)
    11199    0.073    0.000    0.211    0.000 rect_drawable_shape.py:118(redraw_state)
      783    0.178    0.000    0.178    0.000 {built-in method pygame.event.get}
       28    0.000    0.000    0.176    0.006 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.171    0.171 ui_handler.py:111(init_game_ui)
   119559    0.165    0.000    0.165    0.000 camera.py:234(world_to_screen_position)
      220    0.001    0.000    0.146    0.001 manager.py:60(process_ui_events)
      220    0.048    0.000    0.145    0.001 ui_manager.py:86(process_events)
     2267    0.018    0.000    0.135    0.000 ui_button.py:537(rebuild_shape)
   122532    0.112    0.000    0.127    0.000 rect_drawable_shape.py:84(collide_point)
     2281    0.007    0.000    0.117    0.000 rect_drawable_shape.py:22(__init__)
     1159    0.109    0.000    0.109    0.000 {method 'fill' of 'pygame.Surface' objects}
     2291    0.022    0.000    0.106    0.000 ui_element.py:23(__init__)
     2281    0.031    0.000    0.104    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
   252907    0.084    0.000    0.101    0.000 sprite.py:208(alive)
     2267    0.010    0.000    0.089    0.000 ui_appearance_theme.py:405(get_font)
  1116421    0.079    0.000    0.079    0.000 {method 'append' of 'list' objects}
    11199    0.062    0.000    0.062    0.000 surface_cache.py:119(build_cache_id)
     2281    0.011    0.000    0.061    0.000 drawable_shape.py:45(redraw_all_states)
        7    0.014    0.002    0.056    0.008 world.py:445(update_tile_visibility)
    13509    0.017    0.000    0.055    0.000 _internal.py:24(wrapper)
       15    0.011    0.001    0.052    0.003 ui_container.py:116(clear)
     2291    0.006    0.000    0.051    0.000 ui_container.py:42(add_element)
    11259    0.051    0.000    0.051    0.000 {method 'copy' of 'pygame.Surface' objects}
   122365    0.048    0.000    0.048    0.000 ui_button.py:154(can_hover)
       10    0.000    0.000    0.045    0.005 ui_text_box.py:50(__init__)
   882337    0.045    0.000    0.045    0.000 {built-in method builtins.len}
       10    0.000    0.000    0.045    0.004 ui_text_box.py:492(rebuild_from_changed_theme_data)
       10    0.000    0.000    0.043    0.004 ui_text_box.py:110(rebuild)
        1    0.000    0.000    0.042    0.042 main.py:183(initialise_game)
     4412    0.042    0.000    0.042    0.000 ui_container.py:62(recalculate_container_layer_thickness)
     2109    0.003    0.000    0.041    0.000 ui_button.py:130(kill)
        8    0.000    0.000    0.041    0.005 message_log.py:49(add_message)
     2121    0.004    0.000    0.039    0.000 ui_element.py:114(kill)
        7    0.000    0.000    0.039    0.006 ui_handler.py:155(process_ui_event)
        7    0.000    0.000    0.039    0.006 ui_handler.py:238(process_message)
        7    0.000    0.000    0.039    0.006 manager.py:444(add_to_message_log)
        2    0.000    0.000    0.039    0.019 entity.py:224(create_actor)
      310    0.002    0.000    0.036    0.000 __init__.py:1496(_log)
      270    0.001    0.000    0.033    0.000 __init__.py:1996(debug)
      270    0.001    0.000    0.033    0.000 __init__.py:1361(debug)
     2291    0.004    0.000    0.031    0.000 sprite.py:121(__init__)
        2    0.008    0.004    0.031    0.016 world.py:26(create_fov_map)
      966    0.011    0.000    0.030    0.000 ui_text_box.py:205(update)
       15    0.000    0.000    0.028    0.002 manager.py:286(update_camera_game_map)
     2291    0.009    0.000    0.027    0.000 sprite.py:126(add)
    13510    0.026    0.000    0.027    0.000 {built-in method _warnings.warn}
        4    0.000    0.000    0.024    0.006 ui_vertical_scroll_bar.py:22(__init__)
     2121    0.004    0.000    0.023    0.000 ui_container.py:52(remove_element)
     2291    0.005    0.000    0.022    0.000 ui_element.py:104(change_layer)
      184    0.001    0.000    0.021    0.000 screen_message.py:34(update)
   130516    0.021    0.000    0.021    0.000 ui_manager.py:167(get_mouse_position)
    24839    0.020    0.000    0.021    0.000 ui_button.py:257(process_event)
    11199    0.017    0.000    0.018    0.000 drawable_shape.py:122(rebuild_images_and_text)
      310    0.001    0.000    0.018    0.000 __init__.py:1521(handle)
      123    0.000    0.000    0.018    0.000 ui_text_box.py:347(redraw_from_chunks)
     5320    0.011    0.000    0.018    0.000 world.py:55(get_tile)
   122378    0.017    0.000    0.017    0.000 {method 'union' of 'pygame.Rect' objects}
     4693    0.012    0.000    0.017    0.000 ui_container.py:124(check_hover)
      310    0.001    0.000    0.017    0.000 __init__.py:1575(callHandlers)
   129368    0.017    0.000    0.017    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     2299    0.014    0.000    0.017    0.000 sprite.py:822(change_layer)
   252907    0.017    0.000    0.017    0.000 {built-in method _operator.truth}
   263054    0.017    0.000    0.017    0.000 {method 'reverse' of 'list' objects}
     2291    0.015    0.000    0.016    0.000 sprite.py:646(add_internal)
      310    0.001    0.000    0.016    0.000 __init__.py:892(handle)
       14    0.000    0.000    0.016    0.001 ui_text_box.py:310(parse_html_into_style_data)
      310    0.000    0.000    0.014    0.000 __init__.py:1123(emit)
     1885    0.014    0.000    0.014    0.000 ui_manager.py:104(<listcomp>)
      310    0.001    0.000    0.014    0.000 __init__.py:1022(emit)
      783    0.003    0.000    0.014    0.000 processors.py:16(process_all)
   131379    0.013    0.000    0.013    0.000 {method 'colliderect' of 'pygame.Rect' objects}
      123    0.002    0.000    0.012    0.000 ui_text_box.py:327(redraw_from_text_block)
      310    0.001    0.000    0.012    0.000 __init__.py:1481(makeRecord)
     2518    0.005    0.000    0.012    0.000 ui_font_dictionary.py:89(find_font)
      310    0.004    0.000    0.011    0.000 __init__.py:293(__init__)
       15    0.000    0.000    0.011    0.001 manager.py:275(update_cameras_tiles)
     2121    0.003    0.000    0.011    0.000 sprite.py:183(kill)
       15    0.004    0.000    0.011    0.001 camera.py:168(update_camera_tiles)
       14    0.000    0.000    0.011    0.001 text_block.py:16(__init__)
      783    0.010    0.000    0.011    0.000 processors.py:23(_process_aesthetic_update)
       14    0.002    0.000    0.011    0.001 text_block.py:40(redraw)
      783    0.002    0.000    0.010    0.000 ui_appearance_theme.py:158(update_shape_cache)
       28    0.000    0.000    0.009    0.000 game_handler.py:26(process_event)
     1003    0.006    0.000    0.009    0.000 sprite.py:814(layers)
    10500    0.005    0.000    0.009    0.000 libtcodpy.py:3300(map_is_in_fov)
      783    0.001    0.000    0.008    0.000 surface_cache.py:24(update)
     2281    0.002    0.000    0.007    0.000 drawable_shape.py:50(compute_aligned_text_rect)
     2121    0.004    0.000    0.007    0.000 sprite.py:728(remove_internal)
     3911    0.006    0.000    0.007    0.000 ui_window.py:97(update)
      310    0.000    0.000    0.007    0.000 __init__.py:869(format)
    11199    0.007    0.000    0.007    0.000 surface_cache.py:109(find_surface_in_cache)
       62    0.000    0.000    0.007    0.000 ui_text_box.py:462(set_active_effect)
      310    0.002    0.000    0.007    0.000 __init__.py:606(format)
        2    0.000    0.000    0.006    0.003 entity.py:324(build_characteristic_sprites)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
     2281    0.006    0.000    0.006    0.000 drawable_shape.py:11(__init__)
     5341    0.005    0.000    0.006    0.000 world.py:347(_is_tile_in_bounds)
     1566    0.006    0.000    0.006    0.000 sprite.py:745(sprites)
      783    0.004    0.000    0.006    0.000 ui_manager.py:158(update_mouse_position)
       30    0.004    0.000    0.005    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
     2287    0.004    0.000    0.005    0.000 ui_element.py:68(create_valid_ids)
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
      202    0.005    0.000    0.005    0.000 {method 'size' of 'pygame.font.Font' objects}
      123    0.002    0.000    0.005    0.000 text_block.py:265(redraw_from_chunks)
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
        1    0.000    0.000    0.005    0.005 manager.py:223(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:16(__init__)
       40    0.000    0.000    0.005    0.000 __init__.py:1986(info)
       40    0.000    0.000    0.005    0.000 __init__.py:1373(info)
      310    0.001    0.000    0.005    0.000 __init__.py:1011(flush)
      312    0.001    0.000    0.004    0.000 ntpath.py:212(basename)
      220    0.001    0.000    0.004    0.000 processors.py:57(process_intent)
    10500    0.004    0.000    0.004    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       14    0.000    0.000    0.004    0.000 parser.py:104(feed)
       14    0.001    0.000    0.004    0.000 parser.py:134(goahead)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
      782    0.002    0.000    0.004    0.000 skill_bar.py:45(update)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
      312    0.002    0.000    0.004    0.000 ntpath.py:178(split)
      385    0.003    0.000    0.004    0.000 ui_vertical_scroll_bar.py:228(update)
       28    0.000    0.000    0.004    0.000 god_handler.py:26(process_event)
     4494    0.004    0.000    0.004    0.000 {method 'remove' of 'list' objects}
     2011    0.004    0.000    0.004    0.000 {built-in method builtins.sorted}
      310    0.002    0.000    0.004    0.000 __init__.py:1451(findCaller)
       63    0.002    0.000    0.004    0.000 styled_chunk.py:8(__init__)
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
     2519    0.003    0.000    0.003    0.000 ui_font_dictionary.py:133(create_font_id)
      310    0.001    0.000    0.003    0.000 __init__.py:539(formatTime)
      205    0.001    0.000    0.003    0.000 processors.py:138(_process_player_turn_intents)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      310    0.003    0.000    0.003    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
     9124    0.003    0.000    0.003    0.000 {built-in method math.floor}
       18    0.000    0.000    0.003    0.000 game_handler.py:42(process_change_game_state)
        7    0.000    0.000    0.003    0.000 pydevd_modify_bytecode.py:213(insert_code)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
      782    0.001    0.000    0.003    0.000 message_log.py:36(update)
        5    0.000    0.000    0.003    0.001 pydevd_modify_bytecode.py:233(_insert_code)
        8    0.000    0.000    0.003    0.000 game_handler.py:81(process_end_turn)
        8    0.000    0.000    0.003    0.000 chrono.py:51(next_turn)
       17    0.000    0.000    0.002    0.000 state.py:71(set_new)
      220    0.002    0.000    0.002    0.000 action.py:12(convert_to_intent)
     2133    0.002    0.000    0.002    0.000 ui_element.py:186(hover_point)
      782    0.001    0.000    0.002    0.000 entity_info.py:45(update)
        5    0.001    0.000    0.002    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
     1594    0.002    0.000    0.002    0.000 state.py:45(get_current)
       63    0.000    0.000    0.002    0.000 parser.py:301(parse_starttag)
     2497    0.002    0.000    0.002    0.000 ui_window_stack.py:73(get_root_window)
      310    0.001    0.000    0.002    0.000 ntpath.py:201(splitext)
     7999    0.002    0.000    0.002    0.000 {built-in method builtins.hasattr}
      128    0.002    0.000    0.002    0.000 {method 'render' of 'pygame.font.Font' objects}
      783    0.002    0.000    0.002    0.000 {built-in method pygame.mouse.get_pos}
    11199    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
     6211    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
      310    0.002    0.000    0.002    0.000 {built-in method time.strftime}
     2281    0.002    0.000    0.002    0.000 drawable_shape.py:46(<listcomp>)
    10678    0.002    0.000    0.002    0.000 world.py:48(get_game_map)
      125    0.000    0.000    0.002    0.000 html_parser.py:118(add_text)
      311    0.001    0.000    0.002    0.000 {method 'write' of '_io.TextIOWrapper' objects}
      126    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
     4685    0.001    0.000    0.001    0.000 {built-in method builtins.min}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     4590    0.001    0.000    0.001    0.000 {method 'insert' of 'list' objects}
     4554    0.001    0.000    0.001    0.000 {built-in method builtins.max}
      624    0.001    0.000    0.001    0.000 ntpath.py:44(normcase)
     2313    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
      125    0.001    0.000    0.001    0.000 html_parser.py:123(add_indexed_style)
       14    0.001    0.000    0.001    0.000 {built-in method nt.stat}
        7    0.000    0.000    0.001    0.000 entity.py:292(create_projectile)
       13    0.000    0.000    0.001    0.000 ui_appearance_theme.py:138(check_need_to_reload)
       63    0.000    0.000    0.001    0.000 html_parser.py:213(handle_starttag)
      310    0.001    0.000    0.001    0.000 genericpath.py:117(_splitext)
      316    0.001    0.000    0.001    0.000 ntpath.py:122(splitdrive)
       14    0.000    0.000    0.001    0.000 html_parser.py:207(__init__)
       14    0.000    0.000    0.001    0.000 html_parser.py:60(__init__)
     5475    0.001    0.000    0.001    0.000 sprite.py:168(update)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
     7782    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
      664    0.001    0.000    0.001    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
        4    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
      783    0.001    0.000    0.001    0.000 {built-in method builtins.any}
     4591    0.001    0.000    0.001    0.000 ui_manager.py:44(get_sprite_group)
        7    0.000    0.000    0.001    0.000 skill.py:92(pay_resource_cost)
        7    0.000    0.000    0.001    0.000 skill.py:73(can_afford_cost)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
       63    0.000    0.000    0.001    0.000 html_parser.py:283(handle_data)
      310    0.000    0.000    0.001    0.000 __init__.py:590(formatMessage)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
     2291    0.001    0.000    0.001    0.000 sprite.py:162(add_internal)
     4544    0.001    0.000    0.001    0.000 {method 'copy' of 'list' objects}
      535    0.001    0.000    0.001    0.000 ui_button.py:170(while_hovering)
      165    0.001    0.000    0.001    0.000 ui_vertical_scroll_bar.py:195(process_event)
      205    0.001    0.000    0.001    0.000 processors.py:71(_get_pressed_direction)
      310    0.000    0.000    0.001    0.000 __init__.py:584(usesTime)
     3911    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
      310    0.001    0.000    0.001    0.000 {built-in method time.gmtime}
       66    0.000    0.000    0.001    0.000 ui_button.py:226(set_position)
       55    0.000    0.000    0.001    0.000 utility.py:188(value_to_member)
     2299    0.001    0.000    0.001    0.000 {method 'pop' of 'dict' objects}
      620    0.000    0.000    0.001    0.000 __init__.py:849(acquire)
      310    0.000    0.000    0.001    0.000 cp1252.py:18(encode)
      235    0.001    0.000    0.001    0.000 entity.py:37(get_player)
      846    0.001    0.000    0.001    0.000 ui_window.py:55(process_event)
      174    0.000    0.000    0.001    0.000 entity.py:86(get_entitys_component)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
     7490    0.001    0.000    0.001    0.000 {method 'contains' of 'pygame.Rect' objects}
       28    0.000    0.000    0.001    0.000 world.py:260(tile_has_tag)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
      310    0.001    0.000    0.001    0.000 __init__.py:432(format)
        1    0.000    0.000    0.001    0.001 warnings.py:96(_showwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
     2291    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
     2133    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
       62    0.000    0.000    0.000    0.000 utility.py:94(get_class_members)
     1235    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
     2281    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
     2177    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
       23    0.000    0.000    0.000    0.000 esper.py:274(get_components)
      220    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
     2291    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
        1    0.000    0.000    0.000    0.000 entity.py:193(create_god)
        7    0.000    0.000    0.000    0.000 god_handler.py:74(process_interventions)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
        9    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      227    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       48    0.000    0.000    0.000    0.000 {built-in method pygame.transform.smoothscale}
       10    0.000    0.000    0.000    0.000 entity.py:166(create)
      220    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
      620    0.000    0.000    0.000    0.000 __init__.py:856(release)
     2276    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
      310    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
       53    0.000    0.000    0.000    0.000 surface_cache.py:80(split_rect)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        7    0.000    0.000    0.000    0.000 entity.py:412(consider_intervening)
       23    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
     2117    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
       52    0.000    0.000    0.000    0.000 entity.py:96(get_name)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
        4    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:104(rebuild)
     1162    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
       59    0.000    0.000    0.000    0.000 entity.py:317(add_component)
      310    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
      310    0.000    0.000    0.000    0.000 {built-in method _codecs.charmap_encode}
        1    0.000    0.000    0.000    0.000 chrono.py:23(build_new_turn_queue)
      620    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
      205    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
        9    0.000    0.000    0.000    0.000 ui_manager.py:59(get_shadow)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
       24    0.000    0.000    0.000    0.000 esper.py:270(get_component)
        7    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
      310    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       20    0.000    0.000    0.000    0.000 entity.py:123(get_primary_stat)
     2121    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
       14    0.000    0.000    0.000    0.000 world.py:359(_is_tile_blocking_movement)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.compile}
      313    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
       52    0.000    0.000    0.000    0.000 entity.py:109(get_identity)
       59    0.000    0.000    0.000    0.000 esper.py:196(add_component)
       62    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
      930    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        7    0.000    0.000    0.000    0.000 world.py:438(recompute_fov)
        9    0.000    0.000    0.000    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       66    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
      255    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
       26    0.000    0.000    0.000    0.000 ui_button.py:381(in_hold_range)
      310    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       91    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
      949    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
     1566    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
       62    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
       14    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
        3    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:167(kill)
       24    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
      259    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       14    0.000    0.000    0.000    0.000 interaction_handler.py:50(_process_move)
       42    0.000    0.000    0.000    0.000 utility.py:107(lerp)
       14    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       63    0.000    0.000    0.000    0.000 event_core.py:38(publish)
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
       30    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
      312    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
      622    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
       14    0.000    0.000    0.000    0.000 world.py:395(_tile_has_other_entity)
      862    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       63    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       61    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      128    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
      310    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      385    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
      382    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
      206    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
      865    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       66    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      310    0.000    0.000    0.000    0.000 threading.py:1052(name)
      223    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
      139    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.000    0.000 chrono.py:83(next_round)
       21    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
      205    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
       30    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
      125    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
      318    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
       15    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        7    0.000    0.000    0.000    0.000 world.py:77(get_direction)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
      491    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
        4    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
        3    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:52(_pydev_stop_at_break)
       63    0.000    0.000    0.000    0.000 event_core.py:12(notify)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
      623    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       30    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        7    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
      310    0.000    0.000    0.000    0.000 {built-in method time.time}
      165    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
       46    0.000    0.000    0.000    0.000 utility.py:121(clamp)
      312    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       94    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
     1239    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        7    0.000    0.000    0.000    0.000 random.py:344(choices)
       59    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
      128    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       14    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        4    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
      310    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
       14    0.000    0.000    0.000    0.000 event.py:53(__init__)
        4    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
      622    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        7    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       20    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        7    0.000    0.000    0.000    0.000 entity.py:67(get_entities_and_components_in_area)
        8    0.000    0.000    0.000    0.000 entity_handler.py:211(process_end_turn)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
        9    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
        5    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
       28    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
      174    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
      119    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
       63    0.000    0.000    0.000    0.000 event_core.py:62(__init__)
        1    0.000    0.000    0.000    0.000 main.py:210(initialise_event_handlers)
        4    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
        7    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
       18    0.000    0.000    0.000    0.000 event.py:122(__init__)
        4    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
        4    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        4    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
       14    0.000    0.000    0.000    0.000 parser.py:96(reset)
       28    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
       14    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        7    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       63    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        8    0.000    0.000    0.000    0.000 entity.py:362(spend_time)
        7    0.000    0.000    0.000    0.000 event.py:174(__init__)
      127    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       30    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
       62    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
       63    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        7    0.000    0.000    0.000    0.000 event.py:76(__init__)
       28    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
      188    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        7    0.000    0.000    0.000    0.000 event.py:30(__init__)
      120    0.000    0.000    0.000    0.000 esper.py:278(try_component)
      118    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
      123    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
        1    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
       61    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        3    0.000    0.000    0.000    0.000 _collections_abc.py:657(get)
       39    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        8    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
       30    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
       66    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
       62    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        7    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
       86    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       10    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
      188    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
        8    0.000    0.000    0.000    0.000 event.py:104(__init__)
       23    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        3    0.000    0.000    0.000    0.000 os.py:673(__getitem__)
        2    0.000    0.000    0.000    0.000 manager.py:264(move_camera)
       14    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       30    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       10    0.000    0.000    0.000    0.000 event_core.py:50(subscribe)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        4    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
        9    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        5    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
       21    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
       15    0.000    0.000    0.000    0.000 camera.py:186(set_tiles)
       61    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
      130    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       67    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        5    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       23    0.000    0.000    0.000    0.000 chrono.py:115(get_turn_holder)
       68    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        2    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        7    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
       63    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
       30    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       10    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 camera.py:224(move_camera)
        7    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       10    0.000    0.000    0.000    0.000 {built-in method math.sin}
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
       64    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
       10    0.000    0.000    0.000    0.000 event_core.py:15(subscribe)
       14    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       34    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        7    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        9    0.000    0.000    0.000    0.000 _weakrefset.py:38(_remove)
       69    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        7    0.000    0.000    0.000    0.000 ai.py:34(__init__)
       14    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        7    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       14    0.000    0.000    0.000    0.000 camera.py:195(set_player_tile)
       14    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
       10    0.000    0.000    0.000    0.000 component.py:80(__init__)
       22    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
       22    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
        3    0.000    0.000    0.000    0.000 os.py:743(encodekey)
        4    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
       21    0.000    0.000    0.000    0.000 entity.py:77(<genexpr>)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        4    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
        2    0.000    0.000    0.000    0.000 entity.py:116(get_combat_stats)
        3    0.000    0.000    0.000    0.000 component.py:46(__init__)
       22    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        4    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:21(update_globals_dict)
        8    0.000    0.000    0.000    0.000 chrono.py:106(add_time)
        5    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        7    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
        7    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       15    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        2    0.000    0.000    0.000    0.000 <string>:1(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
       40    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
        9    0.000    0.000    0.000    0.000 component.py:37(__init__)
       10    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        4    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        1    0.000    0.000    0.000    0.000 event.py:114(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        7    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
       16    0.000    0.000    0.000    0.000 chrono.py:129(get_time_in_round)
        1    0.000    0.000    0.000    0.000 ui_button.py:340(select)
        1    0.000    0.000    0.000    0.000 main.py:160(disable_profiling)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        3    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        5    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        8    0.000    0.000    0.000    0.000 interaction_handler.py:93(_process_end_turn)
        1    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
        8    0.000    0.000    0.000    0.000 chrono.py:143(get_time_of_last_turn)
       12    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       24    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       15    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        7    0.000    0.000    0.000    0.000 component.py:113(__init__)
        3    0.000    0.000    0.000    0.000 pydev_log.py:16(debug)
        5    0.000    0.000    0.000    0.000 event_core.py:46(__init__)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        2    0.000    0.000    0.000    0.000 component.py:176(__init__)
        3    0.000    0.000    0.000    0.000 os.py:737(check_str)
        8    0.000    0.000    0.000    0.000 chrono.py:180(set_time_of_last_turn)
       15    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        1    0.000    0.000    0.000    0.000 event.py:132(__init__)
        1    0.000    0.000    0.000    0.000 ui_button.py:348(unselect)
        3    0.000    0.000    0.000    0.000 component.py:61(__init__)
        8    0.000    0.000    0.000    0.000 chrono.py:166(set_time_in_round)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        4    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:106(_process_end_round)
        5    0.000    0.000    0.000    0.000 {built-in method __new__ of type object at 0x00007FF966139BA0}
        3    0.000    0.000    0.000    0.000 component.py:128(__init__)
        1    0.000    0.000    0.000    0.000 camera.py:58(handle_events)
        8    0.000    0.000    0.000    0.000 chrono.py:136(get_time)
        1    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
        2    0.000    0.000    0.000    0.000 chrono.py:159(set_turn_holder)
        5    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:25(__init__)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        5    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        3    0.000    0.000    0.000    0.000 pydevd_constants.py:479(get_global_debugger)
        3    0.000    0.000    0.000    0.000 {_pydevd_frame_eval.pydevd_frame_evaluator_win32_37_64.get_thread_info_py}
        4    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
       10    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 component.py:71(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:22(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        9    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        4    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.post}
        5    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 chrono.py:99(increment_round)
        1    0.000    0.000    0.000    0.000 chrono.py:173(set_turn_queue)
        2    0.000    0.000    0.000    0.000 ui_element.py:220(select)
        2    0.000    0.000    0.000    0.000 ui_element.py:226(unselect)
        2    0.000    0.000    0.000    0.000 component.py:89(__init__)
        1    0.000    0.000    0.000    0.000 component.py:168(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        1    0.000    0.000    0.000    0.000 {built-in method pygame.event.Event}
        2    0.000    0.000    0.000    0.000 chrono.py:122(get_turn_queue)
        2    0.000    0.000    0.000    0.000 component.py:97(__init__)
        2    0.000    0.000    0.000    0.000 component.py:105(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 ui_window.py:161(unselect)
        1    0.000    0.000    0.000    0.000 entity_info.py:51(handle_events)
        1    0.000    0.000    0.000    0.000 ui_window.py:155(select)
        1    0.000    0.000    0.000    0.000 skill_bar.py:51(handle_events)
        1    0.000    0.000    0.000    0.000 chrono.py:150(get_round)
        1    0.000    0.000    0.000    0.000 message_log.py:42(handle_events)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


