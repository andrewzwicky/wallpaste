def scale_monitors(monitors, target_width, target_height):
    min_x = min(monitor.x() for monitor in monitors)
    min_y = min(monitor.y() for monitor in monitors)
    max_x = max(monitor.x() + monitor.width() for monitor in monitors)
    max_y = max(monitor.y() + monitor.height() for monitor in monitors)

    total_width = max_x - min_x
    total_height = max_y - min_y

    height_rescale = target_height / total_height
    width_rescale = target_width / total_width

    rescale = min(height_rescale, width_rescale)

    return [(int(x*rescale),
             int(y*rescale),
             int(w*rescale),
             int(h*rescale)) for x,y,w,h in [monitor.getRect() for monitor in monitors]]
