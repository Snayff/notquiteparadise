Wed Feb 26 13:42:09 2020    logs/profiling/profile.dump

         2629688 function calls (2546879 primitive calls) in 50.380 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.551    0.551   50.349   50.349 engine.py:63(game_loop)
     2996   39.558    0.013   39.558    0.013 {method 'tick' of 'Clock' objects}
     1498    0.007    0.000   23.676    0.016 game_manager.py:25(update)
     1498    0.006    0.000   23.669    0.016 state_methods.py:66(update_clock)
     1498    0.010    0.000   15.905    0.011 state_methods.py:50(get_delta_time)
     1498    0.035    0.000    6.680    0.004 ui_manager.py:47(draw)
   122203    3.260    0.000    3.260    0.000 {method 'blit' of 'pygame.Surface' objects}
     1530    2.289    0.001    2.289    0.001 {built-in method pygame.transform.scale}
     1498    0.009    0.000    1.811    0.001 ui_manager.py:24(update)
     1498    0.232    0.000    1.802    0.001 ui_manager.py:122(update)
     1498    0.008    0.000    1.671    0.001 ui_manager.py:173(draw_ui)
     1498    0.198    0.000    1.663    0.001 sprite.py:753(draw)
     1498    0.994    0.001    0.994    0.001 {built-in method pygame.event.get}
   112501    0.503    0.000    0.796    0.000 ui_element.py:121(check_hover)
     1498    0.658    0.000    0.658    0.000 {built-in method pygame.display.flip}
     1498    0.132    0.000    0.597    0.000 sprite.py:453(update)
      342    0.005    0.000    0.376    0.001 ui_button.py:30(__init__)
      342    0.020    0.000    0.353    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
      696    0.001    0.000    0.305    0.000 ui_manager.py:36(handle_ui_events)
       19    0.000    0.000    0.304    0.016 data_editor.py:100(handle_events)
    11633    0.031    0.000    0.295    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
70800/11633    0.249    0.000    0.262    0.000 ui_appearance_theme.py:322(get_next_id_node)
      696    0.003    0.000    0.234    0.000 ui_manager.py:30(process_ui_events)
      696    0.107    0.000    0.231    0.000 ui_manager.py:86(process_events)
        6    0.001    0.000    0.230    0.038 data_editor.py:565(_load_details)
    53720    0.115    0.000    0.219    0.000 ui_button.py:197(update)
     2123    0.217    0.000    0.217    0.000 {method 'fill' of 'pygame.Surface' objects}
     5841    0.019    0.000    0.169    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
    11647    0.026    0.000    0.168    0.000 ui_drop_down_menu.py:420(update)
    11672    0.140    0.000    0.156    0.000 sprite.py:913(get_sprites_from_layer)
    53687    0.073    0.000    0.142    0.000 ui_button.py:138(hover_point)
     1498    0.002    0.000    0.140    0.000 event_hub.py:21(update)
        7    0.000    0.000    0.137    0.020 ui_handler.py:28(process_event)
        7    0.000    0.000    0.137    0.020 ui_handler.py:70(process_game_event)
       36    0.001    0.000    0.124    0.003 data_editor.py:295(_create_one_from_options_field)
        2    0.000    0.000    0.123    0.061 ui_handler.py:108(init_game_ui)
       38    0.001    0.000    0.114    0.003 ui_drop_down_menu.py:351(__init__)
       41    0.001    0.000    0.113    0.003 ui_drop_down_menu.py:283(start)
        6    0.001    0.000    0.107    0.018 ui_drop_down_menu.py:139(start)
        2    0.000    0.000    0.104    0.052 ui_handler.py:199(update_camera)
     3903    0.007    0.000    0.101    0.000 ui_appearance_theme.py:428(get_misc_data)
        2    0.000    0.000    0.096    0.048 element_methods.py:222(update_camera_grid)
        2    0.001    0.000    0.096    0.048 camera.py:106(update_grid)
   191919    0.072    0.000    0.086    0.000 sprite.py:208(alive)
    53677    0.034    0.000    0.085    0.000 drawable_shape.py:36(update)
    53991    0.059    0.000    0.069    0.000 rect_drawable_shape.py:84(collide_point)
       12    0.001    0.000    0.068    0.006 data_editor.py:474(_create_row_of_buttons)
     1615    0.015    0.000    0.068    0.000 rect_drawable_shape.py:118(redraw_state)
        4    0.001    0.000    0.063    0.016 data_editor.py:748(_save_updated_field)
        9    0.000    0.000    0.063    0.007 data_editor.py:392(_create_multiple_from_options_field)
        4    0.006    0.002    0.060    0.015 __init__.py:120(dump)
      696    0.008    0.000    0.049    0.000 input_manager.py:21(update)
      439    0.002    0.000    0.047    0.000 rect_drawable_shape.py:22(__init__)
17788/4404    0.024    0.000    0.046    0.000 encoder.py:413(_iterencode)
      439    0.008    0.000    0.044    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
        1    0.000    0.000    0.042    0.042 data_editor.py:181(_select_new_instance)
      342    0.002    0.000    0.042    0.000 ui_button.py:97(set_any_images_from_theme)
    58781    0.033    0.000    0.041    0.000 ui_element.py:186(hover_point)
     1368    0.003    0.000    0.040    0.000 ui_appearance_theme.py:366(get_image)
13620/4404    0.016    0.000    0.040    0.000 encoder.py:333(_iterencode_dict)
   435884    0.038    0.000    0.038    0.000 {method 'append' of 'list' objects}
      696    0.011    0.000    0.035    0.000 control_methods.py:175(reset_intents)
        1    0.000    0.000    0.033    0.033 data_editor.py:229(_process_edit_action)
        1    0.000    0.000    0.031    0.031 initialisers.py:15(initialise_game)
     3665    0.030    0.000    0.031    0.000 ui_manager.py:104(<listcomp>)
    10828    0.023    0.000    0.031    0.000 ui_text_entry_line.py:352(update)
      342    0.003    0.000    0.031    0.000 ui_button.py:537(rebuild_shape)
      135    0.001    0.000    0.030    0.000 ui_label.py:23(__init__)
      178    0.002    0.000    0.029    0.000 screen_message.py:36(update)
       39    0.001    0.000    0.028    0.001 data_editor.py:449(_create_text_entry_field)
      581    0.006    0.000    0.027    0.000 ui_element.py:23(__init__)
     1938    0.026    0.000    0.026    0.000 {method 'copy' of 'pygame.Surface' objects}
      439    0.002    0.000    0.025    0.000 drawable_shape.py:45(redraw_all_states)
    53720    0.025    0.000    0.025    0.000 ui_button.py:154(can_hover)
      123    0.001    0.000    0.024    0.000 ui_text_box.py:347(redraw_from_chunks)
     1498    0.007    0.000    0.024    0.000 ui_appearance_theme.py:158(update_shape_cache)
    27262    0.022    0.000    0.023    0.000 ui_button.py:257(process_event)
      135    0.002    0.000    0.022    0.000 ui_label.py:128(rebuild_from_changed_theme_data)
      767    0.015    0.000    0.021    0.000 dataclasses.py:994(fields)
   115693    0.021    0.000    0.021    0.000 ui_manager.py:167(get_mouse_position)
     2194    0.013    0.000    0.021    0.000 sprite.py:814(layers)
       39    0.001    0.000    0.019    0.000 ui_text_entry_line.py:38(__init__)
   115999    0.019    0.000    0.019    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
      188    0.002    0.000    0.019    0.000 ui_text_box.py:205(update)
      516    0.002    0.000    0.018    0.000 ui_appearance_theme.py:405(get_font)
     1498    0.004    0.000    0.017    0.000 surface_cache.py:24(update)
        1    0.004    0.004    0.017    0.017 fov_methods.py:20(create_player_fov_map)
       39    0.001    0.000    0.017    0.000 ui_text_entry_line.py:708(rebuild_from_changed_theme_data)
      123    0.002    0.000    0.016    0.000 ui_text_box.py:327(redraw_from_text_block)
    11341    0.013    0.000    0.016    0.000 ui_drop_down_menu.py:327(update)
     1615    0.005    0.000    0.015    0.000 drawable_shape.py:122(rebuild_images_and_text)
     1498    0.011    0.000    0.015    0.000 ui_manager.py:158(update_mouse_position)
     3302    0.004    0.000    0.015    0.000 _internal.py:24(wrapper)
   111902    0.015    0.000    0.015    0.000 {method 'union' of 'pygame.Rect' objects}
   191919    0.015    0.000    0.015    0.000 {built-in method _operator.truth}
   118413    0.014    0.000    0.014    0.000 {method 'colliderect' of 'pygame.Rect' objects}
        3    0.000    0.000    0.013    0.004 data_editor.py:341(_create_edit_detail_field)
     3035    0.009    0.000    0.012    0.000 ui_container.py:124(check_hover)
      581    0.002    0.000    0.012    0.000 ui_container.py:42(add_element)
        2    0.000    0.000    0.012    0.006 element_methods.py:61(init_skill_bar)
        2    0.000    0.000    0.012    0.006 skill_bar.py:12(__init__)
     1615    0.011    0.000    0.011    0.000 surface_cache.py:119(build_cache_id)
   176931    0.011    0.000    0.011    0.000 {built-in method builtins.len}
        6    0.001    0.000    0.011    0.002 ui_drop_down_menu.py:45(rebuild)
        2    0.000    0.000    0.011    0.005 entity_methods.py:294(create_actor)
       11    0.000    0.000    0.010    0.001 data_editor.py:721(_kill_details_fields)
     4478    0.010    0.000    0.010    0.000 {built-in method builtins.sorted}
     3353    0.008    0.000    0.010    0.000 {built-in method _warnings.warn}
       81    0.006    0.000    0.010    0.000 surface_cache.py:29(add_surface_to_long_term_cache)
       87    0.001    0.000    0.010    0.000 data_editor.py:801(kill)
      520    0.001    0.000    0.010    0.000 ui_element.py:114(kill)
     1101    0.009    0.000    0.009    0.000 ui_container.py:62(recalculate_container_layer_thickness)
        5    0.000    0.000    0.009    0.002 ui_text_box.py:50(__init__)
     4409    0.006    0.000    0.009    0.000 {method 'write' of '_io.TextIOWrapper' objects}
        5    0.000    0.000    0.009    0.002 ui_text_box.py:492(rebuild_from_changed_theme_data)
       62    0.000    0.000    0.009    0.000 ui_text_box.py:462(set_active_effect)
        1    0.000    0.000    0.008    0.008 fov_methods.py:34(recompute_player_fov)
        1    0.002    0.002    0.008    0.008 fov_methods.py:68(update_tile_visibility)
      581    0.001    0.000    0.008    0.000 sprite.py:121(__init__)
        5    0.000    0.000    0.008    0.002 ui_text_box.py:110(rebuild)
    58781    0.008    0.000    0.008    0.000 ui_element.py:204(can_hover)
       39    0.001    0.000    0.008    0.000 ui_text_entry_line.py:106(rebuild)
     1482    0.007    0.000    0.007    0.000 {method 'render' of 'pygame.font.Font' objects}
      581    0.003    0.000    0.007    0.000 sprite.py:126(add)
      102    0.000    0.000    0.007    0.000 ui_manager.py:59(get_shadow)
      123    0.002    0.000    0.007    0.000 text_block.py:265(redraw_from_chunks)
     3025    0.006    0.000    0.007    0.000 ui_window.py:97(update)
     1487    0.004    0.000    0.007    0.000 data_editor.py:94(update)
      102    0.003    0.000    0.007    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
        5    0.000    0.000    0.007    0.001 ui_text_box.py:310(parse_html_into_style_data)
     5469    0.006    0.000    0.007    0.000 ui_text_entry_line.py:412(process_event)
       41    0.000    0.000    0.006    0.000 ui_drop_down_menu.py:257(rebuild)
      294    0.000    0.000    0.006    0.000 ui_button.py:130(kill)
       38    0.001    0.000    0.006    0.000 ui_drop_down_menu.py:436(rebuild_from_changed_theme_data)
      520    0.001    0.000    0.006    0.000 ui_container.py:52(remove_element)
     1587    0.003    0.000    0.006    0.000 map_methods.py:50(get_tile)
        5    0.000    0.000    0.006    0.001 text_block.py:16(__init__)
      590    0.001    0.000    0.006    0.000 ui_element.py:104(change_layer)
        5    0.000    0.000    0.006    0.001 text_block.py:40(redraw)
        1    0.000    0.000    0.005    0.005 element_methods.py:376(create_screen_message)
        1    0.000    0.000    0.005    0.005 screen_message.py:18(__init__)
    16387    0.005    0.000    0.005    0.000 dataclasses.py:1009(<genexpr>)
      135    0.002    0.000    0.005    0.000 ui_label.py:61(rebuild)
    25312    0.005    0.000    0.005    0.000 ui_element.py:210(process_event)
    39153    0.005    0.000    0.005    0.000 sprite.py:168(update)
     1498    0.005    0.000    0.005    0.000 {built-in method pygame.mouse.get_pos}
      527    0.001    0.000    0.005    0.000 ui_font_dictionary.py:89(find_font)
        2    0.000    0.000    0.005    0.002 element_methods.py:213(update_camera_game_map)
        2    0.004    0.002    0.005    0.002 camera.py:71(update_game_map)
      306    0.004    0.000    0.005    0.000 ui_drop_down_menu.py:213(update)
      618    0.004    0.000    0.005    0.000 sprite.py:822(change_layer)
        2    0.000    0.000    0.004    0.002 element_methods.py:37(init_message_log)
      696    0.003    0.000    0.004    0.000 control_methods.py:185(process_stateless_intents)
        2    0.000    0.000    0.004    0.002 message_log.py:18(__init__)
       84    0.001    0.000    0.004    0.000 ui_text_entry_line.py:212(redraw)
       38    0.000    0.000    0.004    0.000 ui_drop_down_menu.py:412(kill)
      581    0.004    0.000    0.004    0.000 sprite.py:646(add_internal)
     2996    0.004    0.000    0.004    0.000 sprite.py:745(sprites)
   940/62    0.001    0.000    0.004    0.000 extend_json.py:42(default)
        1    0.000    0.000    0.004    0.004 ui_handler.py:130(init_dev_ui)
        1    0.000    0.000    0.004    0.004 element_methods.py:87(init_skill_editor)
        1    0.000    0.000    0.004    0.004 data_editor.py:44(__init__)
      122    0.000    0.000    0.004    0.000 ui_text_entry_line.py:331(redraw_cursor)
    15326    0.004    0.000    0.004    0.000 ui_button.py:304(check_pressed)
    14624    0.003    0.000    0.003    0.000 {built-in method builtins.setattr}
        1    0.000    0.000    0.003    0.003 data_editor.py:270(_create_data_category_selector)
        1    0.000    0.000    0.003    0.003 map_methods.py:33(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:14(__init__)
        1    0.000    0.000    0.003    0.003 data_editor.py:160(_select_new_category)
        1    0.000    0.000    0.003    0.003 data_editor.py:283(_create_data_instance_selector)
       81    0.000    0.000    0.003    0.000 surface_cache.py:21(add_surface_to_cache)
        2    0.000    0.000    0.003    0.001 element_methods.py:193(update_cameras_tiles)
        1    0.000    0.000    0.003    0.003 ui_handler.py:137(close_dev_ui)
        1    0.000    0.000    0.003    0.003 element_methods.py:392(kill_data_editor)
     4406    0.002    0.000    0.003    0.000 cp1252.py:18(encode)
        2    0.000    0.000    0.003    0.001 message_log.py:48(add_message)
     3700    0.003    0.000    0.003    0.000 state_methods.py:26(get_current)
      439    0.001    0.000    0.003    0.000 drawable_shape.py:50(compute_aligned_text_rect)
      520    0.001    0.000    0.003    0.000 sprite.py:183(kill)
        1    0.000    0.000    0.003    0.003 data_editor.py:704(cleanse)
        2    0.000    0.000    0.003    0.001 element_methods.py:73(init_camera)
       62    0.001    0.000    0.003    0.000 extend_json.py:49(<dictcomp>)
        2    0.002    0.001    0.003    0.001 camera.py:19(__init__)
      106    0.003    0.000    0.003    0.000 {built-in method pygame.transform.smoothscale}
       28    0.002    0.000    0.002    0.000 {built-in method nt.stat}
     1498    0.002    0.000    0.002    0.000 {built-in method builtins.any}
    36361    0.002    0.000    0.002    0.000 {method 'reverse' of 'list' objects}
       25    0.000    0.000    0.002    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      135    0.000    0.000    0.002    0.000 ui_appearance_theme.py:447(get_colour)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
        3    0.000    0.000    0.002    0.001 warnings.py:96(_showwarnmsg)
        3    0.000    0.000    0.002    0.001 warnings.py:20(_showwarnmsg_impl)
        6    0.000    0.000    0.002    0.000 ui_drop_down_menu.py:198(finish)
        6    0.000    0.000    0.002    0.000 dataclasses.py:1023(asdict)
      300    0.001    0.000    0.002    0.000 fov_methods.py:45(is_tile_in_fov)
    168/6    0.001    0.000    0.002    0.000 dataclasses.py:1047(_asdict_inner)
       12    0.000    0.000    0.002    0.000 utility_methods.py:23(get_image)
       41    0.000    0.000    0.002    0.000 ui_drop_down_menu.py:320(finish)
      572    0.002    0.000    0.002    0.000 {method 'size' of 'pygame.font.Font' objects}
     2795    0.001    0.000    0.002    0.000 control_methods.py:169(get_intent)
     1587    0.002    0.000    0.002    0.000 map_methods.py:369(_is_tile_in_bounds)
        1    0.000    0.000    0.002    0.002 ui_handler.py:120(close_game_ui)
      679    0.001    0.000    0.002    0.000 control_methods.py:269(process_dev_mode_intents)
        4    0.000    0.000    0.002    0.000 element_methods.py:402(kill_element)
       17    0.002    0.000    0.002    0.000 {built-in method pygame.imageext.load_extended}
      520    0.001    0.000    0.002    0.000 sprite.py:728(remove_internal)
     1800    0.001    0.000    0.002    0.000 libtcodpy.py:3263(map_is_in_fov)
     1498    0.002    0.000    0.002    0.000 display_methods.py:70(get_desired_resolution)
     1500    0.001    0.000    0.002    0.000 libtcodpy.py:3217(map_set_properties)
        9    0.000    0.000    0.002    0.000 ui_window.py:18(__init__)
        6    0.000    0.000    0.001    0.000 __init__.py:1496(_log)
      572    0.001    0.000    0.001    0.000 ui_element.py:68(create_valid_ids)
     1059    0.001    0.000    0.001    0.000 ui_window_stack.py:73(get_root_window)
        8    0.001    0.000    0.001    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      439    0.001    0.000    0.001    0.000 drawable_shape.py:11(__init__)
        7    0.001    0.000    0.001    0.000 {built-in method io.open}
     4646    0.001    0.000    0.001    0.000 {built-in method builtins.getattr}
        3    0.000    0.000    0.001    0.000 styled_chunk.py:8(__init__)
     1615    0.001    0.000    0.001    0.000 surface_cache.py:109(find_surface_in_cache)
        4    0.000    0.000    0.001    0.000 ui_window.py:146(kill)
     4406    0.001    0.000    0.001    0.000 {built-in method _codecs.charmap_encode}
     2992    0.001    0.000    0.001    0.000 {method 'values' of 'dict' objects}
     3444    0.001    0.000    0.001    0.000 ui_window.py:107(get_container)
        3    0.000    0.000    0.001    0.000 warnings.py:117(_formatwarnmsg)
        3    0.000    0.000    0.001    0.000 warnings.py:35(_formatwarnmsg_impl)
     1682    0.001    0.000    0.001    0.000 {method 'remove' of 'list' objects}
        7    0.000    0.000    0.001    0.000 game_handler.py:26(process_event)
     1498    0.001    0.000    0.001    0.000 display_methods.py:79(get_window)
        3    0.000    0.000    0.001    0.000 linecache.py:15(getline)
        3    0.000    0.000    0.001    0.000 linecache.py:37(getlines)
        5    0.000    0.000    0.001    0.000 element_methods.py:126(remove_ui_element)
        3    0.000    0.000    0.001    0.000 linecache.py:82(updatecache)
     1319    0.001    0.000    0.001    0.000 ui_window.py:55(process_event)
        5    0.000    0.000    0.001    0.000 __init__.py:1971(warning)
      5/4    0.000    0.000    0.001    0.000 ui_container.py:108(kill)
        5    0.000    0.000    0.001    0.000 __init__.py:1385(warning)
        8    0.001    0.000    0.001    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
     1500    0.001    0.000    0.001    0.000 tile.py:22(__init__)
      7/6    0.000    0.000    0.001    0.000 ui_container.py:116(clear)
     1498    0.001    0.000    0.001    0.000 world_manager.py:29(update)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     1800    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
      529    0.001    0.000    0.001    0.000 ui_button.py:170(while_hovering)
      528    0.001    0.000    0.001    0.000 ui_font_dictionary.py:133(create_font_id)
     1498    0.001    0.000    0.001    0.000 display_methods.py:61(get_main_surface)
    10068    0.001    0.000    0.001    0.000 {method 'contains' of 'pygame.Rect' objects}
        5    0.000    0.000    0.001    0.000 game_handler.py:48(process_change_game_state)
        6    0.000    0.000    0.001    0.000 __init__.py:1521(handle)
        6    0.000    0.000    0.001    0.000 __init__.py:1575(callHandlers)
     3025    0.001    0.000    0.001    0.000 ui_window.py:116(check_hover)
       11    0.000    0.000    0.001    0.000 ui_container.py:19(__init__)
        6    0.000    0.000    0.001    0.000 __init__.py:892(handle)
     1756    0.001    0.000    0.001    0.000 {built-in method math.floor}
        6    0.000    0.000    0.001    0.000 __init__.py:1123(emit)
        1    0.000    0.000    0.001    0.001 __init__.py:1986(info)
        6    0.000    0.000    0.001    0.000 __init__.py:1022(emit)
     6060    0.001    0.000    0.001    0.000 {built-in method builtins.isinstance}
        1    0.000    0.000    0.001    0.001 __init__.py:1373(info)
      380    0.001    0.000    0.001    0.000 encoder.py:277(_iterencode_list)
       75    0.000    0.000    0.001    0.000 surface_cache.py:80(split_rect)
      684    0.001    0.000    0.001    0.000 drawable_shape.py:86(get_surface)
     2887    0.001    0.000    0.001    0.000 {built-in method builtins.hasattr}
     3175    0.000    0.000    0.000    0.000 map_methods.py:41(get_game_map)
        6    0.000    0.000    0.000    0.000 dataclasses.py:1081(<genexpr>)
      144    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
        5    0.000    0.000    0.000    0.000 parser.py:104(feed)
       16    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
        5    0.000    0.000    0.000    0.000 parser.py:134(goahead)
        6    0.000    0.000    0.000    0.000 __init__.py:1481(makeRecord)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
        6    0.000    0.000    0.000    0.000 __init__.py:293(__init__)
        1    0.000    0.000    0.000    0.000 entity_methods.py:261(create_god)
      109    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
        5    0.000    0.000    0.000    0.000 html_parser.py:207(__init__)
       16    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
     1236    0.000    0.000    0.000    0.000 {method 'insert' of 'list' objects}
        3    0.000    0.000    0.000    0.000 tokenize.py:443(open)
        5    0.000    0.000    0.000    0.000 html_parser.py:60(__init__)
       84    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
      940    0.000    0.000    0.000    0.000 dataclasses.py:1017(is_dataclass)
       25    0.000    0.000    0.000    0.000 entity_methods.py:186(get_primary_stat)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1079(<genexpr>)
     1615    0.000    0.000    0.000    0.000 {method 'popleft' of 'collections.deque' objects}
      439    0.000    0.000    0.000    0.000 drawable_shape.py:46(<listcomp>)
        2    0.000    0.000    0.000    0.000 element_methods.py:49(init_entity_info)
      879    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      837    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        2    0.000    0.000    0.000    0.000 entity_info.py:17(__init__)
        6    0.000    0.000    0.000    0.000 __init__.py:1011(flush)
       62    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
        8    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        2    0.000    0.000    0.000    0.000 combat_stats.py:69(max_hp)
     1187    0.000    0.000    0.000    0.000 ui_manager.py:44(get_sprite_group)
     1554    0.000    0.000    0.000    0.000 {built-in method _json.encode_basestring_ascii}
        3    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
        6    0.000    0.000    0.000    0.000 __init__.py:869(format)
        2    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:36(remove_window)
        6    0.000    0.000    0.000    0.000 __init__.py:606(format)
        6    0.000    0.000    0.000    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       25    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
       61    0.000    0.000    0.000    0.000 text_effects.py:88(update)
       36    0.000    0.000    0.000    0.000 __init__.py:1996(debug)
     3248    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
      581    0.000    0.000    0.000    0.000 sprite.py:162(add_internal)
        8    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
       14    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
     1115    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
       34    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 combat_stats.py:96(max_stamina)
       10    0.000    0.000    0.000    0.000 ntpath.py:212(basename)
       14    0.000    0.000    0.000    0.000 ui_manager.py:279(select_focus_element)
       45    0.000    0.000    0.000    0.000 {built-in method pygame.draw.rect}
      618    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
      174    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
        8    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       27    0.000    0.000    0.000    0.000 ui_manager.py:271(unselect_focus_element)
       10    0.000    0.000    0.000    0.000 ntpath.py:178(split)
        6    0.000    0.000    0.000    0.000 {method 'clear' of 'list' objects}
       87    0.000    0.000    0.000    0.000 data_editor.py:786(__init__)
        3    0.000    0.000    0.000    0.000 parser.py:301(parse_starttag)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3191(map_new)
        1    0.000    0.000    0.000    0.000 map.py:66(__init__)
        1    0.000    0.000    0.000    0.000 data_editor.py:506(_load_field_options)
       39    0.000    0.000    0.000    0.000 ui_text_entry_line.py:189(set_text)
        3    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        1    0.000    0.000    0.000    0.000 combat_stats.py:288(sight_range)
      581    0.000    0.000    0.000    0.000 {method '__contains__' of 'dict' objects}
       34    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
      165    0.000    0.000    0.000    0.000 {method 'get_rect' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
     1002    0.000    0.000    0.000    0.000 encoder.py:353(<lambda>)
        6    0.000    0.000    0.000    0.000 __init__.py:1451(findCaller)
        5    0.000    0.000    0.000    0.000 combat_stats.py:19(vigour)
      619    0.000    0.000    0.000    0.000 ui_manager.py:37(get_theme)
       12    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
       36    0.000    0.000    0.000    0.000 __init__.py:1361(debug)
        6    0.000    0.000    0.000    0.000 __init__.py:539(formatTime)
       36    0.000    0.000    0.000    0.000 data_editor.py:304(<listcomp>)
        3    0.000    0.000    0.000    0.000 entity_methods.py:233(create)
      372    0.000    0.000    0.000    0.000 ui_manager.py:51(get_window_stack)
      346    0.000    0.000    0.000    0.000 {method 'copy' of 'pygame.Rect' objects}
       81    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 _internal.py:291(__init__)
      123    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
       27    0.000    0.000    0.000    0.000 esper.py:196(add_component)
       38    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:20(__init__)
        1    0.000    0.000    0.000    0.000 _internal.py:274(_get_void_ptr)
        5    0.000    0.000    0.000    0.000 combat_stats.py:29(clout)
       38    0.000    0.000    0.000    0.000 ui_drop_down_menu.py:236(__init__)
       42    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
        5    0.000    0.000    0.000    0.000 ui_appearance_theme.py:386(get_font_info)
       28    0.000    0.000    0.000    0.000 control_methods.py:33(check_directions)
        1    0.000    0.000    0.000    0.000 ui_text_entry_line.py:403(select)
        5    0.000    0.000    0.000    0.000 combat_stats.py:39(skullduggery)
        5    0.000    0.000    0.000    0.000 combat_stats.py:59(exactitude)
      390    0.000    0.000    0.000    0.000 ui_element.py:177(while_hovering)
        3    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
        5    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        5    0.000    0.000    0.000    0.000 html_parser.py:118(add_text)
       45    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
        2    0.000    0.000    0.000    0.000 control_methods.py:209(process_player_turn_intents)
        7    0.000    0.000    0.000    0.000 map_handler.py:23(process_event)
      294    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 ui_text_entry_line.py:394(unselect)
        3    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
        4    0.000    0.000    0.000    0.000 ui_text_box.py:102(kill)
      457    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
       18    0.000    0.000    0.000    0.000 ntpath.py:122(splitdrive)
        5    0.000    0.000    0.000    0.000 html_parser.py:123(add_indexed_style)
      520    0.000    0.000    0.000    0.000 {method 'clear' of 'dict' objects}
        3    0.000    0.000    0.000    0.000 html_parser.py:213(handle_starttag)
       20    0.000    0.000    0.000    0.000 ntpath.py:44(normcase)
        1    0.000    0.000    0.000    0.000 game_handler.py:83(process_end_turn)
      191    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        6    0.000    0.000    0.000    0.000 ntpath.py:201(splitext)
       28    0.000    0.000    0.000    0.000 control_methods.py:61(check_actions)
        4    0.000    0.000    0.000    0.000 encoder.py:204(iterencode)
        3    0.000    0.000    0.000    0.000 html_parser.py:283(handle_data)
       84    0.000    0.000    0.000    0.000 data_editor.py:406(<genexpr>)
       34    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        6    0.000    0.000    0.000    0.000 {built-in method time.strftime}
       10    0.000    0.000    0.000    0.000 camera.py:53(update)
       13    0.000    0.000    0.000    0.000 ui_button.py:340(select)
       10    0.000    0.000    0.000    0.000 message_log.py:36(update)
      326    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
       13    0.000    0.000    0.000    0.000 ui_button.py:333(set_inactive)
      380    0.000    0.000    0.000    0.000 {built-in method builtins.id}
       67    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
      302    0.000    0.000    0.000    0.000 fov_methods.py:59(get_player_fov)
       12    0.000    0.000    0.000    0.000 utility_methods.py:71(get_class_members)
        4    0.000    0.000    0.000    0.000 entity_methods.py:34(get_player)
       62    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
        1    0.000    0.000    0.000    0.000 initialisers.py:43(initialise_event_handlers)
      136    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
       81    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       13    0.000    0.000    0.000    0.000 html_parser.py:94(push_style)
       19    0.000    0.000    0.000    0.000 camera.py:59(handle_events)
       10    0.000    0.000    0.000    0.000 entity_info.py:43(update)
        8    0.000    0.000    0.000    0.000 codecs.py:319(decode)
      123    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
       30    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       10    0.000    0.000    0.000    0.000 skill_bar.py:42(update)
        4    0.000    0.000    0.000    0.000 _bootlocale.py:11(getpreferredencoding)
      150    0.000    0.000    0.000    0.000 esper.py:278(try_component)
       23    0.000    0.000    0.000    0.000 {method 'match' of 're.Pattern' objects}
       61    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
        6    0.000    0.000    0.000    0.000 genericpath.py:117(_splitext)
       16    0.000    0.000    0.000    0.000 encoder.py:223(floatstr)
        8    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        7    0.000    0.000    0.000    0.000 event_hub.py:38(publish)
        2    0.000    0.000    0.000    0.000 {method 'blits' of 'pygame.Surface' objects}
       28    0.000    0.000    0.000    0.000 control_methods.py:86(check_dev_actions)
       27    0.000    0.000    0.000    0.000 esper.py:51(clear_cache)
      173    0.000    0.000    0.000    0.000 {method 'keys' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 parser.py:87(__init__)
        4    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
       39    0.000    0.000    0.000    0.000 ui_text_entry_line.py:688(validate_text_string)
        4    0.000    0.000    0.000    0.000 ui_text_entry_line.py:624(find_edit_position_from_pixel_pos)
        1    0.000    0.000    0.000    0.000 turn_manager.py:54(end_turn)
        6    0.000    0.000    0.000    0.000 __init__.py:590(formatMessage)
       13    0.000    0.000    0.000    0.000 ui_button.py:348(unselect)
        6    0.000    0.000    0.000    0.000 __init__.py:584(usesTime)
        2    0.000    0.000    0.000    0.000 control_methods.py:104(get_pressed_direction)
        1    0.000    0.000    0.000    0.000 _asarray.py:16(asarray)
        6    0.000    0.000    0.000    0.000 {built-in method time.gmtime}
        1    0.000    0.000    0.000    0.000 esper.py:270(get_component)
       13    0.000    0.000    0.000    0.000 ui_button.py:326(set_active)
       19    0.000    0.000    0.000    0.000 {built-in method pygame.event.post}
        1    0.000    0.000    0.000    0.000 {built-in method numpy.array}
        1    0.000    0.000    0.000    0.000 data_editor.py:686(_load_library_data)
        4    0.000    0.000    0.000    0.000 state_methods.py:73(set)
      144    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        1    0.000    0.000    0.000    0.000 esper.py:274(get_components)
        9    0.000    0.000    0.000    0.000 element_methods.py:116(add_ui_element)
       71    0.000    0.000    0.000    0.000 {method 'pop' of 'list' objects}
        8    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        4    0.000    0.000    0.000    0.000 {built-in method _locale._getdefaultlocale}
        3    0.000    0.000    0.000    0.000 parser.py:352(check_for_whole_start_tag)
       61    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
        1    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        5    0.000    0.000    0.000    0.000 parser.py:96(reset)
        1    0.000    0.000    0.000    0.000 turn_manager.py:75(next_turn)
      112    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 esper.py:276(<listcomp>)
        5    0.000    0.000    0.000    0.000 game_events.py:32(__init__)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3246(map_compute_fov)
        8    0.000    0.000    0.000    0.000 event_hub.py:50(subscribe)
        1    0.000    0.000    0.000    0.000 {built-in method _ctypes.pointer}
        1    0.000    0.000    0.000    0.000 esper.py:272(<listcomp>)
        6    0.000    0.000    0.000    0.000 __init__.py:432(format)
       12    0.000    0.000    0.000    0.000 __init__.py:849(acquire)
       70    0.000    0.000    0.000    0.000 ui_element.py:171(on_hovered)
        1    0.000    0.000    0.000    0.000 map_handler.py:80(process_end_of_turn_updates)
        7    0.000    0.000    0.000    0.000 event_hub.py:12(notify)
        8    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        3    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       19    0.000    0.000    0.000    0.000 {built-in method pygame.event.Event}
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
        5    0.000    0.000    0.000    0.000 sprite.py:217(__repr__)
        8    0.000    0.000    0.000    0.000 _markupbase.py:48(updatepos)
        2    0.000    0.000    0.000    0.000 control_methods.py:135(get_pressed_skills_number)
       26    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
        6    0.000    0.000    0.000    0.000 __init__.py:429(usesTime)
        6    0.000    0.000    0.000    0.000 __init__.py:154(<lambda>)
        4    0.000    0.000    0.000    0.000 encoder.py:259(_make_iterencode)
        5    0.000    0.000    0.000    0.000 entity_methods.py:140(get_component)
        3    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        3    0.000    0.000    0.000    0.000 esper.py:254(_get_components)
       18    0.000    0.000    0.000    0.000 data_editor.py:355(<genexpr>)
       19    0.000    0.000    0.000    0.000 element_methods.py:110(get_ui_elements)
        3    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
       68    0.000    0.000    0.000    0.000 ui_element.py:198(on_unhovered)
       62    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
       12    0.000    0.000    0.000    0.000 __init__.py:856(release)
        1    0.000    0.000    0.000    0.000 game_events.py:14(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
       15    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        4    0.000    0.000    0.000    0.000 encoder.py:104(__init__)
        3    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        7    0.000    0.000    0.000    0.000 event_hub.py:62(__init__)
        8    0.000    0.000    0.000    0.000 event_hub.py:15(subscribe)
        1    0.000    0.000    0.000    0.000 debug_methods.py:88(disable_profiling)
       10    0.000    0.000    0.000    0.000 html_parser.py:8(__init__)
       28    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
       10    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
        3    0.000    0.000    0.000    0.000 data_editor.py:193(_process_dropdown_change)
        1    0.000    0.000    0.000    0.000 _internal.py:262(__array_interface__)
       16    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
       28    0.000    0.000    0.000    0.000 library.py:181(get_people_data)
       12    0.000    0.000    0.000    0.000 __init__.py:747(filter)
        1    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
       28    0.000    0.000    0.000    0.000 library.py:203(get_homeland_data)
        5    0.000    0.000    0.000    0.000 {built-in method math.sin}
       18    0.000    0.000    0.000    0.000 {method 'rfind' of 'str' objects}
        6    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
        6    0.000    0.000    0.000    0.000 __init__.py:117(getLevelName)
       36    0.000    0.000    0.000    0.000 data_editor.py:407(<genexpr>)
        5    0.000    0.000    0.000    0.000 html_parser.py:27(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
       28    0.000    0.000    0.000    0.000 library.py:159(get_savvy_data)
        3    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
       14    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
        1    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
        2    0.000    0.000    0.000    0.000 {built-in method pygame.key.set_repeat}
       28    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        2    0.000    0.000    0.000    0.000 esper.py:243(_get_component)
       20    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
        1    0.000    0.000    0.000    0.000 __init__.py:489(cast)
        3    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
        6    0.000    0.000    0.000    0.000 threading.py:1052(name)
        6    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
       11    0.000    0.000    0.000    0.000 element_methods.py:101(get_ui_element)
       19    0.000    0.000    0.000    0.000 skill_bar.py:48(handle_events)
       54    0.000    0.000    0.000    0.000 {method 'cache_clear' of 'functools._lru_cache_wrapper' objects}
        1    0.000    0.000    0.000    0.000 entity_methods.py:357(spend_time)
       19    0.000    0.000    0.000    0.000 message_log.py:42(handle_events)
        1    0.000    0.000    0.000    0.000 entity_methods.py:156(get_components)
        1    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
        9    0.000    0.000    0.000    0.000 ui_button.py:356(set_text)
        1    0.000    0.000    0.000    0.000 game_events.py:24(__init__)
        4    0.000    0.000    0.000    0.000 codecs.py:186(__init__)
        5    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
        2    0.000    0.000    0.000    0.000 entity_methods.py:173(get_combat_stats)
        7    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       19    0.000    0.000    0.000    0.000 entity_info.py:49(handle_events)
        3    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
       10    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
        1    0.000    0.000    0.000    0.000 data_editor.py:212(_process_textbox_change)
        5    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        3    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        6    0.000    0.000    0.000    0.000 {built-in method time.time}
        3    0.000    0.000    0.000    0.000 esper.py:100(create_entity)
        1    0.000    0.000    0.000    0.000 entity_methods.py:168(get_identity)
        6    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        3    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
        6    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        4    0.000    0.000    0.000    0.000 control_methods.py:162(set_intent)
        1    0.000    0.000    0.000    0.000 esper.py:160(components_for_entity)
        5    0.000    0.000    0.000    0.000 library.py:273(get_secondary_stat_data)
        1    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        5    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
       15    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
        5    0.000    0.000    0.000    0.000 event_hub.py:46(__init__)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        7    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
        3    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 {method 'from_buffer' of '_ctypes.PyCArrayType' objects}
        6    0.000    0.000    0.000    0.000 process.py:180(name)
        8    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        6    0.000    0.000    0.000    0.000 process.py:36(current_process)
       27    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
        3    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        6    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
        3    0.000    0.000    0.000    0.000 components.py:69(__init__)
        5    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
        6    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        3    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        3    0.000    0.000    0.000    0.000 components.py:48(__init__)
       12    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
        7    0.000    0.000    0.000    0.000 state_methods.py:32(get_previous)
        3    0.000    0.000    0.000    0.000 components.py:37(__init__)
        1    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        6    0.000    0.000    0.000    0.000 esper.py:146(component_for_entity)
        7    0.000    0.000    0.000    0.000 data_editor.py:177(<genexpr>)
        8    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       10    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
       12    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        6    0.000    0.000    0.000    0.000 data_editor.py:357(<genexpr>)
        3    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
        5    0.000    0.000    0.000    0.000 esper.py:176(has_component)
        3    0.000    0.000    0.000    0.000 components.py:113(__init__)
        2    0.000    0.000    0.000    0.000 components.py:27(__init__)
        1    0.000    0.000    0.000    0.000 entity_handler.py:24(__init__)
        2    0.000    0.000    0.000    0.000 esper.py:266(<listcomp>)
        1    0.000    0.000    0.000    0.000 map_handler.py:20(__init__)
        2    0.000    0.000    0.000    0.000 components.py:59(__init__)
        2    0.000    0.000    0.000    0.000 camera.py:168(set_tiles)
        1    0.000    0.000    0.000    0.000 god_handler.py:21(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:25(__init__)
        1    0.000    0.000    0.000    0.000 esper.py:265(<listcomp>)
        8    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 data_editor.py:514(<listcomp>)
        1    0.000    0.000    0.000    0.000 library.py:298(get_god_data)
        1    0.000    0.000    0.000    0.000 data_editor.py:275(<listcomp>)
        1    0.000    0.000    0.000    0.000 data_editor.py:515(<listcomp>)
        1    0.000    0.000    0.000    0.000 data_editor.py:520(<listcomp>)
        1    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 components.py:149(__init__)
        2    0.000    0.000    0.000    0.000 combat_stats.py:16(__init__)
        1    0.000    0.000    0.000    0.000 library.py:217(get_skills_data)
        1    0.000    0.000    0.000    0.000 library.py:111(get_afflictions_data)
        2    0.000    0.000    0.000    0.000 components.py:97(__init__)
        2    0.000    0.000    0.000    0.000 components.py:79(__init__)
        1    0.000    0.000    0.000    0.000 library.py:195(get_homelands_data)
        1    0.000    0.000    0.000    0.000 library.py:266(get_primary_stats_data)
        1    0.000    0.000    0.000    0.000 <string>:1(__init__)
        2    0.000    0.000    0.000    0.000 components.py:88(__init__)
        1    0.000    0.000    0.000    0.000 _internal.py:259(__init__)
        1    0.000    0.000    0.000    0.000 library.py:71(get_aspects_data)
        1    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 library.py:151(get_savvys_data)
        1    0.000    0.000    0.000    0.000 library.py:173(get_peoples_data)
        1    0.000    0.000    0.000    0.000 library.py:282(get_secondary_stats_data)
        1    0.000    0.000    0.000    0.000 library.py:289(get_gods_data)
        1    0.000    0.000    0.000    0.000 _internal.py:340(data)
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}


