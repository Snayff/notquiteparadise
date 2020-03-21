Sat Mar 21 15:17:23 2020    logs/profiling/profile.dump

         8810742 function calls (7672025 primitive calls) in 18.210 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.115    0.115   18.168   18.168 main.py:85(game_loop)
      337    0.001    0.000    7.332    0.022 event_core.py:24(update)
      128    0.001    0.000    7.238    0.057 ui_handler.py:30(process_event)
      674    7.141    0.011    7.141    0.011 {method 'tick' of 'Clock' objects}
       43    0.000    0.000    7.011    0.163 ui_handler.py:207(update_camera)
       43    0.000    0.000    6.906    0.161 manager.py:295(update_camera_grid)
       43    0.040    0.001    6.906    0.161 camera.py:105(update_grid)
       83    0.000    0.000    6.850    0.083 ui_handler.py:48(process_entity_event)
     6518    0.082    0.000    6.797    0.001 ui_button.py:30(__init__)
     6518    0.351    0.000    6.399    0.001 ui_button.py:403(rebuild_from_changed_theme_data)
   189631    0.475    0.000    5.185    0.000 ui_appearance_theme.py:347(build_all_combined_ids)
1328307/189631    4.423    0.000    4.674    0.000 ui_appearance_theme.py:322(get_next_id_node)
      337    0.002    0.000    3.814    0.011 state.py:38(get_delta_time)
      337    0.001    0.000    3.330    0.010 state.py:63(update_clock)
    98050    0.254    0.000    2.922    0.000 ui_appearance_theme.py:466(get_colour_or_gradient)
      337    0.001    0.000    1.793    0.005 manager.py:54(update)
      337    0.095    0.000    1.792    0.005 ui_manager.py:122(update)
    58942    0.116    0.000    1.715    0.000 ui_appearance_theme.py:428(get_misc_data)
      337    0.005    0.000    1.595    0.005 manager.py:73(draw)
   117923    1.182    0.000    1.182    0.000 {method 'blit' of 'pygame.Surface' objects}
      337    0.055    0.000    1.125    0.003 sprite.py:453(update)
     6518    0.040    0.000    0.799    0.000 ui_button.py:97(set_any_images_from_theme)
    26072    0.048    0.000    0.759    0.000 ui_appearance_theme.py:366(get_image)
      379    0.334    0.001    0.739    0.002 camera.py:79(update_game_map)
      336    0.002    0.000    0.674    0.002 camera.py:72(update)
      337    0.002    0.000    0.599    0.002 ui_manager.py:173(draw_ui)
      337    0.093    0.000    0.596    0.002 sprite.py:753(draw)
      345    0.476    0.001    0.476    0.001 {built-in method pygame.transform.scale}
    54368    0.233    0.000    0.414    0.000 ui_element.py:121(check_hover)
     6518    0.053    0.000    0.363    0.000 ui_button.py:537(rebuild_shape)
    53016    0.107    0.000    0.338    0.000 ui_button.py:197(update)
     6567    0.021    0.000    0.310    0.000 rect_drawable_shape.py:22(__init__)
     6577    0.063    0.000    0.295    0.000 ui_element.py:23(__init__)
    14519    0.103    0.000    0.290    0.000 rect_drawable_shape.py:118(redraw_state)
     6567    0.085    0.000    0.273    0.000 rect_drawable_shape.py:32(full_rebuild_on_size_change)
     6518    0.029    0.000    0.258    0.000 ui_appearance_theme.py:405(get_font)
    53016    0.047    0.000    0.210    0.000 drawable_shape.py:36(update)
       28    0.000    0.000    0.201    0.007 ui_text_box.py:50(__init__)
       28    0.001    0.000    0.200    0.007 ui_text_box.py:492(rebuild_from_changed_theme_data)
       25    0.001    0.000    0.198    0.008 message_log.py:49(add_message)
       24    0.000    0.000    0.197    0.008 ui_handler.py:155(process_ui_event)
       24    0.000    0.000    0.196    0.008 ui_handler.py:238(process_message)
       24    0.000    0.000    0.196    0.008 manager.py:444(add_to_message_log)
       28    0.001    0.000    0.194    0.007 ui_text_box.py:110(rebuild)
       21    0.000    0.000    0.175    0.008 ui_handler.py:72(process_game_event)
        1    0.000    0.000    0.169    0.169 ui_handler.py:111(init_game_ui)
     6567    0.031    0.000    0.168    0.000 drawable_shape.py:45(redraw_all_states)
  2447634    0.154    0.000    0.154    0.000 {method 'append' of 'list' objects}
       43    0.025    0.001    0.151    0.004 ui_container.py:116(clear)
     6577    0.017    0.000    0.141    0.000 ui_container.py:42(add_element)
     6360    0.008    0.000    0.126    0.000 ui_button.py:130(kill)
    53016    0.064    0.000    0.124    0.000 ui_button.py:138(hover_point)
    12984    0.121    0.000    0.121    0.000 ui_container.py:62(recalculate_container_layer_thickness)
      337    0.120    0.000    0.120    0.000 {built-in method pygame.display.flip}
     6407    0.014    0.000    0.118    0.000 ui_element.py:114(kill)
      337    0.114    0.000    0.114    0.000 {built-in method pygame.event.get}
     3442    0.106    0.000    0.112    0.000 sprite.py:913(get_sprites_from_layer)
  2216036    0.109    0.000    0.109    0.000 {built-in method builtins.len}
       49    0.001    0.000    0.099    0.002 ui_text_box.py:310(parse_html_into_style_data)
       21    0.001    0.000    0.088    0.004 ui_vertical_scroll_bar.py:22(__init__)
     6577    0.011    0.000    0.088    0.000 sprite.py:121(__init__)
    14519    0.085    0.000    0.085    0.000 surface_cache.py:119(build_cache_id)
    56853    0.081    0.000    0.081    0.000 camera.py:233(world_to_screen_position)
     6577    0.025    0.000    0.077    0.000 sprite.py:126(add)
      528    0.004    0.000    0.072    0.000 __init__.py:1496(_log)
     6407    0.013    0.000    0.071    0.000 ui_container.py:52(remove_element)
       43    0.000    0.000    0.068    0.002 manager.py:286(update_camera_game_map)
      449    0.001    0.000    0.067    0.000 __init__.py:1996(debug)
    14657    0.067    0.000    0.067    0.000 {method 'copy' of 'pygame.Surface' objects}
      449    0.002    0.000    0.066    0.000 __init__.py:1361(debug)
      104    0.000    0.000    0.061    0.001 entity_handler.py:27(process_event)
    53016    0.053    0.000    0.060    0.000 rect_drawable_shape.py:84(collide_point)
     6577    0.013    0.000    0.059    0.000 ui_element.py:104(change_layer)
       49    0.000    0.000    0.059    0.001 text_block.py:16(__init__)
       49    0.019    0.000    0.059    0.001 text_block.py:40(redraw)
   757016    0.050    0.000    0.050    0.000 {method 'reverse' of 'list' objects}
     1010    0.050    0.000    0.050    0.000 {method 'fill' of 'pygame.Surface' objects}
   110417    0.039    0.000    0.048    0.000 sprite.py:208(alive)
     6577    0.044    0.000    0.046    0.000 sprite.py:646(add_internal)
     6585    0.040    0.000    0.046    0.000 sprite.py:822(change_layer)
      368    0.002    0.000    0.043    0.000 screen_message.py:34(update)
        1    0.000    0.000    0.042    0.042 main.py:193(initialise_game)
      337    0.001    0.000    0.038    0.000 ui_appearance_theme.py:158(update_shape_cache)
        2    0.000    0.000    0.038    0.019 entity.py:232(create_actor)
      337    0.001    0.000    0.037    0.000 surface_cache.py:24(update)
      246    0.001    0.000    0.037    0.000 ui_text_box.py:347(redraw_from_chunks)
      528    0.002    0.000    0.037    0.000 __init__.py:1521(handle)
       43    0.000    0.000    0.036    0.001 manager.py:275(update_cameras_tiles)
       69    0.028    0.000    0.036    0.001 surface_cache.py:29(add_surface_to_long_term_cache)
       43    0.011    0.000    0.036    0.001 camera.py:167(update_camera_tiles)
       49    0.000    0.000    0.036    0.001 parser.py:104(feed)
       49    0.006    0.000    0.035    0.001 parser.py:134(goahead)
      528    0.002    0.000    0.035    0.000 __init__.py:1575(callHandlers)
      704    0.007    0.000    0.035    0.000 ui_text_box.py:205(update)
     9560    0.021    0.000    0.035    0.000 world.py:55(get_tile)
     6407    0.010    0.000    0.033    0.000 sprite.py:183(kill)
      528    0.002    0.000    0.033    0.000 __init__.py:892(handle)
     9084    0.018    0.000    0.032    0.000 ui_font_dictionary.py:89(find_font)
        2    0.008    0.004    0.031    0.015 world.py:26(create_fov_map)
       21    0.000    0.000    0.031    0.001 entity_handler.py:127(_process_use_skill)
      528    0.001    0.000    0.029    0.000 __init__.py:1123(emit)
      528    0.002    0.000    0.028    0.000 __init__.py:1022(emit)
      246    0.003    0.000    0.026    0.000 ui_text_box.py:327(redraw_from_text_block)
      642    0.015    0.000    0.025    0.000 styled_chunk.py:8(__init__)
       20    0.000    0.000    0.025    0.001 skill.py:111(use)
    14519    0.023    0.000    0.025    0.000 drawable_shape.py:122(rebuild_images_and_text)
      528    0.002    0.000    0.024    0.000 __init__.py:1481(makeRecord)
     6407    0.012    0.000    0.023    0.000 sprite.py:728(remove_internal)
      528    0.008    0.000    0.022    0.000 __init__.py:293(__init__)
    53016    0.021    0.000    0.021    0.000 ui_button.py:154(can_hover)
      337    0.001    0.000    0.019    0.000 processors.py:16(process_all)
       36    0.000    0.000    0.019    0.001 manager.py:60(process_ui_events)
     4503    0.006    0.000    0.019    0.000 _internal.py:24(wrapper)
      642    0.004    0.000    0.019    0.000 parser.py:301(parse_starttag)
       36    0.007    0.000    0.019    0.001 ui_manager.py:86(process_events)
      337    0.010    0.000    0.018    0.000 processors.py:23(_process_aesthetic_update)
       20    0.000    0.000    0.018    0.001 skill.py:139(_call_skill_func)
       43    0.001    0.000    0.017    0.000 entity.py:485(take_turn)
     6567    0.017    0.000    0.017    0.000 drawable_shape.py:11(__init__)
      337    0.009    0.000    0.017    0.000 ecs.py:265(process_pending_deletions)
       46    0.001    0.000    0.016    0.000 chrono.py:24(rebuild_turn_queue)
     6573    0.012    0.000    0.016    0.000 ui_element.py:68(create_valid_ids)
     1282    0.003    0.000    0.015    0.000 html_parser.py:118(add_text)
       20    0.000    0.000    0.015    0.001 __init__.py:133(reload)
      528    0.001    0.000    0.014    0.000 __init__.py:869(format)
      124    0.001    0.000    0.014    0.000 ui_text_box.py:462(set_active_effect)
      528    0.003    0.000    0.013    0.000 __init__.py:606(format)
       83    0.000    0.000    0.013    0.000 god_handler.py:26(process_event)
     1282    0.010    0.000    0.013    0.000 html_parser.py:123(add_indexed_style)
       20    0.000    0.000    0.012    0.001 entity_handler.py:164(_process_die)
     3088    0.009    0.000    0.012    0.000 query.py:212(__iter__)
       22    0.001    0.000    0.012    0.001 entity_handler.py:49(_process_move)
      642    0.002    0.000    0.012    0.000 html_parser.py:213(handle_starttag)
     9603    0.010    0.000    0.011    0.000 world.py:348(_is_tile_in_bounds)
       21    0.000    0.000    0.011    0.001 interaction_handler.py:26(process_event)
       21    0.000    0.000    0.011    0.001 interaction_handler.py:88(_process_entity_collision)
    13222    0.011    0.000    0.011    0.000 {method 'remove' of 'list' objects}
     9085    0.011    0.000    0.011    0.000 ui_font_dictionary.py:133(create_font_id)
       20    0.000    0.000    0.011    0.001 <frozen importlib._bootstrap>:610(_exec)
      246    0.003    0.000    0.010    0.000 text_block.py:265(redraw_from_chunks)
       22    0.000    0.000    0.010    0.000 <frozen importlib._bootstrap_external>:722(exec_module)
    14519    0.010    0.000    0.010    0.000 surface_cache.py:109(find_surface_in_cache)
    57401    0.009    0.000    0.009    0.000 ui_manager.py:167(get_mouse_position)
       79    0.000    0.000    0.009    0.000 __init__.py:1986(info)
     4504    0.009    0.000    0.009    0.000 {built-in method _warnings.warn}
       79    0.000    0.000    0.009    0.000 __init__.py:1373(info)
      528    0.002    0.000    0.009    0.000 __init__.py:1011(flush)
       22    0.000    0.000    0.009    0.000 <frozen importlib._bootstrap_external>:793(get_code)
   110417    0.008    0.000    0.008    0.000 {built-in method _operator.truth}
      642    0.001    0.000    0.008    0.000 html_parser.py:283(handle_data)
      533    0.001    0.000    0.008    0.000 ntpath.py:212(basename)
    56385    0.008    0.000    0.008    0.000 {method 'collidepoint' of 'pygame.Rect' objects}
     5840    0.006    0.000    0.008    0.000 ecs.py:247(delete_entity_immediately)
        1    0.002    0.002    0.008    0.008 world.py:446(update_tile_visibility)
     2017    0.006    0.000    0.008    0.000 ui_container.py:124(check_hover)
    26268    0.008    0.000    0.008    0.000 {built-in method math.floor}
      528    0.004    0.000    0.007    0.000 __init__.py:1451(findCaller)
     1284    0.007    0.000    0.007    0.000 {method 'metrics' of 'pygame.font.Font' objects}
      533    0.004    0.000    0.007    0.000 ntpath.py:178(split)
      528    0.002    0.000    0.007    0.000 __init__.py:539(formatTime)
    45/43    0.000    0.000    0.007    0.000 <frozen importlib._bootstrap>:211(_call_with_frames_removed)
     6567    0.006    0.000    0.007    0.000 drawable_shape.py:50(compute_aligned_text_rect)
       21    0.001    0.000    0.007    0.000 interaction_handler.py:137(_apply_effects_to_tiles)
    47962    0.006    0.000    0.006    0.000 {method 'union' of 'pygame.Rect' objects}
       21    0.000    0.000    0.006    0.000 game_handler.py:26(process_event)
        2    0.000    0.000    0.006    0.003 entity.py:342(build_characteristic_sprites)
      528    0.006    0.000    0.006    0.000 {method 'flush' of '_io.TextIOWrapper' objects}
       20    0.000    0.000    0.006    0.000 entity_handler.py:225(_process_created_timed_entity)
       40    0.000    0.000    0.006    0.000 utility.py:13(get_image)
        2    0.000    0.000    0.005    0.003 manager.py:223(create_screen_message)
        2    0.000    0.000    0.005    0.003 screen_message.py:16(__init__)
    53282    0.005    0.000    0.005    0.000 {method 'colliderect' of 'pygame.Rect' objects}
       12    0.000    0.000    0.005    0.000 utility.py:39(get_images)
       22    0.000    0.000    0.005    0.000 <frozen importlib._bootstrap_external>:785(source_to_code)
       24    0.005    0.000    0.005    0.000 {built-in method builtins.compile}
       41    0.005    0.000    0.005    0.000 {built-in method pygame.imageext.load_extended}
    50516    0.005    0.000    0.005    0.000 {method 'contains' of 'pygame.Rect' objects}
     6565    0.004    0.000    0.005    0.000 ui_window_stack.py:73(get_root_window)
       21    0.000    0.000    0.005    0.000 ui_vertical_scroll_bar.py:328(rebuild_from_changed_theme_data)
     6567    0.005    0.000    0.005    0.000 drawable_shape.py:46(<listcomp>)
      797    0.004    0.000    0.004    0.000 {method 'render' of 'pygame.font.Font' objects}
       21    0.001    0.000    0.004    0.000 skill.py:219(process_effect)
       22    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap>:882(_find_spec)
     1301    0.004    0.000    0.004    0.000 typing.py:806(__new__)
     1301    0.003    0.000    0.004    0.000 query.py:170(__init__)
    21987    0.004    0.000    0.004    0.000 {built-in method builtins.hasattr}
       20    0.001    0.000    0.004    0.000 entity.py:303(create_projectile)
        6    0.000    0.000    0.004    0.001 game_handler.py:78(process_end_turn)
       22    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:1272(find_spec)
      528    0.001    0.000    0.004    0.000 ntpath.py:201(splitext)
        6    0.000    0.000    0.004    0.001 chrono.py:47(next_turn)
       22    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:1240(_get_spec)
        1    0.000    0.000    0.004    0.004 manager.py:182(init_skill_bar)
        1    0.000    0.000    0.004    0.004 skill_bar.py:15(__init__)
    13231    0.004    0.000    0.004    0.000 {built-in method builtins.min}
    18265    0.004    0.000    0.004    0.000 {method 'pop' of 'dict' objects}
       75    0.004    0.000    0.004    0.000 {built-in method nt.stat}
       49    0.000    0.000    0.004    0.000 html_parser.py:207(__init__)
       22    0.000    0.000    0.004    0.000 <frozen importlib._bootstrap_external>:1356(find_spec)
    13162    0.004    0.000    0.004    0.000 {method 'insert' of 'list' objects}
     6631    0.003    0.000    0.003    0.000 drawable_shape.py:86(get_surface)
      528    0.003    0.000    0.003    0.000 {built-in method time.strftime}
       49    0.001    0.000    0.003    0.000 html_parser.py:60(__init__)
    12432    0.003    0.000    0.003    0.000 {built-in method builtins.max}
        1    0.000    0.000    0.003    0.003 world.py:19(create_game_map)
        1    0.002    0.002    0.003    0.003 game_map.py:12(__init__)
     1681    0.003    0.000    0.003    0.000 ui_window.py:97(update)
       69    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap_external>:74(_path_stat)
        1    0.000    0.000    0.003    0.003 manager.py:156(init_message_log)
        1    0.000    0.000    0.003    0.003 message_log.py:18(__init__)
      373    0.002    0.000    0.003    0.000 sprite.py:814(layers)
       20    0.000    0.000    0.003    0.000 entity.py:189(delete)
      529    0.002    0.000    0.003    0.000 {method 'write' of '_io.TextIOWrapper' objects}
    19187    0.003    0.000    0.003    0.000 world.py:48(get_game_map)
       20    0.000    0.000    0.003    0.000 __init__.py:109(import_module)
    21/20    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap>:994(_gcd_import)
      410    0.001    0.000    0.003    0.000 entity.py:103(get_name)
    21/20    0.000    0.000    0.003    0.000 <frozen importlib._bootstrap>:978(_find_and_load)
     1066    0.002    0.000    0.003    0.000 ntpath.py:44(normcase)
       21    0.000    0.000    0.003    0.000 skill.py:74(can_afford_cost)
     3777    0.003    0.000    0.003    0.000 ui_button.py:257(process_event)
     3000    0.001    0.000    0.003    0.000 libtcodpy.py:3254(map_set_properties)
    13163    0.003    0.000    0.003    0.000 ui_manager.py:44(get_sprite_group)
      692    0.002    0.000    0.003    0.000 entity.py:93(get_entitys_component)
       20    0.000    0.000    0.003    0.000 skill.py:93(pay_resource_cost)
     6577    0.002    0.000    0.002    0.000 sprite.py:162(add_internal)
       44    0.002    0.000    0.002    0.000 <frozen importlib._bootstrap_external>:914(get_data)
       14    0.000    0.000    0.002    0.000 game_handler.py:39(process_change_game_state)
      528    0.001    0.000    0.002    0.000 genericpath.py:117(_splitext)
        1    0.002    0.002    0.002    0.002 ui_font_dictionary.py:155(preload_font)
      337    0.001    0.000    0.002    0.000 ui_manager.py:158(update_mouse_position)
      410    0.001    0.000    0.002    0.000 entity.py:117(get_identity)
    14519    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
      543    0.002    0.000    0.002    0.000 ntpath.py:122(splitdrive)
      674    0.002    0.000    0.002    0.000 sprite.py:745(sprites)
    13080    0.002    0.000    0.002    0.000 {method 'copy' of 'list' objects}
      233    0.002    0.000    0.002    0.000 ui_manager.py:104(<listcomp>)
    13471    0.002    0.000    0.002    0.000 {built-in method builtins.isinstance}
       73    0.001    0.000    0.002    0.000 entity.py:43(get_player)
       27    0.000    0.000    0.002    0.000 ui_text_box.py:102(kill)
       13    0.000    0.000    0.002    0.000 state.py:71(set_new)
     8250    0.002    0.000    0.002    0.000 ui_window.py:107(get_container)
      528    0.001    0.000    0.002    0.000 __init__.py:590(formatMessage)
      312    0.002    0.000    0.002    0.000 ui_vertical_scroll_bar.py:228(update)
      2/1    0.000    0.000    0.002    0.002 <frozen importlib._bootstrap>:948(_find_and_load_unlocked)
       44    0.000    0.000    0.002    0.000 world.py:261(tile_has_tag)
      336    0.001    0.000    0.002    0.000 skill_bar.py:45(update)
     1288    0.001    0.000    0.002    0.000 _markupbase.py:48(updatepos)
     2580    0.002    0.000    0.002    0.000 {method 'match' of 're.Pattern' objects}
       21    0.000    0.000    0.002    0.000 ui_vertical_scroll_bar.py:104(rebuild)
      740    0.001    0.000    0.002    0.000 html_parser.py:94(push_style)
     1352    0.001    0.000    0.002    0.000 ui_element.py:186(hover_point)
     2166    0.001    0.000    0.001    0.000 query.py:243(<listcomp>)
      642    0.001    0.000    0.001    0.000 parser.py:352(check_for_whole_start_tag)
      528    0.001    0.000    0.001    0.000 {built-in method time.gmtime}
      528    0.001    0.000    0.001    0.000 __init__.py:584(usesTime)
       21    0.000    0.000    0.001    0.000 god_handler.py:74(process_interventions)
       20    0.000    0.000    0.001    0.000 ui_vertical_scroll_bar.py:167(kill)
     1973    0.001    0.000    0.001    0.000 {method 'size' of 'pygame.font.Font' objects}
       40    0.001    0.000    0.001    0.000 ai.py:42(act)
     6577    0.001    0.000    0.001    0.000 {method '__contains__' of 'dict' objects}
     3000    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_set_properties}
     6533    0.001    0.000    0.001    0.000 ui_manager.py:51(get_window_stack)
       36    0.000    0.000    0.001    0.000 processors.py:57(process_intent)
      336    0.001    0.000    0.001    0.000 message_log.py:36(update)
      747    0.001    0.000    0.001    0.000 {built-in method builtins.sorted}
       46    0.000    0.000    0.001    0.000 chrono.py:153(_get_pretty_queue)
      528    0.001    0.000    0.001    0.000 cp1252.py:18(encode)
       21    0.001    0.000    0.001    0.000 entity.py:428(consider_intervening)
     1500    0.001    0.000    0.001    0.000 libtcodpy.py:3300(map_is_in_fov)
     1056    0.001    0.000    0.001    0.000 __init__.py:849(acquire)
     1301    0.001    0.000    0.001    0.000 query.py:50(__init__)
     6577    0.001    0.000    0.001    0.000 ui_manager.py:37(get_theme)
      528    0.001    0.000    0.001    0.000 __init__.py:432(format)
       22    0.000    0.000    0.001    0.000 processors.py:138(_process_player_turn_intents)
     6465    0.001    0.000    0.001    0.000 {method 'pop' of 'list' objects}
       24    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:93(_path_isfile)
       25    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:84(_path_is_mode_type)
        2    0.000    0.000    0.001    0.001 <frozen importlib._bootstrap>:663(_load_unlocked)
     1282    0.001    0.000    0.001    0.000 html_parser.py:27(__init__)
     6545    0.001    0.000    0.001    0.000 {method 'copy' of 'pygame.Rect' objects}
      123    0.001    0.000    0.001    0.000 surface_cache.py:80(split_rect)
       23    0.000    0.000    0.001    0.000 {built-in method builtins.exec}
      336    0.000    0.000    0.001    0.000 entity_info.py:45(update)
       26    0.000    0.000    0.001    0.000 ui_manager.py:59(get_shadow)
      693    0.001    0.000    0.001    0.000 state.py:45(get_current)
     2985    0.001    0.000    0.001    0.000 {method 'get' of 'dict' objects}
       68    0.000    0.000    0.001    0.000 utility.py:188(value_to_member)
      444    0.001    0.000    0.001    0.000 query.py:225(<listcomp>)
    12353    0.001    0.000    0.001    0.000 {method 'keys' of 'dict' objects}
     1331    0.001    0.000    0.001    0.000 html_parser.py:8(__init__)
        1    0.000    0.000    0.001    0.001 manager.py:195(init_camera)
       22    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:951(path_stats)
       22    0.000    0.000    0.001    0.000 world.py:360(_is_tile_blocking_movement)
        1    0.000    0.000    0.001    0.001 camera.py:24(__init__)
       26    0.000    0.000    0.001    0.000 ui_shadow.py:178(find_closest_shadow_scale_to_size)
       21    0.000    0.000    0.001    0.000 skill.py:247(_process_trigger_skill_effect)
     1500    0.001    0.000    0.001    0.000 tile.py:20(__init__)
     1056    0.001    0.000    0.001    0.000 __init__.py:856(release)
     6407    0.001    0.000    0.001    0.000 {method 'clear' of 'dict' objects}
       41    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:147(__enter__)
       22    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:504(_init_module_attrs)
      528    0.000    0.000    0.001    0.000 __init__.py:429(usesTime)
       49    0.000    0.000    0.001    0.000 ui_appearance_theme.py:386(get_font_info)
      337    0.001    0.000    0.001    0.000 {built-in method pygame.mouse.get_pos}
       64    0.001    0.000    0.001    0.000 {built-in method pygame.transform.smoothscale}
       89    0.001    0.000    0.001    0.000 utility.py:94(get_class_members)
       44    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap_external>:271(cache_from_source)
       60    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:157(_get_module_lock)
      528    0.000    0.000    0.001    0.000 __init__.py:154(<lambda>)
      528    0.001    0.000    0.001    0.000 {built-in method _codecs.charmap_encode}
     1056    0.001    0.000    0.001    0.000 __init__.py:747(filter)
       22    0.000    0.000    0.001    0.000 world.py:396(_tile_has_other_entity)
     1302    0.001    0.000    0.001    0.000 {built-in method __new__ of type object at 0x00007FF84F319BA0}
      149    0.000    0.000    0.001    0.000 event_core.py:41(publish)
        6    0.000    0.000    0.001    0.000 dataclasses.py:1023(asdict)
      528    0.000    0.000    0.001    0.000 __init__.py:117(getLevelName)
     1500    0.001    0.000    0.001    0.000 {built-in method tcod._libtcod.TCOD_map_is_in_fov}
       21    0.000    0.000    0.001    0.000 entity.py:73(get_entities_and_components_in_area)
        2    0.000    0.000    0.001    0.000 pydevd_modify_bytecode.py:213(insert_code)
     42/6    0.000    0.000    0.001    0.000 dataclasses.py:1047(_asdict_inner)
       22    0.001    0.000    0.001    0.000 {method 'read' of '_io.FileIO' objects}
        1    0.000    0.000    0.001    0.001 pydevd_modify_bytecode.py:233(_insert_code)
        4    0.000    0.000    0.001    0.000 ui_window.py:18(__init__)
     1584    0.001    0.000    0.001    0.000 {method 'rfind' of 'str' objects}
       44    0.000    0.000    0.001    0.000 <frozen importlib._bootstrap>:403(cached)
      528    0.000    0.000    0.000    0.000 threading.py:1206(current_thread)
      316    0.000    0.000    0.000    0.000 ui_button.py:170(while_hovering)
       23    0.000    0.000    0.000    0.000 entity.py:174(create)
      736    0.000    0.000    0.000    0.000 ecs.py:167(has_component)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:555(get_abs_path_real_path_and_base_from_file)
     2628    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
     1192    0.000    0.000    0.000    0.000 {method 'find' of 'str' objects}
     2746    0.000    0.000    0.000    0.000 {built-in method nt.fspath}
        1    0.000    0.000    0.000    0.000 warnings.py:96(_showwarnmsg)
       69    0.000    0.000    0.000    0.000 surface_cache.py:68(<listcomp>)
        1    0.000    0.000    0.000    0.000 warnings.py:20(_showwarnmsg_impl)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:369(_get_cached)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:128(_update_label_offsets)
     1620    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
      528    0.000    0.000    0.000    0.000 __init__.py:371(getMessage)
        5    0.000    0.000    0.000    0.000 ui_appearance_theme.py:138(check_need_to_reload)
      642    0.000    0.000    0.000    0.000 styled_chunk.py:73(unset_underline_style)
      533    0.000    0.000    0.000    0.000 ntpath.py:34(_get_bothseps)
       23    0.000    0.000    0.000    0.000 ecs.py:32(new_entity)
       35    0.000    0.000    0.000    0.000 {method 'convert_alpha' of 'pygame.Surface' objects}
     1058    0.000    0.000    0.000    0.000 {method 'acquire' of '_thread.RLock' objects}
        1    0.000    0.000    0.000    0.000 entity.py:201(create_god)
     2353    0.000    0.000    0.000    0.000 sprite.py:168(update)
       25    0.000    0.000    0.000    0.000 entity.py:131(get_primary_stat)
      124    0.000    0.000    0.000    0.000 text_effects.py:81(__init__)
     1286    0.000    0.000    0.000    0.000 {method 'count' of 'str' objects}
       36    0.000    0.000    0.000    0.000 action.py:12(convert_to_intent)
      111    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:56(_path_join)
     1681    0.000    0.000    0.000    0.000 ui_window.py:116(check_hover)
      528    0.000    0.000    0.000    0.000 __init__.py:1619(isEnabledFor)
      528    0.000    0.000    0.000    0.000 threading.py:1052(name)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:228(_NormPaths)
      122    0.000    0.000    0.000    0.000 text_effects.py:88(update)
      642    0.000    0.000    0.000    0.000 text_block.py:11(__init__)
       60    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:58(__init__)
        1    0.000    0.000    0.000    0.000 warnings.py:117(_formatwarnmsg)
        1    0.000    0.000    0.000    0.000 warnings.py:35(_formatwarnmsg_impl)
        1    0.000    0.000    0.000    0.000 linecache.py:15(getline)
        1    0.000    0.000    0.000    0.000 linecache.py:37(getlines)
       69    0.000    0.000    0.000    0.000 {method 'subsurface' of 'pygame.Surface' objects}
      149    0.000    0.000    0.000    0.000 event_core.py:15(notify)
      339    0.000    0.000    0.000    0.000 {built-in method builtins.any}
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:245(_NormPath)
        1    0.000    0.000    0.000    0.000 linecache.py:82(updatecache)
       21    0.000    0.000    0.000    0.000 world.py:77(get_direction)
      691    0.000    0.000    0.000    0.000 ecs.py:129(entity_component)
        1    0.000    0.000    0.000    0.000 manager.py:169(init_entity_info)
     1352    0.000    0.000    0.000    0.000 ui_element.py:204(can_hover)
        1    0.000    0.000    0.000    0.000 entity_info.py:19(__init__)
       19    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:194(_lock_unlock_module)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1351(_get_spec)
       53    0.000    0.000    0.000    0.000 ui_button.py:162(on_hovered)
      149    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:1009(_handle_fromlist)
       69    0.000    0.000    0.000    0.000 surface_cache.py:21(add_surface_to_cache)
       49    0.000    0.000    0.000    0.000 parser.py:87(__init__)
       21    0.000    0.000    0.000    0.000 random.py:344(choices)
     1484    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
        5    0.000    0.000    0.000    0.000 ui_container.py:19(__init__)
      799    0.000    0.000    0.000    0.000 {method 'rstrip' of 'str' objects}
       10    0.000    0.000    0.000    0.000 ntpath.py:523(abspath)
      529    0.000    0.000    0.000    0.000 {built-in method sys._getframe}
        2    0.000    0.000    0.000    0.000 combat_stats.py:67(max_health)
      814    0.000    0.000    0.000    0.000 {built-in method builtins.getattr}
      120    0.000    0.000    0.000    0.000 {built-in method _thread.allocate_lock}
       46    0.000    0.000    0.000    0.000 chrono.py:161(_get_next_entity_in_queue)
      648    0.000    0.000    0.000    0.000 __init__.py:122(unescape)
     1176    0.000    0.000    0.000    0.000 {built-in method _thread.get_ident}
       44    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:62(_path_split)
      528    0.000    0.000    0.000    0.000 {built-in method time.time}
       21    0.000    0.000    0.000    0.000 ui_button.py:226(set_position)
       69    0.000    0.000    0.000    0.000 surface_cache.py:62(<listcomp>)
        1    0.000    0.000    0.000    0.000 combat_stats.py:270(sight_range)
       10    0.000    0.000    0.000    0.000 ntpath.py:450(normpath)
       21    0.000    0.000    0.000    0.000 world.py:106(get_tiles)
      528    0.000    0.000    0.000    0.000 {built-in method nt.getpid}
        2    0.000    0.000    0.000    0.000 combat_stats.py:92(max_stamina)
       22    0.000    0.000    0.000    0.000 event.py:63(__init__)
      133    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:103(_unpack_opargs)
     1924    0.000    0.000    0.000    0.000 {method 'get_ascent' of 'pygame.font.Font' objects}
       60    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:78(acquire)
       49    0.000    0.000    0.000    0.000 parser.py:96(reset)
        3    0.000    0.000    0.000    0.000 ai.py:68(act)
       41    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:151(__exit__)
      696    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
      149    0.000    0.000    0.000    0.000 event_core.py:73(__init__)
      111    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:58(<listcomp>)
      675    0.000    0.000    0.000    0.000 {method 'endswith' of 'str' objects}
     1058    0.000    0.000    0.000    0.000 {method 'release' of '_thread.RLock' objects}
      126    0.000    0.000    0.000    0.000 abc.py:137(__instancecheck__)
       60    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:103(release)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:574(spec_from_file_location)
      416    0.000    0.000    0.000    0.000 {method 'values' of 'dict' objects}
       49    0.000    0.000    0.000    0.000 text_block.py:54(<listcomp>)
     1292    0.000    0.000    0.000    0.000 {method 'end' of 're.Match' objects}
      251    0.000    0.000    0.000    0.000 {method 'set_alpha' of 'pygame.Surface' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:576(module_from_spec)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1203(_path_importer_cache)
      650    0.000    0.000    0.000    0.000 {method 'group' of 're.Match' objects}
      312    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:159(check_has_moved_recently)
       12    0.000    0.000    0.000    0.000 utility.py:51(flatten_images)
       24    0.000    0.000    0.000    0.000 entity.py:335(add_component)
       20    0.000    0.000    0.000    0.000 event.py:54(__init__)
       28    0.000    0.000    0.000    0.000 text_block.py:288(add_chunks_to_hover_group)
      164    0.000    0.000    0.000    0.000 manager.py:128(get_ui_element)
        1    0.000    0.000    0.000    0.000 tokenize.py:443(open)
      642    0.000    0.000    0.000    0.000 {method 'set_underline' of 'pygame.font.Font' objects}
      145    0.000    0.000    0.000    0.000 library.py:169(get_skill_data)
        5    0.000    0.000    0.000    0.000 combat_stats.py:22(vigour)
       60    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:176(cb)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1190(_path_hooks)
        2    0.000    0.000    0.000    0.000 libtcodpy.py:3228(map_new)
       21    0.000    0.000    0.000    0.000 event.py:136(__init__)
        1    0.000    0.000    0.000    0.000 __init__.py:316(namedtuple)
        2    0.000    0.000    0.000    0.000 map.py:66(__init__)
       36    0.000    0.000    0.000    0.000 copy.py:132(deepcopy)
      126    0.000    0.000    0.000    0.000 {built-in method _abc._abc_instancecheck}
       21    0.000    0.000    0.000    0.000 event.py:29(__init__)
        1    0.000    0.000    0.000    0.000 {method 'readlines' of '_io._IOBase' objects}
       24    0.000    0.000    0.000    0.000 event.py:184(__init__)
       96    0.000    0.000    0.000    0.000 chrono.py:111(get_turn_holder)
        5    0.000    0.000    0.000    0.000 combat_stats.py:31(clout)
      643    0.000    0.000    0.000    0.000 {method 'strip' of 'str' objects}
        4    0.000    0.000    0.000    0.000 ui_window_stack.py:23(add_new_window)
       19    0.000    0.000    0.000    0.000 ui_vertical_scroll_bar.py:195(process_event)
       43    0.000    0.000    0.000    0.000 camera.py:185(set_tiles)
        5    0.000    0.000    0.000    0.000 combat_stats.py:40(skullduggery)
       36    0.000    0.000    0.000    0.000 processors.py:118(_process_stateless_intents)
       22    0.000    0.000    0.000    0.000 processors.py:71(_get_pressed_direction)
        5    0.000    0.000    0.000    0.000 combat_stats.py:49(bustle)
        5    0.000    0.000    0.000    0.000 combat_stats.py:58(exactitude)
      132    0.000    0.000    0.000    0.000 ui_window.py:55(process_event)
       36    0.000    0.000    0.000    0.000 action.py:34(_check_directions)
       34    0.000    0.000    0.000    0.000 ui_text_box.py:379(process_event)
       24    0.000    0.000    0.000    0.000 ecs.py:66(add_component)
       69    0.000    0.000    0.000    0.000 {method 'get_size' of 'pygame.Surface' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1404(_fill_cache)
        4    0.000    0.000    0.000    0.000 ui_window.py:135(change_window_layer)
        6    0.000    0.000    0.000    0.000 entity_handler.py:217(_process_end_turn)
        2    0.000    0.000    0.000    0.000 map.py:74(__as_cdata)
      122    0.000    0.000    0.000    0.000 text_effects.py:100(should_redraw_from_chunks)
       21    0.000    0.000    0.000    0.000 random.py:365(<listcomp>)
      124    0.000    0.000    0.000    0.000 text_effects.py:2(__init__)
       70    0.000    0.000    0.000    0.000 dis.py:436(findlinestarts)
        2    0.000    0.000    0.000    0.000 pydevd_frame_tracing.py:96(create_pydev_trace_code_wrapper)
       87    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:222(_verbose_message)
        6    0.000    0.000    0.000    0.000 dataclasses.py:994(fields)
      458    0.000    0.000    0.000    0.000 drawable_shape.py:33(clean_up_temp_shapes)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1445(path_hook_for_FileFinder)
       21    0.000    0.000    0.000    0.000 ui_element.py:160(set_position)
        2    0.000    0.000    0.000    0.000 ui_shadow.py:99(create_new_rectangle_shadow)
      246    0.000    0.000    0.000    0.000 text_effects.py:107(get_final_alpha)
      112    0.000    0.000    0.000    0.000 chrono.py:118(get_turn_queue)
       20    0.000    0.000    0.000    0.000 event.py:77(__init__)
      180    0.000    0.000    0.000    0.000 ui_element.py:210(process_event)
        1    0.000    0.000    0.000    0.000 {built-in method nt.listdir}
        1    0.000    0.000    0.000    0.000 {built-in method io.open}
       23    0.000    0.000    0.000    0.000 ecs.py:44(<setcomp>)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:401(_check_name_wrapper)
        6    0.000    0.000    0.000    0.000 entity.py:380(spend_time)
       21    0.000    0.000    0.000    0.000 god_handler.py:49(process_judgements)
       89    0.000    0.000    0.000    0.000 {method 'keys' of 'mappingproxy' objects}
        1    0.000    0.000    0.000    0.000 main.py:220(initialise_event_handlers)
      166    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
       41    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
        1    0.000    0.000    0.000    0.000 world.py:439(recompute_fov)
        1    0.000    0.000    0.000    0.000 tokenize.py:350(detect_encoding)
        1    0.000    0.000    0.000    0.000 ui_image.py:20(__init__)
       14    0.000    0.000    0.000    0.000 event.py:106(__init__)
       34    0.000    0.000    0.000    0.000 chrono.py:132(get_time)
      120    0.000    0.000    0.000    0.000 {method 'discard' of 'set' objects}
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:550(is_real_file)
       20    0.000    0.000    0.000    0.000 ecs.py:233(delete_entity)
       66    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:859(__exit__)
       20    0.000    0.000    0.000    0.000 ai.py:34(__init__)
       22    0.000    0.000    0.000    0.000 <string>:1(__init__)
       48    0.000    0.000    0.000    0.000 dataclasses.py:1012(_is_dataclass_instance)
       46    0.000    0.000    0.000    0.000 chrono.py:183(set_turn_queue)
       22    0.000    0.000    0.000    0.000 processors.py:98(_get_pressed_skills_number)
       66    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:855(__enter__)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:98(_path_isdir)
       49    0.000    0.000    0.000    0.000 {method 'sort' of 'list' objects}
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:792(find_spec)
        2    0.000    0.000    0.000    0.000 parser.py:386(parse_endtag)
        1    0.000    0.000    0.000    0.000 basic_attack.py:1(<module>)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:369(__init__)
      162    0.000    0.000    0.000    0.000 {method 'setdefault' of 'dict' objects}
       69    0.000    0.000    0.000    0.000 {method 'popitem' of 'dict' objects}
       21    0.000    0.000    0.000    0.000 utility.py:147(get_coords_from_shape)
       28    0.000    0.000    0.000    0.000 {built-in method math.sin}
      178    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
       10    0.000    0.000    0.000    0.000 pydevd_file_utils.py:171(normcase)
        5    0.000    0.000    0.000    0.000 pydevd_file_utils.py:542(_is_int)
      186    0.000    0.000    0.000    0.000 {built-in method _imp.acquire_lock}
      110    0.000    0.000    0.000    0.000 {method 'rpartition' of 'str' objects}
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:884(__init__)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:416(parent)
       21    0.000    0.000    0.000    0.000 rect_drawable_shape.py:107(set_position)
        2    0.000    0.000    0.000    0.000 manager.py:345(should_camera_move)
       44    0.000    0.000    0.000    0.000 {method 'rsplit' of 'str' objects}
       34    0.000    0.000    0.000    0.000 action.py:60(_check_actions)
      122    0.000    0.000    0.000    0.000 text_effects.py:5(should_full_redraw)
       11    0.000    0.000    0.000    0.000 ui_button.py:187(on_unhovered)
       49    0.000    0.000    0.000    0.000 _markupbase.py:36(reset)
        4    0.000    0.000    0.000    0.000 ui_container.py:75(change_container_layer)
        1    0.000    0.000    0.000    0.000 tokenize.py:374(read_or_stop)
       21    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:929(_sanity_check)
       80    0.000    0.000    0.000    0.000 ui_manager.py:294(clear_last_focused_from_vert_scrollbar)
        6    0.000    0.000    0.000    0.000 event.py:88(__init__)
      186    0.000    0.000    0.000    0.000 {built-in method _imp.release_lock}
       21    0.000    0.000    0.000    0.000 library.py:273(get_god_attitudes_data)
        1    0.000    0.000    0.000    0.000 {method 'readline' of '_io.BufferedReader' objects}
       41    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:143(__init__)
       21    0.000    0.000    0.000    0.000 {built-in method builtins.setattr}
       47    0.000    0.000    0.000    0.000 chrono.py:169(set_turn_holder)
        6    0.000    0.000    0.000    0.000 utility.py:107(lerp)
        1    0.000    0.000    0.000    0.000 libtcodpy.py:3283(map_compute_fov)
        3    0.000    0.000    0.000    0.000 manager.py:398(world_to_screen_position)
      135    0.000    0.000    0.000    0.000 {built-in method builtins.abs}
       33    0.000    0.000    0.000    0.000 action.py:83(_check_dev_actions)
        3    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:12(_add_attr_values_from_insert_to_original)
        1    0.000    0.000    0.000    0.000 map.py:100(compute_fov)
       79    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
       23    0.000    0.000    0.000    0.000 component.py:82(__init__)
        8    0.000    0.000    0.000    0.000 event_core.py:53(subscribe)
       21    0.000    0.000    0.000    0.000 {built-in method _bisect.bisect_right}
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:36(_relax_case)
       21    0.000    0.000    0.000    0.000 library.py:248(get_god_intervention_data)
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1319(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:318(__exit__)
       10    0.000    0.000    0.000    0.000 {built-in method nt._getfullpathname}
        2    0.000    0.000    0.000    0.000 {method 'new' of 'CompiledFFI' objects}
        2    0.000    0.000    0.000    0.000 {built-in method numpy.zeros}
        3    0.000    0.000    0.000    0.000 codecs.py:319(decode)
       22    0.000    0.000    0.000    0.000 {built-in method _imp.is_frozen}
        1    0.000    0.000    0.000    0.000 {built-in method tcod._libtcod.TCOD_map_compute_fov}
        3    0.000    0.000    0.000    0.000 __init__.py:186(easeOutCubic)
       21    0.000    0.000    0.000    0.000 entity.py:84(<listcomp>)
       42    0.000    0.000    0.000    0.000 dataclasses.py:1009(<genexpr>)
        7    0.000    0.000    0.000    0.000 abc.py:141(__subclasscheck__)
       22    0.000    0.000    0.000    0.000 component.py:56(__init__)
        2    0.000    0.000    0.000    0.000 html_parser.py:272(handle_endtag)
       22    0.000    0.000    0.000    0.000 component.py:31(__init__)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:48(_modify_new_lines)
        1    0.000    0.000    0.000    0.000 __init__.py:1(<module>)
       20    0.000    0.000    0.000    0.000 component.py:199(__init__)
       27    0.000    0.000    0.000    0.000 library.py:139(get_people_data)
       21    0.000    0.000    0.000    0.000 component.py:118(__init__)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:719(find_spec)
       21    0.000    0.000    0.000    0.000 {method 'random' of '_random.Random' objects}
       19    0.000    0.000    0.000    0.000 ui_manager.py:303(get_last_focused_vert_scrollbar)
        3    0.000    0.000    0.000    0.000 entity.py:124(get_combat_stats)
       27    0.000    0.000    0.000    0.000 library.py:123(get_savvy_data)
        4    0.000    0.000    0.000    0.000 manager.py:236(is_target_pos_in_camera_edge)
        3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
        6    0.000    0.000    0.000    0.000 utility.py:121(clamp)
        7    0.000    0.000    0.000    0.000 {built-in method _abc._abc_subclasscheck}
        2    0.000    0.000    0.000    0.000 _internal.py:251(__init__)
        8    0.000    0.000    0.000    0.000 event_core.py:18(subscribe)
       27    0.000    0.000    0.000    0.000 library.py:155(get_homeland_data)
        3    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
       22    0.000    0.000    0.000    0.000 state.py:17(get_previous)
        3    0.000    0.000    0.000    0.000 component.py:40(__init__)
       28    0.000    0.000    0.000    0.000 ui_appearance_theme.py:130(get_font_dictionary)
       21    0.000    0.000    0.000    0.000 ui_button.py:370(set_hold_range)
        2    0.000    0.000    0.000    0.000 manager.py:305(set_player_tile)
        2    0.000    0.000    0.000    0.000 {method 'cast' of 'CompiledFFI' objects}
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:909(get_filename)
        2    0.000    0.000    0.000    0.000 html_parser.py:102(pop_style)
        1    0.000    0.000    0.000    0.000 main.py:170(disable_profiling)
       36    0.000    0.000    0.000    0.000 copy.py:190(_deepcopy_atomic)
        1    0.000    0.000    0.000    0.000 event.py:98(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:212(_acquireLock)
        1    0.000    0.000    0.000    0.000 tokenize.py:380(find_cookie)
       22    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:424(has_location)
        2    0.000    0.000    0.000    0.000 _internal.py:45(verify_order)
        6    0.000    0.000    0.000    0.000 chrono.py:102(add_time)
       18    0.000    0.000    0.000    0.000 chrono.py:125(get_time_in_round)
        5    0.000    0.000    0.000    0.000 library.py:206(get_secondary_stat_data)
        1    0.000    0.000    0.000    0.000 entity_handler.py:24(__init__)
        1    0.000    0.000    0.000    0.000 codecs.py:309(__init__)
        5    0.000    0.000    0.000    0.000 event_core.py:49(__init__)
       36    0.000    0.000    0.000    0.000 {built-in method builtins.id}
        6    0.000    0.000    0.000    0.000 chrono.py:139(get_time_of_last_turn)
        4    0.000    0.000    0.000    0.000 manager.py:91(add_ui_element)
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:195(add_jump_instruction)
       10    0.000    0.000    0.000    0.000 {method 'lstrip' of 'str' objects}
        6    0.000    0.000    0.000    0.000 manager.py:121(get_gui_manager)
        2    0.000    0.000    0.000    0.000 component.py:184(__init__)
        2    0.000    0.000    0.000    0.000 __init__.py:221(_releaseLock)
        3    0.000    0.000    0.000    0.000 component.py:64(__init__)
        3    0.000    0.000    0.000    0.000 combat_stats.py:19(__init__)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:35(_new_module)
        1    0.000    0.000    0.000    0.000 warnings.py:419(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:190(set_time_of_last_turn)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:321(<genexpr>)
        8    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1325(<genexpr>)
        2    0.000    0.000    0.000    0.000 _internal.py:305(data)
        3    0.000    0.000    0.000    0.000 __init__.py:102(_checkRange)
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:311(__enter__)
        3    0.000    0.000    0.000    0.000 component.py:133(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:146(get_round)
        1    0.000    0.000    0.000    0.000 god_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 interaction_handler.py:23(__init__)
        1    0.000    0.000    0.000    0.000 {built-in method _imp.is_builtin}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap>:307(__init__)
        6    0.000    0.000    0.000    0.000 chrono.py:176(set_time_in_round)
        4    0.000    0.000    0.000    0.000 ui_window.py:127(get_top_layer)
        1    0.000    0.000    0.000    0.000 game_handler.py:23(__init__)
        2    0.000    0.000    0.000    0.000 component.py:73(__init__)
        1    0.000    0.000    0.000    0.000 ui_handler.py:27(__init__)
        2    0.000    0.000    0.000    0.000 {method 'search' of 're.Pattern' objects}
        1    0.000    0.000    0.000    0.000 pydevd_modify_bytecode.py:82(<lambda>)
        2    0.000    0.000    0.000    0.000 __init__.py:1605(getEffectiveLevel)
        2    0.000    0.000    0.000    0.000 camera.py:194(set_player_tile)
        2    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
        1    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:1433(<setcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.repr}
        3    0.000    0.000    0.000    0.000 __init__.py:388(<genexpr>)
        1    0.000    0.000    0.000    0.000 ecs.py:150(entity_components)
        2    0.000    0.000    0.000    0.000 component.py:92(__init__)
        1    0.000    0.000    0.000    0.000 <string>:1(__new__)
        1    0.000    0.000    0.000    0.000 {method 'decode' of 'bytes' objects}
        2    0.000    0.000    0.000    0.000 component.py:110(__init__)
        1    0.000    0.000    0.000    0.000 ai.py:65(__init__)
        2    0.000    0.000    0.000    0.000 parser.py:127(clear_cdata_mode)
        1    0.000    0.000    0.000    0.000 {method 'startswith' of 'bytes' objects}
        1    0.000    0.000    0.000    0.000 codecs.py:260(__init__)
        1    0.000    0.000    0.000    0.000 library.py:231(get_god_data)
        1    0.000    0.000    0.000    0.000 component.py:176(__init__)
        1    0.000    0.000    0.000    0.000 {method 'seek' of '_io.BufferedReader' objects}
        3    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
        3    0.000    0.000    0.000    0.000 {method 'isidentifier' of 'str' objects}
        2    0.000    0.000    0.000    0.000 component.py:101(__init__)
        2    0.000    0.000    0.000    0.000 {method 'partition' of 'str' objects}
        2    0.000    0.000    0.000    0.000 <frozen importlib._bootstrap_external>:719(create_module)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 basic_attack.py:13(use)
        2    0.000    0.000    0.000    0.000 {method 'upper' of 'str' objects}
        1    0.000    0.000    0.000    0.000 {built-in method sys.intern}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


